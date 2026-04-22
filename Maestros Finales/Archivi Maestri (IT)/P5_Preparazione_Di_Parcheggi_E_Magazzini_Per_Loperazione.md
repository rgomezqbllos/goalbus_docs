---
title: Preparazione di parcheggi e magazzini per l'operazione
shortTitle: Parcheggi e magazzini
intro: Scopri come impostare i parcheggi e i magazzini in modo coerente in modo che
  Schedulering possa utilizzare un'infrastruttura fisica realistica, minimizzare il
  chilometraggio vuoto e rispettare la corretta gerarchia dei dati.
contentType: how-tos
versions:
- '*'
---
## Configurazione del deposito come struttura operativa e di relè

Prima di creare il parcheggio, è necessario controllare il **deposito**. In GoalBus, il deposito è la base operativa dell'organizzazione ed è il collegamento obbligatorio per veicoli e piloti. Inoltre, la sua configurazione serve non solo per identificare l'unità, ma anche per definire dove i turni possono iniziare o finire, compresi intestazioni autorizzate o terminali che consentono relè efficienti e ridurre il chilometraggio sottovuoto.

Prima di iniziare questa sezione, assicurarsi che:
1. Sai quale deposito è responsabile per la linea o il servizio che stai preparando.
2. Si capisce che il deposito è l'entità principale e che il parcheggio dipende da esso.
3. Hai già creato tutti i tipi di veicoli necessari per l'operazione.

Per creare o convalidare il deposito del caso:
1. In GoalBus, aprire il modulo **depositi**.
ref: P5_Imagen3.png | full
2. Vedere se il deposito necessario esiste già.
3. Se il deposito esiste già, aprilo e controlla le impostazioni.
4. Se non esiste, creane una nuova.
ref: P5_Imagen4.png | compact(2x)
5. Definisce o convalida questi campi:
   1. **Codice** come identificatore unico.
   2. **Nome corto** per viste compatte.
   3. **Quota %** come quota di deposito nel totale delle operazioni. Tra tutti i depositi deve aggiungere il 100%.
   4. **Nome lungo** come nome principale del deposito.
   5. **ID esterno**, se il cliente lavora con integrazioni ERP o HR.
6. Aggiungere **Fermate autorizzate di inizio e fine** come intestazioni o terminali dove sono consentiti i relè o la fine dello shift.
7. Risparmia il deposito.
ref: P5_Imagen5.png | compact(8.5x)
8. Conferma che il deposito può già sostenere operativamente il caso che stai costruendo.

Per il caso di riferimento, verificare che:
1. Il Deposito Nord è il deposito organizzativo corretto.
2. Le intestazioni o i terminali L1 rilevanti sono autorizzati come posizioni di inizio o di fine quando si applicano.

Quando si conclude questa sezione, si dovrebbe avere un deposito correttamente identificato collegato alle vostre posizioni operative autorizzate.

## Configurazione del parcheggio come nodo fisico della rete

Dopo aver definito il deposito e prima di andare in gite vuote, flotta o regole di programmazione, è necessario lasciare **parcheggio** ben configurato che terrà il caso. In GoalBus, un parcheggio non è solo un'etichetta amministrativa. Si tratta di un nodo fisico geolocalizzato della rete, e quando si crea il sistema genera automaticamente una fermata associata a quelle coordinate in modo che il motore possa calcolare le distanze, i tempi di ingresso e i tempi di uscita in modo coerente. Inoltre, ogni parcheggio deve essere collegato a un deposito organizzativo.

Utilizza questo avvio rapido quando hai già creato la rete di base e hai bisogno di collegare quella rete all'infrastruttura fisica reale prima di procedere e programmare.

Prima di iniziare, assicurati che:
1. Sei chiaro che linea o servizio userai come caso di riferimento.
2. Sai da che base fisica dovrebbe uscire l'operazione.
3. Hai già organizzato i depositi operativi.
4. Hai già creato tutti i tipi di veicoli necessari.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Preparo il parcheggio North Depot e convalido che il vostro rapporto con il deposito e la linea L1 è coerente prima di continuare con viaggi vuoti e programmazione.**

