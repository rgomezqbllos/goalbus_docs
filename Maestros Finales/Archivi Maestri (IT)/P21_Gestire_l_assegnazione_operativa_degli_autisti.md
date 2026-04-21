---
title: Gestire l’assegnazione operativa dell’autista
shortTitle: Assegnazione operativa
intro: 'Scopri come collegare ogni autista a depot, business unit e work group e capire come questa assegnazione condiziona l’idoneità reale prima di passare a regole, assenze e calcolo di Rostering.'
contentType: how-tos
versions:
  - '*'
---

## Capire l’assegnazione operativa di un autista

Prima di definire regole avanzate, assenze o calcoli di Rostering, devi capire come ogni autista è **assegnato** nell’organizzazione. In GoalBus, l’assegnazione operativa non è un singolo campo. È costruita combinando tre coordinate principali:
1. **Depot**
2. **Business unit**
3. **Work group**

Questa combinazione definisce da dove lavora la persona, a quale divisione appartiene e che tipo di duties può ricevere. Influenza anche la visibilità delle risorse per planner e manager.

Usa questo quick start quando la baseline autisti è caricata e devi assicurarti che ogni persona sia nel contesto operativo corretto prima di passare a regole e disponibilità.

Prima di iniziare, assicurati che:
1. Tu abbia caricato e rivisto gli autisti in P20.
2. Tu sappia quali depots, units e groups usa la tua operazione.
3. Tu sappia quale popolazione staff parteciperà al calcolo di Rostering.
4. Tu capisca che una cattiva assegnazione può rendere una persona non idonea anche se esiste nel sistema.

Per questo quick start, usa questo caso di riferimento:

> **Rivedrò che gli autisti che copriranno la linea L1 siano assegnati al depot, business unit e work group corretti prima di configurare regole e disponibilità.**

Per interpretare l’assegnazione operativa:
1. Tratta il **depot** come la base fisica della risorsa.
2. Tratta la **business unit** come la divisione strategica/modale a cui appartiene la persona.
3. Tratta il **work group** come la funzione che determina che tipo di duties può ricevere.
4. Usa questa regola di lettura:
   1. depot risponde **dove lavora**,
   2. unit risponde **in quale business/mode opera**,
   3. group risponde **che lavoro può fare**.
5. Non confondere questi tre concetti come se fossero la stessa cosa.

Quando termini questa sezione, dovresti capire che l’assegnazione operativa è una struttura composta, non un attributo isolato.

## Rivedere depot, business unit e work group nel profilo autista

Una volta chiara la logica, conferma come è configurata nel profilo reale. Questi campi fanno parte del “DNA strutturale” dell’employee e definiscono il contesto operativo. Se sono errati, l’assegnazione a valle è contaminata fin dall’inizio.

Prima di iniziare questa sezione, assicurati che:
1. Gli autisti esistano nella baseline.
2. Tu sappia quale autista o gruppo campione rivedere.
3. Tu voglia rivedere l’assegnazione strutturale, non un prestito temporaneo.

Per rivedere l’assegnazione nel profilo:
1. Dalla lista generale autisti, apri un driver profile.
2. Rivedi il pannello laterale dei dati strutturali.
3. Controlla almeno:
   1. **Primary depot**
   2. **Business unit**
   3. **Work group**
   4. **Area**, se la tua operazione la usa
4. Conferma che questi valori corrispondano a dove la persona dovrebbe lavorare realmente.
5. Se un valore è errato, aggiornalo nel profilo.
6. Salva i cambi.
7. Ripeti su più autisti per confermare la coerenza della baseline.

Per il caso di riferimento, conferma che:
1. Gli autisti L1 appartengano al depot corretto.
2. La business unit corrisponda al mode/business atteso.
3. Il work group sia davvero **Drivers** e non un altro ruolo.

Quando termini questa sezione, dovresti aver rivisto l’assegnazione strutturale per gli autisti che partecipano al calcolo.

## Capire la differenza tra assegnazione primaria, qualification e prestito temporaneo

Prima di procedere, distingui tre concetti spesso confusi:
1. **Primary assignment**
2. **Qualification**
3. **Temporary loan/transfer**

L’assegnazione primaria definisce dove una persona appartiene strutturalmente. La qualification risponde se **può** lavorare legalmente/tecnicamente in un altro contesto. Il loan/transfer risponde dove la persona **sta effettivamente lavorando** durante un periodo. Questi layer coesistono, ma non sono la stessa cosa.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia rivisto la primary assignment nel profilo.
2. Tu capisca che alcune persone possono lavorare fuori dal loro contesto primario.
3. Tu voglia evitare di confondere “appartiene a” vs “può lavorare in” vs “sta lavorando in”.

