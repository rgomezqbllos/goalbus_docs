---
title: Eseguire il primo calcolo della Rostering
shortTitle: Calcola la registrazione
intro: Imparare come preparare ed eseguire il primo calcolo di Rostering, verificare
  se la soluzione personale è valida, e individuare quali problemi appartengono a
  regole, disponibilità, o distacco prima di validare l'assegnazione.
contentType: how-tos
versions:
- '*'
---
## Preparazione della base prima di lanciare il calcolo della Rostering

Prima di eseguire il calcolo, è necessario verificare che la base dello staff sia abbastanza matura. La registrazione non dovrebbe essere utilizzata per scoprire i dati master mancanti all'ultimo minuto. Se il modello, distacco, regole o disponibilità non sono ben preparati, il calcolo fallirà o produrrà una soluzione fuorviante.

Utilizza questo avvio rapido quando hai già una soluzione di programmazione stabile e hai preparato tutto il personale necessario per assegnare un lavoro reale ai piloti.

Prima di iniziare, assicurati che:
1. Hai gia' chiuso la transizione da Scheduling alla P19.
2. Hai già caricato e controllato i driver su P20.
3. Hai già convalidato il distacco operativo a P21.
4. Hai già impostato le regole della registrazione a P22.
5. Avete già registrato assenze, inattività e disponibilità a P23.
6. Avete già registrato assegnazioni, trasferimenti o modifiche di distacco in P24.
7. Siete chiari che soluzione di programmazione funzionerà come input per il calcolo.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Sto per eseguire il primo calcolo di Rostering per la linea L1, utilizzando una soluzione già stabile di Scheduling e una base di driver adeguatamente preparata.**

Per preparare la base prima del calcolo:
1. Apre l'ambiente o il modulo **Registrazione**.
ref: P25_Imagen1.png | compact
2. Controllare quale soluzione di programmazione sarà l'input del calcolo.
3. Conferma che il collettivo di driver che parteciperà è disponibile e appartiene al contesto corretto.
4. Verifica che le regole di registrazione attive rispondano al vero caso.
5. Verifica che le principali assenze e inattività siano già registrate.
6. Conferma che le assegnazioni o i trasferimenti pertinenti sono già riflessi.
7. Se si rileva un problema di dati master, correggere prima di calcolare.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. La soluzione L1 non necessita più di cambiamenti strutturali.
2. Il collettivo di piloti esiste già ed è pronto.
3. Le regole e la disponibilità rappresentano già la realtà del periodo.
4. Ora puoi provare un vero lavoro.

Quando si termina questa sezione, si dovrebbe avere una base abbastanza stabile per lanciare la Rostering.

## Selezionare la voce corretta dalla programmazione

La registrazione ha bisogno di un'entrata di lavoro chiara. Questa entrata non dovrebbe essere un mix ambiguo di scenari, ma una soluzione di programmazione ben nota e utilizzabile. In questa fase, la cosa importante è di confermare che si sta per assegnare le persone al lavoro giusto.

Prima di iniziare questa sezione, assicurarsi che:
1. Sai che scenario o soluzione di programmazione userai.
2. Sai che linea, tipo di giorno o contesto hai intenzione di coprire.
3. Ora è possibile distinguere tra la soluzione attuale e una iterazione non consolidata.

Per selezionare correttamente l'input del calcolo:
1. Nel modulo Rostering, aprire le impostazioni di calcolo o lo scenario di mappatura.
2. Selezionare **Soluzione di programmazione** che fungerà da voce, cioè quale soluzione viene pubblicata per un intervallo di date.
3. Controllare che il tipo di giorno corrisponda al calcolo che si desidera fare.
4. Controllare che la linea o l'insieme di linee corrispondano al caso.
5. Se ci sono diverse versioni possibili, scegli solo quella che vuoi davvero usare come base.
6. Salva la selezione.
7. Controllare che il sistema mostra già chiaramente quale lavoro sarà assegnato.

Per il caso di riferimento, assicurarsi che:
1. La voce corrisponde a L1 utilizzabile.
2. Non mischi una versione pubblicata con una iterazione non approvata.
3. Il lavoro che viene a Rostering è esattamente quello che vuoi coprire.

Quando si conclude questa sezione, si dovrebbe avere una ben definita voce di programmazione per il calcolo del personale.

## Configurazione del calcolo della registrazione con le regole corrette e collettive

Una volta scelta la voce, è necessario verificare che il calcolo utilizza il collettivo e le regole corrette. In Rostering, una cattiva combinazione di collettivo, regole e disponibilità può rendere una soluzione che in Schedulering è stato corretto invisibile.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già selezionato l'entrata da Scheduling.
2. Sapete che gruppo di personale parteciperà.
3. Hai già definito se userai regole di base avanzate o una combinazione controllata.

Per configurare il calcolo della Rostering:
1. Inizia la configurazione del calcolo della mappatura creando un nuovo scenario di torrefazione.
2. Selezionare i seguenti dati di ingresso:
   1. Il **Depositi** che parteciperà.
   2. Selezionare il **date** dal nuovo scenario di torrefazione.
   3. Controllare quale **Regole tipo** si applicherà al calcolo. Confermare che le regole attive corrispondono al gruppo corretto.
   4. Aggiungere un **descrizione** se si desidera dare più dettagli.
3. Salva le impostazioni.
ref: P25_Imagen2.png | compact(x10)
4. Controllare se il calcolo prenderà in considerazione:
   1. assenze,
   2. inattività,
   3. assegnazioni,
   4. e restrizioni di disponibilità.
