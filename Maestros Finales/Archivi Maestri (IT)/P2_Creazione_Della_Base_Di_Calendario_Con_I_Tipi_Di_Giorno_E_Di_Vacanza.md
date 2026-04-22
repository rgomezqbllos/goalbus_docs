---
title: Creazione della base di calendario con i tipi di giorno e di vacanza
shortTitle: Tipi di giorni e festività
intro: Scopri come impostare i tipi di giorno e le vacanze in modo che la logica di
  pianificazione applichi il corretto modello operativo prima di passare ai percorsi,
  ai tempi di viaggio e alla creazione di servizi.
contentType: how-tos
versions:
- '*'
---
## Creazione del tipo di giorno che si userà per pianificare

Prima di creare servizi o di lanciare calcoli di pianificazione, è necessario definire la logica del calendario che indica al sistema che tipo di giorno si sta lavorando con. A GoalBus, i tipi di giorno sono le categorie operative che raggruppano giorni come lavori standard, venerdì, fine settimana o giorni speciali, in modo da non dover costruire la data logica di pianificazione per data.

Utilizza questo rapido inizio quando stai preparando il tuo primo caso di pianificazione, quando devi creare o convalidare il tipo di giorno che la tua fase userà, o quando vuoi assicurarti che la logica di vacanza sia pronta prima di continuare.

Prima di iniziare, assicurati che:
1. Avete accesso all'ambiente con i permessi per visualizzare o modificare le impostazioni del calendario.
2. Sai che caso di pianificazione vuoi costruire.
3. Sapete che periodo volete preparare, per esempio gennaio 2026.
4. Hai già rivisto il tuo ruolo di pianificazione e il flusso complessivo in P1.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Sto preparando la base del calendario per uno scenario di lavoro del gennaio 2026, compreso il corretto comportamento delle festività.**

Per creare o convalidare il tipo di giorno del tuo caso:
1. In GoalBus, andare a **Impostazioni** > **Gestione del tempo** > **Gestione dei tipi di giorno**.
ref: P2_Imagen1.png | compact
2. Controllare i tipi di giorno esistenti e vedere se c'è già uno che rappresenta la logica operativa di cui avete bisogno.
3. Se esiste già un tipo appropriato di giorno, esso conferma che:
   1. Il suo nome è chiaro.
   2. Il suo nome è chiaro.
   3. Rappresenta davvero lo schema operativo di cui hai bisogno.
4. Se non esiste un tipo di giorno corretto, fare clic su **Crea tipo di giorno**.
ref: P2_Imagen2.png | compact(2x)
5. Definire **nome** e **nome corto** per il nuovo tipo di giorno.
ref: P2_Imagen3.png | compact(8.5x)
6. Selezionare i giorni della settimana che si applicano a questo tipo di giorno.
ref: P2_Imagen4.png | compact(8.5x8)
7. Se il tipo di giorno dovrebbe applicarsi anche ai giorni festivi, attivare l'opzione di applicare il tipo di giorno ai giorni festivi.
ref: P2_Imagen5.png | compact(8.5x8)
8. Salvare il ragazzo del giorno.
9. Controlla il risultato e conferma che il tipo di giorno ora rappresenta chiaramente il caso che stai preparando.

Quando si termina questa sezione, si dovrebbe avere una sorta di giorno che il sistema può utilizzare come una categoria operativa per il vostro caso di pianificazione.

## Registrazione di vacanze che alterano la logica normale del calendario

Dopo aver definito il tipo di giorno generale, è necessario dire al sistema cosa fare con le date eccezionali. Le festività sono importanti perché il calendario può dire che una data è martedì, mentre l'operazione dovrebbe comportarsi come una domenica o come un altro modello speciale. Se non si registrano bene le festività, il sistema può applicare il piano sbagliato quando si pubblica più tardi o calcola gli scenari.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai creato o confermato il tipo di giorno che il tuo caso userà.
2. Sapete se il periodo di pianificazione include festività o date speciali.
3. Siete pronti a decidere quale modello operativo dovrebbe seguire ogni vacanza.

Per registrare e convalidare le festività del vostro caso:
1. Nella stessa sezione di gestione di tipo giorno, passare alla scheda **Vacanze**.
ref: P2_Imagen6.png | compact
2. Controllare se la vacanza di cui hai bisogno esiste già nel sistema.
3. Se la vacanza non esiste, creare un nuovo record di vacanza.
4. Se la vacanza esiste già, aprila e controlla le sue impostazioni.
5. Inserire o confermare il **nome** della vacanza.
6. Assegna il corretto **tipo di giorno** a quella vacanza.
ref: P2_Imagen7.png | compact
7. Tieni il registro delle feste.
8. Ripetere questo processo per qualsiasi altra vacanza che influisca sul periodo che si sta preparando.
9. Controllare l'elenco delle vacanze e confermare che ogni data eccezionale indica il corretto modello operativo.

Per il caso di riferimento, fatevi queste domande:
1. Il gennaio 2026 include una vacanza che dovrebbe comportarsi diversa da una normale praticabile?
2. Quella festa dovrebbe comportarsi come domenica, come sabato, o come un altro tipo di giorno speciale?
3. Se si pubblicasse uno scenario per questo periodo, il sistema saprebbe esattamente quale modello applicare a quella data?

Quando si conclude questa sezione, il sistema dovrebbe essere in grado di sostituire il normale comportamento di calendario alle date di vacanza che contano per voi.

## Controllo che la vostra base di calendario è pronta a pianificare

Ora che avete già definito il tipo di giorno generale e le eccezioni di vacanza, dovete confermare che la base del calendario è davvero utilizzabile. Questo è il passo in cui si verifica che la struttura che avete creato può tenere le seguenti iniziali rapidi senza introdurre errori evitabili.

Prima di continuare, assicurarsi che:
1. Il tipo di giorno esiste e ha la corretta logica settimanale.
2. Le relative festività sono registrate.
3. Ogni vacanza è collegata al tipo di giorno giusto.
4. Il suo caso di pianificazione rimane chiaro e concreto.

Per convalidare la base del calendario prima di passare al prossimo avvio rapido:
1. Revidi il caso di pianificazione che hai definito all'inizio di questo articolo.
2. Conferma che il tipo di giorno che hai creato o convalidato corrisponde a quel caso.
3. Confermare che ogni vacanza entro il periodo di pianificazione è stata registrata e associata al tipo di giorno corretto.
4. Controllare se l'opzione app vacanza che hai attivato nel tipo di giorno realmente riflette il comportamento che vuoi.
5. Chiedetevi se il sistema potrebbe già distinguere:
   1. giorni normali del periodo; e
   2. le date eccezionali da seguire da un altro modello operativo.
6. Se la risposta è sì, continuare con il prossimo inizio rapido.
7. Se la risposta è no, tornare indietro e correggere il tipo di giorno o l'associazione di vacanza prima di continuare.

Alla fine di questa sezione, si dovrebbe essere in grado di affermare che il vostro caso di pianificazione ha una base di calendario affidabile e che i seguenti avvi rapidi possono contare su di esso senza ereditare un errore logico temporaneo.

## Letture aggiuntive

- [Convalida dell'anno operativo prima della pianificazione](P3_Convalida_Dellanno_Operativo_Prima_Della_Pianificazione.md)
