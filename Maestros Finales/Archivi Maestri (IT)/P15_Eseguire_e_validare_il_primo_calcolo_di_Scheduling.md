---
title: Eseguire e validare il primo calcolo di Scheduling
shortTitle: Calcolare e validare
intro: 'Scopri come eseguire il primo calcolo di Scheduling, rivedere il lifecycle dello scenario, validare la soluzione preparata e lasciare lo scenario pronto per la pubblicazione o per un audit successivo.'
contentType: how-tos
versions:
  - '*'
---

## Eseguire il calcolo dello scenario

Ora che lo scenario è creato e configurato con l’offerta validata, le matrici corrette e i vehicle/shift rules models, il passo successivo è eseguire il calcolo.

In questa fase, il motore prende:
1. l’offerta validata,
2. le regole attive,
3. la logistica dei deadhead trips,
4. e la struttura dello scenario,

per costruire logical duties schedulabili.

Usa questo quick start quando il tuo scenario di Scheduling è pronto e devi ottenere la prima soluzione calcolata prima di rivederla e validarla.

Prima di iniziare, assicurati che:
1. Tu abbia già creato lo scenario in P14.
2. Tu abbia selezionato il servizio validato corretto.
3. Tu abbia assegnato la deadhead-trip matrix appropriata.
4. Tu abbia selezionato il vehicle rules model corretto.
5. Tu abbia selezionato lo shift rules model corretto.
6. Tu abbia configurato il motore Classic e i parametri di calcolo.

Per questo quick start, usa questo caso di riferimento:

> **Eseguirò il primo calcolo dello scenario di Scheduling per la linea L1, rivedrò se la soluzione è coerente e lascerò lo scenario pronto per la validazione.**

Per eseguire il calcolo dello scenario:
1. Apri lo scenario che vuoi calcolare.
2. Rivedi un’ultima volta che gli input dello scenario siano corretti.
3. Esegui **Calculate** / **Start calculation**.
ref: P15_Imagen1.png | compact
ref: P15_Imagen2.png | compact
4. Conferma che lo status dello scenario cambi da **Solution pending** a **Solution calculation**.
ref: P15_Imagen3.png | full
ref: P15_Imagen4.png | full
5. Attendi che il motore finisca.
ref: P15_Imagen5.png | full
6. Rivedi il nuovo status dello scenario.
7. Se il calcolo termina correttamente, conferma che lo scenario passi a **Solution prepared**.
ref: P15_Imagen6.png | compact
8. Se la soluzione richiede aggiustamenti manuali, entra in **Edit** per il refinement.
9. Se il motore non restituisce una soluzione valida, rivedi di nuovo:
   1. l’offerta,
   2. la deadhead-trip matrix,
   3. le regole,
   4. e i parametri dello scenario.

Per il caso di riferimento, conferma che:
1. Lo scenario L1 esca dallo status iniziale.
2. Il motore completi senza bloccarsi.
3. Lo scenario arrivi a una soluzione preparata o a una fase di edit ragionevole.

Inoltre, se il tipo di scenario scelto include vehicles e duties, puoi vedere la duty solution generata dalla vista staff.
ref: P15_Imagen12.png | compact

Quando termini questa sezione, dovresti avere una prima soluzione calcolata o un segnale chiaro su quale parte della parametrizzazione deve essere corretta.

## Rivedere lo status dello scenario e i risultati del calcolo

Dopo aver eseguito il calcolo, devi capire dove lo scenario è atterrato nel lifecycle. Ogni status ha un significato operativo diverso e ti dice cosa puoi fare dopo.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già eseguito il calcolo.
2. Tu conosca il nome dello scenario che stai rivedendo.
3. Tu sappia se ti aspettavi una soluzione pronta o una fase di refinement.

Per rivedere status e risultati:
1. Torna alla tabella principale degli scenari o resta dentro lo scenario.
2. Rivedi lo status corrente.
3. Interpreta lo status con questa logica:
   1. **Solution pending**: lo scenario non è ancora stato calcolato.
   2. **Solution calculation**: il motore sta processando la soluzione.
   3. **Edit**: un utente sta aggiustando manualmente la soluzione.
   4. **Solution prepared**: calcolo/editing è finito e lo scenario è pronto per la review.
   5. **Validated**: la soluzione è stata approvata e bloccata.
   6. **Publishing**: la soluzione sta venendo inserita nel calendario operativo.
   7. **Published**: la soluzione è già deployata alle operations.
4. Se lo scenario è in **Solution prepared**, continua con la review di coerenza.
5. Se lo scenario è in **Edit**, completa prima gli aggiustamenti manuali necessari.
6. Se lo scenario resta in **Solution calculation** troppo a lungo, verifica se c’è un problema tecnico o una configurazione troppo restrittiva.

Per il caso di riferimento, dovresti aspettarti che lo scenario finisca almeno in:
1. **Solution prepared**, se non devi più aggiustare la struttura, oppure
2. **Edit**, se vuoi ancora rifinire manualmente.

Quando termini questa sezione, dovresti capire chiaramente cosa significa lo status corrente e quale azione dovrebbe seguire.

