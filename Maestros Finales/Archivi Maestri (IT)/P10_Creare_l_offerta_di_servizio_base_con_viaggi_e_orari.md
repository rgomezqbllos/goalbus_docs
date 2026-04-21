---
title: Creare l’offerta di servizio base con viaggi e orari
shortTitle: Offerta di servizio
intro: "Scopri come creare un servizio commerciale, rivedere i suoi trips per linea e direzione e lasciare un’offerta validata ed eseguibile prima di passare a Scheduling in GoalBus."
contentType: how-tos
versions:
  - "*"
---

## Creare il servizio commerciale che conterrà l’offerta

Prima di rivedere i singoli trips, devi creare il **commercial service** che fungerà da contenitore per la tua offerta. In GoalBus, i commercial services sono il livello di governance dell’offerta: collegano lines e routes, tipi di giorno e logica di calendario, e i trips che definiscono il servizio reale. Questa struttura aiuta a evitare che timetables incompleti o non revisionati vengano usati operativamente.

Usa questo quick start quando hai già una rete validata, una base tempi definita e devi trasformare quella struttura in un’offerta reale che possa essere validata, misurata e consumata in Scheduling.

Prima di iniziare, assicurati che:
1. Tu abbia già configurato tipi di giorno e festività in P2.
2. Tu abbia già validato l’anno operativo in P3.
3. Tu abbia già preparato le reti master e operativa in P6 e P7.
4. Tu abbia già preparato parkings e depots in P5.
5. Tu abbia già definito gli allowed vehicle types in P4.
6. Tu abbia già caricato deadhead trips e driver repositioning in P8.
7. Tu abbia già creato la time version e i travel times in P9.
8. Tu sappia quale linea, tipo di giorno e direzione userai come caso di riferimento.

Per questo quick start, usa questo caso di riferimento:

> **Creerò il commercial service feriale per la linea L1, rivedrò i suoi trips di andata e ritorno e lascerò l’offerta validata prima di passare a Scheduling.**

Per creare il commercial service per il tuo caso:
1. In GoalBus, vai alla vista **Services**.
ref: P10_Imagen1.png | compact
2. Verifica se esiste già un commercial service adatto al tuo caso.
3. Se esiste, aprilo e conferma che corrisponda davvero al tipo di giorno e all’offerta che vuoi preparare.
4. Se non esiste, creane uno nuovo.
ref: P10_Imagen2.png | compact
5. Definisci:
   1. un **name** chiaro per il servizio,
   2. il **day type** applicabile,
   3. le **lines** incluse in quel servizio,
   4. la **description** se vuoi fornire più dettaglio (opzionale).
6. Salva il servizio.
ref: P10_Imagen3.png | compact
7. Conferma di poter entrare nella sua vista timetable o nella trip grid.

Per il caso di riferimento, un’opzione valida potrebbe essere:
- **Standard workday - L1**

È anche possibile creare il nuovo servizio importando file GTFS. Per farlo:
1. In GoalBus, vai alla vista **Services**.
ref: P10_Imagen1.png | compact
2. Importa i file GTFS tramite **Import services**.
ref: P10_Imagen11.png | compact
3. Se non ci sono errori di upload, il servizio verrà creato correttamente.
4. Apri il servizio per vedere tutti i trips creati dall’import.

Quando termini questa sezione, dovresti avere un commercial service che agisce come contenitore strutturato dell’offerta.
ref: P10_Imagen4.png  | full

## Accedere alla trip grid e cambiare contesto

Una volta creato il servizio, il passo successivo è aprire la trip grid. Questa vista è una “control tower” centrale per tutti i trips pianificati nel servizio. Da qui puoi cambiare linea, cambiare servizio e alternare tra **Direction 1** e **Direction 2** senza perdere il contesto operativo.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già creato o validato il commercial service.
2. Tu sappia quale linea vuoi rivedere per prima.
3. Tu sappia quale direzione userai come punto di partenza.

Per accedere e cambiare contesto nella trip grid:
1. Nell’elenco servizi, fai clic sull’identificatore del servizio o sull’icona **View timetables**.
2. Usa il selettore di linea per passare tra le lines incluse nel servizio.
3. Usa il menu a tendina dei servizi se vuoi confrontare con un altro commercial service.
4. Alterna tra **Direction 1** e **Direction 2** per rivedere separatamente trips di andata e ritorno.
5. Mantieni il focus su una linea e una direzione mentre costruisci il tuo caso base.

Per il caso di riferimento:
1. Apri **Standard workday - L1**.
2. Inizia con **Direction 1**.
3. Poi rivedi **Direction 2**.
ref: P10_Imagen5.png  | full

Quando termini questa sezione, dovresti essere in grado di navigare l’offerta senza perdere contesto di linea, servizio e direzione.

## Creare o rivedere i trips del servizio

Ora entra nei dettagli dei trips. Un timetable è una sequenza di eventi e ogni trip dovrebbe essere collegato a:
1. una specifica route variation,
2. una stop sequence,
3. e un riferimento tempi.

