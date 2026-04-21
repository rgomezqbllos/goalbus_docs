---
title: Assegnare compiti logici ai veicoli reali
shortTitle: Assegnazione veicoli
intro: 'Scopri come assegnare i logical vehicle tasks prodotti in Scheduling a veicoli reali che sono stati caricati o creati in precedenza.'
contentType: how-tos
versions:
  - '*'
---

## Caricare o creare i veicoli reali usati per l’assegnazione

Una volta che le soluzioni di Scheduling e Rostering sono validate e published (Rostering non è strettamente richiesto), puoi creare o caricare i veicoli reali che verranno usati per assegnare i logical tasks calcolati nella vehicle Scheduling solution.

Usa questo quick start quando hai già eseguito Scheduling e (opzionalmente) Rostering e devi iniziare l’assegnazione veicoli.

Prima di iniziare, assicurati che:
1. Tu abbia published la Scheduling solution in P16.
2. Tu abbia validato e consolidato la soluzione di Rostering in P27.

Per questo quick start, usa questo caso di riferimento:

> **Assegnerò i logical tasks calcolati in vehicle Scheduling alle targhe dei veicoli che ho caricato o creato.**

Per caricare o creare targhe veicolo reali:
1. Apri **Configuration** > **Vehicles** > **Registered vehicles**.
ref: P28_Imagen1.png | compact
2. Se vuoi creare più targhe insieme, l’opzione migliore è importarle.
3. Seleziona il pulsante di import delle targhe.
ref: P28_Imagen2.png | compact
4. Carica il file CSV con i nuovi veicoli seguendo le istruzioni del modal.
ref: P28_Imagen3.png | compact
5. Se non ci sono errori, i veicoli verranno registrati.
6. Se preferisci creare i veicoli uno per uno, fai clic su **New vehicle**.
ref: P28_Imagen4.png | compact
7. Nel modal, compila:
   1. **License plate**.
   2. **Depot** a cui appartiene il veicolo.
   3. **Model**.
   4. **Manufacturing year** (opzionale).
   5. **Start-of-operations date** a partire dalla quale possono essere assegnati task.
ref: P28_Imagen5.png | compact
8. Salva i cambi.
9. Conferma che il record creato compaia nella vista registro veicoli.

Per il caso di riferimento, non procedere finché puoi affermare:
1. Tutte le targhe necessarie sono caricate o create.
2. I veicoli sono collegati al **model** corretto.
3. Non ti servono veicoli aggiuntivi oltre quelli caricati/creati.

Quando termini questa sezione, dovresti avere tutte le targhe necessarie per eseguire l’assegnazione.

Per il caso di riferimento, puoi creare targhe con un formato come:
- **001-LFX**
- **002-LFX**
...
- **NNN-LFX**

## Assegnare i logical tasks di Scheduling ai veicoli reali

Una volta caricati/creati tutti i veicoli necessari, puoi iniziare l’assegnazione.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già tutti i veicoli caricati o creati.
2. Tu sappia quali criteri di assegnazione applicare.
3. Tu abbia una soluzione di Rostering validata.

Per iniziare l’assegnazione veicoli:
1. Apri il modulo **Vehicle assignment**.
ref: P28_Imagen6.png | compact
2. Rivedi i task non assegnati nella barra superiore.
ref: P28_Imagen7.png | compact
3. Nel pannello destro, vedrai i task da assegnare manualmente.
ref: P28_Imagen8.png
4. Quando selezioni **assign task**, il sistema mostrerà i veicoli disponibili (senza task assegnati o assegnati senza sovrapposizioni).
Ref: P28_Imagen9.png
5. Assegna i task ai veicoli corrispondenti.
6. Quando finisci, fai clic su **Confirm** per **publish** le modifiche.
ref: P28_Imagen10.png
7. Se hai ancora task non assegnati o non vuoi fare tutto manualmente, usa **Optimize fleet assignment**.
ref: P28_Imagen11.png
8. Ripeti per ogni giorno su cui vuoi lavorare.

Per il caso di riferimento, assicurati che:
1. Tutti i task siano assegnati a un veicolo.
2. Le assegnazioni siano coerenti.
3. Tutti i giorni richiesti siano coperti.

Quando termini questa sezione, dovresti avere una soluzione veicoli nominata/assegnata.

