---
title: Caricare i viaggi a vuoto e i riposizionamenti
shortTitle: Deadhead trips
intro: "Scopri come configurare matrici di deadhead trips e driver repositioning in modo che GoalBus usi tempi logistici realistici, minimizzi costi non produttivi e costruisca orari e turni più realistici."
contentType: how-tos
versions:
  - "*"
---

## Creare la matrice corretta per il tipo di giorno corretto

Prima di calcolare Scheduling, devi definire come l’operatività si muove fisicamente quando non genera ricavi. In GoalBus, questo modulo copre due aspetti diversi:

1. **Deadhead trips**, che rappresentano un bus con un autista che si muove tra depot, parking, inizio linea o tra linee.
2. **Driver repositioning**, che rappresenta l’autista che si muove senza veicolo, ad esempio a piedi, in taxi o con navetta.

GoalBus non tratta questi movimenti come un unico elenco fisso. Lo strumento rende chiaro che devono essere organizzati in **matrici per tipo di giorno**, perché il traffico cambia a seconda del contesto operativo. Una connessione può richiedere 15 minuti di domenica e 45 minuti di lunedì mattina, quindi lo stesso collegamento non dovrebbe riutilizzare sempre lo stesso tempo.

Usa questo quick start quando hai già configurato parkings e depots e devi preparare la “logistica invisibile” che rende possibile una pianificazione realistica.

Prima di iniziare, assicurati che:
1. Tu abbia già preparato parkings e depots in P5.
2. Tu sappia quale linea o servizio userai come riferimento.
3. Tu sappia quale tipo di giorno stai modellando.
4. Tu capisca la differenza tra deadhead trip e driver repositioning.

Per questo quick start, usa questo caso di riferimento:

> **Preparerò la matrice di deadhead trips per un giorno feriale sulla linea L1, collegando North Parking a North Terminal, e anche la matrice di driver repositioning quando necessario per i relief.**

Per creare la matrice corretta per il tuo caso:
1. In GoalBus, apri il modulo **deadhead trips and repositioning**.
ref: P8_Imagen1.png | full
2. Decidi prima se creerai una matrice **deadhead trips**, una matrice **driver repositioning** o entrambe.
3. Fai clic su **Create new**.
ref: P8_Imagen2.png | compact
4. Inserisci un **name** chiaro per la matrice.
5. Aggiungi una **description** che ti aiuti a riconoscere il contesto operativo.
6. Assegna i **day types** a cui si applicherà questa matrice.
7. Salva la matrice.
ref: P8_Imagen3.png | compact
8. Conferma che la matrice sia chiaramente legata al contesto corretto e non a una logica generica.

Per il caso di riferimento, nomi validi potrebbero essere:
- **Deadheads - January 2026**
- **Driver repositioning - Workdays**

Quando termini questa sezione, dovresti avere una matrice creata e collegata al tipo di giorno appropriato.

## Caricare le connessioni tramite import massivo o modifica manuale

Una volta creata la matrice, devi riempirla con le connessioni reali tra origini e destinazioni. GoalBus supporta due modalità di lavoro:

1. **Bulk CSV import**, consigliato per reti grandi.
2. **Manual entry**, utile per casi piccoli o per aggiustamenti puntuali.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già creato la matrice corretta.
2. Tu abbia già identificato origini e destinazioni rilevanti.
3. Tu sappia se il tuo caso può essere caricato manualmente o se è meglio l’import massivo.

Per caricare dati via import massivo:
1. Prepara un file CSV con il formato standard di GoalBus.
2. Assicurati di includere almeno:
   1. Origins
   2. Destinations
   3. Distances
   4. Time bands, quando applicabile
   5. Durations
3. In GoalBus, seleziona l’opzione **upload/import**.
ref: P8_Imagen4.png | compact
4. Scegli il file CSV.
5. Rivedi la **pre-validation** del sistema.
6. Verifica se il sistema:
   1. rileva errori,
   2. indica quanti record verranno creati.
ref: P8_Imagen5.png |compact
7. Se la validazione è corretta, conferma l’upload.
8. Verifica che la griglia sia popolata con i record attesi.

Se tutto è corretto, la matrice sarà simile all’immagine seguente:
ref: P8_Imagen6.png |full

