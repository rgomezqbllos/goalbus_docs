---
title: Eseguire e convalidare il primo calcolo della programmazione
shortTitle: Calcola e convalida
intro: Scopri come eseguire il primo calcolo di Scheduling, rivedere il ciclo di vita
  dello stadio, convalidare la soluzione preparata e lasciare lo scenario pronto per
  la pubblicazione o il successivo audit.
contentType: how-tos
versions:
- '*'
---
## Eseguire il calcolo dello scenario

Ora che avete già creato e configurato lo scenario con l'offerta validata, le matrici corrette e i modelli di regole e turni del veicolo, il passo successivo è quello di eseguire il calcolo.

In questa fase, il motore prende:
1. l'offerta convalidata,
2. regole attive,
3. la logistica dei viaggi vuoti,
4. e la struttura del palcoscenico,

per costruire compiti logici programmabili.

Usa questo avvio rapido quando hai lo scenario pianificato pronto e hai bisogno di ottenere la prima soluzione calcolata prima di rivedere e validare.

Prima di iniziare, assicurati che:
1. Hai già preparato il palcoscenico alla P14.
2. Hai già selezionato il corretto servizio convalidato.
3. Hai già assegnato la corretta matrice di viaggio vuota.
4. Hai già selezionato il modello giusto di regole del veicolo.
5. Hai già selezionato il modello giusto di regole di turno.
6. Hai già impostato il motore Classic e i parametri di calcolo.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Eseguirò il primo calcolo dello scenario pianificato sulla linea L1, controllare se la soluzione è coerente e lasciare lo scenario pronto per la convalida.**

Per eseguire il calcolo dello scenario:
1. Apri lo scenario che vuoi calcolare.
2. Controlla un'ultima volta che i biglietti del palcoscenico siano corretti.
3. Avvia l'azione **Calcola** o **Inizio calcolo**.
ref: P15_Imagen1.png | compact(3x)
ref: P15_Imagen2.png | compact
4. Controllare che lo stato dello stadio cambia da **Soluzione in attesa** a **Calcolo della soluzione**.
ref: P15_Imagen3.png | full
ref: P15_Imagen4.png | full
5. Aspetta che il motore finisca il processo.
ref: P15_Imagen5.png | compact(1x18)
6. Controlla lo stato del nuovo palcoscenico.
7. Se il calcolo si conclude correttamente, conferma che lo scenario passa a **Soluzione preparata**.
ref: P15_Imagen6.png | compact(x7)
8. Se la soluzione richiede regolazioni manuali, inserire lo stato **Modifica** per la raffinatezza.
9. Se il motore non restituisce una soluzione valida, controllare di nuovo:
   1. l'offerta,
   2. la matrice di viaggio vuota,
   3. le regole,
   4. e i parametri dello scenario.

Per il caso di riferimento, essa conferma che:
1. Lo scenario L1 esce dallo stato iniziale.
2. Il motore completa il calcolo senza bloccare.
3. Lo scenario è una soluzione preparata o una fase di editing ragionevole.

Inoltre, nel caso in cui il tipo di scenario scelto sia per veicoli e turni, è possibile vedere la soluzione generata dai turni dalla vista del personale.
ref: P15_Imagen12.png | compact

Quando si termina questa sezione, si dovrebbe avere una prima soluzione calcolata o un segnale chiaro di quale parte della parametrizzazione necessita di correzione.

## Riesame dello stato dello scenario e del risultato del calcolo

Dopo aver eseguito il calcolo, è necessario capire a quale punto del ciclo di vita lo scenario è rimasto. Questo è importante perché ogni stato ha un significato operativo diverso e vi dice quali azioni potete fare dopo.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai gia' controllato il calcolo.
2. Conosci il nome del palcoscenico che stai esaminando.
3. Sai se ti aspettavi una soluzione pronta o una fase di raffinamento.

Per rivedere lo stato e il risultato:
1. Tornate al tavolo dello scenario principale o restate sul palco.
2. Controlla lo stato attuale.
3. Egli interpreta lo stato secondo questa logica:
   1. **Soluzione in attesa**: Lo scenario non è ancora stato calcolato.
   2. **Calcolo della soluzione**: Il motore sta elaborando la soluzione.
   3. **Modifica**: Un utente sta regolando manualmente la soluzione.
   4. **Soluzione preparata**: La fase di calcolo o di modifica è finita e lo scenario è pronto per la revisione.
   5. **Convalida**: La soluzione è già stata approvata e bloccata.
   6. **Pubblicazione**: La soluzione viene incorporata nel calendario operativo.
   7. **Pubblicato**: La soluzione è già stata impiantata nell'operazione.
4. Se lo scenario è in **Soluzione preparata**, continuare con la revisione della coerenza.
5. Se lo scenario è in **Modifica**, finire prima le impostazioni manuali necessarie.
6. Se lo scenario è ancora in **Calcolo della soluzione** per troppo tempo, controllare se c'è stata un'incidenza tecnica eccessivamente restrittiva o una configurazione.

Per il caso di riferimento, si dovrebbe aspettare che lo scenario finisca almeno in:
1. **Soluzione preparata**, se non hai più bisogno di toccare la struttura,
2. o **Modifica**, se si desidera ancora raffinare manualmente.

Quando si conclude questa sezione, si dovrebbe capire chiaramente che cosa significa lo stato di fase attuale e che azione segue.

