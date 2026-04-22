---
title: Gestione del distacco operativo del conducente
shortTitle: distacco operativo
intro: Imparare come collegare ogni driver con il loro deposito, business unit e gruppo
  di lavoro, e capire come questo distacco condiziona la loro reale ammissibilità
  prima di passare alle regole di Rostering, assenze e calcolo.
contentType: how-tos
versions:
- '*'
---
## Comprendere il distacco operativo del conducente

Prima di definire regole avanzate, assenze o calcoli di Rostering, è necessario capire come **distaccato** viene lasciato per ogni driver all'interno dell'organizzazione. In GoalBus, il distacco operativo non si basa su un unico campo. È costruito combinando tre coordinate principali:
1. **Deposito**
2. **Unità aziendale**
3. **Gruppo di lavoro**

Questa combinazione definisce dove lavora la persona, a quale divisione appartiene e a che tipo di compiti può ricevere. Condivide anche la visibilità della risorsa per i pianificatori e i manager. fileciteturn39file3L1-L20

Usa questo avvio rapido quando hai già caricato il modello del driver e devi assicurarti che ogni persona si trovi nel giusto contesto operativo prima di passare alle regole e alla disponibilità.

Prima di iniziare, assicurati che:
1. Hai già caricato e controllato i piloti alla P20.
2. Sai quali depositi, unità e gruppi usano la tua operazione.
3. Siete chiari che gruppo di staff parteciperà al calcolo della Rostering.
4. Sapete che un cattivo distacco può rendere una persona inammissibile anche se esiste nel sistema.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Controllerò che i driver che copriranno la linea L1 siano collegati al deposito corretto, all'unità e alla task force prima di stabilire le regole e la disponibilità.**

Per comprendere il distacco operativo:
1. Tratta il **deposito** come la posizione di base fisica della risorsa.
2. Tratta **unità aziendale** come la divisione strategica o modale a cui appartiene la persona.
3. Trattare **gruppo di lavoro** come la funzione che determina che tipo di attività si può ricevere.
4. Usa questa regola di lettura:
   1. il deposito risponde a **dove lavora**,
   2. l'unità risponde a **in cui opera l'impresa o la modalità**,
   3. il gruppo risponde a **che tipo di lavoro puoi fare**.
5. Non mescolare questi tre concetti come se fossero uguali.

Quando si conclude questa sezione, si dovrebbe essere chiari che il distacco operativo è una struttura composita e non un singolo attributo isolato. fileciteturn39file1turn39file3

## Serbatoio di controllo, unità e gruppo di lavoro sul profilo del conducente

Una volta che la logica è compresa, è necessario controllare come è configurato nel profilo del driver effettivo. Questi campi fanno parte del DNA strutturale del dipendente e sono la base del loro contesto operativo. Se sono mal definiti, la mappatura posteriore è contaminata dalla sorgente. fileciteturn39file0turn39file2

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già dei driver creati nel modello.
2. Sai quale autista o gruppo userai come campione.
3. Vuoi rivedere il distacco strutturale, non ancora un incarico temporaneo.

Per rivedere il distacco nel profilo:
1. Sull'elenco generale dei piloti, aprire il profilo di una persona.
2. Controlla la barra laterale dei dati strutturali.
3. Controllare almeno:
   1. **Deposito principale**
   2. **Unità aziendale**
   3. **Gruppo di lavoro**
   4. **Superficie**, se la vostra operazione lo utilizza
4. Conferma che tali valori coincidono con il contesto reale in cui la persona deve lavorare.
5. Se un dato è errato, aggiornarlo nel profilo.
6. Salva i cambiamenti.
7. Ripetere la revisione su più driver per confermare che il modello è coerente.

Per il caso di riferimento, ritiene che:
1. I conducenti L1 appartengono al serbatoio corretto.
2. L'unità commerciale corrisponde alla modalità o all'attività attesa.
3. Il gruppo di lavoro corrisponde davvero a **Autisti** e non ad un altro ruolo.

Quando si conclude questa sezione, si dovrebbe aver rivisto l'allegato strutturale dei driver che parteciperanno al calcolo. fileciteturn39file1turn39file2

## Comprendere la differenza tra distacco principale, abilitazione e assegnazione

Prima di andare avanti, è necessario distinguere tre concetti che sono spesso confusi:
1. **distacco principale**
2. **Impiego**
3. **Trasferimento o trasferimento temporaneo**

L'annuncio principale definisce dove la persona appartiene strutturalmente. L'abilitazione risponde a se **può** funziona legalmente o tecnicamente in un altro contesto. La cessione risponde a dove **Sta davvero lavorando.** per un periodo temporaneo. Questi tre strati coexistono, ma non significano lo stesso. fileciteturn39file0turn39file4

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già controllato il distacco principale nel profilo.
2. Sapete che alcune persone possono lavorare al di fuori del loro contesto principale.
3. Si vuole evitare l'interpretazione errata tra i membri a, può lavorare su e sta lavorando su.

