---
title: Gestione delle assenze, dell'inattività e della disponibilità del personale
shortTitle: Disponibilità personale
intro: Scopri come registrare assenze, inattività e restrizioni di disponibilità in
  modo che la Rostering assegna solo a persone veramente ammissibili e non tenta di
  coprire il lavoro con driver non disponibili.
contentType: how-tos
versions:
- '*'
---
## Comprendere la differenza tra assenza, inattività e disponibilità

Prima di calcolare la Rostering, è necessario controllare quali persone sono veramente disponibili per lavorare. In questo livello non è più sufficiente per il driver di esistere, essere collegato al contesto corretto e avere le regole applicabili. È anche necessario dire al sistema se quella persona:
1. è disponibile,
2. è assente,
3. E' inattivo.
4. o ha una disponibilità parziale o limitata.

Utilizza questo avvio rapido quando hai già caricato i driver, rivedere il loro distacco operativo e preparare la base delle regole di registrazione, e è necessario evitare che il calcolo di cercare di assegnare il lavoro a persone non ammissibili.

Prima di iniziare, assicurati che:
1. Hai già caricato e controllato i driver su P20.
2. Ha già convalidato il suo distacco operativo alla P21.
3. Hai già definito la base delle regole di Rostering in P22.
4. È chiaro a voi quale gruppo di personale parteciperà al calcolo.
5. Sapete se nella vostra operazione dovete registrare vacanze, vittime, permessi, indisponibilità parziale o stati non operativi.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Sto andando a registrare assenze, inattività e restrizioni di disponibilità sui piloti che copriranno la linea L1 per assicurarmi che la Rostering assegna solo il lavoro a persone veramente ammissibili.**

Per capire correttamente questi concetti:
1. Utilizzare un **assenza** quando la persona esiste e appartiene al collettivo, ma non è disponibile per un periodo specifico.
2. Utilizzare un **inattività** quando la persona deve essere esclusa dal funzionamento per un periodo più strutturale o non deve partecipare al calcolo.
3. Utilizzare un **limitazione della disponibilità** quando la persona può lavorare, ma non in ogni momento o non in tutte le condizioni.
4. Non mescolare questi concetti come se fossero uguali.
5. Usa questa regola di lettura:
   1. **assenza** = non può funzionare per un determinato periodo,
   2. **inattività** = non deve essere trattato come una risorsa operativa in tale contesto o periodo,
   3. **disponibilità limitata** = può funzionare, ma con limiti.

Per registrare i tipi di assenze, inattività o indisponibilità:
1. In GoalBus, è necessario aprire **Impostazioni** > **Personale** > **Impostazioni di assenza**.
ref: P23_Imagen1.png | compact
2. Verifica se vengono creati tutti i tipi di assenza di cui hai bisogno.
3. Se non c'è assenza o è necessario crearne una nuova, fare clic sul pulsante **Crea nuova assenza**.
ref: P23_Imagen2.png | compact(2x)
4. Per creare un nuovo tipo di assenza, i seguenti campi devono essere compilati:
   1. **Nome dell'assenza**: nome del tipo di assenza da creare.
   2. **Nome corto**: per le viste compatte.
   3. **ID del conducente di obiettivo**: codice interno se si lavora con le integrazioni.
   4. **Categoria di assunzione**: Può essere **Puro**, **Gratuito** o **Lavoro**. A seconda di quello che si sceglie, si deve assegnare una durata (**Tempo** o **Giorno intero**), una durata di **Orario di lavoro** o **Giorni massimi**.
   5. **Ammissibilità all'assegnazione del lavoro**: Se puoi scegliere il driver da assegnare o no, nonostante la tua assenza.
   6. Selezionare se questo tipo di assenza sarà **Richiedibile dal conducente**.
5. Risparmia il nuovo tipo di assenza.
ref: P23_Imagen3.png | compact(x10)
6. Essa continua a registrare tutti i tipi di assenza necessari.
7. Conferma che hai tutti i tipi di assenza necessari per la tua pianificazione.

