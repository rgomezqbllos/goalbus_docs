import json

filepath = 'global_translations.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define translations for D1_imagen4 specific terms
new_translations = {
    "ui_text_1074": { # Leyenda
        "ES": "Leyenda",
        "EN": "Legend",
        "PT_BR": "Legenda",
        "IT": "Legenda",
        "FR": "Légende",
        "DE": "Legende"
    },
    "ui_text_1080": { # mayo 2026
        "ES": "mayo 2026",
        "EN": "May 2026",
        "PT_BR": "maio de 2026",
        "IT": "Maggio 2026",
        "FR": "Mai 2026",
        "DE": "Mai 2026"
    },
    "ui_text_1075": { # abril 2026
        "ES": "abril 2026",
        "EN": "April 2026",
        "PT_BR": "abril de 2026",
        "IT": "Aprile 2026",
        "FR": "Avril 2026",
        "DE": "April 2026"
    },
    "ui_text_1076": { # otto:absence
        "ES": "Ausencia",
        "EN": "Absence",
        "PT_BR": "Ausência",
        "IT": "Assenza",
        "FR": "Absence",
        "DE": "Abwesenheit",
        "_match": "attr:aria-label"
    },
    "ui_text_1077": { # otto:day-off
        "ES": "Descanso",
        "EN": "Day off",
        "PT_BR": "Descanso",
        "IT": "Riposo",
        "FR": "Repos",
        "DE": "Ruhe",
        "_match": "attr:aria-label"
    },
    "ui_text_1078": { # otto:stand-by
        "ES": "Disponibilidad",
        "EN": "Stand by",
        "PT_BR": "Disponibilidade",
        "IT": "Disponibilità",
        "FR": "Disponibilité",
        "DE": "Bereitschaft",
        "_match": "attr:aria-label"
    },
    "ui_text_1079": { # otto:task
        "ES": "Trabajo",
        "EN": "Duty",
        "PT_BR": "Trabalho",
        "IT": "Lavoro",
        "FR": "Travail",
        "DE": "Dienst",
        "_match": "attr:aria-label"
    }
}

# Apply new translations
for key, entry in new_translations.items():
    if key in data:
        data[key].update(entry)

# Ensure no other PENDING entries for these keys
for key in new_translations:
    if key in data:
        for lang in ["EN", "PT_BR", "IT", "FR", "DE"]:
            if data[key].get(lang) == "PENDING":
                # This shouldn't happen with update, but just in case
                pass

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Filled PENDING translations for D1_imagen4")
