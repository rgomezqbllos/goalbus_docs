---
title: Analizzare e confrontare scenari di Scheduling
shortTitle: Confrontare scenari
intro: 'Scopri come confrontare scenari di Scheduling, rivedere KPI e differenze operative e decidere con criteri chiari quale soluzione deve restare il riferimento o avanzare come nuova iterazione.'
contentType: how-tos
versions:
  - '*'
---

## Identificare quali scenari confronterai

Dopo aver creato, calcolato, validato e pubblicato scenari, il passo naturale successivo è confrontarli. Confrontare scenari non è solo un esercizio intuitivo di “quale sembra migliore”. Significa rivedere cosa è cambiato, quale impatto ha avuto quel cambiamento e se la nuova iterazione migliora davvero la soluzione di riferimento.

Usa questo quick start quando hai almeno due scenari comparabili (ad esempio una soluzione published e una nuova iterazione calcolata) e devi decidere quale deve restare il riferimento operativo o quale deve avanzare nel lifecycle.

Prima di iniziare, assicurati che:
1. Tu abbia già creato e calcolato almeno uno scenario base.
2. Tu abbia una seconda versione/iterazione/variante che vuoi confrontare.
3. Tu sappia quale linea, tipo di giorno e contesto operativo stai rivedendo.
4. Tu sappia quale versione è il riferimento corrente.

Per questo quick start, usa questo caso di riferimento:

> **Confronterò lo scenario published per la linea L1 con una nuova iterazione calcolata per decidere se la nuova soluzione migliora davvero lo scheduling corrente.**

Per identificare correttamente gli scenari da confrontare:
1. In GoalBus, apri il modulo **Planning scenarios**.
ref: P18_Imagen1.png | compact
2. Individua lo scenario che funge da riferimento corrente.
3. Individua il nuovo scenario/iterazione che vuoi valutare.
4. Conferma che entrambi gli scenari appartengano allo stesso contesto funzionale:
   1. stessa linea (o insieme comparabile di linee),
   2. stesso tipo di giorno,
   3. stessa logica operativa generale.
5. Rivedi name, description e status di ciascuno scenario.
6. Conferma quale è:
   1. il riferimento attivo/published,
   2. e quale è la nuova proposta.
7. Se gli scenari non sono comparabili, non procedere finché non lo correggi.

Per il caso di riferimento, assicurati che:
1. Entrambi gli scenari appartengano alla linea L1.
2. Entrambi siano feriali (o nello stesso contesto temporale).
3. Uno sia il riferimento e l’altro l’alternativa.

Quando termini questa sezione, dovresti aver identificato chiaramente quali scenari confronterai e il ruolo di ciascuno.

## Rivedere KPI, volume di lavoro e bilanciamento complessivo

Una volta selezionati gli scenari, inizia con un confronto ad alto livello. L’obiettivo è rivedere indicatori generali prima di scendere nel dettaglio di duties o regole. Questo aiuta a capire se la nuova soluzione è davvero meglio bilanciata o solo diversa.

Prima di iniziare questa sezione, assicurati che:
1. Tu sappia quali due scenari stai confrontando.
2. Tu abbia identificato quale è il riferimento.
3. Tu abbia accesso a KPI visibili o metriche comparabili.

Per rivedere KPI ad alto livello:
1. Apri il primo scenario e rivedi i KPI chiave.
2. Annota almeno:
   1. volume totale di lavoro,
   2. numero di duties,
   3. tempo totale,
   4. distanza totale (o altra grandezza rilevante),
   5. qualsiasi altro indicatore visibile.
3. Apri il secondo scenario e rivedi gli stessi KPI.
4. Confronta se la nuova iterazione:
   1. riduce complessità inutile,
   2. migliora il bilanciamento,
   3. oppure sposta semplicemente il problema altrove.
5. Evita di accettare un’iterazione solo perché i numeri cambiano: il cambiamento deve avere senso operativo.

Per il caso di riferimento, chiediti:
1. La nuova iterazione riduce duties non necessarie?
2. Il bilanciamento complessivo sembra più ragionevole?
3. Il volume totale resta coerente con l’offerta validata?
4. Il miglioramento è reale o solo redistribuzione senza beneficio chiaro?

Quando termini questa sezione, dovresti avere un senso globale se la nuova soluzione merita una review più profonda.

## Confrontare l’impatto su vehicles vs. duties

Dopo aver riveduto i KPI globali, confronta la logica funzionale separando:
1. impatto su **vehicles**,
2. e impatto su **duties/shifts**.

