---
title: Definizione dei tipi di turni e delle regole dei turni
shortTitle: Tipi e norme
intro: Imparare a creare tipi di turni, organizzarli all'interno di modelli di regola
  e attivare le restrizioni o sanzioni necessarie per Scheduling per costruire compiti
  legalmente validi e operativi coerenti.
contentType: how-tos
versions:
- '*'
---
## Creazione dei tipi di turni che strutturano il lavoro

Prima di impostare le regole di shift, è necessario definire il **tipi di turni** che il sistema userà per raggruppare viaggi in un lavoro umano coerente. Un tipo di shift non è solo un tag visivo. È la categoria logica che guida il motore a costruire compiti riconoscibili e utilizzabili in seguito in liste, funzionamento quotidiano e integrazione con altri sistemi.

Utilizza questo avvio rapido quando hai già un'offerta validata, una logica del veicolo definita, e devi dire al sistema quali forme di lavoro sono valide per il tuo caso.

Prima di iniziare, assicurati che:
1. Hai già creato e convalidato l'offerta di servizio a P10.
2. Hai già convalidato la struttura operativa in P11.
3. Hai già definito le regole del veicolo in P12.
4. Siete chiari quale servizio e contesto operativo userete come riferimento.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Definirò i tipi di shift della linea L1 in modo che la programmazione possa costruire compiti coerenti prima di creare lo scenario di calcolo.**

Per creare i tipi di shift del tuo caso:
1. In GoalBus, andare a **Impostazioni** > **Personale** > **Tipi di turni**.
ref: P13_Imagen1.png | compact
2. Controllare se ci sono già tipi appropriati di turni per il vostro caso.
3. Se il tipo esiste già, aprilo e controlla se è ancora valido.
4. Se non esiste, creane una nuova.
5. Definisce questi campi:
   1. **Nome completo**, con un nome chiaro e descrittivo.
   2. **Nome corto**, per viste compatte e schede operative.
   3. **ID esterno**, se il cliente ha bisogno di integrazione con sistemi HR o paga.
ref: P13_Imagen2.png | compact
6. Segna il tipo come **Attivo** se dovete partecipare a calcoli futuri.
7. Salva il tizio del turno.
8. Ripeti il processo per ogni categoria di lavoro di cui hai davvero bisogno nel tuo caso.

Per il caso di riferimento, è possibile creare tipi come:
1. **Gira domani.**
2. **Svolta tardiva**
3. **Giro rotto**, se l'operazione richiede

Quando si conclude questa sezione, si dovrebbe avere i tipi di turni che serviranno come DNA dei compiti che Scheduling costruirà.

## Creazione o selezione del modello di regola di turno

Dopo aver creato i tipi di shift, è necessario definire il contenitore dove vivra' le regole. Le regole di turno non sono gestite come un elenco piatto, ma all'interno di **modelli** che raggruppa un insieme coerente di restrizioni per uno stadio, un periodo o una simulazione di concreto. Questo consente di mantenere diverse configurazioni senza miscelare le regole storiche con regole attive.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già creato o convalidato i tipi di turni che userai.
2. Sapete che servizio o simulazione userete come riferimento.
3. Siete già chiari se questo modello sarà riutilizzabile o specifico di caso.

Per creare o selezionare il modello di regola:
1. In GoalBus, andare a **Impostazioni** > **Personale** > **Regole di turno**.
2. Controlla se esiste già un **Regole tipo** adatto al tuo caso.
3. Se il modello esiste già, aprilo e controlla se è ancora valido.
4. Se non esiste, creare un nuovo modello cliccando su **Aggiungi un nuovo modello**.
5. Assegna un **Nome** chiaro al modello.
6. Se applicabile, aggiungere un **Designazione delle merci** che ne identifichi l'uso.
7. Salva il modello.
ref: P13_Imagen3.png | compact
8. Conferma che puoi già aggiungere regole all'interno del contenitore.

Per il caso di riferimento, un'opzione valida potrebbe essere:
- **Giri - L1**
- **Regole di turno**

Quando si conclude questa sezione, si dovrebbe avere un modello di regole preparati per ricevere specifiche restrizioni e sanzioni.

## Attivare le regole di turno come restrizioni o sanzioni

Ora si può iniziare a impostare le regole. Qui è importante distinguere due logiche:
1. **Restrizioni**, che sono obbligatorie e bloccano le attività non valide.
2. **Sanzioni**, che non blocca, ma spinge l'ottimizzatore verso le soluzioni preferite.

Questa differenza è fondamentale perché non tutto ciò che si desidera nell'operazione deve diventare un divieto assoluto. Alcune condizioni devono agire come guida e non come un muro.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già creato o selezionato un modello di regole.
2. Sai che comportamento di lavoro vuoi fermare.
3. Sai che comportamento vuoi favorire senza renderlo obbligatorio.

