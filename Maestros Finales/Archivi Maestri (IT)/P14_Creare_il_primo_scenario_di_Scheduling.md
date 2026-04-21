---
title: Creare il primo scenario di Scheduling con il motore Classic
shortTitle: Scenario Classic
intro: 'Scopri come creare il tuo primo scenario di Scheduling con il motore GoalBus Classic, selezionare correttamente gli input di calcolo e distinguere quando applicare vehicle rules rispetto a shift rules.'
contentType: how-tos
versions:
  - '*'
---

## Creare lo scenario con l’offerta validata come punto di partenza

Ora che hai l’offerta validata, la logica veicolo e la logica turni, il passo successivo è creare lo **scenario di Scheduling** che userà questa base per calcolare una soluzione eseguibile.

Questo scenario è l’ambiente controllato in cui combini:
1. l’**offerta validata**,
2. la **deadhead-trip matrix**,
3. il **vehicle rules model**,
4. e lo **shift rules model**.

Usa questo quick start quando hai chiuso la parametrizzazione base e vuoi preparare lo scenario di calcolo definitivo con il motore Classic.

Prima di iniziare, assicurati che:
1. Tu abbia già configurato e validato l’offerta di servizio in P10.
2. Tu abbia già rivisto la struttura operativa in P11.
3. Tu abbia già definito vehicle rules in P12.
4. Tu abbia già definito shift types e shift rules in P13.
5. Tu abbia già preparato la deadhead-trip matrix in P8.
6. Tu sappia quale tipo di giorno e quali lines faranno parte del calcolo.

Per questo quick start, usa questo caso di riferimento:

> **Creerò il primo scenario di Scheduling per la linea L1 usando l’offerta feriale validata, la deadhead matrix corrispondente e i corretti vehicle e shift rules models, per eseguire il calcolo finale con GoalBus Classic.**

Per creare lo scenario base per il tuo caso:
1. In GoalBus, apri il modulo **Planning**.
ref: P14_Imagen1.png | compact
2. Fai clic su **New scenario**.
ref: P14_Imagen2.png | compact
3. Inserisci l’identità base dello scenario:
   1. **Name**
   2. **Day type**
   3. **Description** (opzionale)
   4. Scenario **vehicles-only** (oppure no)
ref: P14_Imagen3.png | compact
4. Seleziona gli elementi core dello scenario:
   1. il **validated commercial service** da coprire
   2. lo **Shift Rules Model**
   3. il **Vehicle Type Rules Model** (opzionale)
   4. la **deadhead-trip matrix** che corrisponde allo stesso tipo di giorno
   5. la **driver repositioning matrix** che farà parte dello scenario
ref: P14_Imagen4.png | compact
5. Seleziona la linea.
ref: P14_Imagen5.png | compact
6. Salva/termina la creazione dello scenario.
7. Conferma che lo scenario compaia nella tabella principale di planning.

Per il caso di riferimento, un’opzione valida potrebbe essere:
- **Scheduling Classic - L1 workday**

Quando termini questa sezione, dovresti avere uno scenario creato con i corretti input commerciali e logistici, simile alla seguente immagine:
ref: P14_Imagen6.png | full

## Capire quando usare vehicle rules vs. shift rules

Prima di configurare il motore, chiarisci una distinzione importante: **vehicle rules e shift rules non risolvono lo stesso problema**.

Usa le **vehicle rules** quando vuoi controllare il comportamento della flotta. Sono le regole giuste se devi modellare:
1. compatibilità fisica del veicolo,
2. limiti di capacità o autonomia,
3. restrizioni infrastrutturali,
4. policy operative legate all’uso della flotta.

Usa le **shift rules** quando vuoi controllare come viene organizzato il lavoro umano. Sono le regole giuste se devi modellare:
1. orario di lavoro,
2. pause e riposi,
3. orari di inizio e fine,
4. spread,
5. differenze tra shift types come morning, afternoon o night.

Prima di continuare, assicurati che:
1. Tu sappia quali vincoli appartengono al veicolo.
2. Tu sappia quali vincoli appartengono al turno.
3. Tu non stia cercando di risolvere un problema staff con regole flotta, o viceversa.

Per decidere quale modello usare:
1. Chiediti se il vincolo riguarda il **bus** o il **driver**.
2. Se riguarda il **bus**, usa il **vehicle rules model**.
3. Se riguarda il **lavoro umano** o lo shift type, usa lo **shift rules model**.
4. Se una regola deve applicarsi a tutti gli shift types, configurala come globale o con lo scope più ampio disponibile.
5. Se una regola si applica solo a uno shift type specifico, assegnala solo a quel tipo.

