---
title: Gestire assenze, inattività e disponibilità del personale
shortTitle: Disponibilità staff
intro: 'Scopri come registrare assenze, inattività e restrizioni di disponibilità in modo che Rostering assegni solo persone davvero idonee e non provi a coprire lavoro con autisti non disponibili.'
contentType: how-tos
versions:
  - '*'
---

## Capire la differenza tra assenza, inattività e disponibilità

Prima di calcolare Rostering, devi controllare chi è davvero disponibile a lavorare. A questo livello non basta che l’autista esista, sia assegnato al contesto corretto e abbia regole applicabili. Devi anche dire al sistema se quella persona:
1. è disponibile,
2. è assente,
3. è inattiva,
4. oppure ha disponibilità parziale/restritta.

Usa questo quick start quando gli autisti sono caricati, l’assegnazione operativa è stata rivista e le Rostering rules sono pronte e devi evitare che il calcolo assegni lavoro a persone non idonee.

Prima di iniziare, assicurati che:
1. Tu abbia caricato e rivisto gli autisti in P20.
2. Tu abbia validato la loro assegnazione operativa in P21.
3. Tu abbia definito la baseline di Rostering rules in P22.
4. Tu sappia quale popolazione staff parteciperà al calcolo.
5. Tu sappia se devi registrare ferie, malattia, permessi, indisponibilità parziale o stati non operativi.

Per questo quick start, usa questo caso di riferimento:

> **Registrerò assenze, inattività e restrizioni di disponibilità per gli autisti che copriranno la linea L1 in modo che Rostering assegni lavoro solo a persone davvero idonee.**

Per interpretare correttamente questi concetti:
1. Usa un’**assenza** quando la persona appartiene alla popolazione ma non è disponibile in un periodo specifico.
2. Usa **inattività** quando la persona deve essere esclusa dalle operations (o dal calcolo) in modo più strutturale o per un periodo più ampio.
3. Usa una **availability restriction** quando la persona può lavorare ma non sempre o non in tutte le condizioni.
4. Non confondere questi concetti come se fossero la stessa cosa.
5. Usa questa regola di lettura:
   1. **assenza** = non può lavorare in un periodo specifico,
   2. **inattività** = non deve essere trattata come risorsa operativa in quel contesto/periodo,
   3. **disponibilità restritta** = può lavorare, ma con limiti.

Per definire tipi di assenza/inattività/indisponibilità:
1. In GoalBus, apri **Configuration** > **Staff** > **Absence configuration**.
ref: P23_Imagen1.png | compact
2. Verifica se tutti i tipi di assenza necessari esistono già.
3. Se devi creare un nuovo tipo, fai clic su **Create new absence**.
ref: P23_Imagen2.png | compact
4. Compila almeno questi campi:
   1. **Absence name**
   2. **Short name**
   3. **GoalDriver ID** (se si usano integrazioni)
   4. **Absence category** (es. Pure / Free / Work) e le relative duration rules
   5. **Eligibility to assign work** (se l’autista può essere comunque selezionato nonostante l’assenza)
   6. Se questo tipo è **Requestable by the driver**
5. Salva il nuovo tipo di assenza.
ref: P23_Imagen3.png | compact
6. Continua finché hai tutti i tipi di assenza richiesti.
7. Conferma che la tua pianificazione abbia l’intero set di tipi assenza necessario.

Quando termini questa sezione, dovresti sapere quali tipi di assenza puoi usare nel planning di Rostering e assegnare a diversi autisti.

## Registrare assenze pianificate degli autisti

Le assenze pianificate sono tra i primi elementi da caricare prima del calcolo di Rostering. Questo include ferie, permessi, malattia, licenze o qualsiasi altro periodo in cui una persona non dovrebbe ricevere lavoro.

Prima di iniziare questa sezione, assicurati che:
1. Tu sappia quali autisti avranno assenze nell’orizzonte di calcolo.
2. Tu conosca le date esatte o approssimative di quelle assenze.
3. Tu voglia rimuovere ambiguità su quali giorni la persona non può essere usata.
4. Tu abbia già creato i tipi di assenza necessari.

Per registrare le assenze:
1. In GoalBus, apri **Configuration** > **Staff** > **Driver management**.
ref: P23_Imagen4.png | compact
2. Fai clic sul pulsante della barra superiore per caricare dati assenza.
ref: P23_Imagen5.png | compact
3. Seleziona **Upload staff absences**.
ref: P23_Imagen6.png | compact
4. Carica il file assenze nel modal. Puoi rivedere il formato file tramite le istruzioni o scaricando un template di esempio.
ref: P23_Imagen7.png | full
5. Conferma l’upload.
6. Salva il record.
7. Rivedi le assenze caricate in ciascun driver profile.

Per il caso di riferimento, una logica minima potrebbe essere:
1. Driver A: ferie dal 10 al 20
2. Driver B: permesso il giorno 14
3. Driver C: malattia per una settimana specifica

Quando termini questa sezione, dovresti avere registrate le principali assenze che impattano il calcolo di Rostering.

## Verificare che Rostering veda correttamente l’idoneità reale

L’ultimo passo è validare che la combinazione di autisti, assegnazione operativa, regole e disponibilità rifletta la realtà di calcolo. L’obiettivo è assicurarti che Rostering non provi ad assegnare lavoro a persone assenti/inattive o modellate male e non escluda persone che dovrebbero essere idonee.

Prima di concludere, assicurati che:
1. Tu abbia registrato le assenze rilevanti.
2. Tu abbia configurato restrizioni di disponibilità parziale se necessario.
3. Tu sappia quale popolazione userà il prossimo calcolo.

Per verificare che la disponibilità reale sia modellata correttamente:
1. Torna alla lista generale autisti.
2. Rivedi diversi profili rappresentativi della popolazione.
3. Conferma che le persone assenti abbiano i periodi correttamente registrati.
4. Conferma che restrizioni parziali non siano modellate per errore come assenze complete.
5. Chiediti se il sistema potrebbe:
   1. escludere chi non deve lavorare,
   2. includere chi può lavorare,
   3. e rispettare restrizioni parziali senza rompere il calcolo.
6. Se sì, continua con il prossimo quick start.
7. Se no, correggi i record prima di procedere.

Per il caso di riferimento, non procedere finché puoi affermare:
1. Gli autisti L1 hanno la disponibilità reale correttamente riflessa.
2. Le assenze sono caricate.
3. L’inattività è distinta.
4. Le restrizioni parziali non sono state confuse con assenze complete.

Quando termini questa sezione, dovresti avere una baseline di disponibilità abbastanza affidabile per passare a prestiti/trasferimenti e cambi di assegnazione.

## Additional reading

- [Gestire trasferimenti, prestiti e modifiche di assegnazione](P24_Gestire_trasferimenti_prestiti_e_modifiche_di_assegnazione.md)

