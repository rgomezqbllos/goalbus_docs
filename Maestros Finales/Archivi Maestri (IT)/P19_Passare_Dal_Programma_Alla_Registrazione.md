---
title: Passare dal programma alla registrazione
shortTitle: Dalle scadenze alla registrazione
intro: Scopri cosa dovrebbe essere pronto nella programmazione prima di entrare in
  Rostering, quali informazioni ereditano l'assegnazione del personale, e quali problemi
  dovrebbero essere risolti prima di calcolare i veri driver.
contentType: how-tos
versions:
- '*'
---
## Conferma che dovrebbe essere chiuso a Scheduling prima di trasferirsi a Rostering

Prima di entrare in Rostering, è necessario verificare che Scheduling già lasciato una base sufficientemente stabile. Rostering non sostituisce Scheduling. Rostering parte del lavoro già costruito e decide come assegnare a persone reali.

Usa questo avvio rapido quando hai già una soluzione calcolata e validata di programmazione, e devi decidere se puoi iniziare a lavorare con personale reale.

Prima di iniziare, assicurati che:
1. Hai già creato, calcolato e convalidato lo scenario di Schedulering.
2. Hai già rivisto l'offerta di servizio e la sua consistenza complessiva.
3. Sapete quali linee, che tipo di giorno e quale soluzione userete come riferimento.
4. E' chiaro che Rostering non e' il posto giusto per sistemare una cattiva base strutturale per il programma.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Confermo che la soluzione convalidata di Scheduling per la linea L1 è abbastanza matura da passare alla Rostering e iniziare ad assegnare il lavoro ai veri piloti.**

Per confermare che il programma è pronto:
1. Apri lo scenario di programmazione che userai come riferimento.
2. Controlla che la tua condizione sia già corretta per smettere di trattarla come una bozza di lavoro.
3. Verificare che l'offerta utilizzata sia ancora quella giusta.
4. Verificare che la logica dei veicoli e la logica dei turni siano già state applicate.
5. Essa conferma che non vi sono evidenti incoerenze strutturali nella soluzione.
6. Se è ancora necessario rifare la base del veicolo, orari, servizi o regole, tornare a Schedule prima di seguire.
7. Se la soluzione è già stabile, continuare al passo successivo.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. La soluzione L1 è già stata calcolata.
2. E' stato controllato.
3. Non c'è più bisogno di correzioni strutturali da Schedulering.
4. Ora può essere trattato come una base di lavoro per il personale.

Quando concluderete questa sezione, dovrete chiarire se Scheduling ha già fornito una base utilizzabile per la Rostering.

## Capire cosa eredita l'iscrizione dalla programmazione

Una volta che la base è confermata, è necessario capire quali informazioni accade da Schedule a Rostering. Qui la chiave è di non pensare che Rostering parte da zero. Rostering eredita il lavoro già strutturato e da lì decide quale persona reale può assumerlo.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già identificato la soluzione di programmazione che userai.
2. Sai che parte di questa soluzione dovrebbe rimanere stabile.
3. Capisci che Rostering lavora su un lavoro già costruito, non su un'offerta non strutturata.

Per capire cosa eredita la Rostering:
1. Controllare la soluzione convalidata di programmazione.
2. Identificare i compiti, i blocchi o le strutture di lavoro che serviranno da base.
3. Verificare che la soluzione abbia già una forma funzionalmente riconoscibile.
4. Tenete presente che, trasferendovi alla Rostering, il sistema non sta più creando lavoro astratto, ma cercando di assegnare quel lavoro a persone reali.
5. Usa questa regola di lettura:
   1. La programmazione definisce **che lavoro esiste**.
   2. La registrazione definisce **Chi farà quel lavoro?**.

Per il caso di riferimento, chiedetevi:
1. La soluzione L1 ha già un lavoro abbastanza chiaro da assegnarla?
2. I blocchi di lavoro sono riconoscibili e utilizzabili?
3. Il problema che resta da risolvere è già di persone e non di struttura?

Quando si conclude questa sezione, si dovrebbe capire cosa Rostering eredita e cosa non dovrebbe essere ridefinito lì di nuovo.

## Distinguendo quali problemi si risolvono nel programma e quali nella lista

Prima di passare finalmente al livello personale, è necessario separare molto bene le responsabilità. Questa distinzione è fondamentale perché molti errori appaiono quando si cerca di correggere in Rostering qualcosa che avrebbe dovuto essere risolto in precedenza in Scheduling.

Prima di continuare, assicurarsi che:
1. Sai che palcoscenico sarà il programma alla base.
2. Capisci che Rostering consuma una soluzione precedente.
3. Siete pronti a distinguere i problemi strutturali dai problemi del personale.

