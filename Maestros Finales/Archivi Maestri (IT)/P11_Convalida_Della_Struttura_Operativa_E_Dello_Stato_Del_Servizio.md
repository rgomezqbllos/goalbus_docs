---
title: Convalida della struttura operativa e dello stato del servizio
shortTitle: Struttura operativa
intro: Scopri come rivedere i depositi, le unità e i gruppi operativi e convalida
  il servizio creato per renderlo realmente idoneo per la programmazione prima di
  passare alle regole e al calcolo.
contentType: how-tos
versions:
- '*'
---
## Revisione della struttura operativa che supporta il vostro servizio

Prima di passare alle regole e allo scenario di programmazione, è necessario verificare che la vostra offerta non solo esiste, ma è supportata da una struttura operativa coerente. In questa fase è necessario verificare se la linea, deposito, unità operativa e gruppi correlati appartengono allo stesso contesto aziendale e operativo.

Usa questo avvio rapido quando hai già creato l'offerta di servizio base e hai bisogno di confermare che l'ambiente organizzativo che lo supporta è corretto prima di calcolare.

Prima di iniziare, assicurati che:
1. Hai già creato l'offerta di servizio a P10.
2. Hai già installato parcheggi e magazzini a P6.
3. Avete già definito le restrizioni della flotta e della linea di base a P8.
4. Sei chiaro che linea e servizio userai come riferimento.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Ho intenzione di convalidare che la linea L1, il North Depot, l'unità operativa associata e i relativi gruppi formano una base coerente prima di portare il servizio a Scheduling.**

Per rivedere la struttura operativa del vostro caso:
1. Apre la configurazione o la vista operativa relativa al servizio appena creato.
2. Identificare quale **deposito** supporta il servizio.
3. Controlla che il deposito corrisponda alla base fisica che hai definito prima.
4. Controllare a quale **unità operativa** appartiene la linea o il servizio.
5. Controllare se quell'unità si adatta all'infrastruttura, alla geografia e all'organizzazione del caso.
6. Controllare il relativo **gruppi** che influisce su quel contesto, se esistono.
7. Conferma che la linea, l'unità e il deposito non appartengono a strutture incompatibili.
8. Se rilevate un'incoerenza, correggetela prima di continuare.

Per il caso di riferimento, controllare:
1. Questa linea L1 è associata al North Depot.
2. Quel deposito appartiene all'unità giusta.
3. I gruppi collegati non indicano un'altra area operativa.

Quando si termina questa sezione, si dovrebbe essere chiari che l'offerta di servizio vive all'interno di una struttura operativa coerente.

## Conferma che il servizio è già convalidato e pronto per la programmazione

Dopo aver riesaminato la struttura operativa, è necessario confermare qualcosa di critico: che il servizio creato in P10 è già in stato **Convalida**. Non basta avere creato viaggi, intervalli e percorsi. Per poter leggere il servizio e considerarlo idoneo, il servizio deve essere passato attraverso l'azione di convalida.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già controllato il servizio commerciale e i loro viaggi P10.
2. Hai già controllato gli intervalli, le rotte e le durate.
3. Non c'è più bisogno di modificare il servizio in questa fase.

Per confermare che il servizio è pronto per la programmazione:
1. Aprire il servizio commerciale che userete come riferimento.
2. Controlla il tuo **stato** attuale.
3. Se lo stato è già **Convalida**, confermare che non c'è nulla in sospeso prima di continuare.
4. Se il servizio è ancora in fase di modifica o in uno stato precedente, eseguire l'azione **Convalida**.
5. Controllare che lo stato cambia correttamente.
6. Controlla che:
   1. il servizio non è più una bozza,
   2. il viaggio è protetto da cambiamenti accidentali,
   3. e il servizio può già essere consumato da Scheduling.
7. Se rilevate un errore di struttura, correggetelo prima di rivalidarlo.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. La linea L1 ha già la sua offerta operativa riveduta.
2. Il servizio è già cambiato in stato **Convalida**.
3. Il sistema può ora essere utilizzato come input di programmazione.

Quando si termina questa sezione, si dovrebbe avere un servizio davvero preparato per essere letto dal motore.

## Controllo della coerenza tra struttura, servizio e ammissibilità

Ora è necessario fare una revisione congiunta finale. L'obiettivo non è solo di avere un servizio convalidato, ma di confermare che il servizio convalidato vive nella corretta struttura e non trascina le incoerenze organizzative che poi complicano il calcolo.

Prima di continuare, assicurarsi che:
1. Avete già controllato magazzino, unità e gruppi.
2. Hai già convalidato il servizio o ne hai confermato la convalida.
3. Sai qual e' il prossimo caso che accetterai.

Per convalidare l'ammissibilità completa prima della programmazione:
1. Controlla il servizio convalidato e conferma quale linea usi.
2. Controllare che la linea è ancora collegata al deposito corretto.
3. Verificare che l'unità operativa e i gruppi non contraddicano il contesto del servizio.
4. Chiedetevi se il sistema potrebbe già prendere quel servizio come un input valido e coerente per il calcolo.
5. Se la risposta è sì, continuare con il prossimo inizio rapido.
6. Se la risposta è no, correggere la struttura o restituire il servizio all'editing solo se è necessario rifare parte della base prima di rivalidarlo.

Per il caso di riferimento, assicurarsi che:
1. L1 appartiene al contesto organizzativo corretto.
2. Il Deposito Nord è davvero la base per il servizio.
3. Il servizio funzionale è già convalidato e non presenta contraddizioni con la sua struttura.

Quando si conclude questa sezione, si dovrebbe essere in grado di affermare che l'offerta non solo è creata, ma anche strutturalmente allineata e ammissibile per il programma.

## Letture aggiuntive

- [Definizione delle regole sui veicoli per la programmazione](P12_Definizione_Delle_Regole_Sui_Veicoli_Per_La_Programmazione.md)
