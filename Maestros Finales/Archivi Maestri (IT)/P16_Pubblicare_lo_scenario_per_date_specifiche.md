---
title: Pubblicare lo scenario per date specifiche
shortTitle: Pubblicare scenario
intro: 'Scopri come pubblicare uno scenario validato per date specifiche, controllare quale solution entra in operations e mantenere la tracciabilità tra planning, validazione e deployment operativo.'
contentType: how-tos
versions:
  - '*'
---

## Preparare lo scenario validato prima di pubblicare

Dopo aver calcolato e validato una solution, il passo successivo è decidere **quando** deve diventare effettiva nelle operazioni reali. Pubblicare uno scenario non è solo approvarlo: significa inserire quella solution validata nel calendario operativo per date specifiche, senza confonderla con una bozza o una versione ancora in review.

Usa questo quick start quando hai già uno scenario la cui solution è in stato **Validated** e devi deployarlo alle operations per un periodo specifico.

Prima di iniziare, assicurati che:
1. Tu abbia già eseguito e validato lo scenario in P15.
2. La solution che vuoi pubblicare sia in stato **Validated**.
3. Tu conosca le date esatte che vuoi coprire.
4. Tu capisca che la pubblicazione cambia lo stato operativo della solution e la rende visibile come versione deployata.

Per questo quick start, usa questo caso di riferimento:

> **Pubblicherò lo scenario validato per la linea L1 in modo che diventi effettivo durante un periodo feriale specifico senza impattare soluzioni che non corrispondono a quelle date.**

Per preparare la pubblicazione:
1. Apri il modulo **Planning scenarios**.
2. Individua lo scenario che hai già validato.
3. Conferma che lo status corrente della solution sia **Validated**.
4. Rivedi il nome dello scenario, la/le linee incluse, il tipo di giorno e la description.
5. Conferma che stai per pubblicare esattamente la solution corretta.
6. Se lo scenario non è ancora validato, torna indietro e completa P15 prima di continuare.
7. Se è corretto, procedi con la pubblicazione.

Quando termini questa sezione, dovresti aver identificato chiaramente lo scenario validato che vuoi deployare.

## Selezionare la finestra temporale di pubblicazione

Una volta confermato lo scenario, devi decidere **quali date** copre. La pubblicazione non deve essere ambigua. Deve essere chiaro da quando a quando questa solution sarà il riferimento operativo.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia confermato quale scenario pubblicare.
2. Tu sappia se la pubblicazione copre un giorno, una settimana, un intervallo continuo o un blocco operativo più lungo.
3. Tu capisca che il periodo scelto non deve contraddire tipo di giorno e logica temporale dello scenario.

Per selezionare la finestra temporale:
1. Dallo scenario validato, apri l’azione **Publish**.
ref: P16_Imagen1.png | compact
2. Nel form di publishing, definisci il **Date range**.
3. Aggiungi ulteriori **Date ranges** se necessario (opzionale).
ref: P16_Imagen2.png | compact
4. Conferma che le date abbiano senso per:
   1. il day type dello scenario,
   2. la/le linee coinvolte,
   3. e la finestra operativa reale che vuoi coprire.
5. Conferma di non lasciare per errore un intervallo troppo ampio.
6. Se lo scenario deve applicarsi solo in un periodo breve, limita la finestra in modo preciso.
7. Conferma la pubblicazione per il/i date range selezionati.

Per il caso di riferimento, chiediti:
1. La pubblicazione copre esattamente i giorni feriali che voglio deployare?
2. Sto evitando di pubblicare più giorni del necessario?
3. La solution corrisponde davvero alle date selezionate?

Quando termini questa sezione, dovresti avere una finestra temporale chiara e controllata per il deployment.

## Confermare la pubblicazione e cambiare lo status dello scenario

Dopo aver selezionato l’intervallo, conferma l’azione di publishing. A questo punto, la solution smette di essere solo uno scenario validato e diventa un elemento operativo nel calendario.

Prima di continuare, assicurati che:
1. Tu abbia selezionato correttamente le date.
2. Tu abbia rivisto lo scenario validato.
3. Tu sia pronto perché la solution avanzi nel suo lifecycle.