Questo garantisce che partenze e arrivi siano fisicamente eseguibili. La grid mostra solo key stops/time points per default per mantenere una vista chiara, ma puoi espandere la vista per vedere tutte le fermate intermedie.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia una time version valida in P9.
2. Tu sappia quale route variation corrisponde al trip che vuoi creare o rivedere.
3. Tu sappia quale linea e direzione stai modificando.

Per creare o rivedere i trips del servizio:
1. All’interno del servizio, seleziona una linea e una direzione.
2. Rivedi i trips già presenti nella grid.
3. Se devi creare un nuovo trip, usa l’azione per aggiungere una nuova partenza.
ref: P10_Imagen9.png | compact
4. Assegna al trip:
   1. la corretta **route/variation**,
   2. il **departure time**,
   3. e un **time reference** coerente con la versione creata in P9.
   ref: P10_Imagen10.png
5. Se il trip esiste già, passa sopra il suo identificatore per verificare quale route variation usa.
6. Conferma che la durata totale calcolata abbia senso rispetto ai travel times definiti.
7. Espandi la sequenza se devi rivedere tutte le fermate intermedie.
8. Ripeti finché hai una base minima di trips per direzione.

Per il caso di riferimento, puoi iniziare con una struttura minimale come:
1. L1 - Direction 1
   1. Trip 1: departure 06:00
   2. Trip 2: departure 06:20
2. L1 - Direction 2
   1. Trip 1: departure 06:10
   2. Trip 2: departure 06:30

Quando termini questa sezione, dovresti avere un’offerta base di trips già collegata a route, direzione e riferimento tempi.

## Rivedere headways, durata totale e bilanciamento dell’offerta

Dopo aver creato o rivisto i trips, devi verificare che l’offerta abbia senso come insieme. La grid ti permette di monitorare continuamente:
1. la **total duration** di ogni trip,
2. la **headway** rispetto al trip precedente,
3. e KPI globali per linea come numero di trips, distanza totale e tempo totale di guida.

Questo ti aiuta a valutare se l’offerta è bilanciata, simmetrica ed economicamente ragionevole.

Prima di continuare, assicurati che:
1. Tu abbia almeno alcuni trips creati o rivisti.
2. Tu possa vedere la loro durata totale.
3. Tu possa confrontare direzioni e frequenze.

Per validare il bilanciamento dell’offerta:
1. Nella grid, rivedi la **total duration** di ciascun trip.
2. Conferma che corrisponda ragionevolmente ai travel times attesi.
3. Rivedi la **headway** rispetto al trip precedente e individua gap eccessivi o partenze troppo ravvicinate.
4. Confronta il numero di trips in **Direction 1** rispetto a **Direction 2**.
5. Rivedi i KPI globali della linea:
   1. **Trip count**,
   2. **Total distance**,
   3. **Total time**.
ref: P10_Imagen6.png | compact
6. Correggi eventuali sbilanciamenti evidenti prima di considerare pronto il servizio.

Per il caso di riferimento, chiediti:
1. Andata e ritorno sono bilanciati?
2. Le headways corrispondono al livello di servizio che vuoi costruire?
3. La durata totale di ogni trip è coerente con il riferimento tempi?
4. L’offerta sembra economicamente ragionevole o è sovradimensionata?

Quando termini questa sezione, dovresti avere un’offerta non solo creata, ma anche rivista dal punto di vista di frequenza, durata e bilanciamento.

## Validare il servizio in modo che sia pronto per il calcolo

L’ultimo passo è **validare** il servizio. La validazione blocca i dati dei trips e abilita il servizio per lo scheduling, mentre un servizio non validato resta in editing e non è pronto per il calcolo. Un servizio validato diventa più restrittivo in editing, non può più essere eliminato ed è pronto per l’uso nello scheduling.

Prima di concludere, assicurati che:
1. Tu abbia già rivisto i trips del servizio.
2. Tu abbia già verificato routes, durate e headways.
3. Tu abbia già confermato che l’offerta corrisponda al caso che vuoi costruire.

Per validare il servizio e lasciarlo pronto per Scheduling:
1. Rivedi la trip grid un’ultima volta.
2. Conferma che non ti serva continuare a modificare il servizio.
3. Esegui l’azione **Validate** sul servizio (o sul set di trips rilevante).
ref: P10_Imagen7.png | full
4. Conferma che lo stato del servizio cambi in **Validated**.
ref: P10_Imagen8.png | compact
5. Conferma che:
   1. i trips siano bloccati contro modifiche accidentali,
   2. il servizio sia ora **ready for calculation**,
   3. Scheduling possa leggerlo nei passaggi successivi.
6. Se hai ancora bisogno di modifiche, usa **Unvalidate** solo per riportare il servizio in editing, completare gli aggiustamenti e validare di nuovo.

Per il caso di riferimento, non continuare con Scheduling finché puoi affermare:
1. La linea L1 ha un’offerta feriale coerente.
2. I trips sono collegati alla route variation corretta.
3. Durata totale e headways hanno senso.
4. Il servizio è in stato **Validated**.

Quando termini questa sezione, dovresti avere un’offerta commerciale strutturata, revisionata e validata, pronta perché Scheduling la consumi.

## Additional reading

- [Validare struttura operativa e stato del servizio](P11_Validare_struttura_operativa_e_stato_del_servizio.md)

