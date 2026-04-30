#!/usr/bin/env python3
"""
run_pipeline.py — Full GoalBus translation pipeline
Runs all five language profiles in sequence using the translate_docs engine.

Order:
  1. ES -> EN   (~33 min)
  2. EN -> PT_BR (~50 min, uses glossary)
  3. EN -> IT   (~50 min)
  4. ES -> FR   (~33 min)
  5. EN -> DE   (~33 min)

Total estimated time: ~3h 20min on a 4-core CPU.
Run as: python run_pipeline.py
"""

import json
import logging
import sys
import argparse
from pathlib import Path

# ── Import translation engine ─────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
import translate_docs as td

# ── Pipeline definition ───────────────────────────────────────────────────────
# Each tuple: (label, model, lang_tag, src_dir, tgt_dir, tgt_lang, glossary_path)
PIPELINE = [
    (
        "ES -> EN",
        "Helsinki-NLP/opus-mt-es-en",
        "",
        td._ES, td._EN,
        "en",
        None,
        "EN", "PT-BR",   # glossary col hints (unused when glossary_path=None)
    ),
    (
        "EN -> PT_BR",
        "Helsinki-NLP/opus-mt-en-ROMANCE",
        ">>pt<<",
        td._EN, td._PT,
        "pt",
        td._PT / "glossary-transport-ops.md",
        "EN", "PT-BR",
    ),
    (
        "EN -> IT",
        "Helsinki-NLP/opus-mt-en-ROMANCE",
        ">>it<<",
        td._EN, td._IT,
        "it",
        None,
        "EN", "PT-BR",
    ),
    (
        "ES -> FR",
        "Helsinki-NLP/opus-mt-es-fr",
        "",
        td._ES, td._FR,
        "fr",
        None,
        "EN", "PT-BR",
    ),
    (
        "EN -> DE",
        "Helsinki-NLP/opus-mt-en-de",
        "",
        td._EN, td._DE,
        "de",
        None,
        "EN", "DE",
    ),
]


def run_profile(label, model, lang_tag, src_dir, tgt_dir, tgt_lang,
                glossary_path, glos_src_col, glos_tgt_col):
    """Run one translation profile end-to-end."""
    banner = f"[PIPELINE] {label}"
    print(f"\n{'='*60}\n{banner}\n{'='*60}\n", flush=True)

    # ── Override module-level config ──────────────────────────────────────────
    td.MODEL_NAME     = model
    td.TGT_LANG_TAG   = lang_tag
    td.NLLB_SRC       = ""
    td.NLLB_TGT       = ""
    td.SRC_DIR        = src_dir
    td.TGT_DIR        = tgt_dir
    td.TGT_LANG       = tgt_lang
    td.GLOSSARY_PATH  = glossary_path
    td.GLOSSARY_SRC_COL = glos_src_col
    td.GLOSSARY_TGT_COL = glos_tgt_col
    td.FILENAME_MAP_PATH = tgt_dir / "filename_map.json"
    td.LOG_PATH          = tgt_dir / "translation.log"

    # ── Reset & configure logging for this profile ────────────────────────────
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    td.setup_logging()
    log = logging.getLogger(__name__)

    # ── Glossary ──────────────────────────────────────────────────────────────
    td.GLOSSARY.clear()
    td.GLOSSARY.update(
        td.load_glossary(glossary_path, glos_src_col, glos_tgt_col)
    )

    # ── Source files ──────────────────────────────────────────────────────────
    src_files = [
        p for p in src_dir.iterdir()
        if p.is_file() and p.suffix == ".md"
        if not p.name.startswith("glossary")
        if not p.name.startswith("translation")
    ]
    if not src_files:
        log.error(f"No .md files found in: {src_dir}")
        return False

    log.info(f"Found {len(src_files)} source files in {src_dir}")

    # ── Load model ────────────────────────────────────────────────────────────
    translator = td.MarkdownTranslator()
    translator.load_model()

    # ── Pass 1: filename map ──────────────────────────────────────────────────
    filename_map = td.build_filename_map(src_files, translator)
    td.FILENAME_MAP_PATH.write_text(
        json.dumps(filename_map, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    log.info(f"[MAP] Saved to {td.FILENAME_MAP_PATH}")

    # ── Pass 2: translate files ───────────────────────────────────────────────
    for i, src_path in enumerate(sorted(src_files), 1):
        log.info(f"[PASS2] ({i}/{len(src_files)}) {src_path.name}")
        td.translate_file(src_path, tgt_dir, filename_map, translator)

    log.info(f"[COMPLETE] {label} done.")
    return True


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run GoalBus markdown translation profiles.")
    parser.add_argument(
        "--only",
        help='Run one profile by label, for example: --only "EN -> DE"',
    )
    parser.add_argument("--list", action="store_true", help="List available profiles and exit")
    args = parser.parse_args()

    if args.list:
        for profile in PIPELINE:
            print(profile[0])
        sys.exit(0)

    selected = PIPELINE
    if args.only:
        selected = [profile for profile in PIPELINE if profile[0] == args.only]
        if not selected:
            print(f"[ERROR] Unknown profile: {args.only}")
            print("Available profiles:")
            for profile in PIPELINE:
                print(f"  - {profile[0]}")
            sys.exit(1)

    total = len(selected)
    for step, profile_args in enumerate(selected, 1):
        label = profile_args[0]
        print(f"\n[{step}/{total}] Starting: {label}", flush=True)
        ok = run_profile(*profile_args)
        if not ok:
            print(f"\n[ERROR] Pipeline aborted at step {step}: {label}")
            sys.exit(1)

    print("\n" + "=" * 60)
    print("ALL TRANSLATIONS COMPLETE")
    print("  EN  ->  Master Files (EN)")
    print("  PT  ->  Arquivos Mestres (PT_BR)")
    print("  IT  ->  Archivi Maestri (IT)")
    print("  FR  ->  Fichiers Maitres (FR)")
    print("  DE  ->  Master Files (DE)")
    print("=" * 60)
