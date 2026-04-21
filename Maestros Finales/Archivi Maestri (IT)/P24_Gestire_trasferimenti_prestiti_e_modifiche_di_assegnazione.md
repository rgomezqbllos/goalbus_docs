---
title: Gestire trasferimenti, prestiti e modifiche di assegnazione
shortTitle: Prestiti e cambi
intro: 'Scopri come gestire cambi di contesto operativo degli autisti distinguendo tra transfer, temporary loan e assignment change, così Rostering usa ogni persona nel perimetro corretto senza perdere tracciabilità.'
contentType: how-tos
versions:
  - '*'
---

## Capire la differenza tra transfer, loan e assignment change

Prima di calcolare Rostering, devi distinguere correttamente i movimenti dello staff tra contesti operativi. Non tutte le situazioni significano la stessa cosa. Un autista può appartenere ancora al suo primary depot ma lavorare temporaneamente altrove. Può anche cambiare assegnazione in modo più permanente. Se confondi questi concetti, l’idoneità staff diventa confusa e il calcolo può assegnare lavoro nel contesto sbagliato.

Usa questo quick start quando gli autisti sono caricati, la primary assignment è stata rivista e assenze/inattività sono modellate e devi riflettere movimenti reali tra depots, groups o units.

Prima di iniziare, assicurati che:
1. Tu abbia caricato e rivisto gli autisti in P20.
2. Tu abbia validato l’assegnazione operativa in P21.
3. Tu abbia configurato Rostering rules in P22.
4. Tu abbia registrato assenze, inattività e disponibilità in P23.
5. Tu sappia chi cambierà contesto e per quale periodo.

Per questo quick start, usa questo caso di riferimento:

> **Registrerò che un autista che normalmente appartiene a North Depot lavorerà temporaneamente in un altro contesto e che un altro autista cambierà assegnazione in modo più permanente prima del calcolo di Rostering.**

Per distinguere correttamente ogni movimento:
1. Usa un **loan** quando la persona appartiene ancora al contesto primario ma lavorerà temporaneamente in un altro.
2. Usa un **transfer** quando la persona cambia contesto in modo più strutturale o permanente.
3. Usa un **assignment change** quando devi aggiornare formalmente il primary depot/group/unit sotto cui il sistema deve trattare l’autista.
4. Non usare un’assenza per modellare un cambio di contesto operativo.
5. Non usare un loan per correggere una primary assignment configurata male.

Tieni queste domande come guida:
1. Dove appartiene normalmente questa persona?
2. Dove lavorerà realmente in questo periodo?
3. Il movimento è temporaneo o strutturale?

Quando termini questa sezione, dovresti sapere quale tipo di record si applica a ciascun cambio di contesto.

## Registrare un temporary loan

Un loan riflette che un autista lavorerà temporaneamente fuori dal suo contesto usuale senza perdere la primary assignment. È utile quando qualcuno appartiene ancora al suo depot/unit/group principale ma opererà per un periodo in un altro ambiente.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia identificato la persona che sarà in prestito.
2. Tu conosca il suo contesto primario.
3. Tu conosca il contesto di destinazione e le date di efficacia.

Per registrare un loan temporaneo:
1. Apri il driver profile dalla lista generale.
2. Vai alla sezione **movements**, **temporary assignment** o **loans** (a seconda della vista).
3. Crea un nuovo record di loan.
4. Definisci:
   1. **origin context**,
   2. **destination context**,
   3. **start date**,
   4. **end date**,
   5. ed eventuali note.
5. Salva il record.
6. Conferma che l’autista mantenga la primary assignment.
7. Conferma che durante il periodo di loan il sistema tratti l’autista nel corretto contesto temporaneo.

Per il caso di riferimento, un loan valido è:
1. autista assegnato a North Depot,
2. in prestito per due settimane a South Depot,
3. senza cambiare la primary assignment storica.

Quando termini questa sezione, dovresti avere un loan temporaneo correttamente modellato senza perdere tracciabilità strutturale.

## Registrare un transfer o un cambiamento più stabile

A differenza del loan, un transfer è un movimento strutturale. Non riguarda solo lavorare temporaneamente altrove, ma cambiare l’appartenenza operativa dell’autista in modo più duraturo.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia identificato la persona che cambierà contesto in modo duraturo.
2. Tu sappia quale depot/unit/group diventerà il nuovo contesto primario.
3. Questo non sia un bisogno temporaneo o eccezionale.

