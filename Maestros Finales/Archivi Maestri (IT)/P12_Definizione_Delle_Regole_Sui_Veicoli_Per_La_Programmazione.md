---
title: Definizione delle regole sui veicoli per la programmazione
shortTitle: Regole relative ai veicoli
intro: Scopri come impostare le regole dei veicoli che limiteranno quali soluzioni
  del parco sono valide nella programmazione, in modo che il calcolo rispetti la realtà
  operativa, l'infrastruttura e l'offerta convalidata.
contentType: how-tos
versions:
- '*'
---
## Preparazione della base che utilizzerà le regole del veicolo

Prima di attivare le regole del veicolo, è necessario verificare che la base che queste regole stanno per consumare è già pronta. Le regole del veicolo non sostituiscono una precedente parametrizzazione difettosa. La loro funzione è di raffinare il comportamento di calcolo in modo che il motore scarti combinazioni invisibili o indesiderate.

Utilizza questo avvio rapido quando hai già un'offerta di servizio convalidata, una linea con flotta consentita e una struttura operativa coerente, e devi preparare il caso prima di creare lo scenario di programmazione.

Prima di iniziare, assicurati che:
1. Avete gia' sistemato la flotta autorizzata per linea su P8.
2. Hai già definito la versione oraria e i tempi di viaggio in P9.
3. Hai già creato e convalidato l'offerta di servizio a P10.
4. Hai già controllato la struttura operativa e lo stato del servizio a P11.
5. Sei chiaro che linea e servizio userai come riferimento.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Definirò le regole dei veicoli per la linea L1, in modo che la programmazione utilizzi solo una flotta coerente con l'infrastruttura, l'offerta convalidata e le restrizioni di servizio effettive.**

Per preparare la base di casi prima di attivare le regole:
1. Apri la riga che userai come riferimento.
2. Controllare quali tipi di veicolo sono ammessi.
3. Controllare da quale deposito o parcheggio l'operazione lascerà.
4. Conferma che il servizio che userai come ingresso è già **Convalida**.
5. Verificare che non si sta cercando di risolvere con regole un problema che avrebbe dovuto essere corretto prima online, flotta o infrastrutture.
6. Se si rileva un'incoerenza su quella base, correggere prima di passare alle impostazioni delle regole.

Quando si termina questa sezione, si dovrebbe essere chiari su che vero caso si sta cercando di proteggere con le regole del veicolo.

## Creazione o selezione del modello di norme sui veicoli

Una volta controllata la base, è necessario inserire il modello o il catalogo delle regole del veicolo. A questo punto non si tratta di attivare tutto. Si tratta di scegliere o costruire un insieme di restrizioni che rappresentano la vera logica del servizio.

Prima di iniziare questa sezione, assicurarsi che:
1. Sai che servizio convalidato userai come riferimento.
2. Hai già confermato quali tipi di veicolo sono validi per la linea.
3. Sai quali veri problemi vuoi evitare.

Per creare o selezionare il modello di regola:
1. In GoalBus vedere **Impostazioni** > **Veicoli** > **Regole relative al tipo di veicolo**.
ref: P12_Imagen1.png | compact
2. Controlla se c'è già un modello corretto di regole per il tuo caso.
3. Se il modello esiste già, aprilo e controlla la sua configurazione.
4. Se non esiste, creare un nuovo modello di regole.
5. Assegna un **nome** chiaro al modello.
6. Se applicabile, aggiungere un **descrizione** che permette di distinguere il suo scopo.
7. Salva il modello.
ref: P12_Imagen2.png | compact
8. Conferma che il modello è già disponibile per aggiungere regole concrete.

Per il caso di riferimento, un'opzione valida potrebbe essere:
- **Veicoli - L1 utilizzabile**
- **Regole della flotta - Servizio funzionale L1**

Quando si termina questa sezione, si dovrebbe avere un contenitore chiaro per impostare le restrizioni del veicolo del caso.

## Attiva solo le regole del veicolo di cui hai davvero bisogno

Ora è possibile iniziare ad attivare le regole. Qui è importante mantenere un criterio chiaro: una regola deve rappresentare un reale bisogno di funzionamento, sicurezza, infrastruttura o conformità. Se una regola non risponde ad un problema particolare, non è appropriato attivarlo ancora.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già creato o selezionato un modello di regole.
2. Sai che flotta è valida per la linea.
3. Sai quali combinazioni dovrebbero essere vietate o limitate.

