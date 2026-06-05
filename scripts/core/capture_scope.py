#!/usr/bin/env python3
"""
import sys as _sys
import os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(__file__), '..', 'core'))
Wrapper para capturas por alcance:

  python scripts/capture_scope.py Portugues
  python scripts/capture_scope.py Portugues P8
  python scripts/capture_scope.py Portugues P8_imagen3
  python scripts/capture_scope.py Portugues P8 P8_imagen3

Tambien acepta ruta directa:
  python scripts/capture_scope.py Portugues/P8/P8_imagen3
"""

from __future__ import annotations

import argparse
import asyncio
import re
import sys
import unicodedata
from pathlib import Path

from capture_screenshots import (
    BASE_DIR,
    DEFAULT_VIEWPORT_HEIGHT,
    DEFAULT_VIEWPORT_WIDTH,
    discover_all_folders,
    discover_image_folders,
    run_captures,
)
from series_utils import parse_group_name, parse_image_name


IMAGE_SUFFIX_RE = re.compile(r"^imagen\d+$", re.IGNORECASE)


def normalize_token(text: str) -> str:
    stripped = text.strip()
    normalized = unicodedata.normalize("NFD", stripped)
    no_accents = "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")
    return no_accents.lower()


def split_scope_parts(scope_parts: list[str]) -> list[str]:
    if len(scope_parts) == 1 and " " in scope_parts[0] and "/" not in scope_parts[0]:
        return [part for part in scope_parts[0].split() if part.strip()]
    return scope_parts


def find_language_folder(language_token: str) -> str | None:
    requested = normalize_token(language_token)
    language_dirs = [p for p in BASE_DIR.iterdir() if p.is_dir() and not p.name.startswith(".")]
    for lang_dir in language_dirs:
        if normalize_token(lang_dir.name) == requested:
            return lang_dir.name
    return None


def filter_by_scope(scope_parts: list[str]) -> list[dict]:
    if not scope_parts:
        raise ValueError("Debes indicar al menos un idioma.")
    if len(scope_parts) > 3:
        raise ValueError(
            "Formato invalido. Usa: Idioma | Idioma Serie# | Idioma Serie#_imagen# | Idioma Serie# Serie#_imagen#"
        )

    language_token = scope_parts[0]
    language_folder = find_language_folder(language_token)
    if not language_folder:
        raise ValueError(f"Idioma no encontrado: {language_token}")

    page_token: str | None = None
    image_token: str | None = None

    if len(scope_parts) == 2:
        second = scope_parts[1]
        if parse_group_name(second):
            page_token = second
        elif parse_image_name(second) or IMAGE_SUFFIX_RE.match(second):
            image_token = second
        else:
            raise ValueError(f"Segundo parametro invalido: {second}. Esperado Serie# o Serie#_imagen#.")
    elif len(scope_parts) == 3:
        second = scope_parts[1]
        third = scope_parts[2]
        parsed_page = parse_group_name(second)
        if not parsed_page:
            raise ValueError(f"Segundo parametro invalido: {second}. En formato de 3 parametros debe ser Serie#.")
        page_token = second
        parsed_image = parse_image_name(third)
        if not (parsed_image or IMAGE_SUFFIX_RE.match(third)):
            raise ValueError(f"Tercer parametro invalido: {third}. Esperado Serie#_imagen# o imagen#.")
        if parsed_image and (
            parsed_image.group_num != parsed_page.group_num
            or parsed_image.normalized_prefix != parsed_page.normalized_prefix
        ):
            raise ValueError(
                f"Tercer parametro invalido: {third}. Debe pertenecer a la misma serie que {second}."
            )
        image_token = third

    folders = discover_image_folders(language_folder)
    if not folders:
        return []

    if page_token:
        page_norm = normalize_token(page_token)
        folders = [f for f in folders if normalize_token(f["page"]) == page_norm]

    if image_token:
        image_candidate = image_token
        if IMAGE_SUFFIX_RE.match(image_candidate):
            if not page_token:
                raise ValueError(
                    "Formato incompleto: para usar imagen# debes indicar la serie (ej: Portugues O8 imagen3)."
                )
            image_candidate = f"{page_token}_{image_candidate}"

        image_norm = normalize_token(image_candidate)
        folders = [f for f in folders if normalize_token(f["image_name"]) == image_norm]

        # Si se indico imagen con pagina embebida y no se paso pagina aparte, restringir pagina.
        parsed_image = parse_image_name(image_candidate)
        if not page_token and parsed_image:
            inferred_page = image_candidate.split("_", 1)[0]
            inferred_page_norm = normalize_token(inferred_page)
            folders = [f for f in folders if normalize_token(f["page"]) == inferred_page_norm]

    return folders


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Captura imagenes por alcance (idioma/pagina/imagen).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  %(prog)s Portugues
  %(prog)s Portugues O8
  %(prog)s Portugues O8_Imagen3
  %(prog)s Portugues O8 O8_Imagen3
  %(prog)s Portugues/RT2/RT2_Imagen1
  %(prog)s --all
        """,
    )
    parser.add_argument(
        "scope",
        nargs="*",
        help="Alcance: Idioma | Idioma Serie# | Idioma Serie#_imagen# | Idioma Serie# Serie#_imagen# | ruta Idioma/Serie#/Serie#_imagen#",
    )
    parser.add_argument("--all", action="store_true", dest="all_targets", help="Capturar todos los idiomas.")
    parser.add_argument("--dry-run", action="store_true", help="Solo mostrar que se capturaria.")
    parser.add_argument("--width", type=int, default=DEFAULT_VIEWPORT_WIDTH, help=f"Ancho viewport (default: {DEFAULT_VIEWPORT_WIDTH})")
    parser.add_argument("--height", type=int, default=DEFAULT_VIEWPORT_HEIGHT, help=f"Alto viewport (default: {DEFAULT_VIEWPORT_HEIGHT})")
    return parser


def resolve_folders(args: argparse.Namespace) -> list[dict]:
    if args.all_targets:
        return discover_all_folders()

    scope_parts = split_scope_parts(args.scope)
    if not scope_parts:
        raise ValueError("Debes indicar un alcance o usar --all.")

    # Soporte directo para rutas tipo Idioma/P8/P8_imagen3
    if len(scope_parts) == 1 and "/" in scope_parts[0]:
        return discover_image_folders(scope_parts[0])

    return filter_by_scope(scope_parts)


def dedupe_folders(folders: list[dict]) -> list[dict]:
    seen: set[str] = set()
    deduped: list[dict] = []
    for folder in folders:
        key = "|".join(
            [
                normalize_token(str(folder.get("language", ""))),
                normalize_token(str(folder.get("page", ""))),
                normalize_token(str(folder.get("image_name", ""))),
            ]
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(folder)
    return deduped


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        folders = resolve_folders(args)
    except ValueError as exc:
        print(f"❌ {exc}")
        return 2

    folders = dedupe_folders(folders)

    if not folders:
        print("❌ No se encontraron carpetas de imagen para el alcance indicado.")
        return 1

    print(f"🎯 Captura por alcance: {len(folders)} carpeta(s)")
    for item in folders:
        print(f"  - {item['language']}/{item['page']}/{item['image_name']}")

    asyncio.run(run_captures(folders, args.width, args.height, args.dry_run))
    return 0


if __name__ == "__main__":
    sys.exit(main())
