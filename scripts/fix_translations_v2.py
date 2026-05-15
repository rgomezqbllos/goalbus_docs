import json

filepath = 'global_translations.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# ui_text_1073: Source must be the ORIGINAL text from HTML
data['ui_text_1073'] = {
    "ES": "¡Hola, Alan!",  # Source text in HTML
    "_match": "tag",
    "PT_BR": "Olá, João Silva!",
    "FR": "Bonjour, Jean Martin!",
    "IT": "Ciao, Marco Rossi!",
    "EN": "Hello, John Smith!",
    "DE": "Hallo, Thomas Müller!",
    "ES_localized": "¡Hola, Juan Pérez!" # Optional, just for record
}

# For Spanish build, we'll have to handle it separately or just use a manual replacement if needed.
# But for now, let's fix the other 5 languages.

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Fixed global_translations.json: ES source set back to '¡Hola, Alan!'")