## Controllo di KPI, errori e coerenza prima di validare

Prima di validare lo scenario, è necessario rivedere. La validazione non è un semplice clic amministrativo. È la porta di approvazione formale che congela la soluzione e impedisce modifiche successive accidentali.

Prima di iniziare questa sezione, assicurarsi che:
1. La fase è già in **Soluzione preparata** o hai finito la fase **Modifica**.
2. Sapete, dopo la validazione, lo scenario non sarà più modificabile.
3. Sei pronto per una revisione finale prima dell'approvazione.

Per rivedere la soluzione prima di validarla:
1. Apre il palcoscenico nel suo stato attuale.
2. Controlla i KPI disponibili.
ref: P15_Imagen7.png | full
3. Controllare se sono visibili errori, avvertimenti o incongruenze.
ref: P15_Imagen8.png | compact(x7)
4. Utilizzare i filtri disponibili per ispezionare la soluzione da diversi angoli.
ref: P15_Imagen9.png | compact(3x)
5. Controlla che le mappature e la struttura dello scenario abbiano senso operativo.
6. Se si rileva un problema minore e lo scenario è ancora modificabile, correggilo prima di continuare.
7. Se si rileva un problema importante dopo averlo bloccato in seguito, è necessario sbloccarlo con i permessi appropriati o tornare a uno scenario modificabile.

Per il caso di riferimento, assicurarsi che:
1. I KPI di soluzione L1 sono ragionevoli.
2. Non ci sono errori gravi che invalidano la soluzione.
3. La soluzione può ora passare dalla revisione tecnica all'approvazione formale.

Quando si termina questa sezione, si dovrebbe avere abbastanza fiducia per convalidare lo scenario.

## Validare lo stadio e bloccare la soluzione

Ora è possibile eseguire il **convalida dello scenario**. Questo passo segna la chiusura ufficiale della fase di calcolo e editing. Da qui, la soluzione diventa protetta, lo scenario cessa di essere modificabile e non può più essere ricalcolato mentre rimane convalidato.

Prima di iniziare questa sezione, assicurarsi che:
1. Il palcoscenico è su **Soluzione preparata**.
2. Hai finito la revisione KPI e gli errori.
3. Non è necessario effettuare ulteriori aggiustamenti manuali prima di approvare la soluzione.

Per convalidare lo scenario:
1. Dalla tabella degli scenari, aprire il menu di azione del palco.
2. Selezionare **Convalida**.
3. Se preferisci farlo dall'interno del palcoscenico, usa il pulsante **Convalida** nella parte superiore dello schermo.
ref: P15_Imagen10.png | compact(2x)
4. Confermare la convalida quando il sistema lo richiede.
5. Controllare che lo stato della soluzione di stadio cambi a **Convalida**.
ref: P15_Imagen11.png | compact(2x)
6. Controlla che:
   1. lo scenario non è più modificabile,
   2. non può più essere ricalcolato,
   3. e i loro dati principali sono protetti.
7. Se scopri un errore dell'ultimo minuto dopo la convalida, usa il flusso di sblocco solo con i giusti permessi.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. La soluzione L1 è già stata riesaminata.
2. La soluzione dello scenario è cambiata in stato **Convalida**.
3. L'organizzazione può già trattare questo scenario come una versione approvata.

Quando si conclude questa sezione, si dovrebbe avere una soluzione formalmente approvata e bloccata per evitare cambiamenti accidentali.

## Lasciando lo scenario pronto per la pubblicazione o la successiva revisione contabile

Una volta convalidato, lo scenario è pronto per due percorsi:
1. **Pubblicazione**, se si desidera portarlo al calendario operativo effettivo,
2. o **audit**, se è ancora necessario rivedere prima di pubblicare.

A questo punto, lo scenario rimane una soluzione approvata e protetta. Puoi comunque consultarla, rivedere KPI, filtrare le informazioni e usarle come riferimento, ma non dovresti più trattarla come una bozza di lavoro.

Prima di finire, assicurati che:
1. La soluzione stadio è già in stato **Convalida**.
2. Conosci la differenza tra la validazione e l'editoria.
3. Sapete se il vostro prossimo passo sarà quello di impiantare la soluzione o continuare a controllarla.

Per lasciare il palcoscenico pronto per il passo successivo:
1. Controlla la tabella degli scenari e conferma lo stato **Convalida**.
2. Se il piano è già approvato per l'implementazione, preparare il flusso **Pubblica**.
3. Se avete ancora bisogno di revisione interna, mantenere lo scenario convalidato come base di audit.
4. Utilizza filtri, icone di informazione e revisione di stato per controllare quali scenari sono pendenti, convalidati o già pubblicati.
5. Se hai bisogno di iterare una nuova versione, considera di duplicare lo scenario invece di alterarne una già approvata.

Per il caso di riferimento, finite questo avvio rapido solo quando potete dire:
1. Lo scenario L1 è già stato calcolato.
2. La soluzione è stata riesaminata.
3. La soluzione per lo stadio è **Convalida**.
4. Il passo successivo non è più quello di calcolare, ma di decidere se è pubblicato o controllato.

Quando si conclude questa sezione, si dovrebbe avere uno scenario calcolato, rivisto e convalidato, pronto per la produzione o la revisione finale.

## Letture aggiuntive

- [Pubblicazione dello scenario in date specifiche](publicacion-del-escenario)