Per il caso di riferimento:
1. Se vuoi limitare quale flotta può coprire L1, usa le **vehicle rules**.
2. Se vuoi controllare come viene costruita una duty morning o night, usa le **shift rules**.
3. Se un vincolo mescola entrambi, separalo e configuralo nel modello corretto.

Quando termini questa sezione, dovresti sapere quale modello risponde a ciascuna esigenza ed evitare configurazioni incrociate o contraddittorie.

## Selezionare il motore GoalBus Classic per il calcolo finale

Ora configura il motore di calcolo. In questo quick start, il focus è lavorare con **GoalBus Classic** come motore principale dello scenario. È il motore di ottimizzazione profonda orientato a ottenere la migliore soluzione finale quando la parametrizzazione è sufficientemente matura.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già creato lo scenario.
2. Tu abbia selezionato correttamente servizio, lines e deadhead-trip matrix.
3. Tu sappia quali rules models userai.
4. Tu sia pronto per un calcolo finale (o quasi), non solo per un test tattico rapido.

Per selezionare il motore Classic:
1. Apri lo scenario che hai appena creato.
2. Nella barra superiore, fai clic su **Calculation settings**.
ref: P14_Imagen7.png | compact
3. Nel pannello laterale, seleziona **GoalBus Classic Engine**.
4. Conferma che lo scenario non sia più configurato con il motore machine-learning.
5. Imposta **Scheduling flexibility for first solution** (default è 0).
6. Usa un valore prudente che consenta la prima soluzione senza distorcere il caso.
7. Imposta il **Maximum calculation time** affinché il motore cerchi nuove soluzioni.
ref: P14_Imagen8.png | compact
8. Salva la configurazione.

La flessibilità iniziale si applica solo a GoalBus Classic e aiuta a non bloccare la prima soluzione se i vincoli sono troppo rigidi all’inizio. Il maximum calculation time agisce come garanzia di consegna e forza il sistema a restituire la migliore soluzione valida trovata entro la finestra disponibile.

Per il caso di riferimento:
1. Usa **GoalBus Classic** come motore principale.
2. Mantieni il motore machine-learning solo per pre-validazioni rapide, non per il calcolo finale.
3. Usa flessibilità iniziale moderata se sospetti che le restrizioni possano bloccare la prima soluzione.
4. Imposta un tempo massimo realistico così il team riceve una soluzione praticabile nella finestra attesa.

Quando termini questa sezione, dovresti avere il motore Classic configurato dentro un framework di calcolo controllato e realistico.

## Rivedere lo scenario prima di eseguirlo

Prima di calcolare, esegui una revisione finale dell’intero scenario. L’obiettivo è confermare che non stai entrando in calcolo con input contraddittori.

Prima di continuare, assicurati che:
1. Tu abbia selezionato il servizio validato corretto.
2. Tu abbia selezionato la deadhead-trip matrix corretta per il tipo di giorno corretto.
3. Tu abbia assegnato i corretti vehicle e shift rules models.
4. Tu abbia selezionato GoalBus Classic come motore.
5. Tu abbia impostato flessibilità e tempo massimo.

Per rivedere lo scenario prima di eseguire il calcolo:
1. Rivedi name e day type dello scenario.
2. Conferma che il **commercial service** corrisponda esattamente a ciò che vuoi schedulare.
3. Conferma che la **deadhead-trip matrix** corrisponda allo stesso contesto temporale.
4. Rivedi il **vehicle rules model** e conferma che protegga la logica flotta.
5. Rivedi lo **shift rules model** e conferma che protegga la logica del lavoro umano.
6. Conferma di non aver dimenticato un modello richiesto dal tuo caso.
7. Se tutto è coerente, lascia lo scenario pronto per il calcolo.

Per il caso di riferimento, non procedere finché puoi affermare:
1. L1 feriale usa il servizio validato corretto.
2. La matrice feriale è quella corretta.
3. Il modello veicolo limita la flotta in modo realistico.
4. Il modello turni organizza il lavoro in modo coerente.
5. GoalBus Classic è selezionato.

Quando termini questa sezione, dovresti avere uno scenario pulito e coerente, pronto per il calcolo finale.

## Additional reading

- [Eseguire e validare il primo calcolo di Scheduling](P15_Eseguire_e_validare_il_primo_calcolo_di_Scheduling.md)

