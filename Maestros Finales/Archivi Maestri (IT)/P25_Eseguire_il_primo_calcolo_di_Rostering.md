---
title: Eseguire il primo calcolo di Rostering
shortTitle: Calcolare Rostering
intro: 'Scopri come preparare ed eseguire il primo calcolo di Rostering, rivedere se la soluzione staff è praticabile e capire se i problemi appartengono a regole, disponibilità o assegnazione prima di validare.'
contentType: how-tos
versions:
  - '*'
---

## Preparare la baseline prima di eseguire il calcolo di Rostering

Prima di eseguire il calcolo, conferma che la baseline staff sia abbastanza matura. Rostering non dovrebbe essere usato per scoprire master data mancanti all’ultimo minuto. Se roster, assegnazione, regole o disponibilità non sono ben preparati, il calcolo fallirà o produrrà una soluzione fuorviante.

Usa questo quick start quando hai già una soluzione di Scheduling stabile e hai preparato il layer staff necessario per assegnare lavoro reale ad autisti reali.

Prima di iniziare, assicurati che:
1. Tu abbia chiuso la transizione da Scheduling in P19.
2. Tu abbia caricato e rivisto gli autisti in P20.
3. Tu abbia validato l’assegnazione operativa in P21.
4. Tu abbia configurato Rostering rules in P22.
5. Tu abbia registrato assenze, inattività e disponibilità in P23.
6. Tu abbia registrato loans/transfers/assignment changes in P24.
7. Tu sappia quale soluzione di Scheduling sarà l’input del calcolo.

Per questo quick start, usa questo caso di riferimento:

> **Eseguirò il primo calcolo di Rostering per la linea L1 usando una soluzione di Scheduling stabile e una baseline autisti preparata correttamente.**

Per preparare la baseline:
1. Apri l’ambiente/modulo **Rostering**.
ref: P25_Imagen1.png | compact
2. Rivedi quale soluzione di Scheduling sarà l’input.
3. Conferma che la popolazione autisti partecipante sia disponibile e assegnata al contesto corretto.
4. Conferma che le Rostering rules attive corrispondano al caso reale.
5. Conferma che le principali assenze e inattività siano registrate.
6. Conferma che loans/transfers rilevanti siano riflessi.
7. Se rilevi un problema di master data, correggilo prima di calcolare.

Per il caso di riferimento, non procedere finché puoi affermare:
1. La soluzione di L1 non necessita più di cambi strutturali.
2. La popolazione autisti esiste ed è pronta.
3. Regole e disponibilità rappresentano la realtà del periodo.
4. Puoi tentare una reale assegnazione dello staff.

Quando termini questa sezione, dovresti avere una baseline abbastanza stabile per eseguire Rostering.

## Selezionare l’input di Scheduling corretto

Rostering richiede un input di lavoro chiaro. Questo input non dovrebbe essere un mix ambiguo di scenari, ma una soluzione di Scheduling nota e utilizzabile. La chiave è confermare che assegnerai persone al lavoro corretto.

Prima di iniziare questa sezione, assicurati che:
1. Tu sappia quale scenario/soluzione di Scheduling userai.
2. Tu sappia quale linea, tipo di giorno o contesto coprirai.
3. Tu sappia distinguere la soluzione attiva da un’iterazione non consolidata.

Per selezionare l’input corretto:
1. In Rostering, apri la configuration di calcolo / configuration dello scenario di assegnazione.
2. Seleziona la **Scheduling solution** che sarà l’input (cioè la soluzione published per un date range).
3. Conferma che il day type corrisponda a ciò che vuoi calcolare.
4. Conferma che le linee corrispondano al caso.
5. Se ci sono più versioni disponibili, seleziona solo quella che vuoi davvero come baseline.
6. Salva la selezione.
7. Conferma che il sistema mostri chiaramente quale lavoro verrà assegnato.

Per il caso di riferimento, assicurati che:
1. L’input corrisponda a L1 feriale.
2. Non stai mescolando una versione published con un’iterazione non approvata.
3. Il lavoro che entra in Rostering è esattamente quello che vuoi coprire.

Quando termini questa sezione, dovresti avere un input di Scheduling ben definito per il calcolo staff.

## Configurare il calcolo di Rostering con regole e popolazione corrette

Una volta selezionato l’input, conferma che il calcolo usi popolazione e regole corrette. In Rostering, una cattiva combinazione di popolazione, regole e disponibilità può rendere la soluzione non fattibile anche se Scheduling era corretta.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia selezionato l’input di Scheduling.
2. Tu sappia quale popolazione staff partecipa.
3. Tu abbia deciso se usare basic rules, advanced rules o una combinazione controllata.

Per configurare il calcolo di Rostering:
1. Inizia la configuration del calcolo creando un nuovo scenario di Rostering.
2. Seleziona questi input:
   1. i **Depots** partecipanti,
   2. le **dates** per il nuovo scenario di Rostering,
   3. il **rules model** applicato, confermando che le regole attive corrispondano al group corretto,
   4. una **description** se vuoi aggiungere dettagli.
3. Salva la configurazione.
ref: P25_Imagen2.png | compact
4. Conferma che il calcolo consideri:
   1. assenze,
   2. inattività,
   3. loans,
   4. e restrizioni di disponibilità.