Questo è importante perché un’iterazione può migliorare la logica flotta e peggiorare la logica duties, o viceversa. Mescolare entrambi rende l’interpretazione confusa.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già rivisto i KPI globali.
2. Tu sappia quali vehicle/shift rules sono coinvolte nel cambiamento.
3. Tu conosca l’obiettivo dell’iterazione.

Per confrontare l’impatto veicolo:
1. Rivedi come si comporta la soluzione rispetto a:
   1. flotta usata,
   2. compatibilità,
   3. partenze da depots/parkings,
   4. chilometri non produttivi, se visibili o deducibili.
2. Verifica se l’iterazione migliora la coerenza tra linea, flotta e infrastruttura.
3. Individua se il nuovo scenario forza soluzioni meno realistiche di prima.

Per confrontare l’impatto duties:
1. Rivedi come vengono costruite le duties/strutture di lavoro.
2. Conferma che gli shift types attivi abbiano ancora senso.
3. Osserva se la nuova soluzione:
   1. migliora la chiarezza del lavoro,
   2. peggiora la struttura,
   3. oppure introduce rigidità non necessaria.
4. Ricollega il cambiamento allo shift rules model usato.

Per il caso di riferimento, chiediti:
1. La nuova iterazione migliora la logica veicolo senza danneggiare la logica duties?
2. Migliora la logica duties senza danneggiare la flotta?
3. Quale dimensione migliora o peggiora?
4. Il risultato complessivo è più robusto o solo più diverso?

Quando termini questa sezione, dovresti capire dove ogni scenario migliora e dove peggiora.

## Decidere se la nuova iterazione porta valore reale

Ora trasforma il confronto in una decisione. Non ogni nuovo scenario merita di avanzare. A volte un’iterazione è solo apprendimento interno e la decisione migliore è mantenere la versione attiva. Altre volte il miglioramento è sufficientemente chiaro da giustificare un nuovo ciclo di validazione/pubblicazione.

Prima di continuare, assicurati che:
1. Tu abbia confrontato KPI ad alto livello.
2. Tu abbia rivisto l’impatto vehicles vs duties.
3. Tu conosca l’obiettivo originale dell’iterazione.

Per decidere se l’iterazione porta valore reale:
1. Riassumi lo scopo del nuovo scenario.
2. Verifica se quell’obiettivo è stato raggiunto chiaramente.
3. Chiediti se il miglioramento è:
   1. visibile operativamente,
   2. difendibile tecnicamente,
   3. abbastanza stabile da avanzare.
4. Se l’iterazione migliora chiaramente il riferimento, preparala per validazione o pubblicazione come appropriato.
5. Se non migliora il riferimento, mantienila come learning e conserva la versione corrente.
6. Non promuovere un’iterazione solo perché è più nuova: promuovila solo se è migliore per il caso.

Per il caso di riferimento, termina questa sezione solo quando puoi affermare una di queste:
1. La nuova iterazione L1 migliora chiaramente la soluzione published e dovrebbe avanzare.
2. La soluzione published resta il miglior riferimento e la nuova iterazione resta solo analisi.

Quando termini questa sezione, dovresti avere una decisione chiara e difendibile su quale scenario resta il riferimento.

## Lasciare tracciabilità per iterazioni future

L’ultimo passo è lasciare traccia del confronto. Confrontare scenari senza tracciabilità costringe a rifare analisi in seguito e rende più difficile spiegare perché una versione è stata promossa o scartata.

Prima di concludere, assicurati che:
1. Tu abbia già preso una decisione.
2. Tu sappia quale scenario resta il riferimento.
3. Tu conosca il motivo principale della decisione.

Per lasciare tracciabilità:
1. Rivedi name e description di entrambi gli scenari.
2. Se necessario, aggiorna la description del nuovo scenario per riflettere meglio scopo o outcome.
3. Mantieni la versione di riferimento chiaramente identificata come:
   1. published,
   2. validated,
   3. o mantenuta come baseline ufficiale.
4. Mantieni l’iterazione non promossa come riferimento comparativo se ha valore storico.
5. Se il processo interno lo richiede, registra cosa è cambiato e perché è stata presa la decisione finale.

Per il caso di riferimento, assicurati che:
1. Tu possa spiegare perché il nuovo scenario migliora o non migliora l’L1 attivo.
2. La decisione sia riflessa in names/descriptions o nel processo interno.
3. Una futura iterazione non parta dalla confusione.

Quando termini questa sezione, dovresti avere non solo un confronto, ma una decisione tracciabile utile per iterazioni future.

## Additional reading

- [Passare da Scheduling a Rostering](P19_Passare_da_Scheduling_a_Rostering.md)

