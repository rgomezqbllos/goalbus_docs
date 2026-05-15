import json

filepath = 'global_translations.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update ui_text_1073 (The correct greeting extracted from original HTML)
if 'ui_text_1073' in data:
    data['ui_text_1073'] = {
        "ES": "¡Hola, Juan Pérez!",
        "_match": "tag",
        "PT_BR": "Olá, João Silva!",
        "FR": "Bonjour, Jean Martin!",
        "IT": "Ciao, Marco Rossi!",
        "EN": "Hello, John Smith!",
        "DE": "Hallo, Thomas Müller!"
    }

# Fix ui_text_1072 (Últimos mensajes)
if 'ui_text_1072' in data:
    data['ui_text_1072'] = {
        "ES": "Últimos mensajes",
        "_match": "tag",
        "PT_BR": "Últimas mensagens",
        "FR": "Derniers messages",
        "IT": "Ultimi messaggi",
        "EN": "Latest messages",
        "DE": "Letzte Nachrichten"
    }

# Remove corrupted or redundant keys
if 'ui_text_1071' in data:
    del data['ui_text_1071']

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Successfully fixed global_translations.json for D1_imagen3")
