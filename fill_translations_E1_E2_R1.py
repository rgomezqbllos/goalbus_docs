"""
Rellena las traducciones pendientes de E1, E2, R1 para todos los idiomas.
Genera e importa los TSV de cada idioma.
"""
import csv, io, os, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))

# ─── Tabla de traducciones ────────────────────────────────────────────────────
# Formato: ES_value → {lang: translated_value}
# Si un idioma no está en el dict, se usa el valor ES tal cual (identificadores)

TRANSLATIONS = {
    # ── Identificadores técnicos: iguales en todos ──────────────────────────
    "1475_20":                         {},
    "GoalBus.Driver":                  {},
    "newCalendar - 03:21":             {},
    "newCalendar - 16:43":             {},
    "newCalendar - 19:47":             {},
    "newCalendar - 20:10":             {},
    "newCalendar - 20:12":             {},
    "newCalendar - 20:41":             {},
    "newCalendar - 21:58":             {},
    "newCalendar - 22:56":             {},
    "otto:task":                       {},
    "otto:absence":                    {},
    "otto:day-off":                    {},
    "otto:stand-by":                   {},
    "user.consultant@otto.com - 02:40": {},
    "user.consultant@otto.com - 02:41": {},
    "user.consultant@otto.com - 08:38": {},
    "user.consultant@otto.com - 16:03": {},
    "user.consultant@otto.com - 16:05": {},
    "user.consultant@otto.com - 18:19": {},
    "user.consultant@otto.com - 19:59": {},
    "user.consultant@otto.com - 20:00": {},
    "user.consultant@otto.com - 20:51": {},
    "user.consultant@otto.com - 21:42": {},
    "user.consultant@otto.com - 22:06": {},
    "user.consultant@otto.com - 23:09": {},
    "LOOP-JRS":                        {},
    "PnR-1 AQ":                        {},
    "PnR-1 SF":                        {},
    "Qiddiya Test / Welcome Consultant": {},
    "Qiddiya Training Test":           {},
    "SHTL1-JRS AQ":                    {},
    "SHTL1-JRS SF":                    {},
    "SHTL2-STC SF":                    {},
    "Veh_1":  {}, "Veh_2":  {}, "Veh_3":  {}, "Veh_4":  {}, "Veh_5":  {},
    "Veh_6":  {}, "Veh_7":  {}, "Veh_8":  {}, "Veh_9":  {}, "Veh_10": {},
    "Veh_11": {}, "Veh_12": {}, "Veh_13": {}, "Veh_14": {}, "Veh_15": {},
    "Veh_16": {}, "Veh_17": {}, "Veh_18": {}, "Veh_19": {},
    "sort":                            {},
    "3177_1":  {}, "3177_2":  {}, "3177_3":  {}, "3177_4":  {}, "3177_5":  {},
    "3177_6":  {}, "3177_7":  {}, "3177_8":  {}, "3177_9":  {}, "3177_10": {},
    "3177_11": {}, "3177_12": {}, "3177_13": {}, "3177_14": {}, "3177_15": {},
    "3177_16": {}, "3177_17": {}, "3177_18": {}, "3177_19": {}, "3177_20": {},
    "3177_21": {}, "3177_22": {}, "3177_23": {}, "3177_24": {}, "3177_25": {},
    "3177_26": {},
    "DEPOT":                           {},
    "L1":                              {},
    "N":                               {},
    "PA00":                            {},
    "Test_Bruno_Demo / Hola Consultant": {},
    "sync":                            {},
    "STANDARD-ELECTRIC":               {},
    "battery_charging_full-fill":      {},
    ": 13.1 km":                       {},
    ": 23 Kwh":                        {},
    ": L1":                            {},
    ": PA0001":                        {},
    ": PA0002":                        {},
    "5851_1": {}, "5851_2": {}, "5851_3": {}, "5851_5": {},
    "DP TETLAN T01":                   {},
    "ELEC 12M VOLVO LUMINUS":          {},
    "ELEC ART":                        {},
    "PK TALLERESL3 T01":               {},
    "SITEUR GDL / Hola Consultant":    {},
    "T01":                             {},
    "T01 Aeropuerto-Aeropuerto":       {},
    "T01 ELECT":                       {},
    "electric_bolt-fill":              {},
    "1.0x (36 h)":                     {},
    "M45":                             {},
    "Hertzallee-3109":                 {},
    "Memhardstr.-7379":                {},
    "Michelangelostr. [Bushafen]-4474": {},
    "S+U Rathaus Spandau-1880":        {},
    "C":                               {},
    "Dashboard":                       {},
    "Annual Leave":                    {},  # término de producto, igual en todos
    "Morning":                         {},  # igual en todos
    "Night":                           {},  # igual en todos
    "0 km":  {}, "2 km":  {}, "6 km":  {}, "8 km":  {},
    "11 km": {}, "13 km": {}, "14 km": {},
    "0 h":   {}, "125 h": {}, "168 h": {},
    "27.20 km": {}, "3326 kWh": {},
    "Worker Village":                  {},  # nombre de lugar

    # ── Strings ya en inglés, solo traducir para FR/DE/IT/PT_BR ─────────────
    "Advanced filters":     {"FR": "Filtres avancés",          "DE": "Erweiterte Filter",        "IT": "Filtri avanzati",          "PT_BR": "Filtros avançados"},
    "Clear filters":        {"FR": "Effacer les filtres",      "DE": "Filter löschen",           "IT": "Cancella filtri",          "PT_BR": "Limpar filtros"},
    "Scheduling Scenarios": {"FR": "Scénarios de planification","DE": "Planungsszenarien",        "IT": "Scenari di programmazione","PT_BR": "Cenários de programação"},
    "Services Overview":    {"FR": "Vue d'ensemble des services","DE": "Dienstübersicht",         "IT": "Panoramica servizi",       "PT_BR": "Visão geral dos serviços"},
    "Settings":             {"FR": "Paramètres",               "DE": "Einstellungen",            "IT": "Impostazioni",             "PT_BR": "Configurações"},
    "Showing 44 vehicles":  {"FR": "Affichage de 44 véhicules","DE": "44 Fahrzeuge anzeigen",    "IT": "Visualizzazione di 44 veicoli","PT_BR": "Exibindo 44 veículos"},
    "Sort":                 {"FR": "Trier",                    "DE": "Sortieren",                "IT": "Ordina",                   "PT_BR": "Ordenar"},
    "Staff Operations":     {"FR": "Opérations du personnel",  "DE": "Personaloperationen",      "IT": "Operazioni del personale", "PT_BR": "Operações de pessoal"},
    "Tenants":              {"FR": "Locataires",               "DE": "Mandanten",                "IT": "Tenant",                   "PT_BR": "Clientes"},
    "Vehicles Assignment":  {"FR": "Affectation des véhicules","DE": "Fahrzeugzuweisung",        "IT": "Assegnazione veicoli",     "PT_BR": "Atribuição de veículos"},
    "Vehicles View":        {"FR": "Vue des véhicules",        "DE": "Fahrzeugansicht",          "IT": "Vista veicoli",            "PT_BR": "Visão de veículos"},
    "Please enable JavaScript to continue using this application.": {
        "FR": "Veuillez activer JavaScript pour continuer à utiliser cette application.",
        "DE": "Bitte aktivieren Sie JavaScript, um diese Anwendung weiter zu nutzen.",
        "IT": "Si prega di abilitare JavaScript per continuare a utilizzare questa applicazione.",
        "PT_BR": "Por favor, habilite o JavaScript para continuar usando esta aplicação.",
    },
    "Total": {"FR": "Total", "DE": "Gesamt", "IT": "Totale", "PT_BR": "Total"},

    # ── Traducciones completas por idioma ─────────────────────────────────────
    "Actualizaciones de la asignación": {
        "EN": "Assignment Updates",
        "FR": "Mises à jour des affectations",
        "DE": "Zuteilungsaktualisierungen",
        "IT": "Aggiornamenti dell'assegnazione",
        "PT_BR": "Atualizações da atribuição",
    },
    "Calendario": {
        "EN": "Calendar",
        "FR": "Calendrier",
        "DE": "Kalender",
        "IT": "Calendario",
        "PT_BR": "Calendário",
    },
    "Finaliza:": {
        "EN": "Ends:",
        "FR": "Se termine :",
        "DE": "Endet:",
        "IT": "Termina:",
        "PT_BR": "Termina:",
    },
    "Inicio:": {
        "EN": "Start:",
        "FR": "Début :",
        "DE": "Beginn:",
        "IT": "Inizio:",
        "PT_BR": "Início:",
    },
    "La solicitud de Annual Leave entre mar 19 y mar 22 ha sido aprobada y tu horario ha sido actualizado.": {
        "EN": "The Annual Leave request between Tue 19 and Tue 22 has been approved and your schedule has been updated.",
        "FR": "La demande de congé annuel du mar. 19 au mar. 22 a été approuvée et votre planning a été mis à jour.",
        "DE": "Der Antrag auf Jahresurlaub vom Di. 19 bis Di. 22 wurde genehmigt und Ihr Dienstplan wurde aktualisiert.",
        "IT": "La richiesta di Annual Leave tra mar 19 e mar 22 è stata approvata e il tuo orario è stato aggiornato.",
        "PT_BR": "A solicitação de Annual Leave entre ter 19 e ter 22 foi aprovada e seu horário foi atualizado.",
    },
    "La solicitud de Annual Leave para mar 25 ha sido aprobada y tu horario ha sido actualizado.": {
        "EN": "The Annual Leave request for Tue 25 has been approved and your schedule has been updated.",
        "FR": "La demande de congé annuel pour le mar. 25 a été approuvée et votre planning a été mis à jour.",
        "DE": "Der Antrag auf Jahresurlaub für Di. 25 wurde genehmigt und Ihr Dienstplan wurde aktualisiert.",
        "IT": "La richiesta di Annual Leave per mar 25 è stata approvata e il tuo orario è stato aggiornato.",
        "PT_BR": "A solicitação de Annual Leave para ter 25 foi aprovada e seu horário foi atualizado.",
    },
    "La solicitud de Medical Visit para ene 26 ha sido aprobada y tu horario ha sido actualizado.": {
        "EN": "The Medical Visit request for Jan 26 has been approved and your schedule has been updated.",
        "FR": "La demande de visite médicale pour le 26 janv. a été approuvée et votre planning a été mis à jour.",
        "DE": "Der Antrag auf Arztbesuch für den 26. Jan. wurde genehmigt und Ihr Dienstplan wurde aktualisiert.",
        "IT": "La richiesta di visita medica per il 26 gen è stata approvata e il tuo orario è stato aggiornato.",
        "PT_BR": "A solicitação de visita médica para 26 de jan foi aprovada e seu horário foi atualizado.",
    },
    "La solicitud de Medical Visit para mar 16 ha sido aprobada y tu horario ha sido actualizado.": {
        "EN": "The Medical Visit request for Tue 16 has been approved and your schedule has been updated.",
        "FR": "La demande de visite médicale pour le mar. 16 a été approuvée et votre planning a été mis à jour.",
        "DE": "Der Antrag auf Arztbesuch für Di. 16 wurde genehmigt und Ihr Dienstplan wurde aktualisiert.",
        "IT": "La richiesta di visita medica per mar 16 è stata approvata e il tuo orario è stato aggiornato.",
        "PT_BR": "A solicitação de visita médica para ter 16 foi aprovada e seu horário foi atualizado.",
    },
    "La solicitud de Medical Visit para mar 17 ha sido aprobada y tu horario ha sido actualizado.": {
        "EN": "The Medical Visit request for Tue 17 has been approved and your schedule has been updated.",
        "FR": "La demande de visite médicale pour le mar. 17 a été approuvée et votre planning a été mis à jour.",
        "DE": "Der Antrag auf Arztbesuch für Di. 17 wurde genehmigt und Ihr Dienstplan wurde aktualisiert.",
        "IT": "La richiesta di visita medica per mar 17 è stata approvata e il tuo orario è stato aggiornato.",
        "PT_BR": "A solicitação de visita médica para ter 17 foi aprovada e seu horário foi atualizado.",
    },
    "Mensajes": {
        "EN": "Messages",
        "FR": "Messages",
        "DE": "Nachrichten",
        "IT": "Messaggi",
        "PT_BR": "Mensagens",
    },
    "Solicitudes": {
        "EN": "Requests",
        "FR": "Demandes",
        "DE": "Anfragen",
        "IT": "Richieste",
        "PT_BR": "Solicitações",
    },
    "Tienes cambios en tu calendario entre el  dic 15 y el dic 28": {
        "EN": "You have changes in your calendar between Dec 15 and Dec 28",
        "FR": "Vous avez des modifications dans votre planning entre le 15 déc. et le 28 déc.",
        "DE": "Sie haben Änderungen in Ihrem Kalender zwischen dem 15. Dez. und dem 28. Dez.",
        "IT": "Hai modifiche nel tuo calendario tra il 15 dic. e il 28 dic.",
        "PT_BR": "Você tem alterações em seu calendário entre 15 de dez. e 28 de dez.",
    },
    "Tienes cambios en tu calendario entre el  dic 30 y el ene 1": {
        "EN": "You have changes in your calendar between Dec 30 and Jan 1",
        "FR": "Vous avez des modifications dans votre planning entre le 30 déc. et le 1 janv.",
        "DE": "Sie haben Änderungen in Ihrem Kalender zwischen dem 30. Dez. und dem 1. Jan.",
        "IT": "Hai modifiche nel tuo calendario tra il 30 dic. e il 1 gen.",
        "PT_BR": "Você tem alterações em seu calendário entre 30 de dez. e 1 de jan.",
    },
    "Tienes cambios en tu calendario entre el  dic 8 y el dic 14": {
        "EN": "You have changes in your calendar between Dec 8 and Dec 14",
        "FR": "Vous avez des modifications dans votre planning entre le 8 déc. et le 14 déc.",
        "DE": "Sie haben Änderungen in Ihrem Kalender zwischen dem 8. Dez. und dem 14. Dez.",
        "IT": "Hai modifiche nel tuo calendario tra l'8 dic. e il 14 dic.",
        "PT_BR": "Você tem alterações em seu calendário entre 8 de dez. e 14 de dez.",
    },
    "Tienes cambios en tu calendario entre el  ene 26 y el ene 26": {
        "EN": "You have changes in your calendar on Jan 26",
        "FR": "Vous avez des modifications dans votre planning le 26 janv.",
        "DE": "Sie haben Änderungen in Ihrem Kalender am 26. Jan.",
        "IT": "Hai modifiche nel tuo calendario il 26 gen.",
        "PT_BR": "Você tem alterações em seu calendário em 26 de jan.",
    },
    "Tienes cambios en tu calendario entre el  ene 26 y el ene 27": {
        "EN": "You have changes in your calendar between Jan 26 and Jan 27",
        "FR": "Vous avez des modifications dans votre planning entre le 26 janv. et le 27 janv.",
        "DE": "Sie haben Änderungen in Ihrem Kalender zwischen dem 26. Jan. und dem 27. Jan.",
        "IT": "Hai modifiche nel tuo calendario tra il 26 gen. e il 27 gen.",
        "PT_BR": "Você tem alterações em seu calendário entre 26 de jan. e 27 de jan.",
    },
    "Tienes cambios en tu calendario entre el  ene 27 y el feb 1": {
        "EN": "You have changes in your calendar between Jan 27 and Feb 1",
        "FR": "Vous avez des modifications dans votre planning entre le 27 janv. et le 1 févr.",
        "DE": "Sie haben Änderungen in Ihrem Kalender zwischen dem 27. Jan. und dem 1. Feb.",
        "IT": "Hai modifiche nel tuo calendario tra il 27 gen. e il 1 feb.",
        "PT_BR": "Você tem alterações em seu calendário entre 27 de jan. e 1 de fev.",
    },
    "Tienes cambios en tu calendario entre el  mar 16 y el mar 22": {
        "EN": "You have changes in your calendar between Tue 16 and Tue 22",
        "FR": "Vous avez des modifications dans votre planning entre le mar. 16 et le mar. 22",
        "DE": "Sie haben Änderungen in Ihrem Kalender zwischen Di. 16 und Di. 22",
        "IT": "Hai modifiche nel tuo calendario tra mar 16 e mar 22",
        "PT_BR": "Você tem alterações em seu calendário entre ter 16 e ter 22",
    },
    "sí": {
        "EN": "Yes",
        "FR": "Oui",
        "DE": "Ja",
        "IT": "Sì",
        "PT_BR": "Sim",
    },
    "vi": {
        "EN": "Fri",
        "FR": "Ven",
        "DE": "Fr",
        "IT": "Ven",
        "PT_BR": "Sex",
    },
    "22:10 a 02:01": {
        "EN": "22:10 to 02:01",
        "FR": "22:10 à 02:01",
        "DE": "22:10 bis 02:01",
        "IT": "22:10 alle 02:01",
        "PT_BR": "22:10 às 02:01",
    },
    "Cerrar": {
        "EN": "Close",
        "FR": "Fermer",
        "DE": "Schließen",
        "IT": "Chiudi",
        "PT_BR": "Fechar",
    },
    "Detalle de las tareas": {
        "EN": "Task Details",
        "FR": "Détail des tâches",
        "DE": "Aufgabendetails",
        "IT": "Dettaglio compiti",
        "PT_BR": "Detalhes das tarefas",
    },
    "Distancia": {
        "EN": "Distance",
        "FR": "Distance",
        "DE": "Entfernung",
        "IT": "Distanza",
        "PT_BR": "Distância",
    },
    "Eventos": {
        "EN": "Events",
        "FR": "Événements",
        "DE": "Ereignisse",
        "IT": "Eventi",
        "PT_BR": "Eventos",
    },
    "Expedición": {
        "EN": "Trip",
        "FR": "Expédition",
        "DE": "Fahrt",
        "IT": "Corsa",
        "PT_BR": "Viagem",
    },
    "Fin de bus": {
        "EN": "Bus End",
        "FR": "Fin de bus",
        "DE": "Busende",
        "IT": "Fine bus",
        "PT_BR": "Fim de ônibus",
    },
    "Fin de servicio": {
        "EN": "End of Service",
        "FR": "Fin de service",
        "DE": "Dienstende",
        "IT": "Fine servizio",
        "PT_BR": "Fim de serviço",
    },
    "Inicio de servicio": {
        "EN": "Start of Service",
        "FR": "Début de service",
        "DE": "Dienstbeginn",
        "IT": "Inizio servizio",
        "PT_BR": "Início de serviço",
    },
    "Lugar de inicio": {
        "EN": "Starting Location",
        "FR": "Lieu de départ",
        "DE": "Startort",
        "IT": "Luogo di partenza",
        "PT_BR": "Local de início",
    },
    "Sentido": {
        "EN": "Direction",
        "FR": "Direction",
        "DE": "Richtung",
        "IT": "Senso",
        "PT_BR": "Sentido",
    },
    "Tipo Vehículo": {
        "EN": "Vehicle Type",
        "FR": "Type de véhicule",
        "DE": "Fahrzeugtyp",
        "IT": "Tipo veicolo",
        "PT_BR": "Tipo de veículo",
    },
    "Tipo de evento": {
        "EN": "Event Type",
        "FR": "Type d'événement",
        "DE": "Ereignistyp",
        "IT": "Tipo di evento",
        "PT_BR": "Tipo de evento",
    },
    "Viaje en vacío": {
        "EN": "Empty Trip",
        "FR": "Trajet à vide",
        "DE": "Leerfahrt",
        "IT": "Viaggio a vuoto",
        "PT_BR": "Viagem vazia",
    },
    "1 días": {
        "EN": "1 day",
        "FR": "1 jour",
        "DE": "1 Tag",
        "IT": "1 giorno",
        "PT_BR": "1 dia",
    },
    "10 días": {
        "EN": "10 days",
        "FR": "10 jours",
        "DE": "10 Tage",
        "IT": "10 giorni",
        "PT_BR": "10 dias",
    },
    "19 días": {
        "EN": "19 days",
        "FR": "19 jours",
        "DE": "19 Tage",
        "IT": "19 giorni",
        "PT_BR": "19 dias",
    },
    "23 may 2026": {
        "EN": "23 May 2026",
        "FR": "23 mai 2026",
        "DE": "23. Mai 2026",
        "IT": "23 mag 2026",
        "PT_BR": "23 mai 2026",
    },
    "23 may 2026 - 23 may 2026": {
        "EN": "23 May 2026 - 23 May 2026",
        "FR": "23 mai 2026 - 23 mai 2026",
        "DE": "23. Mai 2026 - 23. Mai 2026",
        "IT": "23 mag 2026 - 23 mag 2026",
        "PT_BR": "23 mai 2026 - 23 mai 2026",
    },
    "30 días": {
        "EN": "30 days",
        "FR": "30 jours",
        "DE": "30 Tage",
        "IT": "30 giorni",
        "PT_BR": "30 dias",
    },
    "Annual Leave resumen": {
        "EN": "Annual Leave Summary",
        "FR": "Résumé des congés annuels",
        "DE": "Jahresurlaub Übersicht",
        "IT": "Riepilogo ferie annuali",
        "PT_BR": "Resumo de férias anuais",
    },
    "Aprobado": {
        "EN": "Approved",
        "FR": "Approuvé",
        "DE": "Genehmigt",
        "IT": "Approvato",
        "PT_BR": "Aprovado",
    },
    "Pendiente de aprobación": {
        "EN": "Pending Approval",
        "FR": "En attente d'approbation",
        "DE": "Ausstehende Genehmigung",
        "IT": "In attesa di approvazione",
        "PT_BR": "Pendente de aprovação",
    },
    "Restantes": {
        "EN": "Remaining",
        "FR": "Restants",
        "DE": "Verbleibend",
        "IT": "Rimanenti",
        "PT_BR": "Restantes",
    },
    "Solicitud de ausencia": {
        "EN": "Absence Request",
        "FR": "Demande d'absence",
        "DE": "Abwesenheitsantrag",
        "IT": "Richiesta di assenza",
        "PT_BR": "Solicitação de ausência",
    },
    "Tipo de ausencia": {
        "EN": "Absence Type",
        "FR": "Type d'absence",
        "DE": "Abwesenheitstyp",
        "IT": "Tipo di assenza",
        "PT_BR": "Tipo de ausência",
    },
    "Consultant  comenzó a editar la Celda de Roster a las 13:34": {
        "EN": "Consultant started editing the Roster Cell at 13:34",
        "FR": "Consultant a commencé à modifier la cellule du Roster à 13:34",
        "DE": "Consultant hat angefangen, die Roster-Zelle um 13:34 zu bearbeiten",
        "IT": "Consultant ha iniziato a modificare la cella del Roster alle 13:34",
        "PT_BR": "Consultant começou a editar a Célula de Escala às 13:34",
    },
    "Desasignar": {
        "EN": "Unassign",
        "FR": "Désaffecter",
        "DE": "Zuweisung aufheben",
        "IT": "Annulla assegnazione",
        "PT_BR": "Desatribuir",
    },
    "Reasignar": {
        "EN": "Reassign",
        "FR": "Réaffecter",
        "DE": "Neu zuweisen",
        "IT": "Riassegna",
        "PT_BR": "Reatribuir",
    },
    "Scheduling Classic - L1 Laborable": {
        "EN": "Scheduling Classic - L1 Working Day",
        "FR": "Scheduling Classic - L1 Jour Ouvrable",
        "DE": "Scheduling Classic - L1 Werktag",
        "IT": "Scheduling Classic - L1 Giorno Lavorativo",
        "PT_BR": "Scheduling Classic - L1 Dia Útil",
    },
    "Agregar Viaje Vacío": {
        "EN": "Add Empty Trip",
        "FR": "Ajouter un trajet à vide",
        "DE": "Leerfahrt hinzufügen",
        "IT": "Aggiungi viaggio a vuoto",
        "PT_BR": "Adicionar viagem vazia",
    },
    "Conductor Lógico": {
        "EN": "Logical Driver",
        "FR": "Conducteur logique",
        "DE": "Logischer Fahrer",
        "IT": "Conducente logico",
        "PT_BR": "Condutor lógico",
    },
    "Crear Evento": {
        "EN": "Create Event",
        "FR": "Créer un événement",
        "DE": "Ereignis erstellen",
        "IT": "Crea evento",
        "PT_BR": "Criar evento",
    },
    "Duración": {
        "EN": "Duration",
        "FR": "Durée",
        "DE": "Dauer",
        "IT": "Durata",
        "PT_BR": "Duração",
    },
    "Hora Final": {
        "EN": "End Time",
        "FR": "Heure de fin",
        "DE": "Endzeit",
        "IT": "Ora finale",
        "PT_BR": "Hora final",
    },
    "Parada de Inicio": {
        "EN": "Starting Stop",
        "FR": "Arrêt de départ",
        "DE": "Starthaltestelle",
        "IT": "Fermata di partenza",
        "PT_BR": "Parada inicial",
    },
    ": 45 minutos": {
        "EN": ": 45 minutes",
        "FR": ": 45 minutes",
        "DE": ": 45 Minuten",
        "IT": ": 45 minuti",
        "PT_BR": ": 45 minutos",
    },
    ": Expedicion": {
        "EN": ": Trip",
        "FR": ": Expédition",
        "DE": ": Fahrt",
        "IT": ": Corsa",
        "PT_BR": ": Expedição",
    },
    "E. Consumida": {
        "EN": "E. Consumed",
        "FR": "É. Consommée",
        "DE": "E. Verbraucht",
        "IT": "E. Consumata",
        "PT_BR": "E. Consumida",
    },
    "Estado final de la batería": {
        "EN": "Final Battery Level",
        "FR": "Niveau final de la batterie",
        "DE": "Endladezustand der Batterie",
        "IT": "Livello finale della batteria",
        "PT_BR": "Nível final da bateria",
    },
    "Línea": {
        "EN": "Line",
        "FR": "Ligne",
        "DE": "Linie",
        "IT": "Linea",
        "PT_BR": "Linha",
    },
    "Tipo": {
        "EN": "Type",
        "FR": "Type",
        "DE": "Typ",
        "IT": "Tipo",
        "PT_BR": "Tipo",
    },
    "1 - 10 de 389": {
        "EN": "1 - 10 of 389",
        "FR": "1 - 10 sur 389",
        "DE": "1 - 10 von 389",
        "IT": "1 - 10 di 389",
        "PT_BR": "1 - 10 de 389",
    },
    "19,00 kWh": {
        "EN": "19.00 kWh",
        "FR": "19,00 kWh",
        "DE": "19,00 kWh",
        "IT": "19,00 kWh",
        "PT_BR": "19,00 kWh",
    },
    "Carga Final (%)": {
        "EN": "Final Charge (%)",
        "FR": "Charge finale (%)",
        "DE": "Endladung (%)",
        "IT": "Carica finale (%)",
        "PT_BR": "Carga final (%)",
    },
    "E. Cargada": {
        "EN": "E. Charged",
        "FR": "É. Chargée",
        "DE": "E. Geladen",
        "IT": "E. Caricata",
        "PT_BR": "E. Carregada",
    },
    "Energía total consumida": {
        "EN": "Total energy consumed",
        "FR": "Énergie totale consommée",
        "DE": "Gesamtenergieverbrauch",
        "IT": "Energia totale consumata",
        "PT_BR": "Energia total consumida",
    },
    "Energía total recargada": {
        "EN": "Total energy recharged",
        "FR": "Énergie totale rechargée",
        "DE": "Gesamtenergie aufgeladen",
        "IT": "Energia totale ricaricata",
        "PT_BR": "Energia total recarregada",
    },
    "Inicio de bus": {
        "EN": "Bus Start",
        "FR": "Début de bus",
        "DE": "Busstart",
        "IT": "Inizio bus",
        "PT_BR": "Início de ônibus",
    },
    "Número total de recargas": {
        "EN": "Total number of recharges",
        "FR": "Nombre total de recharges",
        "DE": "Gesamtanzahl der Ladevorgänge",
        "IT": "Numero totale di ricariche",
        "PT_BR": "Número total de recargas",
    },
    "Resultados: 389": {
        "EN": "Results: 389",
        "FR": "Résultats : 389",
        "DE": "Ergebnisse: 389",
        "IT": "Risultati: 389",
        "PT_BR": "Resultados: 389",
    },
    "Tabla General de Eventos": {
        "EN": "General Events Table",
        "FR": "Tableau général des événements",
        "DE": "Allgemeine Ereignistabelle",
        "IT": "Tabella generale degli eventi",
        "PT_BR": "Tabela geral de eventos",
    },
    "Vacío externo": {
        "EN": "External Empty",
        "FR": "Vide externe",
        "DE": "Externe Leerfahrt",
        "IT": "Vuoto esterno",
        "PT_BR": "Vazio externo",
    },
    "Vehículo Lógico": {
        "EN": "Logical Vehicle",
        "FR": "Véhicule logique",
        "DE": "Logisches Fahrzeug",
        "IT": "Veicolo logico",
        "PT_BR": "Veículo lógico",
    },
    "1 - 10 de 17": {
        "EN": "1 - 10 of 17",
        "FR": "1 - 10 sur 17",
        "DE": "1 - 10 von 17",
        "IT": "1 - 10 di 17",
        "PT_BR": "1 - 10 de 17",
    },
    "Final de Recarga": {
        "EN": "Recharge End",
        "FR": "Fin de recharge",
        "DE": "Ladeende",
        "IT": "Fine ricarica",
        "PT_BR": "Final de recarga",
    },
    "Resultados: 17": {
        "EN": "Results: 17",
        "FR": "Résultats : 17",
        "DE": "Ergebnisse: 17",
        "IT": "Risultati: 17",
        "PT_BR": "Resultados: 17",
    },
}