Per creare o convalidare il parcheggio del caso:
1. In GoalBus, aprire il modulo **parcheggi** o **parcheggi** all'interno dell'infrastruttura di rete.
ref: P5_Imagen1.png | full
2. Vedi se il parcheggio di cui hai bisogno esiste già.
3. Se il parcheggio esiste già, aprilo e controlla la sua configurazione.
4. Se il parcheggio non esiste, creane una nuova.
ref: P5_Imagen2.png | compact(2x)
5. Definisce o convalida questi campi:
   1. **Codice** come breve identificatore per le viste compatte.
   2. **Nome corto** per viste compatte.
   3. **Nome lungo** come nome descrittivo del garage o del patio.
   4. **Coordinate** per individuare correttamente il parcheggio sulla mappa.
   5. **ID esterno**, se il cliente lavora con integrazioni ERP o HR.
6. Verificare che il parcheggio sia collegato al corretto **deposito** precedentemente creato.
ref: P5_Imagen6.png | compact(8.5x)
7. Fare clic su **Avanti** per configurare la capacità di parcheggio e i tipi di veicolo consentiti. Questo può essere modificato in futuro a mano che le condizioni cambiano.
ref: P5_Imagen7.png | compact(8.5x)
8. Controlla visualmente la mappa che la tua posizione ha senso per l'operazione effettiva.
9. Conferma che il sistema può già trattare quel parcheggio come la fonte o destinazione logistica dell'operazione.

Quando si termina questa sezione, si dovrebbe avere un posto auto adeguatamente geo-localizzato e adeguatamente subordinato al deposito appropriato.

## Convalida della coerenza tra parcheggio, deposito e linea

Ora che avete già impostato il parcheggio e lo stoccaggio, dovete verificare che questa infrastruttura si adatta alla logica di linea e l'efficienza logistica che GoalBus si aspetta. Il modello di linea stesso consente di definire **parcheggi o magazzini autorizzati** per costringere il sistema a iniziare il servizio dalle basi geograficamente corrette e minimizzare il chilometraggio vuoto. Questa non è una preferenza cosmetica: guidare il programmatore direttamente quando si costruiscono soluzioni.

Prima di continuare, assicurarsi che:
1. Il parcheggio è già collegato al deposito corretto.
2. Il magazzino ha già le sue posizioni autorizzate.

Per convalidare la coerenza completa dell'infrastruttura (se si dispone già di una linea):
1. Apri la configurazione **riga** che userai come riferimento.
2. Controllare la sezione **posti auto consentiti** o **Depositi autorizzati**.
3. Verificare che il deposito corretto sia autorizzato per avviare i servizi su quella linea.
4. Se il deposito corretto non è autorizzato, aggiungetelo.
5. Conferma che non stai lasciando depositi abilitati che non hanno un significato geografico per quella linea.
6. Controllare se il rapporto tra linea, deposito e parcheggio minimizza la guida senza reddito.
7. Conferma che l'infrastruttura fisica che hai appena preparato potrebbe supportare il servizio che creerai o calcolerai in seguito.
8. Se rilevate incongruenze, correggeteli prima di continuare.

Per il caso di riferimento, chiedetevi:
1. La linea L1 è autorizzata a partire dal North Depot?
2. Quel magazzino usa il parcheggio nord come base fisica?
3. La logica risultante riduce le miglia in un vuoto piuttosto che aumentarle?

Quando si termina questa sezione, si dovrebbe essere in grado di dire che la linea, il deposito e il parcheggio formano la stessa logica operativa e logistica.

## Letture aggiuntive

- [Rete master](P6_Preparazione_Della_Rete_Master_Con_Fermate_Linee_E_Percorsi.md)
