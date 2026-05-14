#!/usr/bin/env python3
"""
Pipeline asistido para series GoalBus basadas en referencias *_old.png.

Orden:
1. init (todos los idiomas destino)
2. extract (Español)
3. verificar pendientes
4. build_all
5. auto_select_from_old
6. capture_screenshots
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from series_utils import iter_series_group_dirs, parse_prefix_arg


BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_TARGET_LANGS = ["EN", "PT_BR", "DE", "FR", "IT"]


def run_checked(cmd: list[str]) -> int:
    print(f"▶ {' '.join(cmd)}")
    proc = subprocess.run(cmd, cwd=str(BASE_DIR), check=False)
    return proc.returncode


def resolve_series_dirs(source_lang_dir: Path, prefix_arg: str, from_group: int, to_group: int) -> list[Path]:
    selected_prefixes = parse_prefix_arg(prefix_arg)
    dirs: list[Path] = []
    for group_info, group_dir in iter_series_group_dirs(source_lang_dir, selected_prefixes):
        if from_group <= group_info.group_num <= to_group:
            dirs.append(group_dir)
    return dirs


def pending_summary(target_langs: list[str]) -> dict[str, int]:
    path = BASE_DIR / "global_translations.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    summary = {lang: 0 for lang in target_langs}
    if not isinstance(data, dict):
        return summary
    for row in data.values():
        if not isinstance(row, dict):
            continue
        for lang in target_langs:
            value = row.get(lang)
            if value == "PENDING" or not value:
                summary[lang] += 1
    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Pipeline de traducción + selector + captura por series")
    parser.add_argument("--source-lang-dir", default="Español", help="Carpeta fuente (default: Español)")
    parser.add_argument("--prefix", default="all", help="Prefijo(s) de serie: O | P | RT | O,RT,D | all")
    parser.add_argument("--from-group", type=int, required=True, help="Grupo inicial")
    parser.add_argument("--to-group", type=int, required=True, help="Grupo final")
    parser.add_argument("--from-image", type=int, default=1, help="Imagen inicial para auto-select")
    parser.add_argument("--target-langs", default="EN,PT_BR,DE,FR,IT", help="Idiomas destino separados por coma")
    parser.add_argument("--allow-pending-build", action="store_true", help="Continúa aunque existan PENDING")
    parser.add_argument("--include-source-captures", action="store_true", help="Captura también la carpeta fuente Español")
    parser.add_argument("--include-existing-selectors", action="store_true", help="Reprocesa imágenes con selector existente")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    target_langs = [item.strip() for item in args.target_langs.split(",") if item.strip()]
    source_lang_dir = BASE_DIR / args.source_lang_dir
    series_dirs = resolve_series_dirs(source_lang_dir, args.prefix, args.from_group, args.to_group)

    if not series_dirs:
        print("No se encontraron series para el rango solicitado.")
        return 1

    print("Series a procesar:")
    for path in series_dirs:
        print(f"  - {path.relative_to(BASE_DIR)}")

    for series_dir in series_dirs:
        rel = str(series_dir.relative_to(BASE_DIR))
        for target_lang in target_langs:
            rc = run_checked([sys.executable, str(BASE_DIR / "scripts" / "goalbus_localize.py"), "init", rel, "--target", target_lang])
            if rc != 0:
                return rc

    for series_dir in series_dirs:
        rel = str(series_dir.relative_to(BASE_DIR))
        rc = run_checked([sys.executable, str(BASE_DIR / "scripts" / "goalbus_localize.py"), "extract", rel])
        if rc != 0:
            return rc

    pending = pending_summary(target_langs)
    print("Pendientes actuales:")
    for lang, count in pending.items():
        print(f"  {lang}: {count}")
    if any(count > 0 for count in pending.values()) and not args.allow_pending_build:
        print("Hay traducciones pendientes. Completa global_translations.json o usa --allow-pending-build.")
        return 2

    rc = run_checked([
        sys.executable,
        str(BASE_DIR / "scripts" / "goalbus_localize.py"),
        "build_all",
        "--from",
        "ES",
        "--to",
        ",".join(target_langs),
    ])
    if rc != 0:
        return rc

    select_cmd = [
        sys.executable,
        str(BASE_DIR / "scripts" / "auto_select_from_old.py"),
        "--lang",
        args.source_lang_dir,
        "--prefix",
        args.prefix,
        "--from-group",
        str(args.from_group),
        "--from-image",
        str(args.from_image),
        "--to-group",
        str(args.to_group),
    ]
    if args.include_existing_selectors:
        select_cmd.append("--include-existing")
    rc = run_checked(select_cmd)
    if rc != 0:
        return rc

    capture_langs = list(target_langs)
    if args.include_source_captures:
        capture_langs.insert(0, args.source_lang_dir)

    for lang in capture_langs:
        for series_dir in series_dirs:
            rel = Path(lang) / series_dir.relative_to(source_lang_dir)
            rc = run_checked([sys.executable, str(BASE_DIR / "scripts" / "capture_screenshots.py"), "capture", str(rel)])
            if rc != 0:
                return rc

    print("Pipeline completado.")
    print("Siguiente paso sugerido: review_selectors.py list/show/mark/recapture")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
