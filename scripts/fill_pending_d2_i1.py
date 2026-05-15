import json

filepath = 'global_translations.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_translations = {
    "ui_text_1081": { # 29 may 2025
        "ES": "29 may 2025",
        "EN": "29 May 2025",
        "PT_BR": "29 de maio de 2025",
        "IT": "29 Maggio 2025",
        "FR": "29 mai 2025",
        "DE": "29. Mai 2025"
    },
    "ui_text_1082": { # Evening
        "ES": "Evening",
        "EN": "Evening",
        "PT_BR": "Noite",
        "IT": "Sera",
        "FR": "Soirée",
        "DE": "Abend"
    },
    "ui_text_1083": { # Tipo Vehículo: Standard
        "ES": "Tipo Vehículo: Standard",
        "EN": "Vehicle Type: Standard",
        "PT_BR": "Tipo de Veículo: Standard",
        "IT": "Tipo di Veicolo: Standard",
        "FR": "Type de véhicule : Standard",
        "DE": "Fahrzeugtyp: Standard"
    },
    "ui_text_1084": { # Vehículo: 2975-PU
        "ES": "Vehículo: 2975-PU",
        "EN": "Vehicle: 2975-PU",
        "PT_BR": "Veículo: 2975-PU",
        "IT": "Veicolo: 2975-PU",
        "FR": "Véhicule : 2975-PU",
        "DE": "Fahrzeug: 2975-PU"
    },
    "ui_text_1085": { # diciembre 2024
        "ES": "diciembre 2024",
        "EN": "December 2024",
        "PT_BR": "dezembro de 2024",
        "IT": "Dicembre 2024",
        "FR": "Décembre 2024",
        "DE": "Dezember 2024"
    },
    "ui_text_1086": { # otto:day-off
        "ES": "Descanso",
        "EN": "Day off",
        "PT_BR": "Descanso",
        "IT": "Riposo",
        "FR": "Repos",
        "DE": "Ruhe"
    },
    "ui_text_1087": { # otto:stand-by
        "ES": "Disponibilidad",
        "EN": "Stand by",
        "PT_BR": "Disponibilidade",
        "IT": "Disponibilità",
        "FR": "Disponibilité",
        "DE": "Bereitschaft"
    },
    "ui_text_1088": { # otto:task
        "ES": "Trabajo",
        "EN": "Duty",
        "PT_BR": "Trabalho",
        "IT": "Lavoro",
        "FR": "Travail",
        "DE": "Dienst"
    }
}

for key, entry in new_translations.items():
    if key in data:
        data[key].update(entry)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Filled PENDING translations for D2_imagen1")
