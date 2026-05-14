#!/usr/bin/env python3
"""
Auto selector builder from *_old.png references.

Workflow:
1) For each old image, load the matching HTML with Playwright.
2) Enumerate visible DOM candidates with stable-ish selectors.
3) Compare candidate crops vs old reference with ImageMagick RMSE.
4) Write selector.json with best candidate (or best pair if better).

Soporta series con prefijo arbitrario:
  O10_Imagen3_old.png
  P5_Imagen8_old.png
  RT2_Imagen1_old.png
  D7_Imagen4_old.png
"""

from __future__ import annotations

import argparse
import asyncio
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from series_utils import (
    find_html_file_in_folder,
    iter_series_group_dirs,
    parse_old_png_name,
    parse_prefix_arg,
    prefix_selected,
    resolve_image_folder,
)


BASE_DIR = Path(__file__).resolve().parent.parent
MAGICK = "/opt/homebrew/bin/magick"
HTML_FILENAMES = ("GoalBus.html", "GoalBus Settings.html")


def ensure_playwright_runtime() -> None:
    try:
        import playwright  # noqa: F401
        return
    except ModuleNotFoundError:
        venv_python = BASE_DIR / ".venv" / "bin" / "python"
        if venv_python.exists() and Path(sys.executable).resolve() != venv_python.resolve():
            os.execv(str(venv_python), [str(venv_python), str(Path(__file__).resolve()), *sys.argv[1:]])
        raise


@dataclass
class Target:
    prefix: str
    group_num: int
    image_num: int
    old_path: Path
    group_dir: Path
    image_folder: Path
    html_path: Path
    selector_path: Path
    output_png: Path

    @property
    def target_id(self) -> str:
        return f"{self.prefix.upper()}:{self.group_num}:{self.image_num}"


@dataclass
class Candidate:
    selector: str
    x: int
    y: int
    w: int
    h: int
    tag: str
    text_len: int
    stable_hint: int
    depth: int


