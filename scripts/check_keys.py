import json
import sys

with open('global_translations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for key in sorted(data.keys()):
    if key >= 'ui_text_1050':
        print(f"{key}: {data[key]['ES']}")
