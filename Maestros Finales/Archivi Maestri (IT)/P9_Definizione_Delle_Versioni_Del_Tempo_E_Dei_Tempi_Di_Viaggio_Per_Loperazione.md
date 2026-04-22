---
title: Definizione delle versioni del tempo e dei tempi di viaggio per l'operazione
shortTitle: Versioni e tempi
intro: Scopri come creare versioni orarie, definire orari di viaggio e permanenza
  per tipo di giorno e slot orario, e lasciare un riferimento di tempo affidabile
  prima di creare o adeguare i servizi in GoalBus.
contentType: how-tos
versions:
- '*'
---
## Creazione della versione del tempo che il vostro caso userà

Prima di definire i tempi di viaggio, è necessario creare un **Versione oraria**. In GoalBus, una versione non è solo un tag: è la libreria del tempo che raggruppa la logica del tempo che si applica a percorsi specifici e tipi di giorno specifici. Questo è importante perché il lunedì mattina non si comporta come una domenica mattina, e il sistema non dovrebbe riutilizzare un solo insieme di tempi per tutto l'anno.

Utilizza questo avvio rapido quando hai già una linea e le sue rotte definite, e devi costruire la base temporale che verrà poi utilizzata per calcolare il viaggio, convalidare le durate e confrontare le deviazioni con lo standard.

Prima di iniziare, assicurati che:
1. Hai già preparato il master network al P6.
2. Hai già controllato la rete operativa a P7.
3. Hai già impostato la base temporale dei tipi di giorno a P2.
4. Hai già convalidato l'anno operativo su P3.
5. Sai che linea, che rotte e che tipo di giorno userai come riferimento.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Creerò una versione oraria per la linea L1 nei giorni lavorativi e la userò come riferimento temporaneo prima di creare o adeguare i servizi.**

Per creare la versione oraria del vostro caso:
1. In GoalBus, apri il **Vista percorsi** della linea che userai come riferimento.
2. Selezionare l'icona o l'opzione **Gestione degli orari di viaggio e di sosta**.
ref: P9_Imagen1.png | compact
3. Nella parte superiore della vista, creare una nuova versione selezionando **Nuovi orari**.
ref: P9_Imagen2.png | compact
4. Definisce un **nome** chiaro per la versione.
5. Aggiungere un **descrizione** per aiutarti a distinguere il contesto operativo.
6. Selezionare **tipi di giorno** a cui si applica tale versione, ad esempio **Giorni lavorativi**.
7. Collega la **variazioni di rotta** o sequenze specifiche che faranno parte di quella versione temporanea.
8. Salva la versione.
ref: P9_Imagen3.png | compact(x8)
9. Verificare che la versione sia già disponibile come riferimento temporaneo per quella linea.

Per il caso di riferimento, una versione valida potrebbe essere chiamata:
- **Giorni lavorativi d'inverno**
- **Base di lavoro L1**

Quando si conclude questa sezione, si dovrebbe aver creato una versione temporale che il sistema può utilizzare come riferimento temporaneo per i servizi di quella linea simile a quello dell'immagine sottostante.
ref: P9_Imagen4.png | full

## Definizione dei tempi di viaggio tra le fermate principali

Dopo aver creato la versione, è necessario inserire il **durata del viaggio**. In GoalBus, questi tempi sono principalmente definiti tra **Ferme principali** o **punti temporali**, non tra tutte le fermate intermedie. Le intestazioni sono le principali per default, e da lì si costruisce la logica temporanea che poi alimenterà i servizi.

Inoltre, GoalBus non funziona con un solo valore per segmento. Il motore utilizza una logica **minimo, ottimale e massimo** per dare flessibilità di controllo al calcolo:
1. **Minimo**: il tempo più veloce possibile.
2. **Ottima**: il tempo di destinazione a cui il motore sarà impostato.
3. **Massimo**: il tempo più lento accettabile.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già creato la versione oraria.
2. Sai quali fermate principali userai come riferimento.
3. Hai già identificato prima la direzione che vuoi configurare.

Per definire i tempi di viaggio del vostro caso:
1. All'interno della griglia temporale, selezionare **segmento** tra due fermate principali.
ref: P9_Imagen5.png | full
2. Crea uno o più **slots** per riflettere la realtà operativa.
3. Per ogni striscia, inserire:
   1. l'ora **minimo**,
   2. l'ora **ottimale**,
   3. tempo **massimo**.
ref: P9_Imagen6.png | compact
4. Risparmia il segmento.
5. Ripetere il processo per il prossimo segmento principale.
6. Quando si termina un senso, ripetere la stessa logica per il senso opposto.

Le strisce create non dovrebbero avere lacune o sovrapposizioni tra loro. In caso ci fosse, non sarà possibile salvare i tempi.

Per il caso di riferimento, una logica di base potrebbe essere:
1. **Terminale Nord → Centro**
   1. 07:00–09:00
      1. Minimo: 12 min
      2. Ottima: 15 min
      3. Massimo: 18 min
   2. 09:00-22:00
      1. Minimo: 5 min
      2. Ottima: 5 min
      3. Massimo: 5 min
   3. 22:00–06:00
      1. Minimo: 8 min
      2. Ottima: 10 min
      3. Massimo: 12 min
