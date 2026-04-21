---
title: Validare la struttura operativa e lo stato del servizio
shortTitle: Struttura operativa
intro: 'Scopri come rivedere depots, operating units e operational groups e validare il servizio creato in modo che sia davvero idoneo per Scheduling prima di passare a regole e calcolo.'
contentType: how-tos
versions:
  - '*'
---

## Rivedere la struttura operativa che supporta il tuo servizio

Prima di passare a regole e scenario di Scheduling, devi confermare che la tua offerta non solo esista, ma sia supportata da una struttura operativa coerente. In questa fase dovresti verificare se linea, depot, operating unit ed eventuali gruppi collegati appartengono allo stesso contesto di business e operativo.

Usa questo quick start quando hai già creato l’offerta di servizio base e devi confermare che l’ambiente organizzativo che la supporta sia corretto prima di calcolare.

Prima di iniziare, assicurati che:
1. Tu abbia già creato l’offerta di servizio in P10.
2. Tu abbia già configurato parkings e depots in P5.
3. Tu abbia già definito flotta e vincoli base a livello di linea in P4.
4. Tu sappia quale linea e quale servizio userai come riferimento.

Per questo quick start, usa questo caso di riferimento:

> **Validerò che la linea L1, North Depot, la operating unit associata e i gruppi collegati formino una base coerente prima di portare il servizio in Scheduling.**

Per rivedere la struttura operativa per il tuo caso:
1. Apri la configurazione o la vista operativa legata al servizio che hai appena creato.
2. Identifica quale **depot** supporta il servizio.
3. Conferma che quel depot corrisponda alla base fisica definita in precedenza.
4. Rivedi a quale **operating unit** appartiene la linea o il servizio.
5. Conferma che quell’unità sia coerente con infrastruttura, geografia e organizzazione del caso.
6. Rivedi eventuali **groups** che impattano quel contesto, se esistono.
7. Conferma che linea, unità e depot non appartengano a strutture incompatibili.
8. Se trovi un’incoerenza, correggila prima di procedere.

Per il caso di riferimento, verifica:
1. La linea L1 è associata a North Depot.
2. Quel depot appartiene alla operating unit corretta.
3. I gruppi collegati non puntano a un altro perimetro operativo.

Quando termini questa sezione, dovresti essere sicuro che l’offerta di servizio viva dentro una struttura operativa coerente.

## Confermare che il servizio sia validato e pronto per scheduling

Dopo aver rivisto la struttura operativa, devi confermare un punto critico: il servizio creato in P10 è già in stato **Validated**. Non basta aver creato trips, headways e routes. Perché Scheduling legga il servizio e lo consideri idoneo, il servizio deve essere stato validato.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già rivisto il commercial service e i suoi trips in P10.
2. Tu abbia già controllato headways, routes e durate.
3. Tu non abbia più bisogno di continuare a modificare il servizio in questa fase.

Per confermare che il servizio sia pronto per scheduling:
1. Apri il commercial service che userai come riferimento.
2. Rivedi il suo **status** attuale.
3. Se lo status è già **Validated**, conferma che non ci sia nulla in sospeso prima di continuare.
4. Se il servizio è ancora in editing o in uno stato precedente, esegui **Validate**.
5. Conferma che lo status cambi correttamente.
6. Verifica che:
   1. il servizio non sia più una bozza,
   2. i trips siano protetti da modifiche accidentali,
   3. il servizio possa ora essere consumato da Scheduling.
7. Se rilevi un problema strutturale, correggilo prima di validare di nuovo.

Per il caso di riferimento, non procedere finché puoi affermare:
1. La linea L1 ha già l’offerta feriale revisionata.
2. Il servizio è ora in stato **Validated**.
3. Il sistema può usarlo come input per lo scheduling.

Quando termini questa sezione, dovresti avere un servizio davvero pronto per essere letto dal motore.

## Verificare coerenza tra struttura, servizio e idoneità

Ora fai un’ultima revisione combinata. L’obiettivo non è solo avere un servizio validato, ma confermare che il servizio validato viva nella struttura corretta e non porti incoerenze organizzative che complicheranno il calcolo.

Prima di continuare, assicurati che:
1. Tu abbia già rivisto depot, operating unit e groups.
2. Tu abbia già validato il servizio (o confermato che sia validato).
3. Tu sappia quale caso porterai al passo successivo.

Per validare l’idoneità end-to-end prima di Scheduling:
1. Rivedi il servizio validato e conferma quale linea usa.
2. Conferma che quella linea sia ancora collegata al depot corretto.
3. Conferma che operating unit e groups non contraddicano il contesto del servizio.
4. Chiediti se il sistema potrebbe prendere quel servizio come input valido e coerente per il calcolo.
5. Se la risposta è sì, continua con il prossimo quick start.
6. Se la risposta è no, correggi la struttura o riporta il servizio in editing solo se devi ricostruire parte della base prima di validare di nuovo.

Per il caso di riferimento, assicurati che:
1. L1 appartenga al contesto organizzativo corretto.
2. North Depot supporti davvero il servizio.
3. Il servizio feriale validato non abbia contraddizioni con la sua struttura.

Quando termini questa sezione, dovresti poter affermare che l’offerta non è solo creata, ma anche allineata strutturalmente e idonea per Scheduling.

## Additional reading

- [Definire le regole vehicolo per Scheduling](P12_Definire_le_regole_vehicolo_per_Scheduling.md)

