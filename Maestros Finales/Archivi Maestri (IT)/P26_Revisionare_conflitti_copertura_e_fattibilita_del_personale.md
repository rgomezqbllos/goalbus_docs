---
title: Revisionare conflitti, copertura e fattibilità del personale
shortTitle: Conflitti e copertura
intro: 'Scopri come rivedere la soluzione di Rostering dopo il calcolo, identificare conflitti di copertura, distinguere se i problemi derivano da regole, disponibilità o assegnazione e decidere cosa correggere prima di validare.'
contentType: how-tos
versions:
  - '*'
---

## Capire cosa rivedere dopo il calcolo di Rostering

Dopo aver eseguito il primo calcolo di Rostering, il passo successivo non è validare subito. Prima devi rivedere se l’assegnazione è davvero praticabile. L’obiettivo è confermare se il sistema ha coperto il lavoro con persone reali rispettando vincoli di lavoro, disponibilità e contesto operativo.

Usa questo quick start quando hai già eseguito il calcolo di Rostering e devi analizzare se la soluzione è completa, parziale o conflittuale.

Prima di iniziare, assicurati che:
1. Tu abbia eseguito il primo calcolo di Rostering in P25.
2. Tu sappia quale soluzione di Scheduling era l’input.
3. Tu sappia quale popolazione autisti ha partecipato.
4. Tu sia pronto ad analizzare la soluzione prima di validarla.

Per questo quick start, usa questo caso di riferimento:

> **Rivedrò la soluzione di Rostering per la linea L1 per controllare la copertura, identificare conflitti di assegnazione e confermare la fattibilità prima di validare.**

Per capire cosa rivedere:
1. Tratta la review come diagnosi, non approvazione automatica.
2. Rivedi sempre tre dimensioni:
   1. **coverage**,
   2. **conflicts**,
   3. **overall feasibility**.
3. Non accettare una soluzione solo perché il motore ha finito.
4. Considera che una soluzione può:
   1. coprire tutto il lavoro,
   2. coprire il lavoro parzialmente,
   3. oppure produrre conflitti che richiedono tornare a regole, disponibilità o assegnazione.

Quando termini questa sezione, dovresti sapere cosa significa rivedere una soluzione staff e quali domande rispondere prima di validare.

## Rivedere la copertura del lavoro assegnato

La prima domanda è semplice: **tutto il lavoro è coperto?** Qui non stai ancora diagnosticando il perché: stai misurando se il sistema ha assegnato con successo persone al lavoro ereditato da Scheduling.

Prima di iniziare questa sezione, assicurati che:
1. La soluzione calcolata sia visibile.
2. Tu sappia qual è il lavoro totale che ti aspettavi di coprire.
3. Tu possa rivedere risultati per linea, group o popolazione.

Per rivedere la coverage:
1. Apri la soluzione di Rostering calcolata.
2. Rivedi la vista risultati complessiva.
3. Identifica:
   1. duties coperte,
   2. duties scoperte,
   3. assegnazioni parziali, se presenti.
4. Usa KPI visibili per supportare l’analisi.
ref: P26_Imagen1.png | compact
4. Verifica se la coverage è completa o ha gap usando KPI giornalieri.
ref: P26_Imagen2.png | full
5. Se il sistema mostra riepiloghi di coverage (driver KPI), rivedili.
ref: P26_Imagen3.png | compact
6. Se la coverage non è completa, non validare ancora la soluzione.
7. Annota dove sono i gap per poterli analizzare dopo.

Per il caso di riferimento, chiediti:
1. Il lavoro L1 è completamente coperto?
2. Ci sono giorni o time bands con gap?
3. Il problema impatta l’intera linea o solo parte del servizio?

Quando termini questa sezione, dovresti sapere se la soluzione copre tutto il lavoro o lascia duties non assegnate.

## Individuare conflitti e leggere la causa probabile

Dopo la review coverage, identifica i conflitti. Un conflitto non significa automaticamente che manca staff. Può significare che una regola è troppo restrittiva, che una persona è assegnata male o che un’assenza/loan è stata modellata in modo errato.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia identificato se ci sono duties scoperte.
2. Tu sia disposto a distinguere le cause invece di correggere per intuizione.
3. Tu sappia quale parte della soluzione ispezionare per prima.

