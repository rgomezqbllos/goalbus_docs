---
title: Pubblicazione dello scenario in date specifiche
shortTitle: Pubblicare lo scenario
intro: Scopri come pubblicare uno scenario convalidato su date specifiche, controllare
  la soluzione che entra in funzione e mantenere la tracciabilità tra pianificazione,
  convalida e implementazione operativa.
contentType: how-tos
versions:
- '*'
---
## Preparazione dello scenario convalidato prima della pubblicazione

Dopo il calcolo e la validazione di una soluzione, il passo successivo è quello di decidere che **quando** deve entrare in vigore nell'operazione effettiva. Pubblicare uno scenario non è solo approvarla: si tratta di inserire quella soluzione validata nel calendario operativo per una data specifica, senza confonderla con una bozza o una versione ancora in revisione.

Usa questo avvio rapido quando hai già una fase con una soluzione in stato **Convalida** e devi portarla al funzionamento per un periodo specifico.

Prima di iniziare, assicurati che:
1. Hai già eseguito e convalidato lo scenario su P15.
2. La soluzione di scenario che si desidera pubblicare è in stato **Convalida**.
3. Sai che date esatte vuoi coprire.
4. È chiaro che la pubblicazione cambia lo stato operativo della soluzione e la rende visibile come una versione impianto.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Pubblicherò lo scenario convalidato della linea L1 in modo che entri in vigore durante uno specifico periodo di lavoro senza incidere sulle soluzioni che non corrispondono a tali date.**

Preparare la pubblicazione dello scenario:
1. Aprire il modulo **Scenari di pianificazione**.
2. Trova lo scenario che hai già convalidato.
3. Controllare che lo stato attuale della soluzione sia **Convalida**.
4. Controllare il nome del palcoscenico, le righe incluse, il tipo di giorno e la descrizione.
5. Conferma che stai per pubblicare esattamente la soluzione giusta.
6. Se lo scenario non è ancora convalidato, tornare indietro e finire P15 prima di continuare.
7. Se lo scenario è corretto, continuare con la pubblicazione.

Quando si conclude questa sezione, si dovrebbe avere chiaramente identificato lo scenario convalidato che si desidera implementare.

## Selezionare la finestra di pubblicazione temporanea

Una volta confermato lo scenario, è necessario decidere che **in cui date** si applicherà. La pubblicazione non dovrebbe essere fatta in modo ambiguo. Dovrebbe essere chiaro da quando e fino a quando la soluzione sarà di riferimento operativo.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già confermato quale scenario hai intenzione di pubblicare.
2. Sapete se la pubblicazione copre un giorno, una settimana, un intervallo continuo o un blocco operativo più lungo.
3. Siete già chiari che il periodo scelto non dovrebbe contraddire il tipo di giorno e la logica temporale dello scenario.

Per selezionare la finestra di pubblicazione temporanea:
1. Dallo scenario convalidato, aprire l'azione **Pubblica**.
ref: P16_Imagen1.png | compact
2. Nel modulo di pubblicazione si definisce **Intervallo delle date**.
3. Aggiungere un altro **Intervallo delle date**, se lo considerate e pubblicare per altri giorni non selezionati (facoltativo).
ref: P16_Imagen2.png | compact(x12)
4. Controllare che le date abbiano senso per:
   1. il ragazzo del giorno di scena,
   2. la linea o le linee coinvolte,
   3. E la vera finestra operativa che vuoi coprire.
5. Conferma che non stai lasciando una gamma troppo ampia per errore.
6. Se lo scenario deve essere applicato solo in un breve periodo, limita la finestra con precisione.
7. Conferma la pubblicazione per la/i data/i scelta/i intervallo/i.

Per il caso di riferimento, chiedetevi:
1. La pubblicazione copre esattamente i giorni lavorativi che voglio attuare?
2. Sto evitando di pubblicare più giorni di quanto sia necessario?
3. La soluzione corrisponde davvero alle date selezionate?

Quando si conclude questa sezione, si dovrebbe avere una finestra di tempo chiara e controllata definita per l'impianto.

## Conferma della pubblicazione e modifica dello stato dello scenario

Dopo aver selezionato l'intervallo temporale, è necessario confermare l'azione di pubblicazione. A questo punto, la soluzione cessa di essere solo uno scenario convalidato e diventa operativa all'interno del calendario.

Prima di continuare, assicurarsi che:
1. Hai già selezionato correttamente le date.
2. Hai già controllato lo scenario convalidato.
3. Siete già pronti per la soluzione di avanzare nel suo ciclo di vita.

