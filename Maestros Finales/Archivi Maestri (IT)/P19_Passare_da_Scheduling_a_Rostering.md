---
title: Passare da Scheduling a Rostering
shortTitle: Scheduling to Rostering
intro: 'Scopri cosa deve essere pronto in Scheduling prima di entrare in Rostering, quali informazioni eredita l’assegnazione staff e quali problemi devono essere risolti prima di calcolare autisti reali.'
contentType: how-tos
versions:
  - '*'
---

## Confermare cosa deve essere chiuso in Scheduling prima di passare a Rostering

Prima di entrare in Rostering, devi confermare che Scheduling abbia già lasciato una base sufficientemente stabile. Rostering non sostituisce Scheduling. Rostering parte da lavoro già costruito e decide come assegnarlo a persone reali.

Usa questo quick start quando hai già una soluzione di Scheduling calcolata e validata e devi decidere se puoi iniziare a lavorare con staff reale.

Prima di iniziare, assicurati che:
1. Tu abbia già creato, calcolato e validato lo scenario di Scheduling.
2. Tu abbia già rivisto l’offerta di servizio e la sua coerenza complessiva.
3. Tu sappia quali lines, tipo di giorno e soluzione userai come riferimento.
4. Tu capisca che Rostering non è il posto in cui correggi una baseline di Scheduling strutturalmente debole.

Per questo quick start, usa questo caso di riferimento:

> **Confermerò che la soluzione di Scheduling validata per la linea L1 sia abbastanza matura da passare a Rostering e iniziare ad assegnare lavoro ad autisti reali.**

Per confermare che Scheduling sia pronta:
1. Apri lo scenario di Scheduling che userai come riferimento.
2. Conferma che il suo status sia quello giusto per smettere di trattarlo come bozza di lavoro.
3. Conferma che l’offerta usata sia ancora quella corretta.
4. Conferma che logica veicolo e logica turni siano già state applicate.
5. Conferma che non ci siano incoerenze strutturali evidenti nella soluzione.
6. Se devi ancora ricostruire base veicolo, tempi, servizi o regole, torna a Scheduling prima di procedere.
7. Se la soluzione è stabile, continua con il passo successivo.

Per il caso di riferimento, non procedere finché puoi affermare:
1. La soluzione L1 è stata calcolata.
2. È stata revisionata.
3. Non necessita più di correzioni strutturali di Scheduling.
4. Può essere trattata come baseline di lavoro per l’assegnazione staff.

Quando termini questa sezione, dovresti sapere se Scheduling ha consegnato una base utilizzabile per Rostering.

## Capire cosa eredita Rostering da Scheduling

Una volta confermata la base, capisci cosa passa da Scheduling a Rostering. Il punto chiave è non pensare che Rostering inizi da zero. Rostering eredita lavoro già strutturato e poi decide quale persona reale può prenderlo.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia identificato la soluzione di Scheduling che userai.
2. Tu sappia quali parti di quella soluzione devono restare stabili.
3. Tu capisca che Rostering lavora su lavoro già costruito, non su un’offerta non strutturata.

Per capire cosa eredita Rostering:
1. Rivedi la soluzione di Scheduling validata.
2. Identifica duties/blocks/strutture di lavoro che saranno la baseline.
3. Conferma che la soluzione sia riconoscibile dal punto di vista operativo.
4. Tieni a mente che in Rostering il sistema non crea lavoro astratto: cerca di assegnare quel lavoro a persone reali.
5. Usa questa regola di lettura:
   1. Scheduling definisce **che lavoro esiste**.
   2. Rostering definisce **chi farà quel lavoro**.

Per il caso di riferimento, chiediti:
1. La soluzione di L1 contiene lavoro abbastanza chiaro da assegnare?
2. I blocks di lavoro sono riconoscibili e utilizzabili?
3. Il problema rimanente riguarda le persone più che la struttura?

Quando termini questa sezione, dovresti capire cosa eredita Rostering e cosa non dovrebbe essere ridefinito lì.

## Separare quali problemi si risolvono in Scheduling vs. in Rostering

Prima di entrare pienamente nel layer staff, mantieni le responsabilità ben separate. Molti errori accadono quando si prova a correggere in Rostering ciò che doveva essere corretto prima in Scheduling.