Per attivare le regole del veicolo del caso:
1. All'interno del modello di regola, controllare il catalogo di regole disponibili cliccando su **Aggiungere nuova regola**.
ref: P12_Imagen3.png
2. Identificate quali rispondono alle esigenze effettive del vostro servizio selezionando l'appropriato **modello**.
3. Definire un **Nome** e digitare un **Designazione delle merci** per ogni nuova regola.
4. Attiva solo le regole di cui hai davvero bisogno per il caso.
5. Configura i parametri specifici di ciascuna regola quando si applica.
6. Ripetere il processo per coprire le restrizioni minime richieste.
7. Salva i cambiamenti.
8. Rivedere il modello completo e confermare che non è molto restrittivo o troppo aperto.

Per il caso di riferimento, chiedetevi:
1. Quali situazioni di flotta dovrebbe prevenire il sistema?
2. Quali combinazioni sarebbero fisicamente possibili ma non auspicabili?
3. Quali comportamenti dovrebbero essere guidati dalla logica del deposito, parcheggio o linea?

Quando si conclude questa sezione, si dovrebbe avere un set iniziale di regole del veicolo attivo e coerente simile a quello nella seguente immagine:
ref: P12_Imagen4.png | compact(20x)

## Relativamente alle norme in materia di linea, flotta e infrastrutture

Dopo aver attivato le regole, è necessario verificare che siano realmente allineati con la linea e l'infrastruttura che sostiene il caso. Una regola del veicolo non dovrebbe contraddire la flotta consentita dalla linea o la geografia dei magazzini e del parcheggio.

Prima di continuare, assicurarsi che:
1. Hai già attivato le regole iniziali.
2. Hai già controllato i tipi di veicoli autorizzati.
3. Conosci la base fisica da cui esce l'operazione.

Per verificare la coerenza delle norme:
1. Controlla di nuovo le impostazioni della riga.
2. Conferma che le regole non contraddicono i tipi di veicoli autorizzati.
3. Controllare il rapporto con il magazzino e il parcheggio autorizzato.
4. Essa dimostra che le regole rafforzano questa logica, anziché infrangerla.
5. Se una regola rende il servizio inoperabile o contraddice l'infrastruttura, correggetelo o disattivatelo.
6. Salva la versione finale del modello.

Per il caso di riferimento, assicurarsi che:
1. La linea L1 può ancora utilizzare la flotta autorizzata.
2. Il North Depot rimane un'uscita coerente per il servizio.
3. Nessuna regola blocca un'operazione che dovrebbe essere valida in base alla base già configurata.

Quando si conclude questa sezione, si dovrebbero avere regole allineate con la realtà del servizio, non con un modello astratto o generico.

## Conferma che l'offerta convalidata è ancora calcolabile

L'ultimo passo è quello di verificare che le regole del veicolo che hai appena attivato continuino a consentire il calcolo dell'offerta convalidata. Una cosa è limitare con criteri, e un'altra è chiudere il modello così tanto che il servizio cessa di essere valido prima anche di creare lo scenario.

Prima di finire, assicurati che:
1. Hai già attivato le regole necessarie.
2. Hai gia' controllato la sua relazione con la linea, la flotta e l'infrastruttura.
3. Siete chiari quale sarà l'ingresso di Scheduling.

Per convalidare che il caso è ancora funzionabile:
1. Ricontrolla il servizio convalidato che userai come riferimento.
2. Controlla che la linea abbia ancora accesso alla flotta di cui ha bisogno.
3. Controllare se le regole attivate lasciano almeno una soluzione ragionevole per il caso.
4. Chiedetevi se il sistema potrebbe già creare uno scenario di programmazione senza cadere in contraddizione.
5. Se la risposta è sì, continuare con il prossimo inizio rapido.
6. Se la risposta è no, correggere il modello di regola prima di seguire.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. La linea L1 mantiene una flotta valida e autorizzata.
2. Il servizio funzionale convalidato rimane compatibile con le regole attivate.
3. Il modello di veicolo è ora pronto per essere utilizzato nell'ambito dello scenario di programmazione.

Quando si conclude questa sezione, si dovrebbe essere in grado di dire che la logica dei veicoli è già chiusa ed è abbastanza coerente da passare alla definizione delle regole di turno e la creazione dello scenario.

## Letture aggiuntive

- [Definizione dei tipi di turni e delle regole dei turni](P13_Definizione_Dei_Tipi_Di_Turni_E_Delle_Regole_Dei_Turni.md)