2. **Centro → Ospedale**
3. **Ospedale → Università**
4. **Università → Terminal Sud**

Quando si termina questa sezione, si dovrebbe avere definito tempi di guida elastico tra i principali punti temporali del percorso.

## Definizione dei tempi di ritenzione per la regolazione e il recupero

Oltre al tempo di guida, GoalBus deve sapere quanto tempo un veicolo può rimanere in una fermata principale. Questi **Periodi di scala** sono importanti perché permettono di regolare l'uscita, assorbire gli arrivi anticipati e lasciare spazio per il recupero nei terminali o punti di connessione.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già definito i tempi di viaggio tra i segmenti principali.
2. Sapete quali terminali o punti importanti devono essere regolamentati.
3. Avete già identificato dove è necessario un vero spazio operativo.

Per definire i tempi di scala:
1. Nella griglia temporale, selezionare **colonna** da una fermata principale.
ref: P9_Imagen7.png | full
2. Scegliere un importante terminale, intestazione o punto di connessione.
3. Definisce:
   1. **Minimo**, come tempo di attesa obbligatorio.
   2. **Massimo**, come margine consentito per la regolazione o sincronizzazione.
4. Salva le impostazioni.
5. Ripetere il processo per altre fermate principali dove è necessario controllare la permanenza.

Per il caso di riferimento, una possibile logica sarebbe:
1. **Terminale nord**
   1. Minimo: 4 min
   2. Massimo: 10 min
2. **Terminale Sud**
   1. Minimo: 5 min
   2. Massimo: 12 min

Quando si termina questa sezione, si dovrebbe avere definito i margini che il motore può utilizzare per recuperare o regolare senza deformare la logica del programma.

## Controllo delle slot, vista estesa e coerenza visiva

Una volta che avete già viaggi e periodi di permanenza, è necessario controllare se la griglia riflette una logica realistica. Il documento evidenzia che GoalBus include gli ausili visivi per rilevare errori quando si gestiscono molti punti di dati, molte strisce, o percorsi multipli.

Prima di continuare, assicurarsi che:
1. Hai organizzato almeno una slot.
2. Hai già introdotto valori minimi, ottimali e massimi.
3. Hai già aggiunto tempi di ritenzione ai punti rilevanti.

Per rivedere visivamente la coerenza della configurazione:
1. Controllare la griglia e confermare che ogni segmento principale ha un periodo di tempo valido.
2. Utilizzare gli ausili visivi disponibili per rilevare valori anormali.
3. Controllare se le ore di punta mostrano tempi superiori alle ore di valle.
4. Espandi la vista se hai bisogno di vedere più dettaglio o più fermate intermedie.
5. Corregge qualsiasi valore anomalo direttamente dalla vista o dal pannello di editing.
6. Ripetere la revisione fino a quando la logica temporale rispecchia un'operazione credibile.

Per il caso di riferimento, chiedetevi:
1. L'ora di punta si presenta con tempi più alti della notte?
2. I tempi minimi, ottimali e massimi hanno una relazione logica?
3. I terminali hanno uno spazio regolamentare realistico?
4. La griglia rappresenta già una giornata lavorativa completa?

Quando si conclude questa sezione, si dovrebbe avere una base temporale visivamente rivisto senza grandi incongruenze.

## Applicazione della versione oraria come riferimento per i servizi

L'obiettivo finale di questo avvio rapido non è solo creare dati temporanei, ma lasciare un riferimento che può essere utilizzato per creare o modificare servizi. Il documento indica che ogni viaggio deve essere misurato con un **Versione di riferimento temporanea**, e che questo riferimento viene utilizzato automaticamente quando si creano nuovi viaggi o cambiano la rotta di un viaggio. Permette anche di rilevare deviazioni se un viaggio è stato importato o modificato al di fuori dello standard.

Prima di finire, assicurati che:
1. Hai già creato una versione temporanea valida.
2. Hai già definito i tempi di viaggio e di soggiorno.
3. Hai già controllato la consistenza della griglia.
4. Sai che linea e caso userai per creare servizi.

Per verificare che la vostra base temporanea sia pronta per i servizi:
1. Controlla la versione del tempo che hai appena creato.
2. Conferma che è collegato al tipo corretto di giorno.
3. Conferma che include i percorsi o le variazioni che usi.
4. Verifica che tale versione possa già fungere da riferimento temporaneo per:
   1. creare nuovi viaggi,
   2. ricalcolare gli orari di arrivo e di partenza,
   3. le discrepanze di audit rispetto alla norma.
5. Se la risposta è sì, continuare con il prossimo inizio rapido.
6. Se la risposta è no, tornare indietro e correggere la versione o i suoi tempi prima di continuare.

Quando si conclude questa sezione, si dovrebbe essere in grado di dire che la linea ha già una versione oraria di riferimento sufficiente a creare servizi in modo coerente.

## Letture aggiuntive

- [Creazione dell'offerta di servizio di base: viaggi o gruppi di servizio per linea, percorso e significato](P10_Creazione_Dellofferta_Di_Servizio_Di_Base_Con_Viaggi_E_Orari.md)