Per distinguerli correttamente:
1. Usa la **primary assignment** per descrivere il contesto strutturale base dell’autista.
2. Usa la **qualification** per indicare che l’autista può lavorare in un altro depot, group o unit.
3. Usa il **loan** per indicare che l’autista è spostato temporaneamente in un altro contesto.
4. Non usare un loan per correggere una primary assignment configurata male.
5. Non usare una qualification come se fosse uno spostamento attivo.
6. Tieni queste domande come guida:
   1. Dove appartiene questa persona? → primary assignment
   2. Dove potrebbe lavorare legalmente? → qualification
   3. Dove sta lavorando adesso? → loan

Per il caso di riferimento, chiediti:
1. L’autista appartiene a North Depot?
2. Può lavorare in un altro depot se necessario?
3. È in prestito temporaneo a un’altra base o è nel suo contesto usuale?

Quando termini questa sezione, dovresti avere una lettura corretta della gerarchia tra assignment, qualification e loan.

## Validare che l’assegnazione abiliti filtro corretto e assegnazione

L’assegnazione non è solo descrittiva: influenza come il sistema vede l’autista e quali duties può ricevere. Una persona assegnata male può essere filtrata fuori, comparire nel posto sbagliato o ricevere duties che non le appartengono. Può anche accadere il contrario: una persona valida può essere nascosta o resa non idonea per via di un’assegnazione errata.

Prima di continuare, assicurati che:
1. Tu abbia rivisto depot, unit e group su più profili.
2. Tu capisca la differenza tra assignment e loan.
3. Tu sappia quale popolazione parteciperà al prossimo calcolo.

Per validare l’impatto operativo dell’assegnazione:
1. Rivedi quale set di autisti dovrebbe essere visibile nel contesto di calcolo.
2. Conferma che le persone corrette compaiano sotto depot, unit e group corretti.
3. Verifica se alcuni autisti sono nel group sbagliato.
4. Verifica se alcuni autisti che dovrebbero appartenere non compaiono come tali.
5. Se rilevi un errore di assegnazione, correggilo prima di passare a regole o disponibilità.
6. Salva la configurazione finale per i profili coinvolti.

Per il caso di riferimento, assicurati che:
1. Gli autisti che copriranno L1 compaiano nel contesto operativo corretto.
2. Non siano mescolati con popolazioni che non dovrebbero ricevere duties di guida.
3. Il sistema possa filtrare e assegnare solo lo staff rilevante.

Quando termini questa sezione, dovresti avere una baseline di assegnazione operativa che aiuta il sistema a vedere e usare le persone corrette.

## Confermare che l’assegnazione operativa sia pronta per il prossimo layer

L’ultimo passo è confermare che l’assegnazione sia abbastanza solida per continuare con regole, assenze e calcolo. L’obiettivo non è solo riempire campi, ma lasciare una struttura chiara che il motore possa interpretare senza ambiguità.

Prima di concludere, assicurati che:
1. Tu abbia rivisto l’assegnazione strutturale per profili chiave.
2. Tu sappia distinguere assignment vs qualification vs loan.
3. Tu abbia validato che la popolazione visibile sia quella corretta.
4. Tu abbia corretto disallineamenti importanti.

Per confermare che l’assegnazione sia pronta:
1. Torna alla lista generale autisti.
2. Conferma che la popolazione rilevante per il tuo caso compaia nel contesto corretto.
3. Conferma che non ci siano errori evidenti di depot/unit/group.
4. Chiediti se il sistema potrebbe:
   1. filtrare correttamente gli autisti del caso,
   2. applicare regole alla popolazione corretta,
   3. e trattarli come baseline per disponibilità e calcolo.
5. Se sì, continua con il prossimo quick start.
6. Se no, correggi l’assegnazione prima di procedere.

Per il caso di riferimento, non procedere finché puoi affermare:
1. Gli autisti L1 sono assegnati al contesto corretto.
2. Sai distinguere chi appartiene, chi può lavorare e chi è in prestito.
3. La baseline è pronta per applicare Rostering rules e disponibilità.

Quando termini questa sezione, dovresti avere una baseline di assegnazione operativa abbastanza chiara per continuare con il prossimo layer del processo.

## Additional reading

- [Definire regole di Rostering per l’assegnazione del personale](P22_Definire_regole_di_Rostering_per_l_assegnazione_del_personale.md)