Pubblicare lo scenario:
1. Rivedere la sintesi della pubblicazione per l'ultima volta.
2. Conferma:
   1. il nome del palcoscenico,
   2. l'intervallo temporale,
   3. e il contesto operativo al quale si applicherà.
3. Eseguire l'azione **Pubblica**.
4. Controllare che lo stato dello stadio cambi a **Pubblicazione** mentre il sistema lavora l'impianto.
5. Aspetta che il processo sia finito.
6. Controllare che lo stato finale della soluzione cambi a **Pubblicato**.
ref: P16_Imagen3.png | compact
7. Se lo stato non cambia come previsto, controllare se c'è stata un'incidenza tecnica o un problema di ammissibilità scenario.

Per il caso di riferimento, non chiudere la pubblicazione fino a quando non si può dichiarare:
1. La soluzione di scenario L1 è già uscito da **Convalida**.
2. La piattaforma ha elaborato la pubblicazione.
3. La soluzione di stato finale è **Pubblicato**.

Quando si conclude questa sezione, si dovrebbe avere uno scenario già impiantato nel calendario operativo per il periodo selezionato.

## Verifica che la soluzione pubblicata sia quella in vigore

Dopo la pubblicazione, è necessario verificare che la soluzione attiva sia realmente quella giusta. La pubblicazione non dovrebbe essere un passo cieco. È necessario essere in grado di verificare quale scenario era valido per le date scelte e mantenere la tracciabilità sulla soluzione implementata.

Prima di iniziare questa sezione, assicurarsi che:
1. La soluzione scenario ha già raggiunto lo stato **Pubblicato**.
2. Sai che date copre.
3. Sapete quale servizio o linea dovrebbe essere influenzato dalla pubblicazione.

Per verificare l'attuazione della soluzione:
1. Torna alla tabella degli scenari principali.
2. Filtrare o rivedere gli scenari per stato.
3. Conferma che la soluzione dello scenario pubblicato appare come **Pubblicato**.
4. Controlla le date della tua applicazione, se la vista lo permette.
5. Controllate che non state confondendo questo scenario con un altro convalidato ma non impiantato.
6. Se il processo interno lo richiede, registrati o comunica che questa versione è già la soluzione operativa corrente.
7. Essa conserva il nome, la descrizione e l'intervallo temporale come base di tracciabilità per il successivo audit.

Per il caso di riferimento, assicurarsi che:
1. Lo scenario pubblicato corrisponde a L1 utilizzabile.
2. Le date corrispondono al periodo che hai voluto implementare.
3. Nessun altro scenario è stato attivato per errore.

Quando si conclude questa sezione, si dovrebbe essere sicuri di quale soluzione era in atto e per quale periodo esatto.

## Mantenere la tracciabilità e preparare la prossima iterazione

Una volta pubblicato lo scenario, il lavoro non scompare: cambia il focus. Da qui, la soluzione implementata può diventare un riferimento per audit, confronto o iterazione futura. Non è consigliabile riutilizzare senza controllo uno scenario già pubblicato per subire cambiamenti strutturali; la cosa più sicura è creare una nuova iterazione quando è necessario proporre un miglioramento o una variante.

Prima di finire, assicurati che:
1. Lo scenario è già pubblicato.
2. È chiaro che intervallo di tempo copre.
3. Sapete se la prossima cosa sara' controllare i risultati o preparare una nuova iterazione.

Per mantenere la tracciabilità dopo la pubblicazione:
1. Conserva lo scenario pubblicato con un nome e una descrizione sufficientemente chiari.
2. Utilizzare lo stato **Pubblicato** come riferimento per distinguerlo dagli scenari in bozza, calcolo o convalida.
3. Se avete bisogno di proporre un miglioramento, creare un nuovo scenario invece di alterare la logica storica dello scenario impiantato.
4. Se il tuo team lavora con una revisione successiva, usa questa versione pubblicata come confronto di base.
5. Tenere un registro interno di:
   1. ciò che è stato pubblicato,
   2. quando è stato pubblicato,
   3. e per quali date era valido.

Per il caso di riferimento, finite questo avvio rapido solo quando potete dire:
1. La soluzione L1 è già stata pubblicata.
2. Lo sai esattamente quando e' entrato in vigore.
3. È possibile distinguere questa versione pubblicata da qualsiasi iterazione futura.

Quando si conclude questa sezione, si dovrebbe avere una soluzione pubblicata, tracciabile e pronta per servire come riferimento operativo o come punto di partenza per una nuova iterazione.

## Letture aggiuntive

- [Creazione di una nuova iterazione dello scenario da una soluzione pubblicata](iteracion-del-escenario)
