---
title: Caricamento e gestione driver
shortTitle: Autisti
intro: Scopri come creare, importare e mantenere la base del driver in GoalBus, rivedere
  il tuo profilo operativo e lasciare un modello affidabile prima di passare al distacco
  di Rostering, alle regole e al calcolo.
contentType: how-tos
versions:
- '*'
---
## Creazione o importazione di template driver

Prima di parlare di regole di registrazione, assenze o assegnazione di turni, è necessario avere una base di driver affidabile. In GoalBus, la gestione del driver agisce come la principale fonte di verità per l'operatività umana: permette di combinare la creazione manuale e il carico di massa, e concentra identità, affiliazione di deposito e disponibilità nella stessa directory. fileciteturn38file2L1-L24

Utilizzare questo rapido inizio quando si è chiari circa la transizione da Schedule a Rostering e la necessità di preparare il vero gruppo di persone che parteciperanno all'assegnazione.

Prima di iniziare, assicurati che:
1. Hai gia' chiuso la transizione da Scheduling alla P19.
2. È chiaro a voi quale collettivo di driver parteciperà al calcolo.
3. Sai se vuoi scaricare alcuni driver manualmente o se hai bisogno di un carico enorme.
4. Avete accesso all'ambiente con i permessi per gestire il personale.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Carico e riesami il modello del driver che può coprire la soluzione L1 prima di entrare in distacco, regole e disponibilità.**

Per creare o importare il modello del driver:
1. In GoalBus, vai al modulo **Impostazioni** > **Personale** > **Gestione del conducente**.
ref: P20_Imagen1.png | compact
2. Controllare se i driver del caso esistono già nell'elenco generale.
3. Se è necessario creare pochi driver, fare clic su **Nuovo driver**.
ref: P20_Imagen2.png | compact(2x)
4. Se è necessario caricare molti driver, fare un'importazione massiccia utilizzando file CSV da **Carico personale**.
ref: P20_Imagen3.png | compact
5. Se si sceglie l'importazione di massa, preparare il file con i dati minimi necessari per identificare correttamente ogni persona. La finestra di importazione aiuterà a preparare il carico CSV.
ref: P20_Imagen4.png
6. Esegui il carico e controlla il risultato.
7. Torna alla lista generale e controlla che i driver appaiono correttamente.
8. Se si rilevano duplicati o record incompleti, correggerli prima di continuare.

Per il caso di riferimento, finire questa sezione solo quando si può dire:
1. I conducenti L1 sono già scaricati o importati.
2. L'elenco generale rispecchia un unico modello di riferimento.
3. Ora è possibile aprire il profilo di ogni driver per rivedere il suo contesto operativo.

Quando si termina questa sezione, si dovrebbe avere un modello di driver caricato e visibile nel sistema. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Controllo del profilo del conducente e dei dati strutturali

Una volta creato il template, è necessario rivedere il **profilo del conducente**. Il profilo non è solo una scheda di contatto: è il file digitale completo dell'impiegato all'interno dell'operazione. Ci convivono dati statici, contesto operativo e attributi che il sistema userà in seguito per ragionare circa la sua ammissibilità. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Prima di iniziare questa sezione, assicurarsi che:
1. Avete già driver visibili nella lista generale.
2. Sai quale autista o gruppo userai come campione.
3. Vuoi convalidare che il registro non è solo amministrativo, ma operativo.

Per controllare il profilo del conducente:
1. Nell'elenco generale, fare clic sul nome di un driver.
ref: P20_Imagen5.png | full
2. Controlla la barra laterale dei dati statici.
3. Controllare almeno questi gruppi di informazioni:
   1. dati di base, quali nome e codice,
   2. dati operativi, quali la convenzione collettiva o il tipo di contratto,
   3. collegamenti operativi, quali deposito principale, gruppo di lavoro, zona o tipo di veicoli omologati.
4. Se mancano dati strutturali chiave, compilarli prima di procedere.
5. Risparmia qualsiasi cambiamento necessario.
6. Ripetere la revisione su più driver per confermare la coerenza nel modello.

Per il caso di riferimento, controllare almeno:
1. Il codice del conducente.
2. Il tuo magazzino principale.
3. La tua task force.
4. Le proprietà operative che conditioneranno il tuo successivo incarico.

Quando si termina questa sezione, si dovrebbe essere chiari che ogni driver ha un file operativo coerente e utilizzabile. fileciteturn38file0L8-L20

## Revisione del contesto operativo e dei dati dinamici del conducente

Oltre ai dati strutturali, il profilo del driver include dati dinamici che influenzano direttamente il modo in cui il sistema ragiona la persona. Nella scheda di amministrazione è possibile rivedere i contatori e i modelli di lavoro, che fanno parte del contesto operativo utilizzato successivamente dalla logica di mappatura. fileciteturn38file0L12-L17

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già controllato i dati statici sul profilo.
2. Sapete se la vostra operazione utilizza contatori o modelli ciclici.
3. Si desidera verificare che il conducente non solo esiste, ma ha un contesto operativo interpretabile.

