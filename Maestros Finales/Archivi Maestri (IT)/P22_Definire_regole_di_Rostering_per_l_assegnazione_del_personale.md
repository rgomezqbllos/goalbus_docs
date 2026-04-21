---
title: Definire regole di Rostering per l’assegnazione del personale
shortTitle: Rostering rules
intro: 'Scopri come configurare regole di Rostering di base e avanzate in modo che l’assegnazione staff rispetti limiti di lavoro, criteri di equità e vincoli operativi reali prima di calcolare il roster.'
contentType: how-tos
versions:
  - '*'
---

## Capire cosa controllano le Rostering rules

Prima di calcolare l’assegnazione dello staff, devi definire le **Rostering rules** che guideranno come gli employee vengono assegnati alle duties. Queste regole non costruiscono il lavoro: quello è già stato risolto da Scheduling. Qui controlli come quel lavoro viene distribuito su persone reali, rispettando policy operative, criteri di equità e vincoli di lavoro.

Usa questo quick start quando hai già una soluzione di Scheduling sufficientemente stabile, una baseline autisti caricata e un’assegnazione operativa rivista.

Prima di iniziare, assicurati che:
1. Tu abbia chiuso la transizione da Scheduling in P19.
2. Tu abbia caricato e rivisto gli autisti in P20.
3. Tu abbia validato l’assegnazione operativa in P21.
4. Tu sappia quale soluzione di Scheduling sarà la baseline.
5. Tu sappia quale popolazione staff/work group è impattata dal calcolo.

Per questo quick start, usa questo caso di riferimento:

> **Configurerò Rostering rules per la linea L1 e per il suo gruppo autisti in modo che il calcolo assegni staff reale rispettando riposi, limiti di lavoro e criteri operativi.**

Per capire il ruolo di queste regole:
1. Tratta le Rostering rules come vincoli e preferenze sull’assegnazione delle persone.
2. Usa queste regole quando vuoi controllare:
   1. rests,
   2. work time,
   3. pattern settimanali,
   4. work group,
   5. pairing,
   6. e altri criteri di equità/policy interne.
3. Non usare queste regole per correggere problemi in:
   1. offerta,
   2. tempi,
   3. flotta,
   4. costruzione base delle duties.
4. Se rilevi che il problema è ancora strutturale, torna a Scheduling prima di procedere.

Quando termini questa sezione, dovresti essere chiaro che le Rostering rules governano le persone, non la struttura base del lavoro.

## Distinguere regole di base vs regole avanzate

Prima di creare un rules model, distingui due livelli di configurazione:
1. **Basic rules**
2. **Advanced rules**

Le basic rules sono pensate per configurare rapidamente vincoli comuni. Sono utili per una parametrizzazione veloce o un primo trial. Le advanced rules sono pensate per modellare vincoli e preferenze in modo più preciso tramite limiti e penalità.

Prima di iniziare questa sezione, assicurati che:
1. Tu sappia se il tuo caso richiede velocità o precisione.
2. Tu capisca che le basic rules hanno meno flessibilità di modellazione delle advanced rules.
3. Tu sappia se serviranno modelli diversi per usi diversi.

Per scegliere il tipo di regola appropriato:
1. Usa **basic rules** se vuoi coprire rapidamente vincoli comuni.
2. Usa **advanced rules** se devi modellare in modo preciso policy complesse, accordi o condizioni operative specifiche.
3. Tieni a mente che le basic rules attive si applicano sia in daily operations sia negli assignment calculation scenarios.
4. Se ti servono modelli distinti per contesti distinti (ad esempio daily operations vs un calcolo futuro), usa advanced rules.
5. Decidi l’approccio prima di parametrizzare.

Per il caso di riferimento:
1. Se stai iniziando e vuoi un primo layer di controllo, parti dalle basic rules.
2. Se sai già che ti serviranno preferenze, penalità o modelli specifici per contesto, passa alle advanced rules.

Quando termini questa sezione, dovresti sapere se il tuo caso userà basic rules, advanced rules o una combinazione controllata.

## Abilitare basic rules comuni per una prima assegnazione

Se il tuo caso richiede una configurazione iniziale rapida, inizia con le **basic rules**. Coprono le restrizioni più comuni e ti permettono di eseguire il calcolo con una base ragionevole prima di passare a controlli più fini.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia deciso di iniziare con basic rules.
2. Tu sappia quali restrizioni minime vuoi imporre.
3. Tu capisca che non tutte le regole vanno abilitate per default.

Per abilitare le basic rules:
1. In GoalBus, vai su **Configuration** > **Assignment rules**.
ref: P22_Imagen1.png | compact
2. Apri la sezione **Basic rules**.
3. Rivedi il catalogo di basic rules disponibili.
ref: P22_Imagen2.png | full
4. Abilita solo quelle che corrispondono al caso che stai costruendo.
5. Configura, quando applicabile:
   1. limiti generali,
   2. limiti specifici per proprietà employee,
   3. o eccezioni per employee specifici.
6. Salva i cambi.
7. Conferma che le regole attive riflettano le policy che vuoi imporre.