Per distinguere correttamente questi concetti:
1. Utilizzare **distacco principale** per descrivere il contesto strutturale di base del driver.
2. Utilizzare **valutazione** per indicare che il conducente può lavorare in un altro serbatoio, gruppo o unità.
3. Utilizzare **assegnazione** per indicare che il driver viene temporaneamente spostato in un altro contesto.
4. Non utilizzare un' assegnazione per correggere un distacco principale mal definito.
5. Non usare una valutazione come se fosse una mossa attiva.
6. Tenere queste domande come una guida:
   1. Dove appartiene questa persona? → abbonamento principale
   2. Dove potrei lavorare legalmente? → Abilitare
   3. Dove stai lavorando in questo momento? → cessione

Per il caso di riferimento, chiedetevi:
1. L'autista appartiene al North Depot?
2. Puoi lavorare in un altro magazzino, se necessario?
3. È temporaneamente trasferito in un'altra base o è ancora nel suo contesto abituale?

Quando si conclude questa sezione, si dovrebbe avere una corretta lettura della gerarchia tra distacco, abilitazione e assegnazione. fileciteturn39file0turn39file4

## Convalida che il distacco permette di visualizzare e assegnare correttamente il driver

L'iscrizione non serve solo a descrivere il profilo del driver. Essa condiziona anche come il sistema lo vede e quali compiti può ricevere. Una persona non iscritta può essere lasciata fuori dal filtro corretto, apparire nel posto sbagliato o ricevere compiti che non corrispondono a lui. Il contrario può verificarsi anche: che una persona valida è nascosta o non ammissibile da un allegato mal definito. fileciteturn39file3L1-L20

Prima di continuare, assicurarsi che:
1. Avete già controllato magazzino, unità e gruppo in diversi profili.
2. Capisci la differenza tra distacco e incarico.
3. Siete già chiari quale collettivo parteciperà al prossimo calcolo.

Per convalidare l'impatto operativo del distacco:
1. Controllare quale serie di driver dovrebbe essere visibile per il contesto del vostro calcolo.
2. Controllare che le persone giuste appaiono sotto il deposito destro, unità e gruppo.
3. Controllare se ci sono driver nel gruppo sbagliato.
4. Controllare se ci sono driver che dovrebbero appartenere al contesto e non appaiono come tali.
5. Se rilevate un errore di distacco, correggetelo prima di passare alle regole o alla disponibilità.
6. Salva la configurazione finale dei profili interessati.

Per il caso di riferimento, assicurarsi che:
1. I driver che copriranno L1 appaiono nel contesto operativo corretto.
2. Non si mescolano con gruppi che non devono ricevere compiti di guida.
3. Il sistema potrebbe filtrare e assegnare solo personale rilevante.

Quando si termina questa sezione, si dovrebbe avere una base di distacco operativo che aiuta il sistema vedere e utilizzare le persone giuste.

## Conferma che il distacco operativo è già pronto per il livello successivo

L'ultimo passo è quello di verificare che il distacco sia stato abbastanza solido da continuare con le regole, le assenze e il calcolo. Qui l'obiettivo non è solo di avere riempiti i campi, ma di aver lasciato una struttura chiara che il motore può interpretare inequivocabilmente.

Prima di finire, assicurati che:
1. Hai già controllato il distacco strutturale dei profili chiave.
2. Lei già distingue il distacco, l'abilitazione e l'incarico.
3. Hai già convalidato che il collettivo visibile è quello giusto.
4. Hai corretto i principali disallineamenti.

Per confermare che il distacco è già pronto:
1. Torna alla lista generale dei piloti.
2. Verificare che il collettivo rilevante per il tuo caso appaia nel contesto corretto.
3. Verificare che non ci siano errori evidenti di deposito, unità o gruppo.
4. Chiedetevi se il sistema potrebbe già:
   1. filtrare correttamente i driver della cassa,
   2. applicare loro le regole del diritto collettivo,
   3. e trattarli come base per la disponibilità e il calcolo.
5. Se la risposta è sì, continuare con il prossimo inizio rapido.
6. Se la risposta è no, correggere il distacco prima di continuare.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. I driver L1 sono collegati al contesto corretto.
2. Sai chi appartiene, chi può lavorare e chi è ceduto.
3. La base è ora pronta ad applicare le regole di Rostering e la disponibilità.

Quando si termina questa sezione, si dovrebbe avere un distacco operativo abbastanza chiaro da continuare con il livello successivo del processo.

## Letture aggiuntive

- [Definizione delle regole di registrazione per l'assegnazione del personale](P22_Definizione_Delle_Regole_Di_Registrazione_Per_Lassegnazione_Del_Personale.md)
