---
title: Definizione delle regole di registrazione per l'assegnazione del personale
shortTitle: Regole di registrazione
intro: Imparare come impostare le regole di base e avanzato Rostering in modo che
  l'assegnazione del personale rispetti i limiti di lavoro, criteri di equità, e le
  restrizioni operative reali prima di calcolare la tabella del personale.
contentType: how-tos
versions:
- '*'
---
## Capire cosa controllano le regole di Rostering

Prima di calcolare gli incarichi del personale, è necessario definire il **Regole di registrazione** che guiderà come i dipendenti sono assegnati ai turni. Queste regole non costruiscono il lavoro, perché questo passo è già stato risolto da Scheduling. Qui, quello che si fa è controllare come il lavoro è condiviso tra le persone reali, nel rispetto delle politiche operative, dei criteri di equità e dei limiti di lavoro.

Utilizza questo avvio rapido quando hai già una soluzione di programmazione abbastanza stabile, un modello di driver caricato e un distacco operativo rivisto.

Prima di iniziare, assicurati che:
1. Hai gia' chiuso la transizione da Scheduling alla P19.
2. Hai già caricato e controllato i driver su P20.
3. Hai già convalidato il distacco operativo a P21.
4. Siete già chiari che soluzione di programmazione fungerà da base.
5. Sapete quale collettivo o gruppo di dipendenti sarà influenzato dal calcolo.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Configurerò le regole di registrazione per la linea L1 e il suo gruppo di piloti, in modo che il calcolo attribuisca personale reale rispetto alle pause, ai limiti di lavoro e ai criteri operativi.**

Comprendere il ruolo di queste regole:
1. Tratta le regole di Rostering come restrizioni e preferenze sull'assegnazione delle persone.
2. Utilizzare queste regole quando si desidera controllare:
   1. interruzioni,
   2. orario di lavoro,
   3. modelli settimanali,
   4. gruppo di lavoro,
   5. accoppiamenti,
   6. e altri criteri di equità o di politica interna.
3. Non utilizzare queste regole per correggere i problemi di:
   1. offerta,
   2. volte,
   3. galleggianti,
   4. o la costruzione della base a turni.
4. Se trovate che il problema rimane strutturale, tornate a Scheduling prima di continuare.

Quando si conclude questa sezione, si dovrebbe essere chiari che le regole di registrazione governano le persone e non la struttura di base del lavoro.

## Distinzione tra norme di base e norme avanzate

Prima di creare un modello di regola, è necessario distinguere due livelli di configurazione:
1. **Regole di base**
2. **Regole avanzate**

Le regole di base sono progettate per configurare rapidamente le restrizioni comuni. Sono utili quando si desidera una parametrizzazione agile o un test iniziale. Le regole avanzate sono progettate per modellare più precisamente restrizioni e preferenze attraverso limiti e penalità.

Prima di iniziare questa sezione, assicurarsi che:
1. Sai se il tuo caso ha bisogno di velocità o precisione.
2. Lei capisce che le regole di base hanno meno flessibilità di modellazione di quelle avanzate.
3. Sai se hai bisogno di modelli diversi a seconda dell'uso.

Per scegliere il tipo giusto di regole:
1. Usa **Norme di base** se vuoi coprire rapidamente le restrizioni comuni.
2. Usa **norme avanzate** se hai bisogno di modellare in dettaglio politiche complesse, accordi o condizioni operative specifiche.
3. Si noti che le regole di base attive si applicano sia nelle operazioni quotidiane che negli scenari di calcolo dell'assegnazione.
4. Se avete bisogno di modelli diversi per contesti diversi, ad esempio uno per il funzionamento quotidiano e uno per il calcolo futuro, lavorare con regole avanzate.
5. Decidi quale approccio userai prima di iniziare a parametrizzare.

Per il caso di riferimento, utilizzare questa logica:
1. Se stai iniziando e vuoi un primo livello di controllo, inizia con le regole di base.
2. Se già sapete che dovrete regolare le preferenze, le penalità o i modelli per contesto, continuate con le regole avanzate.

Quando si conclude questa sezione, si dovrebbe essere chiari se il caso sarà risolto con regole di base, avanzate o una combinazione controllata di entrambi.

## Attivare le regole di base più comuni per un primo incarico

Se il caso ha bisogno di una rapida configurazione iniziale, puoi iniziare con **Norme di base**. Questi coprono le restrizioni più comuni e ti permettono di avviare il calcolo su una base ragionevole prima di inserire livelli di controllo più sottili.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già deciso di iniziare con le regole di base.
2. Sai quali restrizioni minime vuoi imporre.
3. Siete chiari che non tutte le regole devono essere attivate per impostazione predefinita.

Per attivare le regole di base:
1. In GoalBus, andare a **Impostazioni** > **Regole di attribuzione**.
ref: P22_Imagen1.png | compact
2. Aprire la sezione **Regole di base**.
3. Consulta il catalogo delle regole di base disponibili.
ref: P22_Imagen2.png | full
4. Attiva solo quelli che corrispondono al caso che stai costruendo.
5. Set, al momento dell'applicazione:
   1. limiti generali,
   2. limiti specifici per le proprietà dei dipendenti,
   3. o eccezioni per alcuni dipendenti.
6. Salva i cambiamenti.
7. Verifica che le regole attive riflettano realmente le politiche che vuoi imporre.

Una prima base delle norme di base può comprendere:
1. **Schema di lavoro**
2. **Riposo tra giorni**
3. **Orario di lavoro mensile**
4. **Orario di lavoro settimanale**
5. **Giorno libero a settimana**
6. **Pubblicata la prima soluzione**
7. **Gruppo di lavoro**
8. **Abbinamento**
9. **Compatibilità dell'assegnazione**
10. **Abilita la riga**
11. **Svolta della prima soluzione pubblicata**
12. **Giorni lavorativi successivi**, quando applicato