Per gestire le regole di turno del vostro caso:
1. Se vuoi creare una nuova regola, tocca **Aggiungere nuova regola**.
2. All'interno del modello di regola, controllare il **Modelli di regole** disponibile e dare un **Nome** e un **Designazione delle merci** alla nuova regola.
3. Selezionare il modello che corrisponde al controllo che si desidera applicare.
4. Crea un **regola specifica** da quel modello cliccando su **Conferma**.
ref: P13_Imagen4.png | compact
6. Decida **a quali tipi di spostamenti si applica ogni regola**. Non tutte le regole dovrebbero applicarsi a tutti i tipi. Alcune possono essere globali e altre dovrebbero riguardare categorie specifiche, come domani, pomeriggio o match.
7. Inserisci i parametri specifici della regola.
8. Mantieni la regola.
9. Ripeti il processo solo per le regole di cui il tuo caso ha davvero bisogno.
10. Verifica se le regole che devi applicare sono attive o no. Per potare una regola, deve essere stato assegnato ad almeno un tipo di turno.
ref: P13_Imagen5.png | compact(x19)

Per il caso di riferimento, pensate ad esempi quali:
1. Il turno di domani dovrebbe iniziare all'interno di una finestra specifica.
2. Un giro di divisione non deve superare un certo livello di ampiezza.
3. Una sequenza indesiderata può essere penalizzata piuttosto che vietata.

Quando si conclude questa sezione, si dovrebbe avere un insieme iniziale di regole che riflettono sia limiti obbligatori che preferenze operative.

## Verifica che le regole siano assegnate al tipo di turno corretto

Una volta che le regole sono state attivate, è necessario controllare **ai quali vengono applicati i tipi di turni**. Non tutte le regole dovrebbero applicarsi a tutti i tipi. Alcune possono essere globali e altre dovrebbero essere indirizzate a categorie specifiche, come domani, tardi o match.

Prima di continuare, assicurarsi che:
1. Hai già attivato almeno una regola all'interno del modello.
2. Hai già definito i tipi di turni coinvolti nel caso.
3. Sai se la regola dovrebbe essere globale o specifica.

Riesaminare adeguatamente il campo di applicazione:
1. Selezionare ogni regola che hai creato.
2. Controlla la sezione **Tipi di turni applicabili**.
3. Selezionare i tipi specifici ai quali dovrebbe applicarsi la regola.
4. Se la regola deve interessare tutti i tipi di scenario, impostarlo come globale selezionando **tutti i tipi di turni**.
5. Verificare che non ci siano due regole attive dello stesso modello che si applichino allo stesso tipo di spostamento se ciò generasse un conflitto logico.
6. Salva le impostazioni.
7. Ripetere la revisione per ogni regola del modello.

Per il caso di riferimento:
1. Una finestra di avvio anticipato può essere applicata solo a **Gira domani.**.
2. Una regola di riposo può essere applicata a diversi tipi.
3. Una preferenza generale potrebbe essere globale.

Quando si conclude questa sezione, si dovrebbero avere regole con una portata chiara e nessun conflitto logico con l'altro simile alla seguente immagine:
ref: P13_Imagen6.png | compact(x19)

## Verificare che la logica di turno rimanga compatibile con il servizio

L'ultimo passo è quello di verificare che i tipi di turni e le regole che avete appena definito sono ancora compatibili con l'offerta convalidata e con la logica dei veicoli che avete già chiuso. Non è utile avere delle regole buoni se il risultato lascia il servizio senza un modo realistico da programmare.

Prima di finire, assicurati che:
1. Hai già creato i tipi di turni di cui hai bisogno.
2. Hai già attivato e assegnato le regole corrispondenti.
3. Siete chiari che servizio sarà l'ingresso al palcoscenico.

Per convalidare che il caso è ancora funzionabile:
1. Controlla il servizio convalidato che userai come riferimento.
2. Controlla che i tipi di turni che hai creato possano organizzare quel lavoro.
3. Controllare se le regole di turno lasciano il caso troppo rigido.
4. Controlla che non vi sia una forte contraddizione con le regole del veicolo già attivate.
5. Chiedetevi se il sistema potrebbe già costruire compiti legali e operativi coerenti con questa base.
6. Se la risposta è sì, continuare con il prossimo inizio rapido.
7. Se la risposta è no, correggere i tipi o le regole prima di seguire.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. L'offerta L1 validata rimane compatibile con i tipi di turni definiti.
2. Le regole non bloccano inutilmente il caso.
3. Il modello è già pronto per entrare nella fase di programmazione.

Quando si conclude questa sezione, si dovrebbe essere in grado di dire che la logica dei turni è già abbastanza chiusa da passare alla creazione dello scenario di programmazione.

## Letture aggiuntive

- [Creazione della prima fase di programmazione](P14_Creazione_Della_Prima_Tappa_Di_Programmazione_Con_Il_Motore_Classic.md)
