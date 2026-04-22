---
title: Creazione dell'offerta di servizio di base con viaggi e orari
shortTitle: Offerta di servizio
intro: Scopri come creare un servizio aziendale, rivedere i tuoi viaggi per linea
  e senso, e lasciare un'offerta valida ed eseguibile prima di passare al programma
  a GoalBus.
contentType: how-tos
versions:
- '*'
---
## Creazione del servizio commerciale che fungerà da container dell'offerta

Prima di rivedere i singoli viaggi, è necessario creare **servizio commerciale** che fungerà da contenitore per la vostra offerta. In GoalBus, i servizi aziendali sono lo strato di governance dell'offerta: collegano linee e percorsi, tipi di giorno e logica di calendario, e viaggi che definiscono il servizio reale. Lo strumento rende chiaro che questa struttura impedisce che gli orari incompleti o non rivisti vengano utilizzati operativamente.

Usa questo avvio rapido quando hai già una rete convalidata, una base temporale definita e devi trasformare questa struttura in un'offerta reale che possa essere convalidata, misurata e consumata in Scheduling.

Prima di iniziare, assicurati che:

1. Hai già impostato tipi di vacanze e giorni in P2.
2. Hai già convalidato l'anno operativo su P3.
3. Avete già preparato la base e la rete operativa a P4 e P5.
4. Avete già definito posti auto, magazzini e viaggi in P6 e P7.
5. Hai già definito i tipi di veicoli ammessi in P8.
6. Hai già creato la versione temporale e i tempi di viaggio su P9.
7. Sei chiaro che linea, che tipo di giorno e che senso userai come caso di riferimento.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Sto per creare il servizio aziendale L1, rivedere i vostri viaggi di ritorno e lasciare l'offerta convalidata prima di passare al programma.**

Per creare il servizio commerciale del vostro caso:

1. In GoalBus, vai alla vista **Servizi**.
ref: P10_Imagen1.png | compact
2. Scopri se c'è già un servizio commerciale adatto al tuo caso.
3. Se il servizio esiste già, aprilo e controlla che corrisponda veramente al tipo di giorno e all'offerta che vuoi preparare.
4. Se non esiste, creane una nuova.
ref: P10_Imagen2.png | compact(2x)
5. Definisce:
   1. Un **nome** chiaro per il servizio,
   2. il **tipo di giorno** da applicare,
   3. Il **righe** che farà parte di quel servizio.
   4. Il servizio **descrizione** se si desidera dare più dettagli, anche se questo campo non è obbligatorio.
6. Risparmia il servizio.
ref: P10_Imagen3.png | compact(x8)
7. Conferma che puoi già inserire la vista del tuo programma o la griglia di viaggio.

Per il caso di riferimento, un'opzione valida potrebbe essere:

- **Giorno lavorativo standard - L1**

È inoltre possibile creare il nuovo servizio a partire dal carico file GTFS. Per farlo:
1. 1. In GoalBus, andare alla vista **Servizi**.
ref: P10_Imagen1.png | compact
2. Importa i file GTFS da **Servizi di importazione**.
ref: P10_Imagen11.png | compact
3. Se non ci sono errori nel caricamento, il servizio sarà stato creato correttamente.
4. Entrando nel servizio, potete vedere tutti i viaggi creati con l'importazione.

Quando si termina questa sezione, si dovrebbe avere un servizio commerciale che agisce come un contenitore strutturato dell'offerta.
ref: P10_Imagen4.png  | full



## Accesso alla griglia di viaggio e cambiamento di contesto

Una volta creato il servizio, il passo successivo è quello di inserire la griglia di viaggio. Questa vista è una torre di controllo centralizzata per tutti i viaggi programmati all'interno del servizio. Da qui è possibile cambiare linea, cambiare servizio e alternare tra **Sentido 1** e **Sentido 2** senza perdere il contesto operativo.

Prima di iniziare questa sezione, assicurarsi che:

1. Hai già creato o convalidato il servizio commerciale.
2. Sai che linea vuoi controllare prima.
3. Sai che senso o direzione userai come punto di partenza.

Per accedere e cambiare il contesto nella griglia di viaggio:

1. Nell'elenco dei servizi, fare clic sull'identificatore del servizio o sull'icona **Visualizza gli orari**.
2. Una volta all'interno, utilizzare il selettore di linea per passare tra le linee incluse nel servizio.
3. Utilizzare il menu a discesa del servizio se si desidera confrontare con un altro servizio commerciale.
4. Passare tra **Sentido 1** e **Sentido 2** per rivedere separatamente i viaggi andata e ritorno.
5. Mantenere l'attenzione su una singola linea e un senso durante la costruzione del vostro caso base.

Per il caso di riferimento:

1. Aprire il servizio **Giorno lavorativo standard - L1**.
2. Inserisci prima **Sentido 1**.
3. Controllare **Sentido 2** più tardi.
ref: P10_Imagen5.png  | full

Quando si termina questa sezione, si dovrebbe essere in grado di navigare l'offerta senza perdere il contesto di linea, servizio e indirizzo.

## Creazione o revisione di viaggi di servizio

Ora sì, inserisci il dettaglio del **viaggi**. Il documento spiega che un programma è una sequenza di eventi e che ogni viaggio deve essere collegato a:

1. una variazione specifica della rotta,
2. una sequenza di fermate,
3. e un riferimento temporaneo.

Questo garantisce che uscite e arrivi siano fisicamente eseguibili. Inoltre, la griglia mostra di default solo le fermate principali o i punti di tempo per mantenere una vista chiara, anche se è possibile ingrandire per vedere tutti gli intermedi.

Prima di iniziare questa sezione, assicurarsi che:

