---
title: Caricare e gestire gli autisti
shortTitle: Autisti
intro: 'Scopri come creare, importare e mantenere la baseline degli autisti in GoalBus, rivedere il profilo operativo e lasciare una base affidabile per il roster prima di passare ad assegnazione, regole e calcolo di Rostering.'
contentType: how-tos
versions:
  - '*'
---

## Creare o importare la baseline del roster autisti

Prima di parlare di Rostering rules, assenze o assegnazione delle duties, ti serve una baseline affidabile di autisti. In GoalBus, la gestione driver è la fonte primaria di verità per le operazioni umane: supporta creazione manuale e bulk upload e centralizza identità, affiliazione al depot e disponibilità in un’unica directory.

Usa questo quick start quando la transizione da Scheduling a Rostering è chiara e devi preparare il gruppo reale di persone che parteciperà all’assegnazione.

Prima di iniziare, assicurati che:
1. Tu abbia già chiuso la transizione da Scheduling in P19.
2. Tu sappia quale popolazione di autisti parteciperà al calcolo.
3. Tu sappia se creerai pochi autisti manualmente o se ti serve un import massivo.
4. Tu abbia accesso con permessi per gestire lo staff.

Per questo quick start, usa questo caso di riferimento:

> **Caricherò e rivedrò la baseline del roster autisti in grado di coprire la soluzione L1 prima di passare ad assegnazione, regole e disponibilità.**

Per creare o importare la baseline driver:
1. In GoalBus, vai su **Configuration** > **Staff** > **Driver management**.
ref: P20_Imagen1.png | compact
2. Verifica se gli autisti del tuo caso esistono già nella lista.
3. Se devi creare pochi autisti, fai clic su **New Driver**.
ref: P20_Imagen2.png | compact
4. Se devi caricare molti autisti, esegui un bulk CSV import tramite **Staff upload**.
ref: P20_Imagen3.png | compact
5. Se scegli il bulk import, prepara il file con i dati minimi necessari a identificare correttamente ogni persona. La finestra di import fornisce indicazioni per preparare il CSV.
ref: P20_Imagen4.png
6. Esegui l’upload e rivedi il risultato.
7. Torna alla lista generale e conferma che gli autisti compaiano correttamente.
8. Se rilevi duplicati o record incompleti, correggili prima di procedere.

Per il caso di riferimento, termina questa sezione solo quando puoi affermare:
1. Gli autisti per L1 sono creati o importati.
2. La lista generale riflette un’unica baseline roster.
3. Puoi aprire il profilo di ogni autista per rivedere il contesto operativo.

Quando termini questa sezione, dovresti avere una baseline autisti caricata e visibile nel sistema.

## Rivedere il profilo autista e i dati strutturali

Una volta che la baseline esiste, rivedi il **driver profile**. Il profilo non è solo una scheda contatto: è il record digitale completo dell’employee nelle operations. Contiene dati statici, contesto operativo e attributi che il sistema userà in seguito per ragionare sull’idoneità.

Prima di iniziare questa sezione, assicurati che:
1. Gli autisti siano visibili nella lista generale.
2. Tu sappia quale autista (o gruppo) usare come campione.
3. Tu voglia validare che il record sia operativo, non solo amministrativo.

Per rivedere il driver profile:
1. Nella lista generale, fai clic sul nome di un autista.
ref: P20_Imagen5.png | full
2. Rivedi il pannello laterale con i dati statici.
3. Controlla almeno questi gruppi informativi:
   1. dati base come name e code,
   2. dati operativi come labor agreement o tipo contratto,
   3. collegamenti operativi come primary depot, work group, area o authorized vehicle types.
4. Se manca un dato strutturale chiave, completalo prima di procedere.
5. Salva eventuali cambi necessari.
6. Ripeti su più autisti per confermare che la baseline sia coerente.

Per il caso di riferimento, rivedi almeno:
1. Driver code.
2. Primary depot.
3. Work group.
4. Le proprietà operative che condizioneranno l’assegnazione successiva.

Quando termini questa sezione, dovresti essere sicuro che ogni autista abbia un record operativo coerente e utilizzabile.

## Rivedere il contesto operativo e i dati dinamici dell’autista

Oltre ai dati strutturali, il profilo può includere dati dinamici che influenzano direttamente come il sistema ragiona sulla persona. Nella tab Administration puoi rivedere contatori e pattern di lavoro che verranno usati in seguito dalla logica di assegnazione.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già rivisto i dati statici del profilo.
2. Tu sappia se la tua operazione usa counters o pattern ciclici.
3. Tu voglia confermare che l’autista abbia un contesto operativo interpretabile.