Prima di continuare, assicurati che:
1. Tu sappia quale scenario di Scheduling è la baseline.
2. Tu capisca che Rostering consuma una soluzione precedente.
3. Tu sia pronto a separare problemi strutturali da problemi staff.

Per separare correttamente i due domini:
1. Tratta come problema di **Scheduling** tutto ciò che riguarda:
   1. struttura del servizio,
   2. logica flotta,
   3. tempi,
   4. vehicle rules,
   5. shift types e costruzione base delle duties.
2. Tratta come problema di **Rostering** tutto ciò che riguarda:
   1. disponibilità reale degli autisti,
   2. assegnazione depot/group,
   3. assenze,
   4. inattività,
   5. prestiti/trasferimenti,
   6. idoneità reale a ricevere una duty.
3. Se rilevi un’incoerenza di lavoro che impatta l’intera struttura, torna a Scheduling.
4. Se rilevi un’incoerenza di persona, risolvila in Rostering.

Per il caso di riferimento:
1. Se il problema è che il lavoro L1 è stato costruito male, torna a Scheduling.
2. Se il problema è quale autista reale può prendere quel lavoro, stai entrando correttamente in Rostering.

Quando termini questa sezione, dovresti essere in grado di spiegare chiaramente cosa va corretto prima di passare allo staff e cosa appartiene al modulo successivo.

## Confermare cosa deve essere pronto sul lato staff prima di calcolare Rostering

Ora che sai cosa riceve Rostering, rivedi cosa deve esistere sul lato staff affinché il prossimo calcolo abbia senso. Un buon Scheduling non basta se non hai una base minima di persone, assegnazioni e disponibilità.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia una baseline valida da Scheduling.
2. Tu sappia quali groups, depots o contesti operativi impattano lo staff.
3. Tu sia pronto a rivedere il layer staff.

Per confermare che la base staff sia pronta:
1. Conferma che esista una popolazione staff che possa ricevere il lavoro.
2. Conferma che le persone siano assegnate al contesto corretto quando applicabile.
3. Conferma che non stai entrando in Rostering senza informazioni minime di disponibilità.
4. Rivedi se esistono le strutture necessarie per:
   1. Rostering rules,
   2. assenze,
   3. inattività,
   4. transfers/loans, quando applicabile.
5. Se non hai ancora questa baseline, non eseguire il calcolo staff.
6. Se la baseline esiste (o è almeno in corso), continua con i prossimi quick start di Rostering.

Per il caso di riferimento, chiediti:
1. Lo staff che riceverà la soluzione di L1 esiste già?
2. Quello staff appartiene al perimetro corretto?
3. La baseline di disponibilità e assegnazione è minimamente preparata?

Quando termini questa sezione, dovresti sapere se il lato staff è pronto per entrare in Rostering.

## Chiarire il punto di transizione tra Scheduling e Rostering

L’ultimo passo è chiudere mentalmente la transizione. Questo quick start non serve a calcolare ancora l’assegnazione staff. Serve a rendere chiarissimo dove finisce Scheduling e dove inizia Rostering per non mescolare i due domini.

Prima di concludere, assicurati che:
1. Tu abbia rivisto la soluzione di Scheduling.
2. Tu capisca cosa eredita Rostering.
3. Tu abbia separato problemi strutturali vs staff.
4. Tu abbia verificato se esiste una base staff minima.

Per chiudere correttamente la transizione:
1. Tratta la soluzione di Scheduling validata come input formale per Rostering.
2. Non continuare ad alterare quella baseline a meno che non rilevi un reale problema strutturale.
3. Usa i prossimi quick start per preparare:
   1. Rostering rules,
   2. assenze e inattività,
   3. transfers, loans e cambi di assegnazione.
4. Considera che da qui cambia l’obiettivo:
   1. non stai più costruendo lavoro,
   2. ora lo stai assegnando a persone reali.
5. Se puoi dirlo chiaramente, la transizione è gestita correttamente.

Per il caso di riferimento, termina questo quick start solo quando puoi affermare:
1. Scheduling ha già lasciato una soluzione L1 stabile.
2. Il prossimo problema non è più strutturale, ma staff assignment.
3. Ora puoi passare alle Rostering rules.

Quando termini questa sezione, dovresti avere una transizione chiara e controllata tra Scheduling e Rostering.

## Additional reading

- [Caricare e gestire gli autisti](P20_Caricare_e_gestire_gli_autisti.md)

