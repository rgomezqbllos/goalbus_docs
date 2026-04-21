---
title: Creare una nuova iterazione dello scenario a partire da una soluzione published
shortTitle: Nuova iterazione
intro: 'Scopri come creare una nuova iterazione di uno scenario già published per testare miglioramenti, aggiustare parametri o introdurre cambi senza alterare la versione attualmente in vigore.'
contentType: how-tos
versions:
  - '*'
---

## Partire da una soluzione published senza alterare la versione attiva

Dopo aver pubblicato una soluzione, è normale continuare a lavorarci. Potresti voler aggiustare regole, provare logiche turni diverse, incorporare cambi dell’offerta o preparare un miglioramento per un periodo futuro. In quel caso non dovresti modificare direttamente la versione published. L’approccio corretto è creare una **nuova iterazione dello scenario** per mantenere tracciabilità e proteggere la versione attualmente in vigore.

Usa questo quick start quando hai già uno scenario la cui soluzione è **Published** e devi generare una nuova variante senza perdere il riferimento storico della soluzione deployata.

Prima di iniziare, assicurati che:
1. Tu abbia già pubblicato lo scenario precedente in P16.
2. La soluzione che userai come base sia **Published**.
3. Tu sappia quale aspetto vuoi rivedere o migliorare nella prossima iterazione.
4. Tu capisca che la nuova iterazione non deve sostituire automaticamente la versione attiva finché non passa di nuovo per calcolo, validazione e pubblicazione.

Per questo quick start, usa questo caso di riferimento:

> **Creerò una nuova iterazione dello scenario published per la linea L1 per testare miglioramenti senza toccare la versione attualmente in vigore.**

Per partire in sicurezza da una soluzione published:
1. In GoalBus, apri il modulo **Planning scenarios**.
2. Individua lo scenario la cui soluzione è **Published**.
3. Rivedi name, description, day type e lines associate.
4. Conferma che sia davvero la versione che vuoi usare come riferimento.
5. Evita di modificare direttamente quella versione come se fosse una nuova bozza.
6. Decidi quale cambiamento vuoi introdurre nella nuova iterazione:
   1. regole,
   2. parametri,
   3. offerta,
   4. o aggiustamenti strutturali consentiti.

Quando termini questa sezione, dovresti aver identificato chiaramente lo scenario published che farà da base per l’iterazione.

## Creare la nuova iterazione a partire dallo scenario published

Una volta identificata la base, il passo successivo è creare una **nuova iterazione**. L’obiettivo è mantenere la versione published come riferimento storico e aprire un nuovo ramo di lavoro controllato sulla stessa logica operativa.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia identificato la solution published corretta.
2. Tu sappia perché ti serve una nuova iterazione.
3. Tu capisca che la nuova iterazione deve essere chiaramente differenziata dalla versione precedente.

Per creare la nuova iterazione:
1. Dalla tabella scenari, apri il menu azioni per lo scenario published.
2. Seleziona l’opzione per **create a new iteration** duplicando lo scenario come baseline di lavoro.
ref: P17_Imagen1.png | compact
3. Inserisci un **new name** per l’iterazione.
4. Se applicabile, aggiorna la **description** per riflettere l’obiettivo del cambiamento.
5. Salva la nuova iterazione.
ref: P17_Imagen2.png | compact
6. Conferma che il nuovo scenario compaia come entità separata rispetto a quello published.
ref: P17_Imagen3.png | full
7. Conferma che la versione published originale resti intatta e chiaramente differenziata.

Per il caso di riferimento, opzioni valide potrebbero essere:
- **Classic calculation - L1 workday - Iteration 2**
- **L1 workday - shift rules improvement**

Quando termini questa sezione, dovresti avere una nuova iterazione creata senza perdere tracciabilità della versione published.

## Definire quali cambiamenti appartengono alla nuova iterazione

Dopo aver creato l’iterazione, decidi cosa cambierai davvero. Non tutte le iterazioni hanno lo stesso obiettivo. Alcune aggiustano regole, altre migliorano l’efficienza, altre riflettono una nuova offerta o una variazione operativa futura.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia creato la nuova iterazione.
2. Tu sappia quale aspetto della soluzione precedente vuoi rivedere.
3. Tu sia disposto a limitare il cambiamento a un obiettivo chiaro per non mescolare troppe variabili.

