#!/usr/bin/env python3
"""
Utilidades compartidas para series GoalBus del tipo:

  P5 / P5_imagen8
  O10 / O10_Imagen3
  RT2 / RT2_Imagen1
  D7 / D7_Imagen4

La idea es centralizar el parsing y descubrimiento para que los scripts no
queden acoplados a un prefijo concreto.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


GROUP_RE = re.compile(r"^(?P<prefix>[A-Za-z]+)(?P<group>\d+)$")
IMAGE_RE = re.compile(
    r"^(?P<prefix>[A-Za-z]+)(?P<group>\d+)_(?P<label>imagen)(?P<image>\d+)$",
    re.IGNORECASE,
)
OLD_RE = re.compile(
    r"^(?P<prefix>[A-Za-z]+)(?P<group>\d+)_(?P<label>imagen)(?P<image>\d+)_old\.png$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class SeriesGroup:
    prefix: str
    group_num: int
    raw_name: str

    @property
    def normalized_prefix(self) -> str:
        return self.prefix.upper()


@dataclass(frozen=True)
class SeriesImage:
    prefix: str
    group_num: int
    image_num: int
    raw_name: str
    image_label: str

    @property
    def normalized_prefix(self) -> str:
        return self.prefix.upper()


def normalize_prefix(prefix: str) -> str:
    return prefix.strip().upper()


def parse_group_name(name: str) -> SeriesGroup | None:
    match = GROUP_RE.match(name.strip())
    if not match:
        return None
    return SeriesGroup(
        prefix=match.group("prefix"),
        group_num=int(match.group("group")),
        raw_name=name,
    )


def parse_image_name(name: str) -> SeriesImage | None:
    match = IMAGE_RE.match(name.strip())
    if not match:
        return None
    return SeriesImage(
        prefix=match.group("prefix"),
        group_num=int(match.group("group")),
        image_num=int(match.group("image")),
        raw_name=name,
        image_label=match.group("label"),
    )


def parse_old_png_name(name: str) -> SeriesImage | None:
    match = OLD_RE.match(name.strip())
    if not match:
        return None
    return SeriesImage(
        prefix=match.group("prefix"),
        group_num=int(match.group("group")),
        image_num=int(match.group("image")),
        raw_name=name,
        image_label=match.group("label"),
    )


def prefix_selected(prefix: str, selected_prefixes: set[str] | None) -> bool:
    if not selected_prefixes:
        return True
    return normalize_prefix(prefix) in selected_prefixes


def parse_prefix_arg(prefix_arg: str | None) -> set[str] | None:
    if not prefix_arg:
        return None
    raw_items = [item.strip() for item in prefix_arg.split(",") if item.strip()]
    if not raw_items:
        return None
    if any(item.lower() == "all" for item in raw_items):
        return None
    return {normalize_prefix(item) for item in raw_items}


def iter_series_group_dirs(lang_dir: Path, selected_prefixes: set[str] | None = None) -> list[tuple[SeriesGroup, Path]]:
    found: list[tuple[SeriesGroup, Path]] = []
    if not lang_dir.exists():
        return found

    for child in sorted(lang_dir.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir():
            continue
        group = parse_group_name(child.name)
        if not group:
            continue
        if not prefix_selected(group.prefix, selected_prefixes):
            continue
        found.append((group, child))

    return sorted(found, key=lambda item: (item[0].normalized_prefix, item[0].group_num, item[0].raw_name.lower()))


def resolve_image_folder(group_dir: Path, prefix: str, group_num: int, image_num: int) -> Path | None:
    for child in sorted(group_dir.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir():
            continue
        if child.name in {f"{prefix}{group_num}_Imagen{image_num}", f"{prefix}{group_num}_imagen{image_num}"}:
            return child

    for child in sorted(group_dir.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir():
            continue
        parsed = parse_image_name(child.name)
        if not parsed:
            continue
        if normalize_prefix(parsed.prefix) != normalize_prefix(prefix):
            continue
        if parsed.group_num != group_num or parsed.image_num != image_num:
            continue
        return child
    return None


def find_html_file_in_folder(image_folder: Path, html_filenames: list[str] | tuple[str, ...]) -> Path | None:
    for name in html_filenames:
        candidate = image_folder / name
        if candidate.exists():
            return candidate
    for candidate in image_folder.glob("*.html"):
        if "_files" not in candidate.name and "_test" not in candidate.name:
            return candidate
    return None
