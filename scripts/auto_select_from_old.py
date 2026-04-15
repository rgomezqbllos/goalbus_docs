#!/usr/bin/env python3
"""
Auto selector builder from *_old.png references.

Workflow:
1) For each old image, load the matching HTML with Playwright.
2) Enumerate visible DOM candidates with stable-ish selectors.
3) Compare candidate crops vs old reference with ImageMagick RMSE.
4) Write selector.json with best candidate (or best pair if better).

Default scope (if no --target):
  Español, from P5_imagen3 up to P27.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import math
import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
MAGICK = "/opt/homebrew/bin/magick"


@dataclass
class Target:
    page: int
    image_num: int
    old_path: Path
    image_folder: Path
    html_path: Path
    selector_path: Path


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


def parse_old_name(path: Path) -> tuple[int, int] | None:
    # Example: P5_Imagen3_old.png
    m = re.match(r"^P(\d+)_Imagen(\d+)_old\.png$", path.name)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def find_html_file(image_folder: Path) -> Path | None:
    for name in ("GoalBus.html", "GoalBus Settings.html"):
        p = image_folder / name
        if p.exists():
            return p
    for p in image_folder.glob("*.html"):
        if "_files" not in p.name and "_test" not in p.name:
            return p
    return None


def discover_targets(
    lang: str = "Español",
    from_page: int = 5,
    from_image: int = 3,
    to_page: int = 27,
    include_existing: bool = False,
) -> tuple[list[Target], list[tuple[int, int, str]]]:
    lang_dir = BASE_DIR / lang
    targets: list[Target] = []
    missing: list[tuple[int, int, str]] = []

    if not lang_dir.exists():
        return targets, missing

    for page in range(from_page, to_page + 1):
        page_dir = lang_dir / f"P{page}"
        if not page_dir.exists():
            continue

        for old_path in sorted(page_dir.glob(f"P{page}_Imagen*_old.png")):
            parsed = parse_old_name(old_path)
            if not parsed:
                continue
            _, image_num = parsed
            if page == from_page and image_num < from_image:
                continue

            image_folder = page_dir / f"P{page}_imagen{image_num}"
            html_path = find_html_file(image_folder)
            selector_path = image_folder / "selector.json"
            if not html_path:
                missing.append((page, image_num, f"Falta HTML en {image_folder}"))
                continue
            if selector_path.exists() and not include_existing:
                continue

            targets.append(
                Target(
                    page=page,
                    image_num=image_num,
                    old_path=old_path,
                    image_folder=image_folder,
                    html_path=html_path,
                    selector_path=selector_path,
                )
            )

    targets.sort(key=lambda t: (t.page, t.image_num))
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
        proc_old = run_cmd(
            [
                MAGICK,
                str(old_png),
                "-resize",
                f"{ow}x{oh}!",
                str(old_norm),
            ]
        )
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
    # Example: "1204.51 (0.0183796)"
    m = re.search(r"\(([\d\.eE+-]+)\)", raw)
    if not m:
        return 1.0
    try:
        return float(m.group(1))
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
    scored = []
    for c in candidates:
        if c.w < 8 or c.h < 8:
            continue

        car = c.w / max(1, c.h)
        ar_ratio = car / target_ar
        # Evita bandas extremadamente horizontales/verticales respecto a la referencia.
        if ar_ratio < 0.25 or ar_ratio > 4.0:
            continue

        # Si la referencia es grande, forzar candidatos de tamaño suficientemente grande.
        if old_area > 500_000:
            min_h = max(120, int(vh * 0.18))
            min_w = max(350, int(vw * 0.35))
            if c.h < min_h or c.w < min_w:
                continue

        # Si la referencia es pequeña (iconos/botones), evitar contenedores gigantes.
        if old_area < 15_000:
            if c.w > int(vw * 0.55) or c.h > int(vh * 0.45):
                continue
            small_hint = c.selector.lower()
            looks_interactive = (
                c.tag in {"button", "a", "gs-icon", "gs-tag", "input"}
                or "button" in small_hint
                or "icon" in small_hint
                or "tag" in small_hint
                or "qa-id" in small_hint
                or c.stable_hint >= 1
            )
            if not looks_interactive:
                continue

        ar_diff = abs(math.log(max(0.001, car / target_ar)))
        area = max(1, c.w * c.h)
        area_diff = abs(math.log(area / old_area))
        stable_bonus = -0.04 * c.stable_hint
        depth_penalty = 0.002 * c.depth
        score = ar_diff * 1.8 + area_diff * 0.35 + stable_bonus + depth_penalty
        scored.append((score, c))
    scored.sort(key=lambda t: t[0])
    return [c for _, c in scored[:limit]]


def confidence_label(best: float, second: float) -> str:
    margin = second - best
    if best <= 0.085 and margin >= 0.02:
        return "high"
    if best <= 0.14 and margin >= 0.01:
        return "medium"
    return "low"


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

    ow, oh = image_size(target.old_path)
    vw = max(1920, min(3200, int(max(ow * 1.1, 1280))))
    vh = max(1080, min(2000, int(max(oh * 1.4, 900))))

    result: dict = {
        "page": target.page,
        "image_num": target.image_num,
        "old": str(target.old_path),
        "html": str(target.html_path),
        "selector_path": str(target.selector_path),
        "status": "error",
        "selector": None,
        "selectors": None,
        "score": None,
        "second_score": None,
        "confidence": "low",
        "notes": "",
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

        # Clamp and filter candidates
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

        shortlist = prefilter_candidates(candidates, (ow, oh), (vw, vh), limit=140)
        if not shortlist:
            result["notes"] = "Shortlist vacío"
            return result

        scored: list[tuple[float, int, tuple[int, int, int, int]]] = []
        for i, c in enumerate(shortlist):
            pad = 6 if (c.w * c.h) < 160000 else 2
            box = clamp_box(c.x - pad, c.y - pad, c.w + pad * 2, c.h + pad * 2, vw, vh)
            if not box:
                continue
            rmse = crop_compare_rmse(full_png, target.old_path, box, (ow, oh), tmp, f"s_{i}")
            scored.append((rmse, i, box))

        if not scored:
            result["notes"] = "No se pudieron evaluar candidatos"
            return result

        scored.sort(key=lambda t: t[0])
        best_rmse, best_idx, best_box = scored[0]
        second_rmse = scored[1][0] if len(scored) > 1 else 1.0
        best_selector = shortlist[best_idx].selector

        selected_selectors = [best_selector]
        selected_box = best_box
        selected_rmse = best_rmse

        # Optional pair search among top-N singles
        if force_pair_search and len(scored) >= 2:
            top_n = min(12, len(scored))
            pair_best_rmse = best_rmse
            pair_best: tuple[int, int, tuple[int, int, int, int]] | None = None

            for ia in range(top_n):
                for ib in range(ia + 1, top_n):
                    _, idx_a, box_a = scored[ia]
                    _, idx_b, box_b = scored[ib]
                    ubox = union_box(box_a, box_b, vw, vh)
                    if not ubox:
                        continue
                    rmse = crop_compare_rmse(full_png, target.old_path, ubox, (ow, oh), tmp, f"p_{ia}_{ib}")
                    if rmse < pair_best_rmse:
                        pair_best_rmse = rmse
                        pair_best = (idx_a, idx_b, ubox)

            if pair_best and pair_best_rmse + 0.007 < best_rmse:
                idx_a, idx_b, ubox = pair_best
                selected_selectors = [shortlist[idx_a].selector, shortlist[idx_b].selector]
                selected_box = ubox
                selected_rmse = pair_best_rmse

        confidence = confidence_label(selected_rmse, second_rmse)
        result["score"] = round(selected_rmse, 6)
        result["second_score"] = round(second_rmse, 6)
        result["confidence"] = confidence

        if len(selected_selectors) == 1:
            result["selector"] = selected_selectors[0]
            config = {
                "selector": selected_selectors[0],
                "bbox_mode": "element",
                "description": f"Auto ({target.old_path.name})",
                "padding": 10,
            }
        else:
            result["selectors"] = selected_selectors
            config = {
                "selectors": selected_selectors,
                "bbox_mode": "element",
                "description": f"Auto par ({target.old_path.name})",
                "padding": 10,
            }

        if not dry_run:
            target.selector_path.parent.mkdir(parents=True, exist_ok=True)
            target.selector_path.write_text(json.dumps(config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        result["status"] = "ok"
        result["notes"] = f"bbox={selected_box[2]}x{selected_box[3]}"
        return result


async def run(args):
    assert_dependencies()

    targets, missing = discover_targets(
        lang=args.lang,
        from_page=args.from_page,
        from_image=args.from_image,
        to_page=args.to_page,
        include_existing=args.include_existing,
    )

    print("=" * 72)
    print("Auto Selector From Old")
    print("=" * 72)
    print(f"Idioma: {args.lang}")
    print(f"Rango: P{args.from_page}_imagen{args.from_image} -> P{args.to_page}")
    print(f"Targets a procesar: {len(targets)}")
    print(f"Omitidos por falta de HTML: {len(missing)}")
    print(f"Dry run: {args.dry_run}")
    print("=" * 72)

    if missing:
        for page, img, reason in missing:
            print(f"  ⚠️  P{page}_imagen{img}: {reason}")

    if not targets:
        print("No hay targets para procesar.")
        return

    report: list[dict] = []
    ok = 0
    fail = 0

    for t in targets:
        print(f"\n📌 P{t.page}_imagen{t.image_num}  ({t.old_path.name})")
        try:
            res = await process_target(t, dry_run=args.dry_run, force_pair_search=not args.no_pair_search)
            report.append(res)
            if res["status"] == "ok":
                ok += 1
                score = res["score"]
                conf = res["confidence"]
                if res.get("selectors"):
                    print(f"  ✅ selectors=2  score={score}  conf={conf}")
                else:
                    print(f"  ✅ selector=1   score={score}  conf={conf}")
                if args.verbose:
                    print(f"     {json.dumps(res, ensure_ascii=False)}")
            else:
                fail += 1
                print(f"  ❌ {res.get('notes','falló')}")
        except Exception as e:
            fail += 1
            print(f"  ❌ Error: {e}")
            report.append(
                {
                    "page": t.page,
                    "image_num": t.image_num,
                    "old": str(t.old_path),
                    "status": "error",
                    "notes": str(e),
                }
            )

    low_conf = [r for r in report if r.get("status") == "ok" and r.get("confidence") == "low"]
    medium_conf = [r for r in report if r.get("status") == "ok" and r.get("confidence") == "medium"]

    print("\n" + "=" * 72)
    print(f"Resultado: ok={ok}  fail={fail}  low_conf={len(low_conf)}  medium_conf={len(medium_conf)}")
    print("=" * 72)

    report_path = BASE_DIR / "scratch" / "auto_select_from_old_report_es_p5_p27.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Reporte: {report_path}")

    if low_conf:
        print("\nCasos de baja confianza (revisar):")
        for r in low_conf[:30]:
            print(f"  - P{r['page']}_imagen{r['image_num']}  score={r['score']}")


def main():
    parser = argparse.ArgumentParser(description="Genera selector.json desde imágenes *_old.png")
    parser.add_argument("--lang", default="Español", help="Idioma/carpeta base (default: Español)")
    parser.add_argument("--from-page", type=int, default=5, help="Página inicial (default: 5)")
    parser.add_argument("--from-image", type=int, default=3, help="Imagen inicial dentro de from-page (default: 3)")
    parser.add_argument("--to-page", type=int, default=27, help="Página final (default: 27)")
    parser.add_argument("--include-existing", action="store_true", help="También procesar carpetas con selector.json existente")
    parser.add_argument("--dry-run", action="store_true", help="No escribir selector.json")
    parser.add_argument("--no-pair-search", action="store_true", help="Desactiva búsqueda de combinación de 2 selectores")
    parser.add_argument("--verbose", action="store_true", help="Imprime detalle JSON por target")
    args = parser.parse_args()

    asyncio.run(run(args))


if __name__ == "__main__":
    main()
