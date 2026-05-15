import sys
import os
from pathlib import Path
import shutil

# Add scripts to path
sys.path.append(os.path.abspath('scripts'))

import goalbus_localize
import locale_pack

# Use specialized glossaries
if not os.path.exists('temp_glossaries'):
    os.makedirs('temp_glossaries')
for f in Path('Glosarios/DriverApp').glob('*.json'):
    shutil.copy(f, 'temp_glossaries/')
if not os.path.exists('temp_glossaries/it.json'):
    shutil.copy('it.json', 'temp_glossaries/')

goalbus_localize.REPO_ROOT = Path('temp_glossaries').resolve()
locale_pack.REPO_ROOT = Path('temp_glossaries').resolve()

target_langs = ["EN", "PT_BR", "IT", "FR", "DE"]
source_path = "Español/D2/D2_imagen1"

for lang in target_langs:
    target_folder = goalbus_localize.LANG_TO_FOLDER[lang]
    target_path = os.path.join(target_folder, "D2/D2_imagen1")
    
    if not os.path.exists(target_path):
        os.makedirs(target_path, exist_ok=True)
    
    # Copy selector.json to target
    shutil.copy(os.path.join(source_path, "selector.json"), target_path)
    
    # Run build
    goalbus_localize.build_folder(source_path, target_path, source_lang="ES", target_lang=lang)

print("Build complete for D2_imagen1.")