def get_translation(es_val, lang):
    """Devuelve la traducción para es_val al idioma lang.
    Si no hay entrada o el lang no está en el dict, devuelve el valor ES original."""
    entry = TRANSLATIONS.get(es_val)
    if entry is None:
        return es_val  # no en la tabla → pasar tal cual
    return entry.get(lang, es_val)


def fill_tsv(tsv_in, lang):
    with open(tsv_in, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = list(reader)
    for row in rows:
        if not row.get(lang):
            row[lang] = get_translation(row["ES"], lang)
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=["key", "ES", lang], delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    with open(tsv_in, "w", encoding="utf-8") as f:
        f.write(buf.getvalue())
    print(f"  Filled {tsv_in} ({lang})")


LANG_TSV = {
    "EN":    "pending_EN_E1_E2_R1.tsv",
    "FR":    "pending_FR_E1_E2_R1.tsv",
    "DE":    "pending_DE_E1_E2_R1.tsv",
    "IT":    "pending_IT_E1_E2_R1.tsv",
    "PT_BR": "pending_PTBR_E1_E2_R1.tsv",
}

for lang, tsv in LANG_TSV.items():
    path = os.path.join(BASE, tsv)
    if not os.path.exists(path):
        print(f"  SKIP {tsv} (not found)")
        continue
    fill_tsv(path, lang)

print("\nAll TSV files filled. Now importing...")

for lang, tsv in LANG_TSV.items():
    path = os.path.join(BASE, tsv)
    if not os.path.exists(path):
        continue
    print(f"\n-- Import {lang} --")
    result = subprocess.run(
        [sys.executable, "scripts/core/goalbus_localize.py", "translate",
         "--import", tsv, "--to", lang],
        cwd=BASE, capture_output=True, text=True
    )
    print(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)
    if result.returncode != 0:
        print("STDERR:", result.stderr[-500:])

print("\nDone.")
