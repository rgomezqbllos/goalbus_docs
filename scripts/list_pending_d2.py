import json

with open('global_translations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for key, entry in data.items():
    if entry.get('EN') == 'PENDING':
        print(f"{key}: {entry['ES']}")
