#!/usr/bin/env python3
"""
Revisión manual asistida de reportes de auto_select_from_old.py.

Permite:
- listar casos de un reporte
- mostrar detalle de un caso
- marcar casos como revisados / corregidos manualmente
- recapturar una sola imagen tras editar su selector.json
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def build_report_path(lang: str, prefix_arg: str | None, from_group: int, to_group: int) -> Path:
    prefix_segment = "all" if not prefix_arg or prefix_arg.lower() == "all" else re.sub(r"[^A-Za-z0-9,_-]+", "-", prefix_arg)
    lang_segment = re.sub(r"[^A-Za-z0-9_-]+", "_", lang)
    return BASE_DIR / "scratch" / f"auto_select_from_old_report_{lang_segment}_{prefix_segment}_{from_group}_{to_group}.json"


def load_report(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"No existe reporte: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Formato inválido de reporte: {path}")
    return data


def save_report(path: Path, rows: list[dict]) -> None:
    path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def resolve_report(args) -> Path:
    if args.report:
        return Path(args.report)
    return build_report_path(args.lang, args.prefix, args.from_group, args.to_group)


def selector_preview(row: dict) -> str:
    if row.get("selector"):
        return row["selector"]
    selectors = row.get("selectors") or []
    if selectors:
        return " | ".join(selectors)
    return "—"


def find_row(rows: list[dict], index: int) -> dict:
    if index < 1 or index > len(rows):
        raise IndexError(f"Índice fuera de rango: {index} (1..{len(rows)})")
    return rows[index - 1]


def cmd_list(args) -> int:
    report_path = resolve_report(args)
    rows = load_report(report_path)
    print(f"Reporte: {report_path}")
    print(f"Casos: {len(rows)}")
    for idx, row in enumerate(rows, start=1):
        target = f"{row.get('prefix','?')}{row.get('group_num','?')}_imagen{row.get('image_num','?')}"
        flags = []
        if row.get("reviewed"):
            flags.append("reviewed")
        if row.get("corrected_manually"):
            flags.append("manual")
        status = ",".join(flags) if flags else "-"
        print(
            f"{idx:>3}. {target:<18} status={row.get('status','?'):<5} "
            f"conf={row.get('confidence','?'):<6} score={row.get('score','-')!s:<8} review={status}"
        )
    return 0


def cmd_show(args) -> int:
    report_path = resolve_report(args)
    rows = load_report(report_path)
    row = find_row(rows, args.index)
    target = f"{row.get('prefix','?')}{row.get('group_num','?')}_imagen{row.get('image_num','?')}"
    print(f"Reporte: {report_path}")
    print(f"Índice: {args.index}")
    print(f"Target: {target}")
    print(f"Estado: {row.get('status')}")
    print(f"Confidence: {row.get('confidence')}")
    print(f"Score: {row.get('score')}")
    print(f"Pattern: {row.get('pattern', '-')}")
    print(f"Selector: {selector_preview(row)}")
    print(f"Selector path: {row.get('selector_path')}")
    print(f"HTML: {row.get('html')}")
    print(f"Old PNG: {row.get('old')}")
    print(f"Capture PNG: {row.get('output_png')}")
    print(f"Reviewed: {row.get('reviewed', False)}")
    print(f"Corrected manually: {row.get('corrected_manually', False)}")
    print(f"Notes: {row.get('notes', '')}")
    print(f"Review notes: {row.get('review_notes', '')}")

    selector_path = row.get("selector_path")
    if selector_path and Path(selector_path).exists():
        print("\nselector.json actual:")
        print(Path(selector_path).read_text(encoding="utf-8"))
    return 0


def cmd_mark(args) -> int:
    report_path = resolve_report(args)
    rows = load_report(report_path)
    row = find_row(rows, args.index)
    row["reviewed"] = True
    if args.corrected:
        row["corrected_manually"] = True
    if args.note is not None:
        row["review_notes"] = args.note
    save_report(report_path, rows)
    print(f"Actualizado: índice {args.index} en {report_path}")
    return 0


def cmd_recapture(args) -> int:
    report_path = resolve_report(args)
    rows = load_report(report_path)
    row = find_row(rows, args.index)
    html_path = Path(row["html"])
    image_folder = html_path.parent
    rel_target = image_folder.relative_to(BASE_DIR)
    cmd = [sys.executable, str(BASE_DIR / "scripts" / "capture_screenshots.py"), "capture", str(rel_target)]
    print(f"Recapturando: {' '.join(cmd)}")
    proc = subprocess.run(cmd, cwd=str(BASE_DIR), check=False)
    return proc.returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Revisión asistida de selectores generados automáticamente")
    parser.add_argument("--report", help="Ruta directa al reporte JSON")
    parser.add_argument("--lang", default="Español", help="Idioma del reporte si no se pasa --report")
    parser.add_argument("--prefix", default="all", help="Prefijo(s) usados para generar el reporte")
    parser.add_argument("--from-group", type=int, default=1, help="Grupo inicial del reporte")
    parser.add_argument("--to-group", type=int, default=9999, help="Grupo final del reporte")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="Listar casos del reporte")

    show = sub.add_parser("show", help="Mostrar detalle de un caso")
    show.add_argument("--index", type=int, required=True, help="Índice 1-based del caso")

    mark = sub.add_parser("mark", help="Marcar un caso como revisado/corregido")
    mark.add_argument("--index", type=int, required=True, help="Índice 1-based del caso")
    mark.add_argument("--corrected", action="store_true", help="Marca también corrected_manually=true")
    mark.add_argument("--note", help="Nota de revisión")

    recapture = sub.add_parser("recapture", help="Recapturar un caso puntual")
    recapture.add_argument("--index", type=int, required=True, help="Índice 1-based del caso")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "list":
        return cmd_list(args)
    if args.command == "show":
        return cmd_show(args)
    if args.command == "mark":
        return cmd_mark(args)
    if args.command == "recapture":
        return cmd_recapture(args)
    parser.error("Comando no soportado")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
