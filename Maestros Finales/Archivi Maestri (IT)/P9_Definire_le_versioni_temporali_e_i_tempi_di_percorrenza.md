---
title: Definire versioni temporali e tempi di viaggio per le operazioni
shortTitle: Versioni e tempi
intro: 'Scopri come creare versioni temporali, definire tempi di viaggio e sosta per tipo di giorno e fascia oraria e stabilire un riferimento temporale affidabile prima di creare o modificare servizi in GoalBus.'
contentType: how-tos
versions:
  - '*'
---

## Creare la versione temporale che userà il tuo caso

Prima di definire i tempi di viaggio, devi creare una **time version**. In GoalBus, una versione non è solo un’etichetta: è la libreria temporale che raggruppa la logica dei tempi applicata a routes specifiche e tipi di giorno specifici. Questo è importante perché il lunedì mattina non si comporta come la domenica mattina e il sistema non dovrebbe riutilizzare un unico set di tempi per tutto l’anno.

Usa questo quick start quando hai già definito una linea e le sue routes e devi costruire la base tempi che in seguito verrà usata per calcolare trips, validare durate e confrontare deviazioni rispetto allo standard.

Prima di iniziare, assicurati che:
1. Tu abbia già preparato la rete maestra in P6.
2. Tu abbia già rivisto la rete operativa in P7.
3. Tu abbia già configurato la base calendario per tipi di giorno in P2.
4. Tu abbia già validato l’anno operativo in P3.
5. Tu sappia quale linea, quali routes e quale tipo di giorno userai come riferimento.

Per questo quick start, usa questo caso di riferimento:

> **Creerò una time version per la linea L1 nei giorni feriali e la userò come riferimento tempi prima di creare o modificare servizi.**

Per creare la time version per il tuo caso:
1. In GoalBus, apri la **Routes view** della linea che userai come riferimento.
2. Seleziona l’icona/opzione per **Travel and stop time management**.
ref: P9_Imagen1.png | compact
3. In alto nella vista, crea una nuova versione selezionando **New timetable set**.
ref: P9_Imagen2.png | compact
4. Definisci un **name** chiaro per la versione.
5. Aggiungi una **description** che ti aiuti a distinguere il contesto operativo.
6. Seleziona i **day types** a cui si applica questa versione, ad esempio **Workdays**.
7. Collega le **route variations** o le sequenze specifiche che faranno parte di quella time version.
8. Salva la versione.
ref: P9_Imagen3.png | compact
9. Conferma che la versione sia ora disponibile come riferimento tempi per quella linea.

Per il caso di riferimento, nomi validi potrebbero essere:
- **Winter workdays**
- **L1 base workday**

Quando termini questa sezione, dovresti aver creato una time version che il sistema può usare come riferimento tempi per i servizi di quella linea, simile alla seguente immagine.
ref: P9_Imagen4.png | full

## Definire i tempi di viaggio tra fermate chiave

Dopo aver creato la versione, devi inserire i **travel times**. In GoalBus, questi tempi sono definiti principalmente tra **key stops** o **time points**, non tra ogni fermata intermedia. I terminali sono key per default e, da lì, la logica tempi viene costruita per alimentare i servizi.

GoalBus non lavora con un singolo valore per segmento. Il motore usa una logica **minimum, optimal e maximum** per offrire flessibilità controllata:
1. **Minimum**: il tempo più rapido possibile.
2. **Optimal**: il tempo obiettivo verso cui il motore tenderà.
3. **Maximum**: il tempo più lento accettabile.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già creato la time version.
2. Tu sappia quali key stops userai come riferimento.
3. Tu abbia identificato quale direzione configurare per prima.

Per definire i travel times per il tuo caso:
1. Nella griglia tempi, seleziona il **segment** tra due key stops.
ref: P9_Imagen5.png | full
2. Crea una o più **time bands** per riflettere la realtà operativa.
3. Per ogni band, inserisci:
   1. il tempo **minimum**,
   2. il tempo **optimal**,
   3. il tempo **maximum**.
ref: P9_Imagen6.png | compact
4. Salva il segmento.
5. Ripeti per il segmento chiave successivo.
6. Quando termini una direzione, ripeti la stessa logica per la direzione opposta.

Le time bands non devono avere lacune o sovrapposizioni. Se le hanno, il sistema non permetterà di salvare i tempi.

Per il caso di riferimento, una logica di base potrebbe essere:
1. **North Terminal → Downtown**
   1. 07:00–09:00
      1. Minimum: 12 min
      2. Optimal: 15 min
      3. Maximum: 18 min
   2. 09:00–22:00
      1. Minimum: 5 min
      2. Optimal: 5 min
      3. Maximum: 5 min
   3. 22:00–06:00
      1. Minimum: 8 min
      2. Optimal: 10 min
      3. Maximum: 12 min