Per registrare un transfer / cambiamento strutturale:
1. Apri il driver profile.
2. Rivedi la primary assignment attuale.
3. Crea il movement di transfer o aggiorna la primary assignment, a seconda del flow del tuo ambiente.
4. Definisci:
   1. il nuovo **primary depot**,
   2. la nuova **business unit**,
   3. il nuovo **work group**, se cambia,
   4. e la data di efficacia.
5. Salva i cambi.
6. Conferma che il profilo rifletta ora il nuovo contesto primario.
7. Conferma che il cambiamento non lasci contraddizioni tra primary assignment e qualifications.

Per il caso di riferimento, un transfer valido è:
1. un autista che smette di appartenere a North Depot,
2. passa ad appartenere a South Depot su base stabile,
3. e da quella data deve essere trattato come risorsa della nuova base.

Quando termini questa sezione, dovresti aver modellato correttamente un cambio di contesto strutturale.

## Rivedere l’impatto su qualifications e idoneità

Dopo aver registrato loans o transfers, rivedi l’impatto operativo. Spostare una persona tra contesti è inutile se qualifications/idoneità non seguono. Conferma che l’autista non solo abbia cambiato contesto nel profilo, ma possa essere usato correttamente nel nuovo ambiente.

Prima di continuare, assicurati che:
1. Tu abbia registrato almeno un loan o transfer.
2. Tu sappia in quale contesto operativo la persona dovrebbe essere vista ora.
3. Tu capisca che un cambio di contesto può richiedere rivedere qualifications attive.

Per rivedere l’impatto operativo:
1. Torna alla tab **Qualifications / Certifications** dell’autista.
2. Conferma che ci siano qualifications valide per il contesto di destinazione.
3. Se mancano, aggiungile con date corrette prima del calcolo.
4. Conferma che la persona non sia visibile contemporaneamente in contesti incompatibili per un errore di configurazione.
5. Conferma che il sistema possa trattare la persona come idonea nel corretto perimetro durante il periodo rilevante.
6. Se rilevi contraddizioni, correggile prima di eseguire il calcolo di Rostering.

Per il caso di riferimento, assicurati che:
1. l’autista in prestito possa lavorare legalmente/tecnicamente nel contesto di destinazione,
2. l’autista trasferito abbia qualifications allineate al nuovo contesto,
3. l’idoneità corrisponda al movimento registrato.

Quando termini questa sezione, dovresti avere movimenti staff utilizzabili operativamente.

## Confermare che i cambi di contesto siano pronti per il calcolo di Rostering

L’ultimo passo è confermare che la combinazione di primary assignment, loans/transfers e qualifications sia abbastanza chiara per alimentare il calcolo. Evita due errori:
1. assegnare qualcuno in un contesto in cui non dovrebbe comparire,
2. escludere qualcuno che dovrebbe essere idoneo a causa di un cambio registrato.

Prima di concludere, assicurati che:
1. Tu abbia registrato i movimenti temporanei o strutturali necessari.
2. Tu abbia rivisto l’impatto sull’idoneità.
3. Tu sappia quale popolazione parteciperà al prossimo calcolo.

Per confermare che questo layer sia pronto:
1. Torna alla lista generale autisti.
2. Rivedi diversi profili impattati da cambi di contesto.
3. Conferma che:
   1. i loans compaiano come temporanei,
   2. i transfers compaiano come cambi strutturali,
   3. la primary assignment resti coerente dove applicabile.
4. Chiediti se il sistema potrebbe:
   1. usare l’autista giusto nel contesto giusto,
   2. nel periodo giusto,
   3. senza confondere appartenenza strutturale con spostamento temporaneo.
5. Se sì, continua con il prossimo quick start.
6. Se no, correggi movimenti o qualifications prima di procedere.

Per il caso di riferimento, non procedere finché puoi affermare:
1. I cambi di contesto degli autisti L1 sono correttamente registrati.
2. Sai chi è in prestito, chi è trasferito e chi mantiene primary assignment.
3. La baseline è pronta per eseguire il primo calcolo di Rostering.

Quando termini questa sezione, dovresti avere il contesto organizzativo dello staff abbastanza chiaro per passare al calcolo di assegnazione.

## Additional reading

- [Eseguire il primo calcolo di Rostering](P25_Eseguire_il_primo_calcolo_di_Rostering.md)

