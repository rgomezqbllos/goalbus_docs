---
title: Preparazione della rete master con fermate, linee e percorsi
shortTitle: Rete master
intro: Scopri come creare e convalidare la base di rete che utilizzerà la tua pianificazione,
  comprese le fermate, le linee e le rotte, in modo che i passaggi successivi nei
  tempi, nei servizi e nella pianificazione partano da una struttura coerente.
contentType: how-tos
versions:
- '*'
---
## Creare o validare le fermate che la rete userà

Prima di creare linee o percorsi, è necessario assicurarsi che il **interruzioni** che userete già esista e siano correttamente definiti. In GoalBus, una stop non è solo un punto geografico. È anche un'entità con identità operativa e più strati di nome che servono diversi spettatori, come pianificatori, passeggeri e dispositivi interni. Inoltre, il sistema consente di disabilitare le stop piuttosto che rimuoverle bruscamente, in modo da non rompere percorsi attivi o viaggi.

Usa questo avvio rapido quando hai già chiuso la base oraria in P2 e P3, e devi iniziare a costruire la rete base su cui potrai quindi definire percorsi, tempi di viaggio e servizi.

Prima di iniziare, assicurati che:

1. Hai già impostato i tipi di vacanze e giorni in P2.
2. Hai già convalidato l'anno operativo su P3.
3. Avete accesso all'ambiente con i permessi per consultare o modificare l'infrastruttura di rete.
4. Sei chiaro che linea o corridoio vuoi preparare come primo caso.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Preparerò la linea L1, creare o convalidare le vostre fermate di base e elencare i vostri percorsi di andata e ritorno per un uso successivo nel mio primo caso di Scheduling.**

Per creare o convalidare le fermate del caso:

1. In GoalBus, vai al modulo **Impostazioni di arresto** all'interno delle impostazioni di servizio.
ref: P6_Imagen1.png
2. Scopri se la base si ferma sul tuo caso esiste già.
3. Se esiste già una fermata, aprila e conferma che la tua identità è corretta.
4. Se un arresto non esiste, fare clic su **Nuova fermata**.
5. Inserisci o convalida questi campi:
   1. **Codice** come identificatore unico.
   2. **Denominazione commerciale** come nome del passeggero visibile.
   3. **Nome lungo** come riferimento descrittivo interno.
   4. **Nome corto** se ne hai bisogno per le viste compatte.
6. Definire la posizione della fermata per coordinate o direzione.
7. Aggiungere un **ID esterno** se si desidera un identificatore aggiuntivo.
8. Risparmia la fermata.
ref: P6_Imagen2.png | compact(20x)
9. Ripeti il processo fino a quando non avrai le soste minime necessarie per il tuo caso.
10. Se si rileva una vecchia fermata che non dovrebbe continuare ad essere utilizzata in una nuova pianificazione, passare a **Inattivo** invece di cancellarla.

Per il caso di riferimento, utilizzare una logica come questa:

1. Terminale nord
2. Centro
3. Ospedale
4. Università
5. Terminale Sud

Quando si termina questa sezione, si dovrebbe avere la base fermate pronte e in uno stato coerente per costruire la linea e i percorsi.

## Creazione o validazione della linea come contenitore operativo

Dopo le soste di base, è necessario controllare il **riga**. In GoalBus, una linea è più di un semplice numero di servizio. Si tratta di un contenitore logico operativo. Configurandolo correttamente, si definiscono i limiti fisici e logistici del servizio, come il tipo di flotta consentita o la geografia operativa di depositi e parcheggi che influenzano quindi l'ottimizzazione.

Prima di iniziare questa sezione, assicurarsi che:

1. Hai già controllato o creato le fermate di base sul tuo caso.
2. Sai che servizio vuoi rappresentare.
3. Siete chiari che la linea è il container amministrativo e non ancora il percorso fisico dettagliato.

Per creare o convalidare la linea di caso:

1. In GoalBus, vai al modulo **Impostazioni di rete**.
ref: P6_Imagen3.png
2. Vedi se la linea di cui hai bisogno esiste già.
3. Se la riga esiste già, aprila e controlla le impostazioni.
4. Se non esiste, creare una nuova linea cliccando su **Crea riga**.
5. Definisce o convalida:
   1. **Nome della riga** per il nome interno.
   2. **Nome corto** per viste compatte.
   3. **Denominazione commerciale**, se del caso.
   4. **Parcheggio** associato alla linea. **EYE: la precedente creazione dei parcheggi è necessaria.**
   5. **Tipi di veicoli** per associare i tipi di veicoli disponibili per la linea. **EYE: è necessaria la pre-creazione di tipi di veicoli.**
   6. **ID esterno** per aggiungere un identificatore aggiuntivo.
   7. **Colore** per assegnare un certo colore alla riga.
6. Controllate che la linea rappresenti davvero il servizio giusto.
7. Risparmia la linea.
ref: P6_Imagen4.png | compact(8.5x)8. Confirma que la línea ya puede usarse como contenedor para crear rutas específicas.

Per il caso di riferimento, si può pensare a una riga come:

- **L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1 L1**
- **L1: Terminale Nord - Terminale Sud**

Quando si termina questa sezione, si dovrebbe avere una linea chiara e utilizzabile sopra la quale si può quindi definire i percorsi per significato.

## Creazione o validazione delle rotte di andata e ritorno

Con la linea già pronta, è ora possibile lavorare con il **percorsi**. In GoalBus, un percorso è il percorso fisico reale che percorre un veicolo. La stessa linea può avere diversi percorsi validi, ad esempio giri brevi, deviazioni o entrate di magazzino. Il sistema organizza queste variazioni per direzione o senso, e protegge i percorsi in uso per evitare cambiamenti pericolosi nei servizi già attivi.

Prima di iniziare questa sezione, assicurarsi che:

1. Hai già creato o convalidato la riga.
2. Hai già le fermate di base che userai nella sequenza.
3. Sapete se si sta per creare un singolo percorso per significato o se il vostro caso ha già bisogno di varianti.

Per creare o convalidare i percorsi del tuo caso:

1. Nella tabella di riga principale, fare clic sulla riga che hai appena creato o convalidato per accedere alla vista percorso.
ref: P6_Imagen5.png
2. Utilizzare le schede o i comandi di sterzo per lavorare con **Sentido 1** e **Sentido 2**.
3. Controllare se c'è già un percorso adatto per il senso di cui avete bisogno.
4. Se la rotta non esiste, creare una nuova variazione di rotta per questo senso.
5. Definisce la sequenza di fermate nell'ordine corretto.
6. Conferma l'intestazione iniziale e l'intestazione finale.
7. Risparmia il percorso.
8. Ripetere la logica per il senso opposto.
9. Se si trova un percorso segnato come **In uso**, non cercare di alterare la sua geometria di base senza prima verificare se c'è un'alternativa sbloccata.


Per il caso di riferimento:
1. Definisce l'itinerario a senso unico:
   1. Terminale nord
   2. Centro
   3. Ospedale
   4. Università
   5. Terminale Sud
2. Definisce il percorso di ritorno:
   1. Terminale Sud
   2. Università
   3. Centro
   4. Terminale nord

Quando si conclude questa sezione, si dovrebbe avere una linea con i suoi percorsi principali per direzione, pronto per voi a rivedere sequenze, punti rilevanti e logica operativa nel prossimo inizio rapido.

## Letture aggiuntive

- [Revisione della rete operativa: sequenze, permessi di arresto e punti di relè]