## Rivedere KPI, errori e coerenza prima di validare

Prima di validare lo scenario, devi rivederlo. La validazione non è solo un clic amministrativo. È il gate formale di approvazione che congela la soluzione e previene modifiche accidentali in seguito.

Prima di iniziare questa sezione, assicurati che:
1. Lo scenario sia in **Solution prepared**, oppure tu abbia terminato **Edit**.
2. Tu capisca che lo scenario smetterà di essere modificabile dopo la validazione.
3. Tu sia pronto per una review finale prima dell’approvazione.

Per rivedere la soluzione prima di validare:
1. Apri lo scenario nel suo status corrente.
2. Rivedi i KPI disponibili.
ref: P15_Imagen7.png | full
3. Controlla errori, warning o incoerenze visibili.
ref: P15_Imagen8.png | compact
4. Usa i filtri disponibili per ispezionare la soluzione da angolazioni diverse.
ref: P15_Imagen9.png | compact
5. Conferma che assegnazioni e struttura abbiano senso operativo.
6. Se trovi un problema minore e lo scenario è ancora modificabile, correggilo prima di continuare.
7. Se trovi un problema maggiore dopo che la soluzione è bloccata, dovrai sbloccare con i permessi appropriati o tornare a uno scenario modificabile.

Per il caso di riferimento, assicurati che:
1. I KPI della soluzione L1 siano ragionevoli.
2. Non ci siano errori importanti che invalidano la soluzione.
3. La soluzione possa passare dalla review tecnica all’approvazione formale.

Quando termini questa sezione, dovresti avere sufficiente confidenza per validare lo scenario.

## Validare lo scenario e bloccare la soluzione

Ora puoi eseguire la **scenario validation**. Questo passo chiude ufficialmente calcolo ed editing. Da qui la soluzione diventa protetta, lo scenario diventa non modificabile e non può essere ricalcolato finché resta validato.

Prima di iniziare questa sezione, assicurati che:
1. Lo scenario sia in **Solution prepared**.
2. Tu abbia terminato la review di KPI ed errori.
3. Tu non abbia bisogno di ulteriori aggiustamenti manuali prima dell’approvazione.

Per validare lo scenario:
1. Dalla tabella degli scenari, apri il menu azioni dello scenario.
2. Seleziona **Validate**.
3. Se preferisci farlo dentro lo scenario, usa il pulsante **Validate** in alto nella schermata.
ref: P15_Imagen10.png | compact
4. Conferma la validazione quando richiesto.
5. Conferma che lo status della solution cambi in **Validated**.
ref: P15_Imagen11.png | compact
6. Verifica che:
   1. lo scenario non sia più modificabile,
   2. non possa più essere ricalcolato,
   3. i dati chiave siano protetti.
7. Se scopri un problema dell’ultimo minuto dopo la validazione, usa il flow di sblocco solo con i permessi appropriati.

Per il caso di riferimento, non procedere finché puoi affermare:
1. La solution di L1 è stata revisionata.
2. Lo status della solution dello scenario è cambiato in **Validated**.
3. L’organizzazione può trattare lo scenario come una versione approvata.

Quando termini questa sezione, dovresti avere una solution formalmente approvata e bloccata per prevenire modifiche accidentali.

## Lasciare lo scenario pronto per la pubblicazione o un audit successivo

Una volta validato, lo scenario è pronto per due percorsi:
1. **publication**, se vuoi deployarlo nel calendario operativo,
2. oppure **audit**, se devi ancora rivederlo prima di pubblicare.

A questo punto lo scenario è una solution approvata e protetta. Puoi ancora consultarlo, rivedere KPI, filtrare e usarlo come riferimento, ma non dovrebbe più essere trattato come una bozza di lavoro.

Prima di concludere, assicurati che:
1. La solution dello scenario sia in stato **Validated**.
2. Tu conosca la differenza tra validare e pubblicare.
3. Tu sappia se il tuo prossimo passo è deployare o fare audit.

Per lasciare lo scenario pronto per il prossimo passo:
1. Rivedi la tabella degli scenari e conferma lo status **Validated**.
2. Se il piano è approvato per il deployment, prepara il flow **Publish**.
3. Se ti serve ancora review interna, mantieni lo scenario validato come baseline di audit.
4. Usa filtri, icone info e review degli status per controllare quali scenari sono pending, validated o già published.
5. Se devi iterare, considera di duplicare lo scenario invece di alterarne uno già approvato.

Per il caso di riferimento, termina questo quick start solo quando puoi affermare:
1. Lo scenario L1 è stato calcolato.
2. La solution è stata revisionata.
3. La solution dello scenario è in stato **Validated**.
4. Il prossimo passo non è più il calcolo, ma decidere se pubblicare o fare audit.

Quando termini questa sezione, dovresti avere uno scenario calcolato, revisionato e validato pronto per produzione o review finale.

## Additional reading

- [Pubblicare lo scenario per date specifiche](P16_Pubblicare_lo_scenario_per_date_specifiche.md)