Un set iniziale di basic rules potrebbe includere:
1. **Work pattern**
2. **Rest between days**
3. **Monthly work time**
4. **Weekly work time**
5. **Days off per week**
6. **First published solution**
7. **Work group**
8. **Pairing**
9. **Assignment compatibility**
10. **Line qualification**
11. **First published solution shift**
12. **Consecutive working days**, quando applicabile

Per il caso di riferimento, non abilitare una regola solo perché esiste. Abilitala solo se:
1. risponde a un bisogno reale,
2. puoi spiegare perché ti serve,
3. e capisci come impatterà l’assegnazione.

Quando termini questa sezione, dovresti avere una baseline iniziale di controllo per l’assegnazione staff.

## Creare un modello di regole avanzate quando serve più precisione

Se le basic rules non bastano, crea un **advanced rules model**. Questo approccio ti permette di controllare l’assegnazione in modo preciso regolando limiti e preferenze secondo policy aziendali, accordi di lavoro e condizioni operative reali.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia identificato cosa non si modella bene con basic rules.
2. Tu sappia quali comportamenti devono essere obbligatori e quali preferiti.
3. Tu abbia bisogno di un modello più fine riutilizzabile per scenario o contesto.

Per creare un advanced rules model:
1. In **Configuration** > **Assignment rules**, apri **Rules models**.
2. Crea un nuovo rules model.
3. Dai al modello un **name** chiaro.
4. Aggiungi una **description** per distinguerlo dagli altri.
5. Salva il modello.
ref: P22_Imagen3.png | compact
6. Aggiungi advanced rules una alla volta.
7. Per ogni regola, decidi:
   1. se è un hard limit,
   2. o una preference via penalty.
8. Salva la configurazione del modello.
9. Attiva il rules model creato.
10. Conferma che il modello possa essere assegnato al calcolo di Rostering appropriato.

Per il caso di riferimento, opzioni valide potrebbero essere:
- **Rostering L1 workday**
- **L1 drivers assignment - advanced rules**

Quando termini questa sezione, dovresti avere un modello avanzato pronto a rappresentare vincoli e preferenze più complessi.

## Collegare le regole alla popolazione corretta e al calcolo reale

Dopo aver abilitato basic rules o creato un modello avanzato, conferma che le regole si applichino alla popolazione corretta e che non stai imponendo vincoli astratti non legati al calcolo reale.

Prima di continuare, assicurati che:
1. Tu abbia abilitato basic rules o creato un modello avanzato.
2. Tu sappia quali employee/groups/depots partecipano al calcolo.
3. Tu sappia quale soluzione di Scheduling sarà l’input.

Per collegare correttamente le regole al contesto di calcolo:
1. Rivedi la popolazione staff a cui Rostering si applicherà.
2. Conferma se le regole impattano:
   1. l’intero roster coinvolto,
   2. un gruppo specifico,
   3. o employee con proprietà specifiche.
3. Conferma di non imporre regole a persone che non partecipano a quel calcolo.
4. Conferma che la logica dello scenario di Scheduling resti compatibile con queste regole.
5. Se una regola rende l’assegnazione non fattibile, aggiusta limite o scope.
6. Salva la configurazione finale.

Per il caso di riferimento, chiediti:
1. Queste regole sono progettate per gli autisti che copriranno davvero L1?
2. Il work group impattato è quello corretto?
3. L’assegnazione è ancora fattibile dopo aver abilitato queste regole?

Quando termini questa sezione, dovresti avere la configurazione regole collegata a persone reali e a un calcolo di Rostering concreto.

## Confermare che la baseline regole sia pronta per calcolare Rostering

L’ultimo passo è assicurarti che la configurazione sia pronta a alimentare il calcolo staff. L’obiettivo non è solo abilitare regole, ma lasciare una baseline coerente, comprensibile e applicabile.

Prima di concludere, assicurati che:
1. Tu abbia scelto basic vs advanced rules in base al caso.
2. Tu abbia abilitato o modellato i vincoli necessari.
3. Tu abbia collegato la logica alla popolazione corretta.
4. Tu abbia confermato che l’assegnazione resti fattibile.

Per validare che la baseline regole sia pronta:
1. Rivedi il set finale di regole attive.
2. Conferma che ogni regola risponda a un bisogno reale.
3. Chiediti se il sistema potrebbe:
   1. bloccare assegnazioni non valide,
   2. rispettare riposi e limiti,
   3. riflettere criteri di equità e work-group,
   4. e comunque produrre una soluzione utilizzabile.
4. Se sì, continua con il prossimo quick start.
5. Se no, aggiusta le regole prima di procedere.

Per il caso di riferimento, non procedere finché puoi affermare:
1. Le Rostering rules per L1 sono chiare.
2. Sai perché ogni regola è abilitata.
3. Il sistema può ancora assegnare persone reali con quella configurazione.
4. La baseline è pronta a gestire disponibilità ed eccezioni staff.

Quando termini questa sezione, dovresti avere una baseline di Rostering rules abbastanza solida per passare ad assenze, inattività e disponibilità.

## Additional reading

- [Gestire assenze, inattività e disponibilità del personale](P23_Gestire_assenze_inattivita_e_disponibilita_del_personale.md)