5. Conferma che il calcolo abbia:
   1. lavoro di input,
   2. popolazione idonea,
   3. regole applicabili.

Per il caso di riferimento, conferma che:
1. Il gruppo autisti di L1 sia quello usato.
2. Le regole attive corrispondano a quel gruppo.
3. La configurazione non stia ereditando vincoli da un altro contesto.

Quando termini questa sezione, dovresti avere il calcolo di Rostering parametrizzato correttamente prima di eseguirlo.

## Eseguire il primo calcolo di assegnazione

Ora puoi eseguire il calcolo. Il sistema proverà ad assegnare persone reali al lavoro ereditato da Scheduling rispettando regole, assegnazione e disponibilità.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia selezionato l’input corretto.
2. Tu abbia configurato popolazione e regole.
3. Tu abbia rivisto disponibilità e cambi di contesto.
4. Tu non stia mancando master data essenziali.

Per eseguire il calcolo di Rostering:
1. Dallo scenario/modulo di Rostering, esegui **Calculate** / **Start calculation**.
ref: P25_Imagen3.png | compact
2. Conferma che il sistema inizi a processare l’assegnazione.
3. Attendi che il calcolo termini.
4. Controlla se il sistema restituisce:
   1. una soluzione assegnata,
   2. una soluzione parziale,
   3. o un segnale chiaro di conflitto.
5. Se il calcolo non produce una soluzione utilizzabile, non assumere subito che manchi staff. Prima rivedi:
   1. regole troppo restrittive,
   2. assegnazione errata,
   3. assenze caricate in modo errato,
   4. loans e qualifications incoerenti.

Per il caso di riferimento, conferma che:
1. Il calcolo L1 giri sulla popolazione attesa.
2. Il sistema provi ad assegnare lavoro reale a persone reali.
3. Il risultato ti permetta di valutare fattibilità o identificare conflitti concreti.

Quando termini questa sezione, dovresti avere una prima soluzione di Rostering o un segnale chiaro su dove si trova il blocco.

## Interpretare se il problema sono regole, disponibilità o assegnazione

Dopo il calcolo, interpreta correttamente il risultato. Non tutti i fallimenti significano la stessa cosa. Se interpreti male la causa, rischi di correggere il layer sbagliato.

Prima di continuare, assicurati che:
1. Tu abbia già eseguito il calcolo.
2. Tu abbia visto se la soluzione è completa, parziale o conflittuale.
3. Tu sia disposto a diagnosticare prima di cambiare dati.

Per interpretare il risultato:
1. Se mancano molte assegnazioni, rivedi prima la **availability** dello staff.
2. Se il sistema esclude persone che dovrebbero essere valide, rivedi **assignment** e **qualifications**.
3. Se l’assegnazione sembra troppo rigida o impossibile, rivedi le **Rostering rules**.
4. Se il lavoro ereditato sembra non fattibile per qualsiasi popolazione, verifica se il problema deriva da **Scheduling**.
5. Non correggere per intuizione: prima localizza se il problema appartiene a:
   1. regole,
   2. disponibilità,
   3. assegnazione,
   4. o struttura ereditata.

Per il caso di riferimento, chiediti:
1. Mi mancano davvero persone o sono configurate male?
2. Una regola abilitata ha reso impossibile l’assegnazione?
3. Sto provando a usare un autista in un contesto in cui non appartiene o per cui non è qualificato?
4. Il problema esisteva già prima di entrare in Rostering?

Quando termini questa sezione, dovresti avere una lettura diagnostica iniziale del risultato del calcolo.

## Lasciare la soluzione pronta per la review funzionale

L’obiettivo di questo quick start non è ancora approvare la soluzione. È eseguire il primo calcolo e lasciare una baseline pronta per la review funzionale: coverage, conflitti, bilanciamento e fattibilità.

Prima di concludere, assicurati che:
1. Tu abbia eseguito il calcolo.
2. Tu abbia rivisto se la soluzione è completa o parziale.
3. Tu abbia identificato se i problemi appartengono a regole, disponibilità, assegnazione o Scheduling.

Per chiudere il primo calcolo in modo utile:
1. Mantieni il risultato del calcolo come baseline di review.
2. Evita cambi massivi prima di identificare la causa.
3. Decidi se il prossimo passo è:
   1. rivedere conflitti di coverage,
   2. aggiustare regole,
   3. correggere dati staff,
   4. oppure tornare a Scheduling se il problema è strutturale.
4. Tratta questa prima esecuzione come validazione dell’intero modello di assegnazione.
5. Se la baseline è ragionevole, continua con la review di conflitti e coverage.

Per il caso di riferimento, termina questo quick start solo quando puoi affermare:
1. Hai eseguito il primo calcolo di Rostering per L1.
2. Sai se la soluzione è praticabile o parziale.
3. Hai un’ipotesi chiara sui conflitti principali.
4. Sei pronto a rivedere coverage e conflitti in maggiore dettaglio.

Quando termini questa sezione, dovresti aver eseguito il primo calcolo di Rostering e avere una baseline chiara per la fase di review successiva.

## Additional reading

- [Revisionare conflitti, copertura e fattibilità del personale](P26_Revisionare_conflitti_copertura_e_fattibilita_del_personale.md)