def run_cmd(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def assert_dependencies() -> None:
    if not Path(MAGICK).exists():
        raise RuntimeError(f"No encontré ImageMagick en {MAGICK}")


def image_size(path: Path) -> tuple[int, int]:
    proc = run_cmd([MAGICK, "identify", "-format", "%w %h", str(path)])
    if proc.returncode != 0:
        raise RuntimeError(f"identify falló para {path}: {proc.stderr.strip()}")
    w, h = proc.stdout.strip().split()
    return int(w), int(h)


def build_report_path(lang: str, prefix_arg: str | None, from_group: int, to_group: int) -> Path:
    prefix_segment = "all" if not prefix_arg or prefix_arg.lower() == "all" else re.sub(r"[^A-Za-z0-9,_-]+", "-", prefix_arg)
    lang_segment = re.sub(r"[^A-Za-z0-9_-]+", "_", lang)
    return BASE_DIR / "scratch" / f"auto_select_from_old_report_{lang_segment}_{prefix_segment}_{from_group}_{to_group}.json"


def load_existing_review_state(report_path: Path) -> dict[str, dict]:
    if not report_path.exists():
        return {}
    try:
        data = json.loads(report_path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    if not isinstance(data, list):
        return {}
    by_id: dict[str, dict] = {}
    for row in data:
        if not isinstance(row, dict):
            continue
        target_id = row.get("target_id")
        if not isinstance(target_id, str) or not target_id:
            continue
        by_id[target_id] = {
            "reviewed": bool(row.get("reviewed", False)),
            "corrected_manually": bool(row.get("corrected_manually", False)),
            "review_notes": row.get("review_notes", ""),
        }
    return by_id


def discover_targets(
    lang: str = "Español",
    prefix_arg: str | None = "all",
    from_group: int = 1,
    from_image: int = 1,
    to_group: int = 9999,
    include_existing: bool = False,
) -> tuple[list[Target], list[tuple[str, int, int, str]]]:
    lang_dir = BASE_DIR / lang
    selected_prefixes = parse_prefix_arg(prefix_arg)
    targets: list[Target] = []
    missing: list[tuple[str, int, int, str]] = []

    if not lang_dir.exists():
        return targets, missing

    for group_info, group_dir in iter_series_group_dirs(lang_dir, selected_prefixes):
        if group_info.group_num < from_group or group_info.group_num > to_group:
            continue

        for old_path in sorted(group_dir.glob("*_old.png"), key=lambda p: p.name.lower()):
            parsed = parse_old_png_name(old_path.name)
            if not parsed:
                continue
            if not prefix_selected(parsed.prefix, selected_prefixes):
                continue
            if parsed.group_num != group_info.group_num:
                continue
            if parsed.group_num == from_group and parsed.image_num < from_image:
                continue

            image_folder = resolve_image_folder(group_dir, parsed.prefix, parsed.group_num, parsed.image_num)
            if not image_folder:
                missing.append((parsed.prefix.upper(), parsed.group_num, parsed.image_num, f"Falta carpeta de imagen en {group_dir}"))
                continue

            html_path = find_html_file_in_folder(image_folder, HTML_FILENAMES)
            if not html_path:
                missing.append((parsed.prefix.upper(), parsed.group_num, parsed.image_num, f"Falta HTML en {image_folder}"))
                continue

            selector_path = image_folder / "selector.json"
            if selector_path.exists() and not include_existing:
                continue

            targets.append(
                Target(
                    prefix=parsed.prefix,
                    group_num=parsed.group_num,
                    image_num=parsed.image_num,
                    old_path=old_path,
                    group_dir=group_dir,
                    image_folder=image_folder,
                    html_path=html_path,
                    selector_path=selector_path,
                    output_png=image_folder.parent / f"{image_folder.name}.png",
                )
            )

    targets.sort(key=lambda t: (t.prefix.upper(), t.group_num, t.image_num, t.old_path.name.lower()))
    return targets, missing


def crop_compare_rmse(
    full_png: Path,
    old_png: Path,
    box: tuple[int, int, int, int],
    old_size: tuple[int, int],
    workdir: Path,
    suffix: str,
) -> float:
    x, y, w, h = box
    ow, oh = old_size
    if w <= 2 or h <= 2:
        return 1.0

    old_norm = workdir / "old_norm.png"
    if not old_norm.exists():
        proc_old = run_cmd([MAGICK, str(old_png), "-resize", f"{ow}x{oh}!", str(old_norm)])
        if proc_old.returncode != 0:
            return 1.0

    cand_norm = workdir / f"cand_{suffix}.png"
    proc_crop = run_cmd(
        [
            MAGICK,
            str(full_png),
            "-crop",
            f"{w}x{h}+{x}+{y}",
            "+repage",
            "-resize",
            f"{ow}x{oh}!",
            str(cand_norm),
        ]
    )
    if proc_crop.returncode != 0:
        return 1.0

    proc_cmp = run_cmd([MAGICK, "compare", "-metric", "RMSE", str(old_norm), str(cand_norm), "null:"])
    raw = (proc_cmp.stderr or proc_cmp.stdout or "").strip()
    match = re.search(r"\(([\d\.eE+-]+)\)", raw)
    if not match:
        return 1.0
    try:
        return float(match.group(1))
    except Exception:
        return 1.0


def clamp_box(x: float, y: float, w: float, h: float, vw: int, vh: int) -> tuple[int, int, int, int] | None:
    x1 = max(0, int(math.floor(x)))
    y1 = max(0, int(math.floor(y)))
    x2 = min(vw, int(math.ceil(x + w)))
    y2 = min(vh, int(math.ceil(y + h)))
    cw = x2 - x1
    ch = y2 - y1
    if cw <= 2 or ch <= 2:
        return None
    return x1, y1, cw, ch


def union_box(a: tuple[int, int, int, int], b: tuple[int, int, int, int], vw: int, vh: int) -> tuple[int, int, int, int] | None:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    x1 = min(ax, bx)
    y1 = min(ay, by)
    x2 = max(ax + aw, bx + bw)
    y2 = max(ay + ah, by + bh)
    return clamp_box(x1, y1, x2 - x1, y2 - y1, vw, vh)


def detect_visual_pattern(old_size: tuple[int, int]) -> str:
    ow, oh = old_size
    area = ow * oh
    aspect = ow / max(1, oh)
    if area <= 18000 or oh <= 140:
        return "micro-crop"
    if aspect >= 3.2 or ow >= 1800:
        return "layout-wide"
    if 0.65 <= aspect <= 1.6 and area <= 700000:
        return "modal-centered"
    return "composite"


def prefilter_candidates(
    candidates: list[Candidate],
    old_size: tuple[int, int],
    viewport_size: tuple[int, int],
    limit: int = 140,
) -> list[Candidate]:
    ow, oh = old_size
    vw, vh = viewport_size
    target_ar = max(0.001, ow / max(1, oh))
    old_area = max(1, ow * oh)
    pattern = detect_visual_pattern(old_size)

    scored = []
    for c in candidates:
        if c.w < 8 or c.h < 8:
            continue

        cand_ar = c.w / max(1, c.h)
        ar_ratio = cand_ar / target_ar
        if ar_ratio < 0.22 or ar_ratio > 4.5:
            continue

        if pattern == "layout-wide":
            min_h = max(110, int(vh * 0.16))
            min_w = max(320, int(vw * 0.32))
            if c.h < min_h or c.w < min_w:
                continue
        elif pattern == "micro-crop":
            if c.w > int(vw * 0.62) or c.h > int(vh * 0.48):
                continue
            hint = c.selector.lower()
            looks_interactive = (
                c.tag in {"button", "a", "gs-icon", "gs-tag", "input", "small", "span"}
                or "button" in hint
                or "icon" in hint
                or "tag" in hint
                or "qa-id" in hint
                or c.stable_hint >= 1
            )
            if not looks_interactive:
                continue
        elif pattern == "modal-centered":
            center_x = c.x + c.w / 2
            center_y = c.y + c.h / 2
            dist_center = abs(center_x - vw / 2) + abs(center_y - vh / 2)
            if dist_center > (vw + vh) * 0.45:
                continue

        ar_diff = abs(math.log(max(0.001, cand_ar / target_ar)))
        area = max(1, c.w * c.h)
        area_diff = abs(math.log(area / old_area))
        stable_bonus = -0.04 * c.stable_hint
        depth_penalty = 0.002 * c.depth
        pattern_bonus = 0.0
        if pattern == "modal-centered":
            center_x = c.x + c.w / 2
            center_y = c.y + c.h / 2
            center_score = (abs(center_x - vw / 2) + abs(center_y - vh / 2)) / max(1, vw + vh)
            pattern_bonus = center_score * 0.2
        score = ar_diff * 1.8 + area_diff * 0.35 + stable_bonus + depth_penalty + pattern_bonus
        scored.append((score, c))

    scored.sort(key=lambda item: item[0])
    return [candidate for _, candidate in scored[:limit]]


def confidence_label(best: float, second: float) -> str:
    margin = second - best
    if best <= 0.085 and margin >= 0.02:
        return "high"
    if best <= 0.14 and margin >= 0.01:
        return "medium"
    return "low"


def build_pre_capture_js(candidates: list[Candidate], old_size: tuple[int, int]) -> str | None:
    if len(candidates) < 2:
        return None
    pattern = detect_visual_pattern(old_size)
    if pattern not in {"layout-wide", "composite"}:
        return None

    sorted_candidates = sorted(candidates, key=lambda c: c.x)
    selectors = [c.selector for c in sorted_candidates[:2]]
    payload = json.dumps(selectors)
    return (
        "(() => {"
        f" const sels = {payload};"
        " document.querySelectorAll('body *').forEach((node) => node.removeAttribute('data-capture-anchor'));"
        " sels.forEach((sel, idx) => {"
        "   const el = document.querySelector(sel);"
        "   if (el) el.setAttribute('data-capture-anchor', `auto-anchor-${idx}`);"
        " });"
        "})();"
    )


async def collect_candidates(page) -> list[Candidate]:
    raw = await page.evaluate(
        """
        () => {
          const IGNORE_PREFIXES = ["ng-", "_ng", "cdk-", "mapboxgl-"];
          const IGNORE_CLASSES = new Set(["ng-star-inserted", "gs-text-ellipsis"]);

          const stableClasses = (el) => {
            const classes = (el.getAttribute("class") || "").split(/\\s+/).filter(Boolean);
            return classes.filter((cls) => !IGNORE_CLASSES.has(cls) && !IGNORE_PREFIXES.some((p) => cls.startsWith(p)));
          };

          const visible = (el) => {
            const st = getComputedStyle(el);
            if (st.display === "none" || st.visibility === "hidden" || st.opacity === "0") return false;
            const r = el.getBoundingClientRect();
            if (r.width < 8 || r.height < 8) return false;
            if (r.bottom <= 0 || r.right <= 0 || r.top >= window.innerHeight || r.left >= window.innerWidth) return false;
            return true;
          };

          const cssPath = (el) => {
            const parts = [];
            let cur = el;
            while (cur && cur.tagName && cur !== document.body) {
              let part = cur.tagName.toLowerCase();
              const parent = cur.parentElement;
              if (parent) {
                const siblings = Array.from(parent.children).filter((s) => s.tagName === cur.tagName);
                if (siblings.length > 1) {
                  const idx = siblings.indexOf(cur) + 1;
                  part += `:nth-of-type(${idx})`;
                } else {
                  const classes = stableClasses(cur).slice(0, 2);
                  if (classes.length) {
                    part += "." + classes.map((c) => CSS.escape(c)).join(".");
                  }
                }
              }
              parts.unshift(part);
              cur = parent;
            }
            return "body > " + parts.join(" > ");
          };

          const selectorFor = (el) => {
            const qa = el.getAttribute("data-qa-id") || el.getAttribute("gsqaid");
            if (qa) {
              const shortSel = `[data-qa-id="${CSS.escape(qa)}"]`;
              if (document.querySelectorAll(shortSel).length === 1) return shortSel;
              const tagSel = `${el.tagName.toLowerCase()}[data-qa-id="${CSS.escape(qa)}"]`;
              if (document.querySelectorAll(tagSel).length === 1) return tagSel;
            }

            if (el.id) {
              const idSel = `#${CSS.escape(el.id)}`;
              if (document.querySelectorAll(idSel).length === 1) return idSel;
            }

            const classes = stableClasses(el).slice(0, 2);
            if (classes.length) {
              const clsSel = `${el.tagName.toLowerCase()}.${classes.map((c) => CSS.escape(c)).join(".")}`;
              if (document.querySelectorAll(clsSel).length === 1) return clsSel;
            }

            const tag = el.tagName.toLowerCase();
            if (tag.includes("-") && document.querySelectorAll(tag).length === 1) {
              return tag;
            }

            return cssPath(el);
          };

          const all = Array.from(document.querySelectorAll("body *"));
          const out = [];
          const seen = new Set();

          for (const el of all) {
            if (!visible(el)) continue;
            const r = el.getBoundingClientRect();
            const selector = selectorFor(el);
            const key = `${selector}|${Math.round(r.left)}|${Math.round(r.top)}|${Math.round(r.width)}|${Math.round(r.height)}`;
            if (seen.has(key)) continue;
            seen.add(key);

            const qa = el.getAttribute("data-qa-id") || el.getAttribute("gsqaid");
            const stableHint = qa ? 3 : ((el.id ? 2 : 0) + ((el.tagName.toLowerCase().includes("-")) ? 1 : 0));

            let depth = 0;
            let cur = el;
            while (cur && cur !== document.body) {
              depth += 1;
              cur = cur.parentElement;
            }

            out.push({
              selector,
              x: r.left,
              y: r.top,
              w: r.width,
              h: r.height,
              tag: el.tagName.toLowerCase(),
              text_len: (el.innerText || "").trim().length,
              stable_hint: stableHint,
              depth,
            });
          }
          return out;
        }
        """
    )

    candidates: list[Candidate] = []
    for row in raw:
        candidates.append(
            Candidate(
                selector=row["selector"],
                x=int(round(row["x"])),
                y=int(round(row["y"])),
                w=int(round(row["w"])),
                h=int(round(row["h"])),
                tag=row["tag"],
                text_len=int(row["text_len"]),
                stable_hint=int(row["stable_hint"]),
                depth=int(row["depth"]),
            )
        )
    return candidates


async def process_target(target: Target, dry_run: bool = False, force_pair_search: bool = True) -> dict:
    from playwright.async_api import async_playwright

    old_size = image_size(target.old_path)
    ow, oh = old_size
    pattern = detect_visual_pattern(old_size)
    vw = max(1920, min(3200, int(max(ow * 1.1, 1280))))
    vh = max(1080, min(2000, int(max(oh * 1.4, 900))))

    result: dict = {
        "target_id": target.target_id,
        "prefix": target.prefix.upper(),
        "group_num": target.group_num,
        "image_num": target.image_num,
        "old": str(target.old_path),
        "html": str(target.html_path),
        "selector_path": str(target.selector_path),
        "output_png": str(target.output_png),
        "status": "error",
        "selector": None,
        "selectors": None,
        "score": None,
        "second_score": None,
        "confidence": "low",
        "pattern": pattern,
        "notes": "",
        "reviewed": False,
        "corrected_manually": False,
        "review_notes": "",
    }

    with tempfile.TemporaryDirectory(prefix="autoselect_old_") as td:
        tmp = Path(td)
        full_png = tmp / "full.png"

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={"width": vw, "height": vh},
                device_scale_factor=1,
            )
            page = await context.new_page()
            await page.goto(target.html_path.resolve().as_uri(), wait_until="load", timeout=30000)
            await page.wait_for_timeout(650)

            await page.screenshot(path=str(full_png))
            raw_candidates = await collect_candidates(page)
            await context.close()
            await browser.close()

        candidates: list[Candidate] = []
        for c in raw_candidates:
            box = clamp_box(c.x, c.y, c.w, c.h, vw, vh)
            if not box:
                continue
            x, y, w, h = box
            if w < 12 or h < 12:
                continue
            candidates.append(Candidate(c.selector, x, y, w, h, c.tag, c.text_len, c.stable_hint, c.depth))

        if not candidates:
            result["notes"] = "Sin candidatos visibles"
            return result

        shortlist = prefilter_candidates(candidates, old_size, (vw, vh), limit=160)
        if not shortlist:
            result["notes"] = "Shortlist vacío"
            return result

        scored: list[tuple[float, int, tuple[int, int, int, int]]] = []
        for idx, candidate in enumerate(shortlist):
            pad = 6 if (candidate.w * candidate.h) < 160000 else 2
            box = clamp_box(candidate.x - pad, candidate.y - pad, candidate.w + pad * 2, candidate.h + pad * 2, vw, vh)
            if not box:
                continue
            rmse = crop_compare_rmse(full_png, target.old_path, box, old_size, tmp, f"s_{idx}")
            scored.append((rmse, idx, box))

        if not scored:
            result["notes"] = "No se pudieron evaluar candidatos"
            return result

        scored.sort(key=lambda item: item[0])
        best_rmse, best_idx, best_box = scored[0]
        second_rmse = scored[1][0] if len(scored) > 1 else 1.0

        selected_candidates = [shortlist[best_idx]]
        selected_box = best_box
        selected_rmse = best_rmse

        if force_pair_search and len(scored) >= 2:
            top_n = min(16, len(scored))
            pair_best_rmse = best_rmse
            pair_best: tuple[int, int, tuple[int, int, int, int]] | None = None

            for ia in range(top_n):
                for ib in range(ia + 1, top_n):
                    _, idx_a, box_a = scored[ia]
                    _, idx_b, box_b = scored[ib]
                    ubox = union_box(box_a, box_b, vw, vh)
                    if not ubox:
                        continue
                    rmse = crop_compare_rmse(full_png, target.old_path, ubox, old_size, tmp, f"p_{ia}_{ib}")
                    if rmse < pair_best_rmse:
                        pair_best_rmse = rmse
                        pair_best = (idx_a, idx_b, ubox)

            if pair_best and pair_best_rmse + 0.007 < best_rmse:
                idx_a, idx_b, ubox = pair_best
                selected_candidates = [shortlist[idx_a], shortlist[idx_b]]
                selected_box = ubox
                selected_rmse = pair_best_rmse

        selectors = [candidate.selector for candidate in selected_candidates]
        confidence = confidence_label(selected_rmse, second_rmse)
        pre_capture_js = build_pre_capture_js(selected_candidates, old_size)

        result["score"] = round(selected_rmse, 6)
        result["second_score"] = round(second_rmse, 6)
        result["confidence"] = confidence
        result["notes"] = f"bbox={selected_box[2]}x{selected_box[3]}"

        config = {
            "bbox_mode": "element",
            "description": f"Auto ({target.old_path.name})",
            "padding": 10,
        }
        if len(selectors) == 1:
            result["selector"] = selectors[0]
            config["selector"] = selectors[0]
        else:
            result["selectors"] = selectors
            config["selectors"] = selectors
            config["description"] = f"Auto par ({target.old_path.name})"

        if pre_capture_js:
            config["pre_capture_js"] = pre_capture_js
            result["pre_capture_js"] = pre_capture_js

        if not dry_run:
            target.selector_path.parent.mkdir(parents=True, exist_ok=True)
            target.selector_path.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        result["status"] = "ok"
        return result


async def run(args):
    assert_dependencies()

    targets, missing = discover_targets(
        lang=args.lang,
        prefix_arg=args.prefix,
        from_group=args.from_group,
        from_image=args.from_image,
        to_group=args.to_group,
        include_existing=args.include_existing,
    )

    report_path = build_report_path(args.lang, args.prefix, args.from_group, args.to_group)
    existing_review_state = load_existing_review_state(report_path)

    print("=" * 72)
    print("Auto Selector From Old")
    print("=" * 72)
    print(f"Idioma: {args.lang}")
    print(f"Prefijo(s): {args.prefix}")
    print(f"Rango: grupo {args.from_group} -> {args.to_group} | desde imagen {args.from_image}")
    print(f"Targets a procesar: {len(targets)}")
    print(f"Omitidos por falta de HTML/carpeta: {len(missing)}")
    print(f"Dry run: {args.dry_run}")
    print("=" * 72)

    if missing:
        for prefix, group_num, image_num, reason in missing:
            print(f"  ⚠️  {prefix}{group_num}_imagen{image_num}: {reason}")

    if not targets:
        print("No hay targets para procesar.")
        return

    report: list[dict] = []
    ok = 0
    fail = 0

    for target in targets:
        print(f"\n📌 {target.prefix.upper()}{target.group_num}_imagen{target.image_num} ({target.old_path.name})")
        try:
            res = await process_target(target, dry_run=args.dry_run, force_pair_search=not args.no_pair_search)
            review_state = existing_review_state.get(target.target_id, {})
            res["reviewed"] = bool(review_state.get("reviewed", False))
            res["corrected_manually"] = bool(review_state.get("corrected_manually", False))
            res["review_notes"] = review_state.get("review_notes", "")
            report.append(res)
            if res["status"] == "ok":
                ok += 1
                selector_mode = "selectors=2" if res.get("selectors") else "selector=1"
                print(f"  ✅ {selector_mode:<12} score={res['score']} conf={res['confidence']} pattern={res['pattern']}")
                if args.verbose:
                    print(f"     {json.dumps(res, ensure_ascii=False)}")
            else:
                fail += 1
                print(f"  ❌ {res.get('notes', 'falló')}")
        except Exception as exc:
            fail += 1
            print(f"  ❌ Error: {exc}")
            report.append(
                {
                    "target_id": target.target_id,
                    "prefix": target.prefix.upper(),
                    "group_num": target.group_num,
                    "image_num": target.image_num,
                    "old": str(target.old_path),
                    "html": str(target.html_path),
                    "selector_path": str(target.selector_path),
                    "output_png": str(target.output_png),
                    "status": "error",
                    "notes": str(exc),
                    "reviewed": bool(existing_review_state.get(target.target_id, {}).get("reviewed", False)),
                    "corrected_manually": bool(existing_review_state.get(target.target_id, {}).get("corrected_manually", False)),
                    "review_notes": existing_review_state.get(target.target_id, {}).get("review_notes", ""),
                }
            )

    low_conf = [row for row in report if row.get("status") == "ok" and row.get("confidence") == "low"]
    medium_conf = [row for row in report if row.get("status") == "ok" and row.get("confidence") == "medium"]

    print("\n" + "=" * 72)
    print(f"Resultado: ok={ok}  fail={fail}  low_conf={len(low_conf)}  medium_conf={len(medium_conf)}")
    print("=" * 72)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Reporte: {report_path}")

    if low_conf:
        print("\nCasos de baja confianza (revisar):")
        for row in low_conf[:30]:
            print(f"  - {row['prefix']}{row['group_num']}_imagen{row['image_num']}  score={row['score']}")


def main():
    ensure_playwright_runtime()
    parser = argparse.ArgumentParser(description="Genera selector.json desde imágenes *_old.png")
    parser.add_argument("--lang", default="Español", help="Idioma/carpeta base (default: Español)")
    parser.add_argument("--prefix", default="all", help="Prefijo(s) de serie: O | P | RT | O,RT,D | all")
    parser.add_argument("--from-group", type=int, default=1, help="Grupo inicial (default: 1)")
    parser.add_argument("--from-image", type=int, default=1, help="Imagen inicial dentro de from-group (default: 1)")
    parser.add_argument("--to-group", type=int, default=9999, help="Grupo final (default: 9999)")
    parser.add_argument("--include-existing", action="store_true", help="También procesar carpetas con selector.json existente")
    parser.add_argument("--dry-run", action="store_true", help="No escribir selector.json")
    parser.add_argument("--no-pair-search", action="store_true", help="Desactiva búsqueda de combinación de 2 selectores")
    parser.add_argument("--verbose", action="store_true", help="Imprime detalle JSON por target")
    args = parser.parse_args()

    asyncio.run(run(args))


if __name__ == "__main__":
    main()
