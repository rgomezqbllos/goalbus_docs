#!/usr/bin/env python3
import argparse
import csv
import json
from pathlib import Path


def build_value_map(en_path: Path, target_path: Path) -> dict[str, str]:
    en_data = json.loads(en_path.read_text(encoding="utf-8"))
    target_data = json.loads(target_path.read_text(encoding="utf-8"))
    value_map: dict[str, str] = {}
    for key, en_val in en_data.items():
        if not isinstance(en_val, str):
            continue
        target_val = target_data.get(key)
        if isinstance(target_val, str) and target_val.strip():
            value_map[en_val.strip()] = target_val.strip()
    return value_map


def apply_global(global_path: Path, value_map: dict[str, str], lang_code: str) -> tuple[int, int]:
    data = json.loads(global_path.read_text(encoding="utf-8"))
    updated = 0
    unresolved = 0
    for entry in data.values():
        en_val = (entry.get("EN") or "").strip()
        if not en_val:
            continue
        mapped = value_map.get(en_val)
        if mapped:
            if entry.get(lang_code) != mapped:
                entry[lang_code] = mapped
                updated += 1
        else:
            unresolved += 1
    global_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return updated, unresolved


def apply_csv(csv_path: Path, value_map: dict[str, str], lang_code: str) -> tuple[int, int]:
    rows: list[dict[str, str]] = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        if lang_code not in fieldnames:
            fieldnames.append(lang_code)
        for row in reader:
            rows.append(row)

    updated = 0
    unresolved = 0
    for row in rows:
        en_val = (row.get("EN") or "").strip()
        if not en_val:
            continue
        mapped = value_map.get(en_val)
        if mapped:
            if (row.get(lang_code) or "").strip() != mapped:
                row[lang_code] = mapped
                updated += 1
        else:
            unresolved += 1

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return updated, unresolved


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply locale pack EN->target for global and CSV.")
    parser.add_argument("--root", default=".", help="Project root")
    parser.add_argument("--lang", default="DE", help="Target language code (e.g. DE)")
    parser.add_argument("--target-json", default="de.json", help="Target locale json file")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    en_path = root / "en.json"
    target_path = root / args.target_json
    global_path = root / "global_translations.json"
    csv_path = root / "translation_data.csv"

    required = [en_path, target_path, global_path, csv_path]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        print("ERROR: Missing required files:")
        for p in missing:
            print(f"  - {p}")
        return 1

    value_map = build_value_map(en_path, target_path)
    if not value_map:
        print("ERROR: EN->target value map is empty.")
        return 1

    g_updated, g_unresolved = apply_global(global_path, value_map, args.lang)
    c_updated, c_unresolved = apply_csv(csv_path, value_map, args.lang)

    print(f"Applied language pack for {args.lang}")
    print(f"  value_map_entries: {len(value_map)}")
    print(f"  global_updated:    {g_updated}")
    print(f"  global_unresolved: {g_unresolved}")
    print(f"  csv_updated:       {c_updated}")
    print(f"  csv_unresolved:    {c_unresolved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