Per caricare dati manualmente:
1. Apri la griglia della matrice.
2. Aggiungi un nuovo record facendo clic su **New relation**.
ref: P8_Imagen7.png | compact
3. Imposta l’**origin**.
4. Imposta la **destination**.
5. Inserisci il tempo o la distanza corrispondente.
6. Se applicabile, imposta la time band.
ref: P8_Imagen8.png | compact
7. Salva il record.
8. Ripeti finché completi le connessioni minime necessarie per il tuo caso.

Per il caso di riferimento, inizia con connessioni come:
1. North Parking → North Terminal
2. South Terminal → North Parking

Quando termini questa sezione, dovresti avere una matrice con connessioni reali, importate o inserite manualmente.

## Distinguere deadhead trips da driver repositioning

Ora devi assicurarti di non mescolare due logiche diverse. GoalBus tratta **deadhead trips** e **driver repositioning** in modo simile nella configurazione, ma con uno scopo di business differente:

1. I deadhead trips usano **bus + driver** e modellano la logistica di spostare un veicolo dove serve.
2. Il repositioning usa **solo driver** e modella il tempo necessario a una persona per raggiungere un relief point o un punto di inizio senza muovere la flotta.

Prima di continuare, assicurati che:
1. Tu abbia già caricato almeno le connessioni essenziali per il tuo caso.
2. Tu possa identificare se ogni connessione corrisponde a un veicolo o solo a una persona.
3. Tu non abbia messo entrambe le logiche nella matrice sbagliata.

Per validare che ogni matrice rappresenti la risorsa corretta:
1. Rivedi una connessione di **deadhead trip** e conferma che rappresenti:
   1. lo spostamento di un veicolo da depot/parking a una linea, oppure
   2. lo spostamento di un veicolo tra linee.
2. Rivedi una connessione di **repositioning** e conferma che rappresenti:
   1. lo spostamento di un autista senza veicolo, oppure
   2. l’abilitazione di un relief a un terminale.
3. Conferma che la matrice deadhead modelli tempi dipendenti dal traffico.
4. Conferma che la matrice di driver repositioning rifletta la reale modalità di viaggio (cammino, taxi, navetta).
5. Correggi qualsiasi connessione inserita nella matrice sbagliata prima di procedere.

Per il caso di riferimento, chiediti:
1. Sto modellando un bus che esce dal parking, o solo un autista che va a un terminale?
2. Il tempo riflette il traffico reale o la modalità di spostamento dell’autista?
3. Il motore userebbe correttamente questa informazione quando costruisce orari e turni?

Quando termini questa sezione, dovresti capire chiaramente quale parte della configurazione appartiene alla logistica del veicolo e quale alla logistica dell’autista.

## Verificare che la matrice sia pronta per Scheduling

L’obiettivo finale di questo quick start non è solo riempire una tabella, ma preparare una base logistica che Scheduling possa consumare. Un modello preciso migliora:

1. **cost transparency**,
2. **realistic shift creation**,
3. **optimization accuracy**.

Prima di concludere, assicurati che:
1. Esista la matrice corretta.
2. Sia collegata al tipo di giorno corretto.
3. Siano caricate le connessioni minime del caso.
4. Tu abbia separato deadhead trips da driver repositioning.

Per validare che la matrice sia pronta per il prossimo passo:
1. Rivedi il caso di riferimento che stai costruendo.
2. Conferma che GoalBus sappia già:
   1. da dove parte fisicamente il veicolo,
   2. dove entra nella linea,
   3. come rientra quando necessario,
   4. e come si sposterebbe un autista per un relief se applicabile.
3. Chiediti se il sistema potrebbe già minimizzare tempo e distanza non produttivi in quel caso.
4. Se la risposta è sì, continua con il prossimo quick start.
5. Se la risposta è no, torna indietro e aggiungi o correggi connessioni prima di procedere.

Quando termini questa sezione, dovresti poter affermare che la tua base logistica è abbastanza realistica da supportare tempi, servizi e Scheduling.

## Additional reading

- [Definire i tipi di veicolo e la flotta consentita per linea](P4_Definire_i_tipi_di_veicolo_e_la_flotta_consentita_per_linea.md)