Quando si conclude questa sezione, si dovrebbe avere una visione chiara di che tipo di assenza si sarà in grado di utilizzare nella vostra pianificazione di torrefazione e che si sarà in grado di assegnare a diversi driver. fileciteturn22file3L1-L20 fileciteturn22file2L1-L18

## Registrazione delle assenze programmate del conducente

Le assenze previste sono uno dei primi elementi da caricare prima del calcolo della Rostering. Ecco le vacanze, i permessi, le disabilità, le licenze o qualsiasi altro periodo in cui una persona non deve ricevere un lavoro.

Prima di iniziare questa sezione, assicurarsi che:
1. Sapete quali piloti avranno assenza all'interno dell'orizzonte di calcolo.
2. Conosci le date esatte o approssimative di quelle assenze.
3. Vuoi lasciare il sistema senza ambiguità circa i giorni in cui una persona non può essere usata.
4. Hai già creato tutti i tipi di assenza necessari.

Per registrare le assenza dal profilo del conducente:
1. In GoalBus, è necessario aprire **Impostazioni** > **Personale** > **Gestione del conducente**.
ref: P23_Imagen4.png | compact
2. Fare clic sul pulsante sulla barra superiore per caricare i dati di assenza.
ref: P23_Imagen5.png | compact(3x)
3. Selezionare l' azione **Assenze di personale**.
ref: P23_Imagen6.png | compact
4. Carica il file di assenza dello staff nella finestra pop-up. In quella finestra è possibile rivedere il formato del file di assenza, leggendo le istruzioni o scaricando un modello di esempio.
ref: P23_Imagen7.png | full
5. Conferma il carico del file.
6. Tieni il registro.
7. Ora è possibile controllare le assenza caricate nel profilo di ogni driver.

Per il caso di riferimento, una logica minima potrebbe essere:
1. Autista A: vacanza da 10 a 20
2. Autista B: permesso il 14
3. Autista C: Incapacità per una settimana specifica

Quando hai finito questa sezione, avresti dovuto registrare le principali assenza che influenzano il calcolo della Rostering.

## Controllo che la registrazione già vede l'ammissibilità effettiva correttamente

L'ultimo passo è quello di convalidare che la combinazione tra driver, distaccamento, regole e disponibilità rifletta già la realtà del calcolo. Qui l'obiettivo è quello di garantire che la registrazione non cercherà di assegnare il lavoro a persone assenti, inattive o mal restritte, né lascerà fuori le persone che dovrebbero essere ammissibili.

Prima di finire, assicurati che:
1. Hai gia' registrato delle assenza rilevanti.
2. Se necessario, avete già configurato le disponibilità parziali.
3. Sapete quale collettivo userà il seguente calcolo.

Per verificare che la disponibilità sia già ben modellata:
1. Torna alla lista generale dei piloti.
2. Rivedere diversi profili rappresentativi del collettivo.
3. Conferma che gli assenti hanno i loro periodi correttamente registrati.
4. Conferma che le restrizioni parziali non sono modellate come assenze totali per errore.
5. Chiedetevi se il sistema potrebbe già:
   1. escludere coloro che non dovrebbero lavorare,
   2. compresi coloro che possono lavorare,
   3. e rispettare restrizioni parziali senza rompere il calcolo.
6. Se la risposta è sì, continuare con il prossimo inizio rapido.
7. Se la risposta è no, correggere i registri prima di continuare.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. I piloti L1 hanno già la loro reale disponibilità ben riflessa.
2. Le assenze sono caricate.
3. L'inattività è differenziata.
4. Le restrizioni parziali non sono state confuse con astensioni complete.

Quando si conclude questa sezione, si dovrebbe avere una base di disponibilità sufficientemente affidabile per passare ad assegnazioni, trasferimenti e modifiche di distacco.

## Letture aggiuntive

- [Gestione dei trasferimenti, assegnazioni e modifiche di distacco](P24_Gestione_Dei_Trasferimenti_Assegnazioni_E_Modifiche_Di_Distacco.md)