Per rivedere il contesto operativo dinamico:
1. Dentro il profilo autista, apri **Administration details**.
2. Rivedi i **counters** o KPI dell’autista se esistono.
3. Verifica se l’autista è collegato a un **work pattern**.
4. Se la tua operazione usa pattern ciclici, rivedi l’offset/posizione corrente dell’autista nel pattern.
5. Conferma che i dati abbiano senso nel contesto reale.
6. Se l’informazione dinamica non è corretta, aggiustala prima di passare a regole o calcolo.

Per il caso di riferimento, chiediti:
1. Questo autista ha il pattern che dovrebbe avere?
2. Counters/KPI sono disponibili se il processo li richiede?
3. Il sistema potrebbe ragionare correttamente su questa persona durante l’assegnazione?

Quando termini questa sezione, dovresti aver validato non solo l’identità dell’autista ma anche il suo contesto operativo dinamico.

## Validare le qualifiche prima di usare un autista in Rostering

Prima di trattare un autista come idoneo, rivedi **qualifications/authorizations**. Rispondono alla domanda: “Questa persona può legalmente o tecnicamente lavorare in questo depot, group o unit?” Sono gestite su una timeline con start e end date e il sistema mostra status come active, future, expired o expiring soon. Se una persona non è qualificata per il contesto richiesto, il motore genererà un errore quando proverà ad assegnarla.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già rivisto il driver profile.
2. Tu sappia quale depot, group o unit serve per il tuo caso.
3. Tu capisca che una qualification non è la stessa cosa di un prestito temporaneo o un’assegnazione temporanea.

Per rivedere e validare le qualifiche:
1. Dentro il profilo autista, apri **Qualifications / Certifications**.
2. Rivedi se ci sono record validi per:
   1. depots,
   2. work groups,
   3. business units.
3. Controlla lo status visivo di ciascuna qualification:
   1. active,
   2. future,
   3. expiring soon,
   4. expired.
4. Se manca una qualification necessaria, aggiungila con date corrette.
5. Se una qualification è scaduta e non va usata, tienila come storico: non cercare di riscrivere il passato.
6. Salva i cambi.
7. Conferma che l’autista sia qualificato per il contesto in cui ti aspetti di usarlo.

Per il caso di riferimento, non procedere finché puoi affermare:
1. L’autista è qualificato per il depot corretto.
2. Il work group richiesto è coperto.
3. Non ci sono scadenze che rompono l’idoneità corrente.

Quando termini questa sezione, dovresti avere autisti che non solo esistono nel roster, ma sono anche operativamente e legalmente idonei.

## Confermare che la baseline sia pronta per il prossimo layer di Rostering

L’ultimo passo è confermare che la baseline autisti sia pronta per passare ad assegnazione operativa, regole, assenze e calcolo. L’obiettivo non è solo avere nomi caricati, ma una baseline coerente e tracciabile che il motore possa usare.

Prima di concludere, assicurati che:
1. Tu abbia caricato o importato la baseline.
2. Tu abbia rivisto profili chiave.
3. Tu abbia controllato dati strutturali e dinamici.
4. Tu abbia validato qualifiche essenziali.

Per confermare che la baseline sia pronta:
1. Torna alla lista generale autisti.
2. Conferma che la popolazione richiesta per il tuo caso sia presente.
3. Conferma che i profili critici non abbiano grossi gap informativi.
4. Conferma che le persone che ti aspetti di usare siano qualificate per il contesto corretto.
5. Chiediti se il sistema potrebbe già usare questa baseline per:
   1. gestire l’assegnazione operativa,
   2. applicare Rostering rules,
   3. e gestire disponibilità reale.
6. Se sì, continua con il prossimo quick start.
7. Se no, correggi la baseline autisti prima di procedere.

Per il caso di riferimento, termina questo quick start solo quando puoi affermare:
1. La baseline autisti di L1 è caricata.
2. I profili chiave sono stati rivisti.
3. Le qualifiche essenziali sono valide.
4. La baseline è pronta per passare all’assegnazione operativa.

Quando termini questa sezione, dovresti avere una baseline autisti abbastanza solida per continuare con il prossimo layer di Rostering.

## Additional reading

- [Gestire l’assegnazione operativa degli autisti](P21_Gestire_l_assegnazione_operativa_degli_autisti.md)

