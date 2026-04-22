---
title: Creazione di una nuova iterazione dello scenario da una soluzione pubblicata
shortTitle: Nuova iterazione
intro: Scopri come creare una nuova iterazione di uno scenario già pubblicato per
  testare i miglioramenti, regolare i parametri o introdurre modifiche senza alterare
  la versione già in funzione.
contentType: how-tos
versions:
- '*'
---
## Basato su una soluzione pubblicata senza alterare la versione attuale

Dopo aver pubblicato una soluzione, è normale che tu debba continuare a lavorare su di essa. È possibile che tu voglia modificare le regole, provare un'altra logica di turno, incorporare cambiamenti di offerta o preparare un miglioramento per un periodo futuro. In questo caso, non dovresti modificare direttamente la versione già pubblicata. La cosa giusta è creare un **nuova iterazione** dello scenario per mantenere la tracciabilità e proteggere la versione già in vigore.

Utilizza questo avvio rapido quando hai già una fase con una soluzione in stato **Pubblicato** e hai bisogno di generare una nuova variante senza perdere il riferimento storico della soluzione implantata.

Prima di iniziare, assicurati che:
1. Hai già pubblicato lo scenario precedente su P16.
2. La soluzione di scenario che prenderete come la vostra base è in stato **Pubblicato**.
3. Sai cosa vuoi sembrare o migliorare la prossima iterazione.
4. È chiaro che la nuova iterazione non dovrebbe sostituire automaticamente la versione corrente finché non passa di nuovo attraverso il calcolo, la convalida e la pubblicazione.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Creerò una nuova iterazione dello scenario L1 pubblicato per testare i miglioramenti nella soluzione senza toccare la versione già in funzione.**

Per una soluzione pubblicata in modo sicuro:
1. In GoalBus, aprire il modulo **Scenari di pianificazione**.
2. Localizza lo scenario la cui soluzione è in stato **Pubblicato**.
3. Controlla il tuo nome, la descrizione, il tipo di giorno e le linee associate.
4. Conferma che è davvero la versione che vuoi usare come riferimento.
5. Evitare di modificare la versione direttamente come se fosse una nuova bozza.
6. Decidete quale cambiamento volete fare nella nuova iterazione:
   1. regole,
   2. parametri,
   3. offerta,
   4. o adeguamenti strutturali consentiti.

Quando si conclude questa sezione, si dovrebbe aver chiaramente identificato lo scenario pubblicato che servirà come base per la vostra nuova iterazione.

## Creazione della nuova iterazione dallo scenario pubblicato

Una volta identificata la base, il passo successivo è quello di creare un **nuova iterazione**. L'obiettivo è quello di preservare la versione pubblicata come riferimento storico e aprire un nuovo ramo di lavoro controllato sulla stessa logica operativa.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già identificato la corretta soluzione pubblicata.
2. Sai perche' hai bisogno di una nuova iterazione.
3. È chiaro che la nuova iterazione deve essere chiaramente differenziata dalla versione precedente.

Per creare la nuova iterazione:
1. Dalla tabella scenario, aprire il menu azione dello scenario pubblicato.
2. Selezionare l'opzione per **creare una nuova iterazione** cliccando su **duplicato** lo scenario come base di lavoro.
ref: P17_Imagen1.png | compact
3. Inserisci un **nuovo nome** per l'iterazione.
4. Se del caso, aggiornare **descrizione** per riflettere l'obiettivo di modifica.
5. Salva la nuova iterazione.
ref: P17_Imagen2.png | compact
6. Verifica che il nuovo scenario appare come entità separata dallo scenario pubblicato.
ref: P17_Imagen3.png | full
7. Verificare che la versione originale pubblicata rimanga intatta e differenziata dalla nuova.

Per il caso di riferimento, un'opzione valida potrebbe essere:
- **Calcolo classico - L1 utilizzabile - Iterazione 2**
- **L1 utilizzabile - miglioramento delle norme sui turni**

Quando si conclude questa sezione, si dovrebbe avere una nuova iterazione creata senza perdere la tracciabilità della versione pubblicata.

## Definire quali cambiamenti appartengono alla nuova iterazione

Dopo aver creato l'iterazione, è necessario decidere cosa si sta realmente per cambiare. Non tutte le iterazioni perseguono lo stesso obiettivo. Alcuni servono a regolare le regole, altri per migliorare l'efficienza, altri per riflettere una nuova offerta o variazione operativa futura.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai creato la nuova iterazione.
2. Sapete quale aspetto della soluzione di cui sopra si desidera rivedere.
3. Siete disposti a limitare il passaggio a un obiettivo specifico in modo da non miscelare troppe variabili.

