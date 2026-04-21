---
title: Preparare parcheggi e depositi per l’operatività
shortTitle: Parcheggi e depositi
intro: 'Scopri come configurare parcheggi e depositi in modo coerente affinché Scheduling possa usare un’infrastruttura fisica realistica, minimizzare i chilometri di deadhead e rispettare la corretta gerarchia dei dati.'
contentType: how-tos
versions:
  - '*'
---

## Configurare il depot come struttura operativa e di relief

Prima di creare il parking, devi rivedere il **depot**. In GoalBus, il depot è la base operativa dell’organizzazione e il collegamento obbligatorio per veicoli e autisti. La sua configurazione non solo identifica l’unità, ma definisce anche dove i turni possono iniziare o terminare, includendo terminali autorizzati che abilitano relief efficienti e riducono i chilometri di deadhead.

Prima di iniziare questa sezione, assicurati che:
1. Tu sappia quale depot è responsabile della linea o del servizio che stai preparando.
2. Tu capisca che il depot è l’entità primaria e che il parking dipende da esso.

Per creare o validare il depot per il tuo caso:
1. In GoalBus, apri il modulo **depots**.
ref: P5_Imagen3.png | full
2. Verifica se il depot di cui hai bisogno esiste già.
3. Se il depot esiste già, aprilo e rivedi la sua configurazione.
4. Se non esiste, creane uno nuovo.
ref: P5_Imagen4.png | compact
5. Definisci o valida questi campi:
   1. **Code** come identificatore univoco.
   2. **Short name** per viste compatte.
   3. **Participation percentage %** come quota del depot sul totale delle operazioni. Su tutti i depots, il totale dovrebbe sommare a 100%.
   4. **Long name** come nome principale del depot.
   5. **External ID**, se il cliente lavora con integrazioni ERP o HR.
6. Aggiungi le **authorized start and end stops**, ad esempio terminali in cui sono consentiti relief o fine turno.
7. Salva il depot.
ref: P5_Imagen5.png | compact
8. Conferma che il depot possa ora supportare operativamente il caso che stai costruendo.

Per il caso di riferimento, verifica che:
1. North Depot sia il depot organizzativo corretto.
2. I terminali rilevanti per la linea L1 siano autorizzati come punti di inizio o fine quando applicabile.

Quando termini questa sezione, dovresti avere un depot correttamente identificato e collegato alle sue location operative autorizzate.

## Configurare il parking come nodo fisico nella rete

Dopo aver definito il depot e prima di passare a deadhead trips, flotta o regole di Scheduling, devi configurare il **parking** che supporterà il tuo caso. In GoalBus, un parking non è solo un’etichetta amministrativa. È un nodo fisico geolocalizzato nella rete e, quando lo crei, il sistema genera automaticamente una fermata associata a quelle coordinate in modo che il motore calcoli distanze e tempi di ingresso/uscita in modo coerente. Inoltre, ogni parking deve essere collegato a un depot organizzativo.

Usa questo quick start quando hai già creato la rete di base e devi collegarla a infrastruttura fisica reale prima di continuare con repositioning e Scheduling.

Prima di iniziare, assicurati che:
1. Tu abbia già preparato fermate, linee e percorsi in P6.
2. Tu abbia già rivisto la rete operativa in P7.
3. Tu sappia quale linea o servizio userai come caso di riferimento.
4. Tu sappia da quale base fisica quell’operazione dovrebbe partire.
5. Tu abbia già configurato il/i depot operativo/i.

Per questo quick start, usa questo caso di riferimento:

> **Preparerò il parking di North Depot e validerò che la sua relazione con il depot e con la linea L1 sia coerente prima di continuare con deadhead trips e Scheduling.**

Per creare o validare il parking per il tuo caso:
1. In GoalBus, apri il modulo **parkings** nell’infrastruttura di rete.
ref: P5_Imagen1.png | full
2. Verifica se il parking di cui hai bisogno esiste già.
3. Se il parking esiste già, aprilo e rivedi la sua configurazione.
4. Se il parking non esiste, creane uno nuovo.
ref: P5_Imagen2.png | compact
5. Definisci o valida questi campi:
   1. **Code** come identificatore breve per viste compatte.
   2. **Short name** per viste compatte.
   3. **Long name** come nome descrittivo del garage o piazzale.
   4. **Coordinates** per posizionare correttamente il parking sulla mappa.
   5. **External ID**, se il cliente lavora con integrazioni ERP o HR.
6. Conferma che il parking sia collegato al **depot** corretto creato in precedenza.
ref: P5_Imagen6.png | compact
7. Fai clic su **Next** per configurare capacità del parking e tipi di veicolo consentiti. Puoi modificarli in seguito se cambiano le condizioni.
ref: P5_Imagen7.png | compact
8. Verifica visivamente sulla mappa che la posizione abbia senso per l’operatività reale.
9. Conferma che il sistema possa già trattare quel parking come origine o destinazione logistica per le operazioni.

Quando termini questa sezione, dovresti avere un parking correttamente geolocalizzato e subordinato al depot giusto.

## Validare la coerenza tra parking, depot e linea

Ora che hai configurato parking e depot, devi verificare che questa infrastruttura si integri con la logica della linea e con l’efficienza logistica che GoalBus si aspetta. Il modello di linea permette di definire **allowed parkings or depots** per forzare il sistema ad avviare il servizio da basi geograficamente corrette e minimizzare i chilometri di deadhead. Non è una preferenza estetica: guida direttamente lo scheduler durante la costruzione delle soluzioni.

Prima di continuare, assicurati che:
1. Il parking sia già collegato al depot corretto.
2. Il depot abbia già le sue location autorizzate.
3. La linea che userai nel tuo caso esista già e sia validata.

Per validare la coerenza completa dell’infrastruttura:
1. Apri la configurazione della **linea** che userai come riferimento.
2. Rivedi la sezione **allowed parkings** o **allowed depots**.
3. Conferma che il depot corretto sia autorizzato ad avviare servizi per quella linea.
4. Se il depot corretto non è autorizzato, aggiungilo.
5. Conferma di non lasciare abilitati depots che non hanno alcun senso geografico per quella linea.
6. Rivedi se la relazione tra linea, depot e parking minimizza la guida non a ricavo.
7. Conferma che l’infrastruttura fisica appena preparata possa supportare il servizio che creerai o calcolerai in seguito.
8. Se rilevi incoerenze, correggile prima di procedere.

Per il caso di riferimento, chiediti:
1. La linea L1 è autorizzata a partire da North Depot?
2. Quel depot usa North Parking come base fisica?
3. La logica risultante riduce i chilometri di deadhead invece di aumentarli?

Quando termini questa sezione, dovresti poter affermare che linea, depot e parking formano un’unica logica operativa e logistica.

## Additional reading

- [Caricare i viaggi a vuoto e i riposizionamenti](P8_Caricare_i_viaggi_a_vuoto_e_i_riposizionamenti.md)

