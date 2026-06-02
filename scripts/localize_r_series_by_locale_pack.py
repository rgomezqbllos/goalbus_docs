#!/usr/bin/env python3
"""
Localize R1/R2 screenshots from the official locale packs.

This deliberately lets the per-language JSON files drive translation:
  - Source text is matched against es.json to obtain the semantic key.
  - Target text is read from the target locale pack only.
  - Missing target keys are left in Spanish and reported.
  - Operational identifiers/codes are preserved.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import shutil
import unicodedata
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_LANG_FOLDER = "Español"
TARGETS = {
    "EN": ("English", "en.json"),
    "PT_BR": ("Portugues", "pt_br.json"),
    "IT": ("Italiano", "it.json"),
    "DE": ("Deutsch", "de.json"),
    "FR": ("Frances", "fr.json"),
}
SERIES_FOLDERS = [
    "R1/R1_imagen1",
    "R1/R1_imagen2",
    "R1/R1_imagen3",
    "R2/R2_imagen1",
    "R2/R2_imagen2",
    "R2/R2_imagen3",
    "R2/R2_imagen4",
]


PRESERVE_RE = re.compile(
    r"^(?:"
    r"GoalBus|SITEUR GDL / Hola Consultant|C|"
    r"TEST GOAL(?: 2)?|T01 HSD SIN DESC|"
    r"Veh_\d+|T\d+[A-Z]?|PKT\d+|"
    r"\d+_\d+|\d+(?:\.\d+)?x \(\d+ h\)|"
    r"\d+ h|\d+ kWh|"
    r"ELEC(?: .*)?|LUMINUS|DP TALLERES.*|"
    r"Aeropuerto - .+"
    r")$"
)


class VisibleTextParser(HTMLParser):
    """Collect visible-ish text nodes for the saved GoalBus HTML."""

    SKIP = {"script", "style", "noscript", "template", "code"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.texts: list[str] = []

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag.lower())

    def handle_endtag(self, tag):
        tag = tag.lower()
        for idx in range(len(self.stack) - 1, -1, -1):
            if self.stack[idx] == tag:
                del self.stack[idx:]
                break

    def handle_data(self, data):
        if any(tag in self.SKIP for tag in self.stack):
            return
        text = " ".join(data.split()).strip()
        if text:
            self.texts.append(text)


def normalize(text: str) -> str:
    value = html.unescape(text or "")
    value = unicodedata.normalize("NFKC", value).strip().lower()
    return re.sub(r"\s+", " ", value)


def load_pack(filename: str) -> dict[str, str]:
    path = ROOT / filename
    data = json.loads(path.read_text(encoding="utf-8"))
    return {k: v for k, v in data.items() if isinstance(v, str)}


def build_reverse_index(pack: dict[str, str]) -> dict[str, str]:
    index: dict[str, str] = {}
    for key, value in pack.items():
        norm = normalize(value)
        if norm:
            index.setdefault(norm, key)
    return index


def collect_texts(html_path: Path) -> list[str]:
    parser = VisibleTextParser()
    parser.feed(html_path.read_text(encoding="utf-8", errors="replace"))
    seen: set[str] = set()
    result: list[str] = []
    for text in parser.texts:
        if len(text) > 120:
            continue
        if re.fullmatch(r"[\d\s:.,%_\-]+", text):
            continue
        if text not in seen:
            seen.add(text)
            result.append(text)
    return result


def replace_text(content: str, source: str, target: str) -> tuple[str, int]:
    if not source or source == target:
        return content, 0
    count = content.count(source)
    if not count:
        return content, 0
    return content.replace(source, target), count


def build_translation_rows(
    es_pack: dict[str, str],
    es_index: dict[str, str],
    target_lang: str,
    target_pack: dict[str, str],
    en_pack: dict[str, str],
) -> tuple[list[dict[str, str]], dict[str, str]]:
    rows: list[dict[str, str]] = []
    replacements: dict[str, str] = {}

    source_root = ROOT / SOURCE_LANG_FOLDER
    for rel in SERIES_FOLDERS:
        html_path = source_root / rel / "GoalBus.html"
        for source_text in collect_texts(html_path):
            key = es_index.get(normalize(source_text))
            status = "pack"
            target_text = ""
            if key:
                target_text = target_pack.get(key, "")
                if target_text:
                    replacements[source_text] = target_text
                else:
                    target_text = en_pack.get(key, "")
                    if target_text:
                        status = "fallback_en"
                        replacements[source_text] = target_text
                    else:
                        status = "missing_target"
            elif PRESERVE_RE.match(source_text):
                status = "preserved"
                target_text = source_text
            else:
                status = "missing_source_key"
                target_text = source_text

            rows.append(
                {
                    "folder": rel.replace("/", "\\"),
                    "target_lang": target_lang,
                    "status": status,
                    "key": key or "",
                    "source_es": source_text,
                    "target": target_text,
                    "source_pack_value": es_pack.get(key or "", ""),
                }
            )
    return rows, replacements


def reset_target_dirs(target_folder: str) -> None:
    for series in ("R1", "R2"):
        target_dir = ROOT / target_folder / series
        resolved = target_dir.resolve()
        expected_parent = (ROOT / target_folder).resolve()
        if not str(resolved).startswith(str(expected_parent)):
            raise RuntimeError(f"Refusing to delete unexpected path: {resolved}")
        if target_dir.exists():
            shutil.rmtree(target_dir)


def copy_source_tree(target_folder: str) -> None:
    for series in ("R1", "R2"):
        src = ROOT / SOURCE_LANG_FOLDER / series
        dst = ROOT / target_folder / series
        shutil.copytree(src, dst)
        for old_png in dst.glob("*_old.png"):
            old_png.unlink()
        for selector_path in dst.glob("R*_imagen*/selector.json"):
            config = json.loads(selector_path.read_text(encoding="utf-8"))
            config["selectors"] = [
                "otto-web-grid-header"
                if isinstance(selector, str) and selector.startswith("otto-web-grid-header")
                else selector
                for selector in config.get("selectors", [])
            ]
            selector_path.write_text(
                json.dumps(config, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )


def localize_html(target_folder: str, replacements: dict[str, str]) -> None:
    for rel in SERIES_FOLDERS:
        html_path = ROOT / target_folder / rel / "GoalBus.html"
        content = html_path.read_text(encoding="utf-8", errors="replace")
        for source, target in sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True):
            content, _ = replace_text(content, source, target)
        html_path.write_text(content, encoding="utf-8")


def write_report(rows: list[dict[str, str]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "folder",
                "target_lang",
                "status",
                "key",
                "source_es",
                "target",
                "source_pack_value",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--targets", default="EN,PT_BR,IT,DE,FR")
    parser.add_argument("--report", default="scratch/r_series_locale_pack_report.tsv")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    es_pack = load_pack("es.json")
    en_pack = load_pack("en.json")
    es_index = build_reverse_index(es_pack)
    all_rows: list[dict[str, str]] = []

    for lang in [item.strip().upper() for item in args.targets.split(",") if item.strip()]:
        if lang not in TARGETS:
            raise SystemExit(f"Unknown target: {lang}")
        target_folder, filename = TARGETS[lang]
        target_pack = load_pack(filename)
        rows, replacements = build_translation_rows(es_pack, es_index, lang, target_pack, en_pack)
        all_rows.extend(rows)
        if not args.dry_run:
            reset_target_dirs(target_folder)
            copy_source_tree(target_folder)
            localize_html(target_folder, replacements)
        counts: dict[str, int] = {}
        for row in rows:
            counts[row["status"]] = counts.get(row["status"], 0) + 1
        print(f"{lang}: {counts}")

    write_report(all_rows, ROOT / args.report)
    print(f"Report: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
