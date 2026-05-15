import json

with open('global_translations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Collect keys starting from ui_text_1050 (numeric)
keys = []
for k in data.keys():
    if k.startswith('ui_text_'):
        try:
            num = int(k.split('_')[-1])
            if num >= 1050:
                keys.append((num, k))
        except ValueError:
            pass

for num, key in sorted(keys):
    print(f"{key}: {repr(data[key]['ES'])}")
