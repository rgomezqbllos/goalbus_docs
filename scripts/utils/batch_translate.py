import json
import os
import re

# Supported languages in global_translations.json
LANGS = ["EN", "PT_BR", "IT", "FR", "DE"]

def translate_batch():
    json_path = "global_translations.json"
    if not os.path.exists(json_path):
        print("global_translations.json not found")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Translation map for common strings
    # Keys are Spanish strings
    trans_map = {
        "Asignación de vehículos": {
            "EN": "Vehicle Assignment", "PT_BR": "Alocação de veículos", "IT": "Assegnazione veicoli", "FR": "Affectation de véhicules", "DE": "Fahrzeugzuweisung"
        },
        "Clientes": {
            "EN": "Clients", "PT_BR": "Clientes", "IT": "Clienti", "FR": "Clients", "DE": "Kunden"
        },
        "Colapsar Menú": {
            "EN": "Collapse Menu", "PT_BR": "Recolher Menu", "IT": "Comprimi Menu", "FR": "Réduire le Menu", "DE": "Menü einklappen"
        },
        "Configuración": {
            "EN": "Settings", "PT_BR": "Configuração", "IT": "Impostazioni", "FR": "Paramètres", "DE": "Einstellungen"
        },
        "Confirmar": {
            "EN": "Confirm", "PT_BR": "Confirmar", "IT": "Conferma", "FR": "Confirmer", "DE": "Bestätigen"
        },
        "Desasignar": {
            "EN": "Unassign", "PT_BR": "Desalocar", "IT": "Annulla assegnazione", "FR": "Désaffecter", "DE": "Zuweisung aufheben"
        },
        "Descartar": {
            "EN": "Discard", "PT_BR": "Descartar", "IT": "Scarta", "FR": "Abandonner", "DE": "Verwerfen"
        },
        "Escala": {
            "EN": "Scale", "PT_BR": "Escala", "IT": "Scala", "FR": "Échelle", "DE": "Skala"
        },
        "No hay asignaciones": {
            "EN": "No assignments", "PT_BR": "Não há alocações", "IT": "Nessuna assegnazione", "FR": "Aucune affectation", "DE": "Keine Zuweisungen"
        },
        "Notificaciones": {
            "EN": "Notifications", "PT_BR": "Notificações", "IT": "Notifiche", "FR": "Notifications", "DE": "Benachrichtigungen"
        },
        "Operaciones de Personal": {
            "EN": "Personnel Operations", "PT_BR": "Operações de Pessoal", "IT": "Operazioni del personale", "FR": "Opérations du personnel", "DE": "Personalbetrieb"
        },
        "Planificación": {
            "EN": "Planning", "PT_BR": "Planejamento", "IT": "Pianificazione", "FR": "Planification", "DE": "Planung"
        },
        "Reasignar": {
            "EN": "Reassign", "PT_BR": "Realocar", "IT": "Riassegna", "FR": "Réaffecter", "DE": "Neu zuweisen"
        },
        "Rostering": {
            "EN": "Rostering", "PT_BR": "Escalamento", "IT": "Turnazione", "FR": "Rostering", "DE": "Dienstplanung"
        },
        "Servicios": {
            "EN": "Services", "PT_BR": "Serviços", "IT": "Servizi", "FR": "Services", "DE": "Dienste"
        },
        "Vehículos": {
            "EN": "Vehicles", "PT_BR": "Veículos", "IT": "Veicoli", "FR": "Véhicules", "DE": "Fahrzeuge"
        },
        "Ver Detalles": {
            "EN": "View Details", "PT_BR": "Ver Detalhes", "IT": "Visualizza Dettagli", "FR": "Voir les Détails", "DE": "Details anzeigen"
        },
        "Asignar": {
            "EN": "Assign", "PT_BR": "Alocar", "IT": "Assegna", "FR": "Affecter", "DE": "Zuweisen"
        },
        "Creación:": {
            "EN": "Creation:", "PT_BR": "Criação:", "IT": "Creazione:", "FR": "Création :", "DE": "Erstellung:"
        },
        "Depósitos:": {
            "EN": "Depots:", "PT_BR": "Depósitos:", "IT": "Depositi:", "FR": "Dépôts :", "DE": "Depots:"
        },
        "Día de creación:": {
            "EN": "Creation day:", "PT_BR": "Dia de criação:", "IT": "Giorno di creazione:", "FR": "Jour de creación :", "DE": "Erstellungstag:"
        },
        "Eventos": {
            "EN": "Events", "PT_BR": "Eventos", "IT": "Eventi", "FR": "Événements", "DE": "Ereignisse"
        },
        "ID Escenario:": {
            "EN": "Scenario ID:", "PT_BR": "ID do Cenário:", "IT": "ID Scenario:", "FR": "ID Scénario :", "DE": "Szenario-ID:"
        },
        "Origen:": {
            "EN": "Origin:", "PT_BR": "Origem:", "IT": "Origine:", "FR": "Origine :", "DE": "Herkunft:"
        },
        "Partir": {
            "EN": "Split", "PT_BR": "Dividir", "IT": "Dividi", "FR": "Diviser", "DE": "Teilen"
        },
        "Sin Asignar": {
            "EN": "Unassigned", "PT_BR": "Sem alocação", "IT": "Non assegnato", "FR": "Non affecté", "DE": "Nicht zugewiesen"
        },
        "Tareas Sin Asignar": {
            "EN": "Unassigned Tasks", "PT_BR": "Tarefas sem alocação", "IT": "Attività non assegnate", "FR": "Tâches non affectées", "DE": "Nicht zugewiesene Aufgaben"
        },
        "Tipo de vehículo": {
            "EN": "Vehicle Type", "PT_BR": "Tipo de veículo", "IT": "Tipo di veicolo", "FR": "Type de véhicule", "DE": "Fahrzeugtyp"
        },
        "Todos": {
            "EN": "All", "PT_BR": "Todos", "IT": "Tutti", "FR": "Tous", "DE": "Alle"
        },
        "VACÍO": {
            "EN": "EMPTY", "PT_BR": "Ocioso", "IT": "VUOTO", "FR": "VIDE", "DE": "LEER"
        },
        "Aplicar": {
            "EN": "Apply", "PT_BR": "Aplicar", "IT": "Applica", "FR": "Appliquer", "DE": "Anwenden"
        },
        "Mostrando 55 vehículos": {
            "EN": "Showing 55 vehicles", "PT_BR": "Mostrando 55 veículos", "IT": "Mostrando 55 veicoli", "FR": "Affichage de 55 véhicules", "DE": "55 Fahrzeuge werden angezeigt"
        },
        "CONDUCTOR": {
            "EN": "DRIVER", "PT_BR": "MOTORISTA", "IT": "CONDUCENTE", "FR": "CONDUCTEUR", "DE": "FAHRER"
        },
        "DOMINGO": {
            "EN": "SUNDAY", "PT_BR": "DOMINGO", "IT": "DOMENICA", "FR": "DIMANCHE", "DE": "SONNTAG"
        },
        "Día libre": {
            "EN": "Day off", "PT_BR": "Folga", "IT": "Giorno libero", "FR": "Jour de repos", "DE": "Freier Tag"
        },
        "Errores  (1)": {
            "EN": "Errors (1)", "PT_BR": "Erros (1)", "IT": "Errori (1)", "FR": "Erreurs (1)", "DE": "Fehler (1)"
        },
        "JUEVES": {
            "EN": "THURSDAY", "PT_BR": "QUINTA-FEIRA", "IT": "GIOVEDÌ", "FR": "JEUDI", "DE": "DONNERSTAG"
        },
        "LUNES": {
            "EN": "MONDAY", "PT_BR": "SEGUNDA-FEIRA", "IT": "LUNEDÌ", "FR": "LUNDI", "DE": "MONTAG"
        },
        "MARTES": {
            "EN": "TUESDAY", "PT_BR": "TERÇA-FEIRA", "IT": "MARTEDÌ", "FR": "MARDI", "DE": "DIENSTAG"
        },
        "MIÉRCOLES": {
            "EN": "WEDNESDAY", "PT_BR": "QUARTA-FEIRA", "IT": "MERCOLEDÌ", "FR": "MERCREDI", "DE": "MITTWOCH"
        },
        "Operaciones diarias": {
            "EN": "Daily Operations", "PT_BR": "Operações diárias", "IT": "Operazioni quotidiane", "FR": "Opérations quotidiennes", "DE": "Täglicher Betrieb"
        },
        "SÁBADO": {
            "EN": "SATURDAY", "PT_BR": "SÁBADO", "IT": "SABATO", "FR": "SAMEDI", "DE": "SAMSTAG"
        },
        "VIERNES": {
            "EN": "FRIDAY", "PT_BR": "SEXTA-FEIRA", "IT": "VENERDÌ", "FR": "VENDREDI", "DE": "FREITAG"
        },
        "Vista Roster": {
            "EN": "Roster View", "PT_BR": "Vista do Roster", "IT": "Vista Turnazione", "FR": "Vue Roster", "DE": "Dienstplanansicht"
        },
        "Vista de Roster": {
            "EN": "Roster View", "PT_BR": "Vista do Roster", "IT": "Vista Turnazione", "FR": "Vue Roster", "DE": "Dienstplanansicht"
        },
        "A órdenes": {
            "EN": "On call", "PT_BR": "À disposição", "IT": "A disposizione", "FR": "De réserve", "DE": "Auf Abruf"
        },
        "VAC": {
            "EN": "VAC", "PT_BR": "FÉR", "IT": "FER", "FR": "CON", "DE": "URL"
        },
        "Limpieza": {
            "EN": "Cleaning", "PT_BR": "Limpeza", "IT": "Pulizia", "FR": "Nettoyage", "DE": "Reinigung"
        },
        "Pinchazo": {
            "EN": "Puncture", "PT_BR": "Furo", "IT": "Foratura", "FR": "Crevaison", "DE": "Reifenschaden"
        },
        "GoalBus": {
            "EN": "GoalBus", "PT_BR": "GoalBus", "IT": "GoalBus", "FR": "GoalBus", "DE": "GoalBus"
        },
        "Logo de GoalBus Ops": {
            "EN": "GoalBus Ops Logo", "PT_BR": "Logo do GoalBus Ops", "IT": "Logo di GoalBus Ops", "FR": "Logo de GoalBus Ops", "DE": "GoalBus Ops Logo"
        },
        "PARKING A PARKING": {
            "EN": "PARKING TO PARKING", "PT_BR": "ESTACIONAMENTO A ESTACIONAMENTO", "IT": "PARCHEGGIO A PARCHEGGIO", "FR": "PARKING À PARKING", "DE": "PARKPLATZ ZU PARKPLATZ"
        }
    }

    # Month mapping for date strings
    months_es = {
        "abr": {"EN": "Apr", "PT_BR": "abr", "IT": "apr", "FR": "avr", "DE": "Apr"},
        "mar": {"EN": "Mar", "PT_BR": "mar", "IT": "mar", "FR": "mar", "DE": "Mrz"},
        "may": {"EN": "May", "PT_BR": "mai", "IT": "mag", "FR": "mai", "DE": "Mai"}
    }

    # Weekday short mapping
    weekdays_es = {
        "lu.": {"EN": "Mon", "PT_BR": "seg.", "IT": "lun.", "FR": "lun.", "DE": "Mo."},
        "ma.": {"EN": "Tue", "PT_BR": "ter.", "IT": "mar.", "FR": "mar.", "DE": "Di."},
        "mi.": {"EN": "Wed", "PT_BR": "qua.", "IT": "mer.", "FR": "mer.", "DE": "Mi."},
        "ju.": {"EN": "Thu", "PT_BR": "qui.", "IT": "gio.", "FR": "jeu.", "DE": "Do."},
        "vi.": {"EN": "Fri", "PT_BR": "sex.", "IT": "ven.", "FR": "ven.", "DE": "Fr."},
        "sa.": {"EN": "Sat", "PT_BR": "sáb.", "IT": "sab.", "FR": "sam.", "DE": "Sa."},
        "do.": {"EN": "Sun", "PT_BR": "dom.", "IT": "dom.", "FR": "dim.", "DE": "So."}
    }

    updated_count = 0

    for key, entry in data.items():
        es_val = entry.get("ES")
        if not es_val:
            continue

        for lang in LANGS:
            if entry.get(lang) == "PENDING" or lang not in entry:
                
                # 1. Direct map
                if es_val in trans_map:
                    entry[lang] = trans_map[es_val][lang]
                    updated_count += 1
                
                # 2. Codes / IDs (No translation)
                elif re.match(r'^(00\d\d-[A-Z]+|Veh_\d+(_\d+)?|PA\d+|[A-Z0-9_\-]+|otto:[a-z_]+|\d+_\d+|\d+\.\d+x \(\d+ h\)|\d+ km|[\w\.]+@[\w\.]+|battery_charging_full-fill)$', es_val):
                    entry[lang] = es_val
                    updated_count += 1
                
                # 3. Names (No translation)
                elif re.match(r'^Nombre\d+ Apellido\d+$', es_val) or "Test_Bruno_Demo / Hola Consultant" in es_val:
                    entry[lang] = es_val
                    updated_count += 1
                
                # 4. Dates "01 abr 2026"
                elif re.match(r'^\d\d [a-z]{3} \d\d\d\d$', es_val):
                    parts = es_val.split()
                    day, month_es, year = parts
                    if month_es in months_es:
                        entry[lang] = f"{day} {months_es[month_es][lang]} {year}"
                        updated_count += 1

                # 5. Relative dates "lu. may 4, 2026"
                elif re.match(r'^[a-z]{2}\. [a-z]{3} \d+, \d\d\d\d$', es_val):
                    m = re.match(r'^([a-z]{2}\.) ([a-z]{3}) (\d+, \d\d\d\d)$', es_val)
                    wd, mo, rest = m.groups()
                    if wd in weekdays_es and mo in months_es:
                        entry[lang] = f"{weekdays_es[wd][lang]} {months_es[mo][lang]} {rest}"
                        updated_count += 1

                # 6. Ordinal dates "abr 1º"
                elif re.match(r'^[a-z]{3} \d+º$', es_val):
                    m = re.match(r'^([a-z]{3}) (\d+º)$', es_val)
                    mo, ord_str = m.groups()
                    if mo in months_es:
                        if lang == "EN":
                            entry[lang] = f"{months_es[mo][lang]} {ord_str[:-1]}"
                        elif lang == "DE":
                            entry[lang] = f"{months_es[mo][lang]} {ord_str[:-1]}."
                        else:
                            entry[lang] = f"{months_es[mo][lang]} {ord_str}"
                        updated_count += 1
                
                # 7. Week ranges "27 abr a 03 may 2026"
                elif re.match(r'^\d\d [a-z]{3} a \d\d [a-z]{3} \d\d\d\d$', es_val):
                    m = re.match(r'^(\d\d) ([a-z]{3}) a (\d\d) ([a-z]{3}) (\d\d\d\d)$', es_val)
                    d1, m1, d2, m2, yr = m.groups()
                    if m1 in months_es and m2 in months_es:
                        sep = {"EN": "to", "PT_BR": "a", "IT": "a", "FR": "à", "DE": "bis"}[lang]
                        entry[lang] = f"{d1} {months_es[m1][lang]} {sep} {d2} {months_es[m2][lang]} {yr}"
                        updated_count += 1

                # 8. Transfer patterns "PARKING A PA0001-PA0001"
                elif " A " in es_val:
                    m = re.match(r'^(.*?) A (.*?)$', es_val)
                    p1, p2 = m.groups()
                    sep = {"EN": "TO", "PT_BR": "A", "IT": "A", "FR": "À", "DE": "ZU"}[lang]
                    entry[lang] = f"{p1} {sep} {p2}"
                    updated_count += 1
                
                # 9. Complex strings with fixed parts "Consultant comenzó a editar..."
                elif "comenzó a editar la Celda de Roster a las" in es_val:
                    m = re.match(r'^(.*?) comenzó a editar la Celda de Roster a las (.*)$', es_val)
                    name, time = m.groups()
                    t_msg = {
                        "EN": f"{name} started editing the Roster Cell at {time}",
                        "PT_BR": f"{name} começou a editar a Célula do Roster às {time}",
                        "IT": f"{name} ha iniziato a modificare la Cella Turnazione alle {time}",
                        "FR": f"{name} a commencé à éditer la cellule de Roster à {time}",
                        "DE": f"{name} hat begonnen, die Dienstplanzelle um {time} Uhr zu bearbeiten"
                    }[lang]
                    entry[lang] = t_msg
                    updated_count += 1

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Updated {updated_count} translation fields.")

if __name__ == "__main__":
    translate_batch()
