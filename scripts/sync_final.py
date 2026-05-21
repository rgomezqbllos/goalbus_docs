#!/usr/bin/env python3
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MASTERS_ROOT = ROOT / "Maestros Finales"

LANGUAGE_TARGETS = {
    "Español": "Archivos Maestros (ES)",
    "English": "Master Files (EN)",
    "Frances": "Fichiers Maîtres (FR)",
    "Portugues": "Arquivos Mestres (PT_BR)",
    "Italiano": "Archivi Maestri (IT)",
    "Deutsch": "Master Files (DE)",
}

PAGE_RE = re.compile(r"^[DP]\d+$")
IMAGE_FOLDER_RE = re.compile(r"^[DP]\d+_(?:imagen|Imagen)\d+$")
OLD_PNG_RE = re.compile(r".*_old\.png$", re.IGNORECASE)


def ignore_old_pngs(_directory: str, names: list[str]) -> list[str]:
    return [name for name in names if OLD_PNG_RE.match(name)]


def sync_language(source_language: str, target_folder: str) -> dict[str, int]:
    source_root = ROOT / source_language
    target_root = MASTERS_ROOT / target_folder
    stats = {"png": 0, "folders": 0, "files": 0, "skipped_old": 0}

    if not source_root.exists():
        print(f"WARN missing source: {source_root}")
        return stats

    target_root.mkdir(parents=True, exist_ok=True)

    for page_dir in sorted(source_root.iterdir()):
        if not page_dir.is_dir() or not PAGE_RE.match(page_dir.name):
            continue

        target_page = target_root / page_dir.name
        target_page.mkdir(parents=True, exist_ok=True)

        for item in sorted(page_dir.iterdir()):
            if item.is_file() and item.suffix.lower() == ".png":
                if OLD_PNG_RE.match(item.name):
                    stats["skipped_old"] += 1
                    continue
                shutil.copy2(item, target_page / item.name)
                stats["png"] += 1
                continue

            if item.is_dir() and IMAGE_FOLDER_RE.match(item.name):
                target_item = target_page / item.name
                if target_item.exists():
                    shutil.rmtree(target_item)
                shutil.copytree(item, target_item, ignore=ignore_old_pngs)
                stats["folders"] += 1
                stats["files"] += sum(1 for path in target_item.rglob("*") if path.is_file())

    return stats


def remove_old_pngs_from_masters() -> int:
    removed = 0
    if not MASTERS_ROOT.exists():
        return removed
    for old_png in list(MASTERS_ROOT.rglob("*_old.png")):
        old_png.unlink()
        removed += 1
    return removed


def main() -> int:
    print("Syncing localized screenshots and HTML folders to Maestros Finales")
    for source_language, target_folder in LANGUAGE_TARGETS.items():
        stats = sync_language(source_language, target_folder)
        print(
            f"{source_language}: png={stats['png']} "
            f"folders={stats['folders']} files={stats['files']} "
            f"skipped_old={stats['skipped_old']}"
        )

    removed = remove_old_pngs_from_masters()
    remaining = len(list(MASTERS_ROOT.rglob("*_old.png"))) if MASTERS_ROOT.exists() else 0
    print(f"old_png_removed={removed}")
    print(f"old_png_remaining={remaining}")
    return 0 if remaining == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