Per pubblicare lo scenario:
1. Rivedi un’ultima volta il riepilogo di publishing.
2. Conferma:
   1. il nome dello scenario,
   2. l’intervallo temporale,
   3. e il contesto operativo a cui si applica.
3. Esegui **Publish**.
4. Conferma che lo status cambi in **Publishing** mentre il sistema processa il deployment.
5. Attendi che il processo finisca.
6. Conferma che lo status finale della solution cambi in **Published**.
ref: P16_Imagen3.png | compact
7. Se lo status non cambia come previsto, verifica un incidente tecnico o un problema di idoneità.

Per il caso di riferimento, non considerare completata la pubblicazione finché puoi affermare:
1. La solution dello scenario L1 è uscita da **Validated**.
2. La piattaforma ha processato la pubblicazione.
3. Lo status finale della solution è **Published**.

Quando termini questa sezione, dovresti avere uno scenario deployato nel calendario operativo per il periodo selezionato.

## Verificare che la solution pubblicata sia quella in vigore

Dopo la pubblicazione, conferma che la solution attiva sia davvero quella corretta. Pubblicare non dovrebbe essere un passo “alla cieca”. Dovresti poter verificare quale scenario è in vigore per le date selezionate e mantenere tracciabilità della solution deployata.

Prima di iniziare questa sezione, assicurati che:
1. La solution dello scenario sia **Published**.
2. Tu sappia quali date copre.
3. Tu sappia quale linea/servizio dovrebbe essere impattata dalla pubblicazione.

Per verificare il deployment:
1. Torna alla tabella principale degli scenari.
2. Filtra o rivedi gli scenari per status.
3. Conferma che lo scenario pubblicato risulti **Published**.
4. Rivedi le date di applicazione se la vista le supporta.
5. Conferma di non confonderlo con un altro scenario validato ma non deployato.
6. Se il tuo processo interno lo richiede, registra o comunica che questa versione è ora la solution operativa attiva.
7. Conserva name, description e intervallo temporale come tracciabilità per un audit successivo.

Per il caso di riferimento, assicurati che:
1. Lo scenario pubblicato corrisponda a L1 feriale.
2. Le date corrispondano al periodo che volevi deployare.
3. Nessun altro scenario sia stato reso attivo per errore.

Quando termini questa sezione, dovresti essere certo quale solution è in vigore e per quale periodo esatto.

## Mantenere tracciabilità e preparare la prossima iterazione

Una volta pubblicato uno scenario, il lavoro non scompare: cambia focus. La solution deployata può diventare una baseline per audit, confronto o un’iterazione futura. È più sicuro creare una nuova iterazione quando devi proporre miglioramenti, invece di alterare uno scenario published con cambi strutturali.

Prima di concludere, assicurati che:
1. Lo scenario sia published.
2. L’intervallo coperto sia chiaro.
3. Tu sappia se il prossimo passo è fare audit dei risultati o preparare una nuova iterazione.

Per mantenere la tracciabilità dopo la pubblicazione:
1. Mantieni lo scenario published con un name e una description sufficientemente chiari.
2. Usa lo status **Published** per distinguerlo da draft, calculating o validated.
3. Se devi proporre un miglioramento, crea un nuovo scenario invece di alterare la logica storica.
4. Se il team fa post-review, usa la versione published come baseline di confronto.
5. Mantieni un record interno di:
   1. cosa è stato pubblicato,
   2. quando è stato pubblicato,
   3. e per quali date è stato in vigore.

Per il caso di riferimento, termina questo quick start solo quando puoi affermare:
1. La solution di L1 è published.
2. Sai esattamente da quale data è diventata effettiva.
3. Puoi distinguere questa versione published da qualsiasi iterazione futura.

Quando termini questa sezione, dovresti avere una solution pubblicata e tracciabile pronta a fungere da riferimento operativo o da punto di partenza per una nuova iterazione.

## Additional reading

- [Creare una nuova iterazione dello scenario](P17_Creare_una_nuova_iterazione_dello_scenario.md)

