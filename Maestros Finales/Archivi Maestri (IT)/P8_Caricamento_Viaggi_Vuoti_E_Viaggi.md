---
title: Caricamento viaggi vuoti e viaggi
shortTitle: Viaggio vuoto
intro: Scopri come impostare le matrici di viaggio e di viaggio del conducente vuoti
  in modo che GoalBus utilizzi tempi reali di logistica, minimizzi i costi non produttivi
  e crei orari e turni più realistici.
contentType: how-tos
versions:
- '*'
---
## Creazione della matrice giusta per il tipo di giorno giusto

Prima di calcolare la programmazione, è necessario definire come l'operazione si muove fisicamente quando non sta generando entrate. In GoalBus, questo modulo copre due cose diverse:

1. **Viaggio vuoto**, che rappresenta il movimento di un autobus con un autista tra il serbatoio, il parcheggio, l'inizio della linea o tra linee.
2. **Spostamenti del conducente**, che rappresenta il movimento del conducente senza veicolo, ad esempio a piedi, in taxi o in navetta.

GoalBus non tratta questi movimenti come una lista unica e fissa. Lo strumento rende chiaro che devono essere organizzati in **matrici per tipo di giorno**, perché il traffico cambia in base al contesto operativo. Un viaggio può durare 15 minuti di domenica e 45 minuti di lunedì mattina, quindi la stessa connessione non dovrebbe sempre riutilizzare lo stesso tempo.

Utilizzate questo rapido inizio quando avete già impostato parcheggi e magazzini, e dovete preparare la logistica invisibile che renderà possibile una pianificazione realistica.

Prima di iniziare, assicurati che:

1. Avete già preparato i parcheggi e i magazzini della P5.
2. Siete già chiari circa la linea o il servizio che userete come riferimento.
3. Sai che tipo di giorno stai modellando.
4. Capisci la differenza tra un viaggio vuoto e un viaggio del conducente.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Preparerò la matrice di viaggio vuota per una giornata lavorativa di linea L1, collegando il parcheggio nord con il terminal nord, e anche la matrice di viaggio del conducente quando necessario per i relè.**

Per creare la matrice corretta per il vostro caso:

1. In GoalBus, aprire il modulo **Viaggi a vuoto e viaggi a vuoto**.
ref: P8_Imagen1.png | full
2. Decidete prima se creare una matrice **viaggi vuoti**, una matrice **Movimenti del conducente**, o entrambi.
3. Fare clic su **Crea un nuovo**.
ref: P8_Imagen2.png | compact(2x5)
4. Inserire un **nome** chiaro per la matrice.
5. Aggiungere un **descrizione** per permettere di riconoscere il contesto operativo.
6. Assegna il **tipi di giorno** al quale si applica tale matrice.
7. Salva la matrice.
ref: P8_Imagen3.png | compact(x8)
8. Verificare che la matrice sia chiaramente associata al contesto corretto e non ad una logica generica.

Per il caso di riferimento, una matrice valida potrebbe essere chiamata:

- **Vuoto - Gennaio 2026**
- **Spostamenti di guida - giorni lavorativi**

Quando si termina questa sezione, si dovrebbe avere una matrice correttamente creata collegata al tipo di giorno giusto.

## Caricamento delle connessioni mediante importazione di massa o modifica manuale

Una volta creata la matrice, è necessario riempirla con le connessioni effettive tra origini e destinazioni. Il documento indica che GoalBus consente due forme di lavoro:

1. **Importazione di massa CSV**, consigliato per grandi reti.
2. **Ingresso manuale**, utile per piccole casse o per completare le regolazioni di punti.

Prima di iniziare questa sezione, assicurarsi che:

1. Hai già creato la matrice giusta.
2. Hai già identificato le origini e le destinazioni rilevanti.
3. Sapete se il vostro caso può essere caricato manualmente o se un'importazione massiccia è desiderabile.

Per caricare i dati per importazione di massa:

1. Preparare un file CSV con il formato standard GoalBus.
2. Assicurati di includere almeno:
   1. Origini
   2. Destinazioni
   3. Distanze
   4. Slot orari, quando applicato.
   5. Durata
3. In GoalBus, selezionare l'opzione **carico** o **importazione**.
ref: P8_Imagen4.png | compact
4. Scegliere il file CSV.
5. Controllare il **prevalidazione** che rende il sistema.
6. Controllare se il sistema:
   1. rileva errori,
   2. indica quanti record verranno creati.
ref: P8_Imagen5.png |compact
7. Se la convalida è corretta, confermare il carico.
8. Controllare che la griglia sia riempita con i registri attesi.

Se tutto è corretto, l'array verrà visualizzato in modo simile a quello della seguente immagine:
ref: P8_Imagen6.png |full

