#!/usr/bin/env python3
"""Split translation_data.csv into pure data + ui_strings.json.

Background
----------
`translation_data.csv` today mixes two kinds of rows:

  1. **Configuration data**: short codes like `L1`, `T001`, terminal names —
     values that are literally pulled from the user's GoalBus configuration.
     These belong in the CSV.
  2. **UI labels**: full sentences like "Día Laborable estándar - L1" or
     "Servicio comercial laborable" that happen to live inside form fields
     (`<input value="...">`). These are UI copy and belong with the rest of
     the localized strings, not with config data.

Mixing the two makes the CSV painful to maintain (which is the user's exact
complaint). This script:

  - Reads `translation_data.csv`
  - Classifies each row as **ui** or **data** using a heuristic on the ES value
  - Writes UI rows to `ui_strings.json` (merged with anything already there)
  - Rewrites the CSV with only data rows
  - Defaults to `--dry-run` so you can review the split before applying

Run
---
    # Preview without changing anything (default):
    python3 scripts/migrate_csv_to_ui_strings.py

    # Apply the split:
    python3 scripts/migrate_csv_to_ui_strings.py --apply
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = REPO_ROOT / "translation_data.csv"
UI_JSON_PATH = REPO_ROOT / "ui_strings.json"

CSV_LANGS = ("ES", "PT_BR", "EN", "FR", "IT", "DE")
TYPES_THAT_CAN_BE_UI = frozenset({"input_value", "field_value"})

# A row is treated as a UI label (not configuration data) when its primary
# value (ES, falling back to EN) looks like a full sentence rather than a
# short code/identifier.
_CODE_RE = re.compile(r"^[A-Z0-9][A-Z0-9_\-./:\s]{0,15}$")
_HAS_LETTER_RE = re.compile(r"[A-Za-zÀ-ÿ]")


def _primary_value(row: dict) -> str:
    """Pick the most representative source value for classification.

    Prefer ES (the source-of-truth language for this project), then EN, then
    any non-empty language column.
    """
    for lang in ("ES", "EN") + CSV_LANGS:
        v = (row.get(lang) or "").strip()
        if v:
            return v
    return ""


def classify_row(row: dict) -> str:
    """Return 'ui' or 'data' for a CSV row.

    Heuristic for 'ui':
      - type is input_value or field_value
      - ES (or fallback) is non-empty
      - the value contains letters (not pure numeric/code)
      - the value has at least 2 words OR is longer than 18 chars
      - the value is NOT a short uppercase code like "L1", "T001", "TERMINAL"

    Everything else stays as 'data', including:
      - empty rows (nothing to translate yet)
      - short codes like "L1", "T001"
      - terminal names in upper case (kept as data even if multi-word — they
        are real configuration values; the localizer already handles them)
      - checkbox_checked / date_picker / class_indexed types
    """
    if (row.get("type") or "").strip() not in TYPES_THAT_CAN_BE_UI:
        return "data"

    value = _primary_value(row)
    if not value:
        return "data"
    if not _HAS_LETTER_RE.search(value):
        return "data"

    # Pure uppercase short codes / terminal-style names live in config.
    if value.isupper() and len(value) <= 30:
        return "data"

    # Short bare-code patterns: "L1", "T001", "L1 - 1"
    if _CODE_RE.match(value):
        return "data"

    word_count = len(value.split())
    if word_count >= 2:
        return "ui"
    if len(value) > 18:
        return "ui"
    return "data"


def _row_key(row: dict) -> str:
    return f"{row.get('folder', '')}|{row.get('field_id', '')}"


def _row_to_entry(row: dict) -> dict:
    entry = {"type": (row.get("type") or "").strip()}
    for lang in CSV_LANGS:
        v = (row.get(lang) or "").strip()
        if v:
            entry[lang] = v
    return entry


def load_existing_ui_strings() -> dict:
    if UI_JSON_PATH.exists():
        try:
            data = json.loads(UI_JSON_PATH.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except json.JSONDecodeError:
            pass
    return {}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to ui_strings.json and translation_data.csv. "
             "Without this flag, runs in dry-run mode (default).",
    )
    args = parser.parse_args()

    if not CSV_PATH.exists():
        print(f"ERROR: {CSV_PATH} not found")
        return 1

    with CSV_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    ui_rows = []
    data_rows = []
    for row in rows:
        if classify_row(row) == "ui":
            ui_rows.append(row)
        else:
            data_rows.append(row)

    print(f"CSV: {len(rows)} total rows")
    print(f"  -> ui   : {len(ui_rows)}")
    print(f"  -> data : {len(data_rows)}")

    # Group UI rows by folder for readable preview / output.
    by_folder = {}
    for row in ui_rows:
        by_folder.setdefault(row.get("folder", ""), []).append(row)

    print()
    print("UI rows preview (first 12):")
    for row in ui_rows[:12]:
        v = _primary_value(row)
        print(f"  [{row['folder']}/{row['field_id']:<14}] {v[:60]}")
    if len(ui_rows) > 12:
        print(f"  ... and {len(ui_rows) - 12} more")

    if not args.apply:
        print()
        print("Dry run — no files modified. Re-run with --apply to write changes.")
        return 0

    # --- Apply ---

    # 1. Merge into ui_strings.json (existing entries win on conflict so we
    #    don't clobber manual edits made directly in the JSON).
    existing = load_existing_ui_strings()
    added = 0
    for row in ui_rows:
        key = _row_key(row)
        if key in existing:
            continue
        existing[key] = _row_to_entry(row)
        added += 1

    UI_JSON_PATH.write_text(
        json.dumps(existing, indent=2, ensure_ascii=False, sort_keys=True),
        encoding="utf-8",
    )
    print()
    print(f"ui_strings.json: {added} new entries added "
          f"({len(existing)} total)")

    # 2. Rewrite CSV with data rows only.
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_rows)
    print(f"translation_data.csv: rewritten with {len(data_rows)} data rows "
          f"(removed {len(ui_rows)})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
