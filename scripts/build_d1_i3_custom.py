import sys
import os
from pathlib import Path

# Add scripts to path
sys.path.append(os.path.abspath('scripts'))

import locale_pack
import goalbus_localize

# Create temp glossaries again
if not os.path.exists('temp_glossaries'):
    os.makedirs('temp_glossaries')
import shutil
for f in Path('Glosarios/DriverApp').glob('*.json'):
    shutil.copy(f, 'temp_glossaries/')
if not os.path.exists('temp_glossaries/it.json'):
    shutil.copy('it.json', 'temp_glossaries/')

# Override REPO_ROOT to use our temporary glossaries
goalbus_localize.REPO_ROOT = Path('temp_glossaries').resolve()
locale_pack.REPO_ROOT = Path('temp_glossaries').resolve()

# Target languages
target_langs = ["EN", "PT_BR", "IT", "FR", "DE"]
source_path = "Español/D1/D1_imagen3"

for lang in target_langs:
    target_folder = goalbus_localize.LANG_TO_FOLDER[lang]
    target_path = os.path.join(target_folder, "D1/D1_imagen3")
    
    # Ensure target exists
    if not os.path.exists(target_path):
        os.makedirs(target_path, exist_ok=True)
    
    # Run build
    goalbus_localize.build_folder(source_path, target_path, source_lang="ES", target_lang=lang)

print("Build complete for all languages using specialized glossaries for D1_imagen3.")