Per rivedere i conflitti in modo utile:
1. Rivedi duties scoperte o problematiche.
2. Verifica se il sistema mostra messaggi, indicatori o conflitti collegati.
3. Classifica la causa probabile in uno di questi gruppi:
   1. **rules troppo restrittive**,
   2. **disponibilità insufficiente**,
   3. **assignment o qualifications errate**,
   4. **struttura ereditata da Scheduling**.
4. Se il conflitto impatta molte persone nella stessa popolazione, rivedi prima regole e assegnazione.
5. Se impatta casi individuali, rivedi prima disponibilità, assenza o loan.
6. Se sembra derivare dal lavoro ereditato, considera di tornare a Scheduling.

Per il caso di riferimento, chiediti:
1. La duty è scoperta perché non c’era nessuna persona disponibile?
2. La persona esiste ma non è qualificata/assegnata al contesto corretto?
3. Una regola di Rostering ha bloccato un’assegnazione che sembrava possibile?
4. Il problema non è lo staff ma la struttura del lavoro ereditato?

Quando termini questa sezione, dovresti avere un’ipotesi ragionevole sulle principali cause di conflitto.

## Rivedere la fattibilità complessiva della soluzione

Una soluzione può essere quasi coperta e comunque essere di scarsa qualità. Oltre a coverage e conflitti, rivedi la **overall feasibility**. La domanda non è solo se le persone sono state assegnate, ma se l’assegnazione risultante ha senso operativo e umano.

Prima di continuare, assicurati che:
1. Tu abbia rivisto la coverage.
2. Tu abbia identificato i conflitti principali.
3. Tu sia pronto a valutare qualità, non solo quantità.

Per rivedere la fattibilità complessiva:
1. Controlla se la distribuzione del lavoro sembra ragionevole.
2. Controlla segnali di sbilanciamento evidenti tra persone o gruppi.
3. Conferma che la soluzione sembri rispettare:
   1. rests,
   2. limiti,
   3. criteri base di equità,
   4. coerenza operativa.
4. Se la soluzione copre il lavoro ma lo fa in modo molto forzato, non validarla ancora.
5. Se il risultato sembra operativo, bilanciato e spiegabile, avvicinati alla decisione.

Per il caso di riferimento, chiediti:
1. La coverage è stata raggiunta in modo ragionevole o troppo forzato?
2. L’assegnazione sembra bilanciata tra gli autisti?
3. La soluzione sembra applicabile nel mondo reale o solo valida “su carta”?

Quando termini questa sezione, dovresti avere una lettura più completa se la soluzione può avanzare o deve essere corretta.

## Decidere cosa correggere prima di validare

L’ultimo passo è trasformare l’analisi in una decisione pratica. L’obiettivo non è correggere tutto insieme, ma identificare il layer corretto su cui intervenire.

Prima di concludere, assicurati che:
1. Tu abbia rivisto la coverage.
2. Tu abbia analizzato i conflitti.
3. Tu abbia valutato la fattibilità complessiva.
4. Tu sappia se la soluzione può avanzare.

Per decidere cosa correggere:
1. Se il problema principale sono le **rules**, torna a P22.
2. Se il problema principale sono **assenze/inattività/disponibilità**, torna a P23.
3. Se il problema principale sono **loans/transfers/assignment**, torna a P24 o P21 come appropriato.
4. Se il problema principale è lavoro ereditato, torna a Scheduling.
5. Se la soluzione è sufficientemente completa e fattibile, preparala per la validazione.
6. Non validare una soluzione solo perché “quasi funziona”. Valida quando capisci perché funziona e perché i conflitti rimanenti sono accettabili o risolti.

Per il caso di riferimento, termina questo quick start solo quando puoi affermare una di queste:
1. La soluzione L1 è abbastanza solida da validare.
2. Sai esattamente quale layer devi correggere prima di ricalcolare.

Quando termini questa sezione, dovresti avere una lettura chiara di coverage, conflitti e fattibilità e una decisione pratica sul prossimo passo.

## Additional reading

- [Validare e consolidare la soluzione di Rostering](P27_Validare_e_consolidare_la_soluzione_di_Rostering.md)