Per definire lo scope dell’iterazione:
1. Apri il nuovo scenario.
2. Rivedi quali elementi vuoi mantenere esattamente uguali alla versione published.
3. Decidi quale elemento cambierai per primo:
   1. **vehicle rules**,
   2. **shift rules**,
   3. **engine parameters**,
   4. **service offer**,
   5. **logistics matrices**.
4. Evita di cambiare troppe cose in una volta nella prima iterazione a meno che non sia strettamente necessario.
5. Documenta l’obiettivo nel name o nella description.
6. Salva i cambi descrittivi prima di eseguire il calcolo.

Per il caso di riferimento, usa una logica come:
1. Mantieni la stessa offerta feriale per L1.
2. Aggiusta solo lo shift rules model.
3. Ricalcola per confrontare la nuova soluzione con quella published.

Quando termini questa sezione, dovresti avere una nuova iterazione con un obiettivo chiaro e delimitato.

## Ricalcolare l’iterazione e confrontare con la versione precedente

Una volta definito lo scope, ricalcola l’iterazione. Il vantaggio è che non parti da zero: parti da una soluzione nota e puoi confrontare l’impatto in modo più chiaro.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia creato la nuova iterazione.
2. Tu abbia definito l’obiettivo del cambiamento.
3. Tu abbia rivisto quali regole, parametri o input modificherai.

Per ricalcolare la nuova iterazione:
1. Rivedi lo scenario iterato e conferma che gli input siano ancora coerenti.
2. Aggiusta l’elemento che vuoi modificare.
3. Salva la configurazione.
4. Esegui il calcolo per il nuovo scenario.
5. Attendi che la fase di calcolo termini.
6. Rivedi se l’iterazione passa a **Solution prepared** o **Edit**.
7. Confronta i risultati con la versione precedente usando:
   1. KPI,
   2. struttura complessiva,
   3. logica delle duties,
   4. coerenza operativa.
8. Se il cambiamento migliora il risultato, continua con la review formale.
9. Se il cambiamento peggiora il risultato, mantieni la versione published come riferimento e decidi se correggere o scartare l’iterazione.

Per il caso di riferimento, confronta:
1. la soluzione L1 published,
2. la nuova iterazione con regole aggiustate,
3. e cosa è cambiato in qualità, fattibilità o bilanciamento.

Quando termini questa sezione, dovresti avere una nuova soluzione calcolata e una baseline chiara con cui confrontarla rispetto alla versione published.

## Decidere se la nuova iterazione sostituirà la versione attiva

L’ultimo passo è decidere se questa iterazione debba diventare la nuova versione operativa. Una nuova iterazione non sostituisce automaticamente la pubblicazione precedente. Per arrivare in produzione deve passare per review, validazione e pubblicazione nel suo lifecycle.

Prima di concludere, assicurati che:
1. Tu abbia calcolato la nuova iterazione.
2. Tu abbia confrontato il risultato con la soluzione published.
3. Tu sappia se il cambiamento porta un reale miglioramento o solo una variante non operativa.

Per chiudere la decisione sull’iterazione:
1. Rivedi la nuova soluzione da un punto di vista tecnico e operativo.
2. Se migliora chiaramente la soluzione attiva, preparala per:
   1. validazione,
   2. e successiva pubblicazione.
3. Se non migliora il risultato, mantieni la versione published corrente come riferimento attivo.
4. Non rimuovere la pubblicazione precedente solo perché esiste una nuova iterazione.
5. Mantieni entrambe le versioni ben identificate per audit e confronto storico.
6. Se vai avanti, tratta l’iterazione come un nuovo scenario che deve seguire il suo flow fino a diventare **Published**.

Per il caso di riferimento, termina questo quick start solo quando puoi affermare una di queste:
1. La nuova iterazione L1 migliora la versione published e dovrebbe continuare il suo lifecycle.
2. La versione published corrente è ancora migliore e l’iterazione resterà solo come test o riferimento di analisi.

Quando termini questa sezione, dovresti avere una nuova iterazione calcolata, confrontata e pronta a diventare una nuova versione oppure a restare una variante di analisi.

## Additional reading

- [Eseguire e validare il primo calcolo di Scheduling](P15_Eseguire_e_validare_il_primo_calcolo_di_Scheduling.md)