5. Verificare che il calcolo abbia già:
   1. lavoro di ingresso,
   2. collettivo ammissibile,
   3. le norme applicabili.

Per il caso di riferimento, essa conferma che:
1. Il gruppo driver L1 è quello da utilizzare.
2. Le regole attive corrispondono a tale gruppo.
3. La configurazione non trascina le restrizioni da un altro contesto.

Quando si termina questa sezione, si dovrebbe avere il calcolo di Rostering parametrizzato correttamente prima di eseguire.

## Eseguire il primo calcolo dell'assegnazione

Ora è possibile avviare il calcolo. A questo punto, il sistema cercherà di assegnare persone reali al lavoro ereditato da Schedule, rispettando le regole, distacco e disponibilità.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già scelto l'entrata giusta.
2. Hai creato il collettivo e le regole.
3. Hai già rivisto la base di disponibilità e i cambiamenti di contesto.
4. Non vi mancano più dati master essenziali.

Per eseguire il calcolo della registrazione:
1. Dalla fase di Rostering o dal modulo, lancia l'azione **Calcola** o **Inizio calcolo**.
ref: P25_Imagen3.png | compact(3x)
2. Controllare che il sistema avvii l'elaborazione dell'assegnazione.
3. Aspetta che il calcolo sia finito.
4. Controllare se il sistema restituisce:
   1. una soluzione assegnata,
   2. una soluzione parziale,
   3. o un chiaro segno di conflitto.
5. Se il calcolo non genera una soluzione utilizzabile, non supporre immediatamente che manca personale. Controllare prima:
   1. regole troppo restrittive,
   2. distacco errato,
   3. assenze indebitamente imputate,
   4. o incarichi e valutazioni divergenti.

Per il caso di riferimento, essa conferma che:
1. Il calcolo di L1 è eseguito sul collettivo previsto.
2. Il sistema cerca di assegnare un lavoro reale a persone reali.
3. Il risultato consente di rivedere la fattibilità o rilevare specifici conflitti.

Quando si termina questa sezione, si dovrebbe avere una prima soluzione di Rostering o un chiaro segno di dove si trova la serratura.

## Interpretare se il problema è regole, disponibilità o distacco

Dopo il calcolo, è necessario interpretare correttamente il risultato. Non tutti i difetti significano la stessa cosa. Se non si distingue bene la causa, si può correggere nel livello sbagliato.

Prima di continuare, assicurarsi che:
1. Hai gia' controllato il calcolo.
2. Hai visto se la soluzione era completa, parziale o in conflitto.
3. Sei disposto a diagnosticare prima di toccare i dati.

Per interpretare correttamente il risultato:
1. Se mancano molti incarichi, controlla prima il personale **disponibilità**.
2. Se il sistema lascia fuori le persone che dovrebbero essere valide, controllare la loro **distacco** e la loro **valutazioni**.
3. Se l'assegnazione sembra troppo rigida o impossibile, controllare **Regole di registrazione**.
4. Se il lavoro ereditario sembra inutilizzabile per qualsiasi gruppo, controlla di nuovo se il problema viene da **Programmazione**.
5. Non correggere per intuizione. Scopri prima se il problema appartiene a:
   1. regole,
   2. disponibilità,
   3. distacco,
   4. o struttura ereditata.

Per il caso di riferimento, fatevi queste domande:
1. Le persone sono davvero scomparse o mal configurate?
2. La regola che ho attivato ha reso impossibile l'incarico?
3. Sto cercando di usare un driver in un contesto in cui non appartiene o non è abilitato?
4. Il problema esisteva già prima di entrare in Rostering?

Quando si termina questa sezione, si dovrebbe avere una prima lettura diagnostica del risultato del calcolo.

## Lasciare la soluzione pronta per la revisione funzionale

Lo scopo di questo rapido avvio non è ancora quello di approvare definitivamente la soluzione. L'obiettivo è quello di eseguire il primo calcolo e lasciare una base pronta per la revisione funzionale: copertura, conflitti, equilibrio e redditività.

Prima di finire, assicurati che:
1. Hai gia' controllato il calcolo.
2. Hai già controllato se la soluzione è completa o parziale.
3. Hai già identificato se i problemi appartengono a regole, disponibilità, distacco o programmazione.

Per chiudere questo primo calcolo utilemente:
1. Essa conserva il risultato del calcolo come base per il riesame.
2. Non fare cambiamenti massicci senza prima identificare la causa del problema.
3. Decide se il prossimo passo sarà:
   1. esaminare i conflitti di copertura,
   2. adeguare le regole,
   3. correzione dei dati del personale,
   4. o ritornare a Scheduling se il problema è strutturale.
4. Tratta questa prima esecuzione come una convalida dell'intero modello di mappatura.
5. Se la base è ragionevole, proseguire con la revisione della copertura e dei conflitti.

Per il caso di riferimento, finite questo avvio rapido solo quando potete dire:
1. Avete già eseguito il primo calcolo di Rostering per L1.
2. Sai se la soluzione è fattibile o parziale.
3. Avete già una chiara ipotesi su dove si trovano i principali conflitti.
4. Siete pronti a rivedere la copertura e i conflitti in modo più dettagliato.

Quando hai finito questa sezione, avresti dovuto eseguire il primo calcolo di Rostering e una base chiara per la prossima fase di revisione.

## Letture aggiuntive

- [Rivedere i conflitti, la copertura e la fattibilità del personale](P26_Rivedere_I_Conflitti_La_Copertura_E_La_Fattibilità_Del_Personale.md)
