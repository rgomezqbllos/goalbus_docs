"""Smoke tests for scripts/series_utils.py.

Run with:
  python scripts/tests/test_series_utils.py
"""

from __future__ import annotations

import sys as _sys
import os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(__file__), '..', 'core'))

import tempfile
from pathlib import Path

from series_utils import (
    parse_group_name,
    parse_image_name,
    parse_old_png_name,
    parse_prefix_arg,
    resolve_image_folder,
)


def _ok(name: str) -> None:
    print(f"  PASS  {name}")


def _fail(name: str, detail: str) -> None:
    print(f"  FAIL  {name}: {detail}")
    raise SystemExit(1)


def test_parse_group_name() -> None:
    parsed = parse_group_name("RT12")
    if not parsed or parsed.prefix != "RT" or parsed.group_num != 12:
        _fail("test_parse_group_name", f"unexpected parse result: {parsed}")
    _ok("test_parse_group_name")


def test_parse_image_name() -> None:
    parsed = parse_image_name("O10_Imagen3")
    if not parsed or parsed.prefix != "O" or parsed.group_num != 10 or parsed.image_num != 3:
        _fail("test_parse_image_name", f"unexpected parse result: {parsed}")
    _ok("test_parse_image_name")


def test_parse_old_png_name() -> None:
    parsed = parse_old_png_name("D7_Imagen4_old.png")
    if not parsed or parsed.prefix != "D" or parsed.group_num != 7 or parsed.image_num != 4:
        _fail("test_parse_old_png_name", f"unexpected parse result: {parsed}")
    _ok("test_parse_old_png_name")


def test_parse_prefix_arg() -> None:
    parsed = parse_prefix_arg("O,RT,d")
    if parsed != {"O", "RT", "D"}:
        _fail("test_parse_prefix_arg", f"unexpected parse result: {parsed}")
    _ok("test_parse_prefix_arg")


def test_resolve_image_folder_supports_imagen_and_Imagen() -> None:
    with tempfile.TemporaryDirectory(prefix="series_utils_") as td:
        root = Path(td)
        group_dir = root / "O10"
        group_dir.mkdir()
        (group_dir / "O10_Imagen3").mkdir()
        (group_dir / "O10_imagen4").mkdir()

        a = resolve_image_folder(group_dir, "O", 10, 3)
        b = resolve_image_folder(group_dir, "O", 10, 4)
        if not a or a.name != "O10_Imagen3":
            _fail("test_resolve_image_folder_supports_imagen_and_Imagen", f"bad Imagen resolution: {a}")
        if not b or b.name != "O10_imagen4":
            _fail("test_resolve_image_folder_supports_imagen_and_Imagen", f"bad imagen resolution: {b}")
    _ok("test_resolve_image_folder_supports_imagen_and_Imagen")


def main() -> int:
    print("series_utils smoke tests:")
    test_parse_group_name()
    test_parse_image_name()
    test_parse_old_png_name()
    test_parse_prefix_arg()
    test_resolve_image_folder_supports_imagen_and_Imagen()
    print("All tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