Per rivedere il contesto operativo dinamico:
1. All'interno del profilo del driver, aprire la scheda **Dettagli amministrativi**.
2. Controllare **contatori** o KPI associati al driver se esistono.
3. Controllare se il driver è collegato a qualsiasi **modello di lavoro**.
4. Se la vostra operazione utilizza modelli ciclici, controllate anche il ritardo o la posizione del driver attuale all'interno del modello.
5. Conferma che questi dati hanno senso per il contesto reale.
6. Se l'informazione dinamica non è corretta, aggiustala prima di passare alle regole o al calcolo.

Per il caso di riferimento, chiedetevi:
1. Questo autista ha il modello che dovrebbe avere?
2. I tuoi contatori o KPI sono disponibili se il processo ne ha bisogno?
3. Potrebbe il sistema ragionare correttamente su questa persona in un calcolo di assegnazione?

Quando si conclude questa sezione, si dovrebbe aver convalidato non solo l'identità del driver, ma anche il suo contesto operativo dinamico. fileciteturn38file0L12-L17

## Valutare le valutazioni prima di utilizzare il driver in Rostering

Prima di considerare un driver idoneo, è necessario rivedere il vostro **valutazioni**. Queste valutazioni rispondono alla domanda .Posso questa persona lavorare legalmente o tecnicamente su questo deposito, gruppo o unità? . Sono gestiti in una linea temporale con la data di inizio e fine, e il sistema mostra gli stati come attivi, futuri, scaduti o vicini a scadere per facilitare la lettura. Se una persona non è abilitata per il contesto richiesto, il motore genera un errore nel tentativo di assegnarlo. fileciteturn38file0L17-L34

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già controllato il profilo del conducente.
2. Sai di quale deposito, gruppo o unità avrai bisogno per il tuo caso.
3. Capisci che un potere non è lo stesso di un incarico temporaneo o distacco.

Per rivedere e convalidare i rating:
1. All'interno del profilo driver, aprire la scheda **Abilitare/qualificare**.
2. Controllare i registri esistenti per:
   1. depositi,
   2. gruppi di lavoro,
   3. Unità d'affari.
3. Controllare lo stato visivo di ogni valutazione:
   1. attivo,
   2. futuro,
   3. dopo la scadenza,
   4. è scaduto.
4. Se manca una valutazione necessaria, aggiungetela con le date corrette.
5. Se un'abilitazione è scaduta e non deve essere usata, lasciatela come storica senza cercare di riscrivere il passato.
6. Salva i cambiamenti.
7. Conferma che il driver è già abilitato per il contesto in cui ti aspetti di usarlo.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. Il conducente è abilitato per il deposito corretto.
2. Il gruppo di lavoro richiesto è coperto.
3. Non ci sono scadenze che infrangano l'ammissibilità attuale.

Quando si conclude questa sezione, si dovrebbe avere driver che non solo esistono nel modello, ma sono anche ammissibili da un punto di vista operativo e regolamentare. fileciteturn38file0L17-L34

## Conferma che il modello è già pronto per il livello successivo di Rostering

L'ultimo passo è quello di verificare che la base del conducente sia pronta a inserire il seguente livello: distacco operativo, regole, assenza e calcolo. Qui l'obiettivo non è solo avere i nomi caricati, ma un modello coerente, tracciabile e utilizzabile dal motore.

Prima di finire, assicurati che:
1. Hai già caricato o importato il modello.
2. Hai già controllato i profili principali.
3. Hai già controllato i dati strutturali e dinamici.
4. Hai già convalidato le valutazioni essenziali.

Per confermare che il modello è già pronto:
1. Torna alla lista generale dei piloti.
2. Controllate che il collettivo necessario per il vostro caso sia presente.
3. Verificare che i profili critici non abbiano lacune importanti in materia di informazioni.
4. Assicurati che le persone che ti aspetti di usare siano abilitate per il contesto giusto.
5. Chiedetevi se il sistema potrebbe già utilizzare questa base come punto di partenza per:
   1. distacco operativo,
   2. Regole di registrazione,
   3. e la disponibilità effettiva.
6. Se la risposta è sì, continuare con il prossimo inizio rapido.
7. Se la risposta è no, correggere la base del conducente prima di continuare.

Per il caso di riferimento, finite questo avvio rapido solo quando potete dire:
1. Il modello del driver L1 è già caricato.
2. I profili chiave sono già stati riesaminati.
3. Le valutazioni essenziali sono già in atto.
4. La base è ora pronta per il distacco operativo.

Quando si termina questa sezione, si dovrebbe avere un modello di driver abbastanza forte per continuare con il livello successivo di Rostering.

## Letture aggiuntive

- [Gestione del distacco operativo del conducente](P21_Gestione_Del_Distacco_Operativo_Del_Conducente.md)