Per definire il campo di applicazione dell'iterazione:
1. Apri il nuovo palcoscenico.
2. Controllare quali elementi si desidera mantenere esattamente lo stesso come nella versione pubblicata.
3. Decidi prima quale elemento cambierai:
   1. **Regole relative ai veicoli**,
   2. **regole di turno**,
   3. **Parametri del motore**,
   4. **offerta di servizio**,
   5. **Matrici logistiche**.
4. Evitare di cambiare troppe cose contemporaneamente nella prima iterazione, a meno che strettamente necessario.
5. Documentare nel nome o nella descrizione lo scopo dell'iterazione.
6. Salva le modifiche descrittive prima di andare al calcolo.

Per il caso di riferimento, utilizzare una logica come questa:
1. Mantenere la stessa L1 offerta praticabile.
2. Aggiusta solo il modello delle regole di turno.
3. Ricalcolare per confrontare la nuova soluzione con quella pubblicata.

Quando hai finito questa sezione, dovresti avere una nuova iterazione con un bersaglio chiaro e ristretto.

## Ricalcolare l'iterazione e confrontarla con la versione precedente

Una volta definita la portata, è necessario ricalcolare l'iterazione. Qui il vantaggio è che non si lascia più da zero: parti da una soluzione conosciuta e si può meglio confrontare l'impatto del cambiamento.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai creato la nuova iterazione.
2. Hai già definito l'obiettivo del cambiamento.
3. Hai già controllato quali regole, parametri o voci hai intenzione di modificare.

Per ricalcolare la nuova iterazione:
1. Rivedere lo scenario iterato e confermare che le sue voci rimangono coerenti.
2. Regolare l'elemento che si desidera modificare.
3. Salva le impostazioni.
4. Esegui il calcolo del nuovo scenario.
5. Aspetta che lo scenario completi la fase di calcolo.
6. Controllare se l'iterazione passa a **Soluzione preparata** o **Modifica**.
7. Confronta il risultato con la versione precedente usando:
   1. KPI,
   2. struttura generale,
   3. logica del compito,
   4. e la coerenza operativa.
8. Se il cambiamento migliora il risultato, continuare con la revisione formale.
9. Se il cambiamento peggiora il risultato, conservare la versione pubblicata come riferimento e decidere se si desidera correggere o scartare questa iterazione.

Per il caso di riferimento, confrontare:
1. La soluzione L1 pubblicata.
2. La nuova iterazione con regolazione delle regole.
3. Ciò che è cambiato nella qualità, nella redditività o nell'equilibrio.

Quando si conclude questa sezione, si dovrebbe avere una nuova soluzione calcolata e una base chiara per confrontarla con la versione già pubblicata.

## Decidere se la nuova iterazione sostituirà la versione attuale

L'ultimo passo è decidere se questa iterazione debba diventare la nuova versione operativa. Una nuova iterazione non sostituisce automaticamente la pubblicazione precedente. Per arrivare alla produzione, è necessario tornare attraverso la revisione, la convalida e la pubblicazione con il proprio ciclo di vita.

Prima di finire, assicurati che:
1. Hai già calcolato la nuova iterazione.
2. Hai già confrontato il risultato con la soluzione pubblicata.
3. Sai se il cambiamento porta un vero miglioramento o solo una variante senza valore operativo.

Per chiudere la decisione sull'iterazione:
1. Rivedere la nuova soluzione dal punto di vista tecnico e operativo.
2. Se l'iterazione migliora chiaramente la soluzione attuale, preparatela per:
   1. convalida,
   2. e successiva pubblicazione.
3. Se l'iterazione non migliora il risultato, conserva l'attuale versione pubblicata come riferimento attuale.
4. Non cancellare la pubblicazione precedente solo perché c'è una nuova iterazione.
5. Mantenere entrambe le versioni ben identificate per l'audit e il confronto storico.
6. Se decidete di andare avanti, trattate l'iterazione come un nuovo scenario che deve viaggiare il proprio flusso fino a raggiungere **Pubblicato**.

Per il caso di riferimento, finite questo rapido inizio solo quando potete affermare una di queste due cose:
1. La nuova iterazione L1 migliora la versione pubblicata e merita di continuare il suo ciclo.
2. L'attuale versione pubblicata rimane migliore e l'iterazione rimarrà solo come prova o riferimento.

Quando si termina questa sezione, si dovrebbe avere una nuova iterazione calcolata, confrontata e pronta per diventare una nuova versione o per essere mantenuta come una variante di analisi.

## Letture aggiuntive

- [Eseguire e convalidare il primo calcolo della programmazione](P15_Eseguire_E_Convalidare_Il_Primo_Calcolo_Della_Programmazione.md)
