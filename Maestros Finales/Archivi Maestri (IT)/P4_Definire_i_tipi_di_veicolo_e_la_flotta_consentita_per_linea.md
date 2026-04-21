---
title: Definire i tipi di veicolo e la flotta consentita per linea
shortTitle: Flotta per linea
intro: 'Scopri come configurare i tipi di veicolo e i vincoli di flotta consentita a livello di linea in modo che GoalBus blocchi assegnazioni non fattibili, rispetti limiti fisici e ambientali e prepari una base coerente prima di definire tempi e servizi.'
contentType: how-tos
versions:
  - '*'
---

## Definire i tipi di veicolo consentiti per una linea

Prima di passare a tempi di viaggio, servizi o regole di Scheduling, devi rendere esplicito quali **tipi di veicolo** possono operare su ciascuna linea. In GoalBus, questo vincolo non è decorativo: funziona come filtro di sicurezza, conformità e fattibilità fisica. L’obiettivo è impedire che il sistema proponga un veicolo che non entra in una strada, viola una restrizione ambientale o non dovrebbe operare quel servizio.

Usa questo quick start quando hai già preparato rete, parkings e depots e devi chiudere la base flotta che userà il tuo caso prima di definire tempi e offerta di servizio.

Prima di iniziare, assicurati che:
1. Tu abbia già preparato la rete maestra in P6.
2. Tu abbia già rivisto la rete operativa in P7.
3. Tu abbia già configurato parkings e depots in P5.
4. Tu sappia quale linea userai come caso di riferimento.
5. Tu capisca, almeno a livello base, quali vincoli fisici o ambientali impattano quella linea.

Per questo quick start, usa questo caso di riferimento:

> **Definirò quali tipi di veicolo possono operare la linea L1 per assicurarmi che il mio primo lavoro di planning usi solo una flotta coerente con la realtà fisica e regolatoria del servizio.**

Per definire i tipi di veicolo consentiti per il tuo caso:
1. In GoalBus, apri la configurazione della **linea** che userai come riferimento.
2. Trova la sezione **Allowed vehicle types**.
3. Verifica se la linea ha già tipi assegnati.
4. Se la linea ha già tipi definiti, conferma che siano ancora corretti per il tuo caso.
5. Se non sono ancora definiti, verifica prima se il **vehicle type** di cui hai bisogno esiste già nella configurazione globale dei veicoli.
6. Se il tipo **esiste**, selezionalo come consentito per quella linea.
7. Se il tipo **non esiste**, esci dalla configurazione della linea e vai alla configurazione globale **vehicles** per creare o completare prima il catalogo dei tipi di veicolo dal pannello **Vehicle Types**.
ref: P4_Imagen1.png | full
8. Crea il tipo di veicolo necessario usando una categoria chiara e business-friendly, ad esempio:
   1. Minibus
   2. Standard electric
   3. Articulated diesel
ref: P4_Imagen2.png | compact
9. Salva il nuovo tipo di veicolo.
ref: P4_Imagen3.png | compact
10. Torna alla configurazione della linea.
11. Seleziona i tipi di veicolo specifici autorizzati a operare su quella linea.
ref: P4_Imagen4.png | compact
12. Lascia deselezionati i tipi che non dovrebbero operare quel servizio.
13. Salva la configurazione.
14. Rivedi la linea e conferma che il filtro corrisponda ora alla realtà operativa.

Per il caso di riferimento, chiediti:
1. La linea L1 può operare con un bus standard, un minibus o entrambi?
2. C’è un tipo di veicolo da escludere per dimensione o ambiente?
3. Se il tipo necessario non esisteva, lo hai creato prima di provare ad assegnarlo alla linea?
4. Il sistema dovrebbe bloccare un’assegnazione manuale se provi a usare un veicolo non autorizzato?

Quando termini questa sezione, dovresti avere un vincolo flotta a livello di linea che può fungere da base per i calcoli a valle.

## Collegare la linea ai depots o parkings consentiti

Dopo aver definito quale flotta è adatta (o non adatta) alla linea, devi rivedere da quali basi fisiche quel servizio può partire. GoalBus ti permette di definire **allowed parkings or depots** per linea per forzare il sistema ad avviare il servizio da posizioni geograficamente corrette e ridurre i chilometri di deadhead.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già configurato gli allowed vehicle types della linea.
2. Tu abbia già preparato parkings e depots per il caso in P5.
3. Tu sappia da quale base operativa il servizio dovrebbe partire realisticamente.

Per collegare la linea ai depots o parkings consentiti:
1. Nella stessa configurazione della linea, individua la sezione **Allowed parkings** o **Allowed depots**.
2. Verifica se la linea ha già depots autorizzati.
3. Seleziona solo i depots/garages che sono geograficamente autorizzati ad avviare servizi su quella linea.
4. Escludi basi che non hanno senso operativo per quel corridoio.
5. Salva la configurazione.
6. Conferma che la linea abbia ora una logica di partenza coerente dalla base più ragionevole.

Per il caso di riferimento, verifica che:
1. La linea L1 possa partire da North Depot.
2. Il parking primario associato sia quello corretto.
3. Non stai consentendo un depot lontano che forzerebbe molti chilometri di deadhead per avviare la prima corsa.

Quando termini questa sezione, dovresti avere linea, flotta consentita e geografia di partenza allineate.

## Validare che la linea abbia già una base flotta coerente

Ora che hai definito i tipi di veicolo consentiti e i depots/parkings autorizzati, devi fare una validazione finale.

Prima di continuare, assicurati che:
1. La linea abbia già tipi di veicolo consentiti.
2. Se il tipo di veicolo necessario non esisteva, sia già stato creato nella configurazione globale.
3. La linea abbia già depots o parkings autorizzati.
4. La configurazione rifletta la realtà del caso che stai costruendo.

Per validare che la base flotta sia pronta:
1. Rivedi di nuovo la configurazione completa della linea.
2. Conferma che i tipi di veicolo selezionati rappresentino la flotta che dovrebbe effettivamente operare il servizio.
3. Conferma che i depots/parkings autorizzati minimizzino i chilometri di deadhead.
4. Chiediti se il sistema, con questa configurazione, eviterebbe già:
   1. assegnazioni fisicamente impossibili,
   2. violazioni di conformità ambientale,
   3. partenze da basi geograficamente inefficienti.
5. Se la risposta è sì, continua con il prossimo quick start.
6. Se la risposta è no, correggi la linea o crea il tipo di veicolo mancante prima di procedere.

Quando termini questa sezione, dovresti poter affermare che la linea ha una base flotta sufficientemente matura per supportare tempi di viaggio, servizi e regole di Scheduling.

## Additional reading

- [Definire le versioni temporali e i tempi di percorrenza](P9_Definire_le_versioni_temporali_e_i_tempi_di_percorrenza.md)