1. Avete già una versione oraria valida in P9.
2. Sapete che variazione di percorso corrisponde al viaggio che volete creare o rivedere.
3. Sai che linea e che senso stai modificando.

Per creare o rivedere viaggi di servizio:

1. All'interno del servizio, selezionare una linea e un senso.
2. Controlla i viaggi che esistono già nella griglia.
3. Se è necessario creare un nuovo viaggio, utilizzare l'azione corrispondente per aggiungere una nuova uscita.
ref: P10_Imagen9.png | compact
4. Assegna il viaggio:
   1. il corretto **percorso o variazione**,
   2. il **ora di partenza**,
   3. e il **riferimento temporaneo** coerente con la versione creata in P9.
ref: P10_Image10.png
5. Se il viaggio esiste già, passa il cursore sul tuo identificatore per verificare quale variazione di percorso stai usando.
6. Verificare che la durata totale calcolata abbia senso rispetto ai tempi di viaggio definiti.
7. Espandi la sequenza se hai bisogno di controllare tutte le fermate intermedie.
8. Ripetere il processo fino ad avere una base minima di viaggi per senso.

Per il caso di riferimento, si può iniziare con una struttura minima come questa:

1. L1 - Sentido 1
   1. Viaggio 1: partenza 06:00
   2. Viaggio 2: uscita 06:20
2. L1 - Sentido 2
   1. Viaggio 1: uscita 06:10
   2. Viaggio 2: partenza 06:30

Quando si conclude questa sezione, si dovrebbe avere un'offerta di viaggio di base già collegato alla rotta, senso, e riferimento temporale.

## Intervalli di revisione, durata totale e bilancia delle forniture

Dopo aver creato o riesaminato i viaggi, è necessario verificare che l'offerta ha senso nel suo complesso. La griglia permette di tenere d'occhio:

1. il **durata totale** per ogni viaggio,
2. il **intervallo** rispetto al viaggio precedente,
3. KPI globali per linea, come il numero di viaggi, la distanza totale e il tempo totale di guida. Ciò permette di valutare se l'offerta è equilibrata, simmetrica e economicamente redditizia.

Prima di continuare, assicurarsi che:

1. Avete già almeno alcuni viaggi creati o rivisti.
2. Potete già vedere la lunghezza totale di quei viaggi.
3. È già possibile confrontare i sensi e le frequenze.

Per convalidare il saldo dell'offerta:

1. Nella griglia, controllare il **durata totale** per ogni viaggio.
2. Verificare che corrisponda ragionevolmente ai tempi di viaggio attesi.
3. Controllare il **intervallo** rispetto al percorso precedente e vedere se ci sono lacune eccessive o uscite troppo vicine insieme.
4. Confronta il numero di viaggi **Sentido 1** con **Sentido 2**.
5. Controlla i KPI globali della linea:
   1. **Conto di viaggio**,
   2. **Distanza totale**,
   3. **Tempo totale**.
ref: P10_Imagen6.png | compact
6. Corregge ogni ovvio squilibrio prima di dare il servizio pronto.

Per il caso di riferimento, chiedetevi:

1. Il viaggio andata e ritorno è equilibrato?
2. Gli intervalli di viaggio corrispondono al livello di offerta che si desidera costruire?
3. La durata totale di ogni viaggio è coerente con il riferimento temporale?
4. L'offerta sembra economicamente ragionevole o è sovradimensionata?

Quando si conclude questa sezione, si dovrebbe avere un'offerta non solo creata, ma anche rivisto dal punto di vista della frequenza, durata e equilibrio.

## Convalida del servizio per lasciarlo pronto per il calcolo

L'ultimo passo è il servizio **convalida**. La validazione blocca i dati di viaggio e lo consente per la programmazione, mentre un servizio non validato è ancora in fase di editing e non è pronto per il calcolo. Indica inoltre che un servizio convalidato diventa limitato per la editing, cessa di essere rimovibile ed è pronto per l'uso di programmazione.

Prima di finire, assicurati che:

1. Hai già controllato i viaggi di servizio.
2. Hai già controllato percorsi, durate e intervalli.
3. Hai già confermato che l'offerta risponde al caso che vuoi costruire.

Per convalidare il servizio e lasciarlo pronto per la programmazione:

1. Controlla la griglia di viaggio del servizio per l'ultima volta.
2. Conferma che non hai più bisogno di modificare il servizio.
3. Eseguire l'azione **Convalida** sul servizio o sul corrispondente set di viaggi.
ref: P10_Imagen7.png | full
4. Controllare che lo stato del servizio cambia a **Convalida**.
ref: P10_Imagen8.png | compact(2x)
5. Conferma che:
   1. il viaggio è bloccato per cambiamenti accidentali,
   2. il servizio è ora **pronto per il calcolo**,
   3. e Scheduling può leggerlo nei prossimi passi.
6. Se hai ancora bisogno di apportare modifiche, usa la logica **Non convalida** solo per restituire il servizio all'editing e finire di regolarlo prima di validarlo di nuovo.

Per il caso di riferimento, non continuare a pianificare fino a quando non è possibile dichiarare:

1. Linea L1 ha una consistente offerta praticabile.
2. I viaggi sono associati alla corretta variazione del percorso.
3. La durata totale e gli intervalli hanno senso.
4. Il servizio è già in stato **Convalida**.

Quando si conclude questa sezione, si dovrebbe avere un'offerta aziendale già strutturata, rivisto e convalidato pronto per il programma di consumo.

## Letture aggiuntive

- [Convalida della struttura operativa: magazzini, unità e gruppi](P11_Convalida_Della_Struttura_Operativa_E_Dello_Stato_Del_Servizio.md)
