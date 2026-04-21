---
title: Verificare la rete operativa con sequenze e punti chiave
shortTitle: Rete operativa
intro: 'Scopri come validare il comportamento della tua rete nelle operazioni reali rivedendo sequenze, permessi di fermata e relief points prima di passare a tempi e servizi.'
contentType: how-tos
versions:
  - '*'
---

## Verificare la sequenza operativa delle routes

Ora che hai creato la rete di base (stops, lines e routes), il passo successivo è validare che la rete funzioni correttamente dal punto di vista operativo.

A questo punto non stai più creando struttura: stai verificando come si comporta nella pratica.

Prima di iniziare:
1. Hai già creato stops, lines e routes in P6.
2. Hai almeno una route per direzione.
3. Sai quale linea stai preparando.

Caso:
> Valida che la route della linea L1 abbia una sequenza operativa coerente prima di definire i tempi.

Passaggi:
1. Apri la linea su cui stai lavorando.
2. Vai alla vista routes.
ref: P7_Imagen1.png | full
3. Seleziona una direzione.
4. Rivedi la sequenza delle fermate.
5. Verifica che:
   - non manchino fermate chiave,
   - non ci siano duplicati inutili,
   - l’ordine sia corretto.
6. Ripeti per l’altra direzione.

Risultato atteso:
- Una sequenza pulita e logica che rappresenta il percorso reale.

## Validare i permessi delle fermate

Non tutte le fermate funzionano allo stesso modo. Alcune consentono la salita, altre la discesa e altre entrambe.

Prima di continuare:
1. Hai già validato la sequenza.
2. Sai come funziona ciascuna fermata nella realtà.

Passaggi:
1. All’interno della route, rivedi ogni fermata.
2. Configura se consente:
   - Boarding
   - Alighting
   - Both
ref: P7_Imagen2.png | compact
3. Assicurati che:
   - i terminali consentano entrambi,
   - le fermate intermedie riflettano l’operatività reale.
4. Salva le modifiche.

Risultato atteso:
- Ogni fermata ha un comportamento coerente con le operazioni.

## Definire i relief points

I relief points sono critici per Rostering e operations.

Prima di iniziare:
1. Hai già validato la sequenza.
2. Sai dove avvengono i relief nell’operatività reale.

Passaggi:
1. Identifica le fermate in cui vengono effettuati i cambi autista.
2. Marca quelle fermate come relief points.
ref: P7_Imagen3.png | compact
3. Verifica che:
   - siano ben posizionati,
   - siano sufficienti per le operazioni.
4. Salva.

Risultato atteso:
- La rete ora include i punti in cui possono avvenire i cambi autista.

## Validazione finale della rete operativa

Prima di proseguire:
1. Rivedi di nuovo l’intera route.
2. Conferma:
   - sequenza corretta,
   - permessi coerenti,
   - relief definiti.
3. Chiediti:
   - Questa linea potrebbe operare nella vita reale?
   - Manca qualche dettaglio operativo?

Se la risposta è sì, puoi continuare.

## Additional reading

- [Preparare parcheggi e depositi per l’operatività](P5_Preparare_parcheggi_e_depositi_per_l_operativita.md)