Per caricare manualmente i dati:

1. Aprire la griglia della matrice.
2. Aggiungi un nuovo record cliccando su **Nuovo rapporto**.
ref: P8_Imagen7.png | compact
3. Definire il **origine**.
4. Definire il **destinazione**.
5. Inserisci il tempo o la distanza corrispondente.
6. Se del caso, definire la fascia oraria.
ref: P8_Imagen8.png | compact(15x)
7. Tieni il registro.
8. Ripetere il processo fino a completare i collegamenti minimi necessari per il vostro caso.

Per il caso di riferimento, inizia con connessioni come queste:

1. Parcheggio nord → Terminale nord
2. Terminal Sud → Parcheggio Nord

Quando si termina questa sezione, si dovrebbe avere una matrice con connessioni reali, o caricato da file o inserito manualmente.

## Differenziare il viaggio vuoto dal viaggio del conducente

Ora è necessario verificare che non si stanno mescolando due logiche diverse. Il documento evidenzia che GoalBus tratta **viaggi vuoti** e **Movimenti del conducente** allo stesso modo nella configurazione, ma con uno scopo commerciale diverso:

1. Il viaggio vuoto utilizza **bus + autista** e modella la logistica di spostare un veicolo dove è necessario.
2. Lo scorrimento utilizza **solo il conducente** e modella quanto tempo una persona ha bisogno per raggiungere un relè o punto di partenza senza flotta in movimento.

Prima di continuare, assicurarsi che:

1. Hai già caricato almeno le connessioni essenziali al tuo caso.
2. È possibile identificare se ogni collegamento corrisponde a un veicolo o a una sola persona.
3. Non hai mescolato entrambe le logiche nella stessa matrice sbagliata.

Per convalidare che ogni matrice rappresenta la risorsa corretta:

1. Controllare una connessione **viaggio vuoto** e confermare che la sua logica risponde a:
   1. spostare un veicolo da un serbatoio o da un parcheggio verso la linea; o
   2. spostare un veicolo tra le linee.
2. Controllare una connessione **spostamento** e confermare che la sua logica risponde a:
   1. spostare un conducente senza veicolo; o
   2. permettere un relè in un terminale o intestazione.
3. Controllare che la matrice di viaggio vuota sta modellando i tempi dipendenti dal traffico.
4. Verificare che la matrice di viaggio del conducente rispecchi la modalità di trasferimento effettiva, come passeggiata, taxi o navetta.
5. Correggere qualsiasi connessione fuori luogo prima di continuare.

Per il caso di riferimento, chiedetevi:

1. Sto modellando qui un autobus che lascia il parcheggio o solo un autista che va in testa?
2. L'ora che ho impostato corrisponde al traffico effettivo o al modo di viaggio del conducente?
3. Il motore utilizzerebbe correttamente queste informazioni quando costruisce il programma e i turni?

Quando si termina questa sezione, si dovrebbe essere chiari quale parte della vostra configurazione appartiene alla logistica del veicolo e quale parte appartiene alla logistica del conducente.

## Verifica che la matrice sia pronta per la programmazione

L'obiettivo finale di questo rapido inizio non è solo quello di riempire un tavolo, ma di preparare una base logistica che Scheduling può consumare. Il documento spiega che una modellazione precisa di queste matrici migliora tre cose:

1. il **trasparenza dei costi**,
2. il **creazione realistica di turni**,
3. e il **Accuratezza dell'ottimizzazione**.

Prima di finire, assicurati che:

1. La matrice corretta esiste.
2. E' associato al tipo di giorno giusto.
3. I collegamenti minimi nel caso sono già caricati.
4. Avete correttamente separato il viaggio vuoto e il viaggio del conducente.

Per convalidare che la matrice è già pronta per il passo successivo:

1. Dai un'occhiata al caso di riferimento che stai costruendo.
2. Conferma che GoalBus sa già:
   1. da dove il veicolo esce fisicamente,
   2. dove entra nella linea,
   3. come torna quando è dovuto,
   4. e come un autista si muoverebbe per un relè se applicato.
3. Chiedetevi se il sistema potrebbe già ridurre al minimo i tempi e le distanze non produttivi in questo caso.
4. Se la risposta è sì, continuare con il prossimo inizio rapido.
5. Se la risposta è no, tornare indietro e aggiungere o correggere le connessioni prima di continuare.

Al momento in cui si termina questa sezione, si dovrebbe essere in grado di affermare che la vostra base logistica è abbastanza realistico per sostenere tempi, servizi e programmazione.

## Letture aggiuntive

- [Definizione dei tipi di veicoli e della flotta autorizzata per linea](P4_Definizione_Dei_Tipi_Di_Veicoli_E_Della_Flotta_Autorizzata_Per_Linea.md)
