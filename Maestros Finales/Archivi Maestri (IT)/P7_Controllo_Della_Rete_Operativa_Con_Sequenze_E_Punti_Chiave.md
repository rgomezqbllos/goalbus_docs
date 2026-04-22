---
title: Controllo della rete operativa con sequenze e punti chiave
shortTitle: Rete operativa
intro: Scopri come convalidare come la tua rete si comporta realmente in esercizio,
  rivedere sequenze, fermare i permessi e i punti di relè prima di passare ai tempi
  e ai servizi.
contentType: how-tos
versions:
- '*'
---
## Controllo della sequenza operativa delle rotte

Ora che avete già creato la rete di base (stop, linee e rotte), il passo successivo è quello di convalidare che la rete funziona correttamente dal punto di vista operativo.

A questo punto non si sta più creando la struttura, si sta validando come si comporta in pratica.

Prima di iniziare:
1. Hai già creato fermate, linee e percorsi su P6.
2. Hai almeno una via a senso.
3. Sai che linea stai preparando.

Caso:
> Validare che l'itinerario L1 ha una sequenza coerente e operativa prima di definire i tempi.

Fasi:
1. Apri la linea su cui stai lavorando.
2. Accedi alla vista dell'itinerario.
ref: P7_Imagen1.png | full
3. Selezionare un senso.
4. Controlla la sequenza di arresto.
5. Controlla che:
   - Non ci sono fermate per le chiavi mancanti.
   - Non ci sono duplicati inutili.
   - L'ordine è corretto.
6. Ripeti per l'altro senso.

Risultato previsto:
- Una sequenza pulita e logica che rappresenta il percorso effettivo.

## Convalida dei permessi di arresto

Non tutti si fermano a lavorare allo stesso modo. Alcuni permettono l'arrampicata, altri più bassi, e altri entrambi.

Prima di continuare:
1. Hai convalidato la sequenza.
2. Sai come funzionano tutte le fermate in realtà.

Fasi:
1. All'interno del percorso, controllate ogni fermata.
2. Configura se permetti:
   - Alzati
   - Giù
   - Entrambi
ref: P7_Imagen2.png | compact
3. Assicurati che:
   - I terminali permettono entrambi.
   - Le fermate intermedie riflettono l'operazione effettiva.
4. Salva i cambiamenti.

Risultato previsto:
- Ogni fermata ha un comportamento coerente con l'operazione.

## Definizione dei punti di collegamento

I punti di relè sono critici per la torrefazione e il funzionamento.

Prima di iniziare:
1. Hai già una sequenza convalidata.
2. Sai dove i relè avvengono nell'operazione.

Fasi:
1. Identificare le fermate in cui vengono apportate le modifiche del driver.
2. Contrassegna quelle fermate come punti di relè.
ref: P7_Imagen3.png | compact
3. Controlla che:
   - Sono ben posizionati.
   - Basta per l'operazione.
4. Guardia.

Risultato previsto:
- La rete contempla già dove possono essere apportati i cambiamenti del driver.

## Convalida finale della rete operativa

Prima di procedere:

1. Controlla di nuovo l'intero percorso.
2. Conferma:
   - Sequenza giusta.
   - Permessi coerenti.
   - Relè determinati.
3. Chiediti:
   - Potresti operare questa linea nella vita reale?
   - Manca qualche dettaglio operativo?

Se la risposta è sì, potete continuare.

## Letture aggiuntive

- P8 Caricamento viaggi vuoti e viaggi
