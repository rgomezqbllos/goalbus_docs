---
title: Validare l’anno operativo prima di pianificare
shortTitle: Anno operativo
intro: 'Scopri come validare l’anno operativo che supporterà il tuo caso di planning per evitare lacune, sovrapposizioni o interruzioni artificiali nei dati prima di passare a rete, infrastruttura e servizi.'
contentType: how-tos
versions:
  - '*'
---

## Creare o validare l’anno operativo che userà la tua pianificazione

Prima di continuare con rete, tempi, servizi o regole, devi verificare che il periodo che vuoi pianificare rientri nell’**anno operativo corretto**. In GoalBus, l’anno operativo serve ad adattare la logica temporale del sistema alla realtà di business. Questo è importante perché molte operazioni non seguono l’anno solare da gennaio a dicembre. Ad esempio, un servizio scolastico può andare da settembre ad agosto, e un contratto fiscale o sindacale può richiedere un intervallo diverso.

Usa questo quick start quando hai già definito i tipi di giorno e la logica delle festività, quando vuoi preparare il tuo primo vero caso di planning, oppure quando devi confermare che il periodo che userai sia supportato da una timeline valida.

Prima di iniziare, assicurati che:
1. Tu abbia già rivisto il ruolo del planner in P1.
2. Tu abbia già configurato o validato tipi di giorno e festività in P2.
3. Tu sappia esattamente quale periodo vuoi pianificare.
4. Tu abbia accesso all’ambiente con permessi per visualizzare o modificare la configurazione temporale.

Per questo quick start, usa questo caso di riferimento:

> **Pianificherò gennaio 2026 e devo confermare che quel periodo rientri nell’anno operativo corretto prima di continuare con il mio primo lavoro di planning.**

Per creare o validare l’anno operativo per il tuo caso:
1. In GoalBus, vai su **Configuration**.
2. Apri **Time Management** > **Operational years**.
ref: P3_Imagen1.png | compact
3. Rivedi gli anni operativi esistenti e identifica quale dovrebbe coprire il periodo che vuoi pianificare.
4. Se non esiste un anno operativo adatto, fai clic sull’opzione per crearne uno nuovo selezionando **Create Operational Year**.
ref: P3_Imagen2.png | full
5. Definisci un **Unique Name** e, se necessario, una **Description**.
6. Regola **Start date** e **End date** per riflettere la realtà operativa o fiscale del tuo caso.
7. Associa le **Business Units** se applicabile.
8. Salva l’anno operativo.
ref: P3_Imagen3.png | compact
9. Conferma che il periodo che vuoi pianificare sia completamente coperto da quell’anno.
10. Se l’anno esisteva già, verifica comunque che sia ancora quello giusto per il tuo caso e che le sue date non siano ambigue.

Quando termini questa sezione, dovresti aver identificato o creato l’anno operativo che supporta davvero il tuo caso di planning.

## Rivedere la continuità temporale ed evitare lacune o sovrapposizioni

Dopo aver identificato l’anno operativo corretto, devi verificare che la sua sequenza temporale sia coerente. In GoalBus, la continuità tra anni operativi non è opzionale. Il sistema è progettato per prevenire **lacune** o **sovrapposizioni** tra anni, perché questi errori finirebbero per impattare metriche accumulate, KPI annuali e calcoli a valle.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già trovato l’anno operativo che dovrebbe coprire il tuo caso.
2. Tu conosca la sua data di inizio e di fine.
3. Tu sappia se esistono anni precedenti o successivi che appartengono alla stessa sequenza.

Per rivedere la continuità temporale dell’anno operativo:
1. Apri i dettagli dell’anno operativo che userai come riferimento.
2. Rivedi **Start date** e **End date**.
3. Verifica che il periodo che vuoi pianificare rientri in quell’intervallo senza ambiguità.
4. Rivedi l’anno operativo precedente o successivo, se esiste, per assicurarti che non ci siano:
   1. lacune tra anni, oppure
   2. sovrapposizioni tra due intervalli temporali.
5. Se devi creare un nuovo anno alla fine della sequenza, aggiungilo solo alla fine e verifica che continui esattamente dove termina il precedente.
6. Se rilevi un’incoerenza, correggi le date prima di continuare.
7. Conferma che il sistema ti permetta di salvare la sequenza senza blocchi dovuti a errori di continuità.

Per il caso di riferimento, chiediti:
1. Gennaio 2026 è interamente dentro un anno operativo valido?
2. Quell’anno si collega correttamente al precedente e al successivo?
3. Il sistema potrebbe accumulare dati senza interrompere la continuità nel periodo?

Quando termini questa sezione, dovresti essere sicuro che non ci siano lacune o sovrapposizioni che impattano il tuo caso.

## Verificare la relazione tra anno operativo e logica di calendario

Ora che hai validato l’anno operativo e la sua continuità, devi collegarlo a ciò che hai definito in P2. Serve a poco avere tipi di giorno e festività configurati correttamente se il periodo temporale in cui vivono quei dati non è costruito correttamente.

Prima di continuare, assicurati che:
1. L’anno operativo corretto sia già identificato.
2. I tipi di giorno e le festività per il caso siano già configurati.
3. Il periodo che pianificherai sia ancora chiaro e delimitato.

Per verificare che l’anno operativo sia pronto a supportare il planning:
1. Rivedi il caso di planning che hai definito all’inizio di questo articolo.
2. Conferma che quel periodo ricada nell’anno operativo corretto.
3. Conferma che la logica di calendario definita in P2 si applichi anche nello stesso intervallo temporale.
4. Chiediti se il sistema potrebbe già usare, allo stesso tempo:
   1. la corretta categoria di tipo di giorno,
   2. le corrette festività, e
   3. il corretto anno operativo.
5. Se la risposta è sì, continua con il prossimo quick start.
6. Se la risposta è no, correggi l’anno operativo o rivedi la coerenza con il calendario prima di procedere.

Quando termini questa sezione, dovresti poter affermare che il tuo caso ha una base temporale completa: il calendario corretto e l’anno operativo corretto.

## Additional reading

- [Definire i tipi di veicolo e la flotta consentita per linea](P4_Definire_i_tipi_di_veicolo_e_la_flotta_consentita_per_linea.md)

