#!/usr/bin/env python3
import sys
from pathlib import Path

# Add the root directory to sys.path to import translate_docs
root_dir = Path(__file__).parent
sys.path.insert(0, str(root_dir))

import translate_docs as td
import run_pipeline as rp

def run_en_de():
    # Define the EN -> DE profile
    label = "EN -> DE"
    model = "Helsinki-NLP/opus-mt-en-de"
    lang_tag = ""
    src_dir = td._EN
    tgt_dir = td._DE
    tgt_lang = "de"
    glossary_path = None # Add if you have one
    glos_src_col = "EN"
    glos_tgt_col = "DE"

    print(f"Starting translation: {label}")
    ok = rp.run_profile(label, model, lang_tag, src_dir, tgt_dir, tgt_lang,
                       glossary_path, glos_src_col, glos_tgt_col)
    
    if ok:
        print(f"Translation {label} completed successfully.")
    else:
        print(f"Translation {label} failed.")

if __name__ == "__main__":
    run_en_de()