Per separare correttamente entrambi i domini:
1. Tratta come un problema **Programmazione** qualsiasi materia legata a:
   1. struttura del servizio,
   2. Logica della flotta,
   3. volte,
   4. norme sui veicoli,
   5. i tipi di turni e la loro costruzione di base.
2. Tratta come un problema **Registrazione** qualsiasi materia legata a:
   1. disponibilità effettiva del conducente,
   2. distacco al deposito o al gruppo,
   3. assenze,
   4. inattività,
   5. trasferimenti o trasferimenti,
   6. l'ammissibilità reale a ricevere un turno.
3. Se si rileva un'incoerenza di lavoro che colpisce l'intera struttura, tornare a Scheduling.
4. Se rilevate l'incoerenza di una persona, risolvetela nella Rostering.

Per il caso di riferimento, utilizzare questa logica:
1. Se il problema è che il lavoro di L1 è stato mal costruito, tornare a Schedulering.
2. Se il problema è che non sai quale vero autista può prendere quel lavoro, stai entrando nella Rostering correttamente.

Quando si conclude questa sezione, si dovrebbe essere in grado di spiegare chiaramente cosa si dovrebbe correggere prima di passare al personale e ciò che appartiene al modulo successivo.

## Confermare ciò che dovrebbe essere pronto dal lato dello staff prima di calcolare la Rostering

Ora che si sa cosa Rostering riceve, è necessario controllare ciò che deve esistere sul lato dello staff in modo che il seguente calcolo ha senso. Non è sufficiente per avere un buon programma se ancora non avete una base minima di persone, distaccamenti e disponibilità.

Prima di iniziare questa sezione, assicurarsi che:
1. Avete già una base valida da Scheduling.
2. Sai quali gruppi, depositi o contesti operativi influiscono sulle persone.
3. Siete pronti a controllare il livello del personale.

Per confermare che la base del personale è pronta:
1. Controlla che c'è già un gruppo di personale che può ricevere il lavoro.
2. Verificare che le persone sono collegate al contesto corretto quando si applica.
3. Verifica di non inserire Rostering senza informazioni sulla disponibilità minima.
4. Controllare se la struttura necessaria esiste già per:
   1. Regole di registrazione,
   2. assenze,
   3. inattività,
   4. trasferimenti o trasferimenti, se del caso.
5. Se non avete ancora questa base, non lanciate il calcolo dello staff.
6. Se la base esiste già o è almeno in pista, proseguire con la seguente rapida partenza da Rostering.

Per il caso di riferimento, chiedetevi:
1. Esiste già lo staff che sarà in grado di ricevere la soluzione L1?
2. Quel personale appartiene al regno giusto?
3. La base di disponibilità e distacco è già minimamente preparata?

Quando si termina questa sezione, si dovrebbe essere chiari se il lato staff è già pronto per entrare in Rostering.

## Chiarire il punto di transizione tra programmazione e registrazione

L'ultimo passo è quello di chiudere mentalmente la transizione. Questo rapido inizio non intende ancora calcolare l'assegnazione dello staff. Lo scopo è di rendere molto chiaro quando terminerà la programmazione e quando inizierà la registrazione in modo da non mescolare entrambi i domini.

Prima di finire, assicurati che:
1. Hai già controllato la soluzione di Scheduling.
2. Capisci cosa eredita la Rostering.
3. Avete già separato i problemi strutturali dai problemi di personale.
4. Hai gia' controllato per vedere se c'e' una base minima di personale.

Per chiudere correttamente la transizione:
1. Tratta la soluzione convalidata di programmazione come un input formale di registrazione.
2. Non continuare a alterare quella base a meno che non si scopra un vero problema strutturale.
3. Utilizzare le seguenti iniziali rapidi per prepararsi:
   1. Regole di registrazione,
   2. assenze e inattività,
   3. trasferimenti, assegnazioni e modifiche di distacco.
4. Considera che l'obiettivo cambia da qui:
   1. Non si tratta piu' di costruire lavori.
   2. Ora si tratta di assegnarlo a persone vere.
5. Se potete affermarlo chiaramente, la transizione è ben fatta.

Per il caso di riferimento, finite questo avvio rapido solo quando potete dire:
1. La programmazione ha già lasciato una soluzione L1 stabile.
2. Il problema successivo non è più strutturale, ma rappresentanza del personale.
3. Ora puoi inserire il livello di regola della Rostering.

Quando si termina questa sezione, si dovrebbe avere una transizione chiara e controllata tra Scheduling e Rostering.

## Letture aggiuntive

- [Definizione delle regole di registrazione per l'assegnazione del personale](P20_Caricamento_E_Gestione_Driver.md)