2. **Downtown → Hospital**
3. **Hospital → University**
4. **University → South Terminal**

Quando termini questa sezione, dovresti avere tempi di guida flessibili definiti tra i principali time points della route.

## Definire i tempi di sosta per regolazione e recupero

Oltre al tempo di guida, GoalBus deve sapere per quanto tempo un veicolo può rimanere in una key stop. Questi **dwell times** sono importanti perché consentono regolazione delle partenze, assorbono arrivi anticipati e creano margine di recupero ai terminali o nei punti di connessione.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già definito travel times tra i segmenti chiave.
2. Tu sappia quali terminali o key points richiedono regolazione.
3. Tu abbia identificato dove serve margine operativo reale.

Per definire i dwell times:
1. Nella griglia tempi, seleziona la **column** di una key stop.
ref: P9_Imagen7.png | full
2. Scegli un terminale, un headway point o un punto di connessione importante.
3. Definisci:
   1. **Minimum** come attesa obbligatoria,
   2. **Maximum** come margine consentito per regolazione o sincronizzazione.
4. Salva la configurazione.
5. Ripeti per altre key stops dove ti serve una sosta controllata.

Per il caso di riferimento, una logica possibile è:
1. **North Terminal**
   1. Minimum: 4 min
   2. Maximum: 10 min
2. **South Terminal**
   1. Minimum: 5 min
   2. Maximum: 12 min

Quando termini questa sezione, dovresti avere margini che il motore può usare per recuperare o regolare senza distorcere la logica dell’orario.

## Rivedere time bands, vista estesa e coerenza visiva

Una volta inseriti travel e dwell times, devi verificare se la griglia riflette una logica realistica. GoalBus include aiuti visivi per individuare errori quando gestisci molti punti, molte bands o più routes.

Prima di continuare, assicurati che:
1. Tu abbia configurato almeno una time band.
2. Tu abbia inserito valori minimum, optimal e maximum.
3. Tu abbia aggiunto dwell times nei punti rilevanti.

Per rivedere visivamente la coerenza:
1. Rivedi la griglia e conferma che ogni segmento chiave abbia una time band valida.
2. Usa gli aiuti visivi disponibili per individuare valori anomali.
3. Verifica che le ore di punta mostrino tempi più alti rispetto alle ore di morbida.
4. Espandi la vista se ti servono più dettagli o più fermate intermedie.
5. Correggi eventuali valori anomali direttamente nella vista o dal pannello di modifica.
6. Ripeti finché la logica tempi riflette un’operatività credibile.

Per il caso di riferimento, chiediti:
1. Le ore di punta mostrano tempi più alti rispetto alla notte?
2. Minimum, optimal e maximum mantengono una relazione logica?
3. I terminali hanno margine di regolazione realistico?
4. La griglia rappresenta già un’intera giornata operativa?

Quando termini questa sezione, dovresti avere una base tempi rivista visivamente e priva di incoerenze importanti.

## Applicare la time version come riferimento per i servizi

L’obiettivo finale non è solo creare dati tempi, ma stabilire un riferimento utilizzabile durante la creazione o modifica dei servizi. Ogni trip dovrebbe essere misurato rispetto a una **reference time version** e quel riferimento viene usato automaticamente quando crei nuovi trips o cambi la route di un trip. Aiuta anche a rilevare deviazioni se un trip è stato importato o modificato fuori dallo standard.

Prima di concludere, assicurati che:
1. Tu abbia già creato una time version valida.
2. Tu abbia già definito travel e dwell times.
3. Tu abbia rivisto la coerenza della griglia.
4. Tu sappia quale linea e quale caso userai per creare servizi.

Per confermare che la tua base tempi sia pronta per i servizi:
1. Rivedi la time version che hai appena creato.
2. Conferma che sia collegata al tipo di giorno corretto.
3. Conferma che includa le routes/variations che userai.
4. Verifica che questa versione possa già agire come riferimento tempi per:
   1. creare nuovi trips,
   2. ricalcolare orari di arrivo e partenza,
   3. auditare discrepanze rispetto allo standard.
5. Se la risposta è sì, continua con il prossimo quick start.
6. Se la risposta è no, torna indietro e correggi la versione o i suoi tempi prima di procedere.

Quando termini questa sezione, dovresti poter affermare che la linea ha già una time version di riferimento sufficiente per creare servizi in modo coerente.

## Additional reading

- [Creare l’offerta di servizio base con viaggi e orari](P10_Creare_l_offerta_di_servizio_base_con_viaggi_e_orari.md)