Per il caso di riferimento, non attivare una regola solo perché esiste. Attivarla solo se:
1. risponde ad un vero bisogno,
2. Puoi spiegare perche' ne hai bisogno.
3. E sai come influenzerà l'incarico.

Quando si termina questa sezione, si dovrebbe avere una prima base di controllo per l'assegnazione del personale.

## Creare un modello di regole avanzate quando si ha bisogno di più precisione

Se le regole di base non sono sufficienti, il passo successivo è quello di creare un **modello di norme avanzate**. Questo approccio permette di controllare accuratamente come vengono generati gli incarichi, adeguando i limiti e le preferenze secondo le politiche aziendali, gli accordi di lavoro e le condizioni operative reali.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già identificato quale parte del caso non può essere risolta bene con le regole di base.
2. Sai quali comportamenti dovrebbero essere obbligatori e che preferivano solo.
3. Hai già bisogno di un modello più raffinato che possa essere riutilizzato per scenario o contesto.

Per creare un modello di regole avanzate:
1. In **Impostazioni** > **Regole di attribuzione**, aprire la sezione **Regole tipo**.
2. Crea un nuovo modello di regole.
3. Assegna un **nome** chiaro al modello.
4. Aggiungete un **descrizione** che vi permette di distinguerlo dagli altri modelli.
5. Salva il modello.
ref: P22_Imagen3.png | compact
6. Inizia ad aggiungere regole avanzate uno per uno.
7. Per ogni regola, decidere:
   1. se agisce come limite obbligatorio,
   2. o se agisce come una preferenza per sanzione.
8. Salva le impostazioni del modello.
9. Attiva il modello di regola creato.
10. Verificare che il modello possa già essere assegnato al corretto calcolo della Rostering.

Per il caso di riferimento, un'opzione valida potrebbe essere:
- **Costering L1 utilizzabile**
- **Assegnazione del conducente L1 - Regole avanzate**

Quando si termina questa sezione, si dovrebbe avere un modello avanzato pronto a rappresentare restrizioni e preferenze più complesse.

## Riferimento delle regole al corretto collettivo e al calcolo effettivo

Dopo aver attivato le regole di base o creato un modello avanzato, è necessario verificare che le regole si applicano al corretto collettivo e che non si stanno imponendo restrizioni astratte non correlate al calcolo effettivo.

Prima di continuare, assicurarsi che:
1. Hai già attivato le regole di base o hai creato un modello avanzato.
2. Sapete quali dipendenti, gruppi o depositi parteciperanno al calcolo.
3. Siete chiari che cosa la soluzione di programmazione servirà come input.

Per collegare correttamente le regole al contesto di calcolo:
1. Controlla il gruppo di personale a cui si applicherà la Rostering.
2. Controllare se le regole incidono:
   1. tutto il personale coinvolto,
   2. a un gruppo specifico,
   3. o dipendenti con proprietà specifiche.
3. Confermate che non state imponendo regole alle persone che non parteciperanno neppure a questo calcolo.
4. Controllare se la logica dello scenario di programmazione è ancora compatibile con queste regole.
5. Se una regola rende la divisione del lavoro infunzionabile, aggiusta il suo limite o la sua portata.
6. Salva la versione finale della configurazione.

Per il caso di riferimento, chiedetevi:
1. Queste regole sono destinate ai conducenti che copriranno effettivamente L1?
2. Il gruppo di lavoro è interessato a quello giusto?
3. L'incarico è ancora valido dopo l'attivazione di queste regole?

Quando si termina questa sezione, si dovrebbe avere un insieme di regole collegate a persone reali e con un calcolo Rostering specifico.

## Conferma che la base delle regole è già pronta a calcolare la Rostering

L'ultimo passo è quello di assicurarsi che le impostazioni siano pronte per alimentare il calcolo dello staff. Non si tratta solo di attivare le regole, ma avendo lasciato una base coerente, comprensibile e applicabile.

Prima di finire, assicurati che:
1. Hai già scelto tra le regole di base e quelle avanzate, secondo il caso.
2. Avete già attivato o modellato le restrizioni necessarie.
3. Hai già collegato la logica al giusto collettivo.
4. Hai già controllato che l'incarico sia ancora valido.

Per convalidare che la base delle regole è già pronta:
1. Controlla l'ultimo set di regole attive.
2. Conferma che ognuno risponde ad un vero bisogno.
3. Chiedetevi se il sistema potrebbe già:
   1. bloccare incarichi non validi,
   2. rispetto dei riposi e dei limiti,
   3. riflettere i criteri di equità e il gruppo di lavoro,
   4. e continuare a generare una soluzione utilizzabile.
4. Se la risposta è sì, continuare con il prossimo inizio rapido.
5. Se la risposta è no, aggiustare le regole prima di seguire.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. Le regole di registrazione per L1 sono ormai chiare.
2. Sai perche' hai attivato ogni regola.
3. Il sistema può ancora assegnare persone reali con quella configurazione.
4. La base è già pronta a trattare la disponibilità del personale e le eccezioni.

Quando si conclude questa sezione, si dovrebbe avere una base di regole di registrazione abbastanza forte per passare al trattamento delle assenze, inattività e disponibilità.

## Letture aggiuntive

- [Gestione delle assenze, dell'inattività e della disponibilità del personale](P23_Gestione_Delle_Assenze_Dellinattività_E_Della_Disponibilità_Del_Personale.md)
