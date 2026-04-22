---
title: Creazione della prima tappa di programmazione con il motore Classic
shortTitle: Stage classico
intro: Scopri come creare il tuo primo scenario di programmazione con il motore GoalBus
  Classic, seleziona correttamente le voci di calcolo e distingue quando applicare
  le regole del veicolo e quando applicare le regole del turno.
contentType: how-tos
versions:
- '*'
---
## Creazione dello scenario con l'offerta convalidata come punto di partenza

Ora che avete già convalidato l'offerta, la logica del veicolo e la logica del giro, il passo successivo è quello di creare il **Stadio di programmazione** che utilizzerà quella base per calcolare una soluzione eseguibile.

Questo scenario è l'ambiente controllato in cui si sta per combinare:
1. il **offerta convalidata**,
2. il **matrice di viaggio vuota**,
3. il **modello di norme sui veicoli**,
4. e il **modello di norme sui turni**.

Usa questo avvio rapido quando hai già chiuso la parametrizzazione di base e vuoi preparare lo scenario definitivo per il calcolo con il motore Classic.

Prima di iniziare, assicurati che:
1. Avete già configurato e convalidato l'offerta di servizio in P10.
2. Hai già controllato la struttura operativa della P11.
3. Hai già definito le regole del veicolo in P12.
4. Hai già definito i tipi di turni e le regole dei turni in P13.
5. Hai già preparato la matrice di viaggio vuota per P7.
6. Sapete che tipo di giorno e quali linee faranno parte del calcolo.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Creerò il primo scenario di Schedule per la linea L1, utilizzando l'offerta praticabile convalidata, la corrispondente matrice di viaggio vuota e i modelli corretti di veicoli e regole di turno, per avviare il calcolo finale con GoalBus Classic.**

Per creare lo scenario di base del vostro caso:
1. In GoalBus, aprire il modulo **Pianificazione**.
ref: P14_Imagen1.png | compact
2. Fare clic su **Nuovo scenario**.
ref: P14_Imagen2.png | compact(2x)
3. Introduce l'identità di base dello scenario:
   1. **Nome**
   2. **Tipo di giorno**
   3. **Designazione delle merci** se si desidera dare più dettagli.
   4. **solo per i veicoli** scenario o no.
ref: P14_Imagen3.png | compact(x10)
4. Selezionare gli elementi di base dello scenario:
   1. Il **servizio commerciale convalidato** che vuoi coprire.
   2. Selezionare **Modello di regole di turno**.
   3. Selezionare **Modello di regole del tipo di veicolo** (opzionale).
   4. Selezionare **matrice di viaggio vuota** corrispondente allo stesso tipo di giorno.
   5. Selezionare il **Matrice di spostamento del conducente** che sarà parte della fase.
ref: P14_Imagen4.png | compact(x10)
5. Selezionare la riga.
ref: P14_Imagen5.png | compact(x12)
6. Salva o completa la creazione del palcoscenico.
7. Controllare che lo scenario appare nella tabella principale di pianificazione.

Per il caso di riferimento, un'opzione valida potrebbe essere:
- **Programmazione Classic - L1 utilizzabile**

Quando si conclude questa sezione, si dovrebbe avere uno scenario creato con la sua corretta logistica e input commerciali creato come nella seguente immagine:
ref: P14_Imagen6.png | full

## Comprendere quando utilizzare le regole sui veicoli e quando utilizzare le regole sui turni

Prima di impostare il motore, è necessario chiarire una distinzione importante: **Le regole dei veicoli e le regole dei turni non risolvono lo stesso problema.**.

Utilizzare **Regole relative ai veicoli** quando si desidera controllare il comportamento della flotta. Queste sono le regole giuste se è necessario modellare:
1. compatibilità fisica dei veicoli,
2. limiti di capacità o di portata,
3. restrizioni in materia di infrastrutture,
4. o politiche operative legate all'uso della flotta.

Utilizzare **regole di turno** quando si desidera controllare come il lavoro umano è organizzato. Sono le regole giuste se è necessario modellare:
1. orari di lavoro,
2. interruzioni e interruzioni,
3. ore di inizio e fine,
4. Ampiezza,
5. o differenze tra i tipi di turno, come ad esempio mattina, pomeriggio o notte.

Prima di continuare, assicurarsi che:
1. Sai quali restrizioni appartengono al veicolo.
2. Sai quali restrizioni appartengono al turno.
3. Non stai cercando di risolvere un problema di personale con le regole della flotta, o al contrario.

Per decidere quale modello utilizzare in ogni caso:
1. Chiedetevi se la restrizione riguarda **autobus** o **autista**.
2. Se colpisce **autobus**, usare **modello di norme sui veicoli**.
3. Se riguarda **lavoro umano** o il tipo di turno, utilizzare **modello di norme sui turni**.
4. Se una regola dovrebbe applicarsi a tutti i tipi di turni, riesaminarla come regola globale o con la più ampia portata disponibile.
5. Se una regola si applica solo a un particolare tipo di spostamento, assegnarlo solo a questo tipo.

Per il caso di riferimento:
1. Se si desidera limitare quale flotta può coprire la L1, utilizzare **Regole relative ai veicoli**.
2. Se vuoi controllare come viene costruito un turno domani o notte, usa **regole di turno**.
3. Se una restrizione mescola entrambi, separatela e configuratela nel modello giusto.

Quando si termina questa sezione, si dovrebbe essere chiari su quale modello risponde a ogni necessità ed evitare le configurazioni incrociate o contraddittorie.

## Selezionare il motore GoalBus Classic per il calcolo finale

Ora è necessario impostare il motore di calcolo. Per questo rapido avvio, il focus è di lavorare con **GoalBus Classic** come motore principale della fase. Questo è il motore di ottimizzazione profonda mirato ad ottenere la migliore soluzione finale quando la parametrizzazione è abbastanza matura. fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già creato il palcoscenico.
2. Hai selezionato correttamente il servizio, le linee e la matrice di viaggio vuota.
3. Sei già chiaro sui modelli di regole che userai.
4. Sei pronto per un calcolo finale o quasi finale, non solo per un rapido test tattico.

Per selezionare il motore Classic:
1. Apri lo scenario che hai appena creato premendo su di esso.
2. Nella barra superiore, fare clic su **Impostazioni di calcolo**.
ref: P14_Imagen7.png | compact
3. Sul pannello laterale, selezionare **Motore classico GoalBus**.
4. Conferma che lo scenario non è più configurato con il motore di machine learning.
5. Determina il **Flessibilità di programmazione per la prima soluzione** (il valore predefinito è 0).
6. Usare un valore prudente che ti permette di trovare una soluzione iniziale senza distorcere il caso.
7. Selezionare il **Tempo massimo di calcolo** che il motore avrà per le nuove soluzioni.
ref: P14_Imagen8.png | compact(x8)
8. Salva le impostazioni.

La flessibilità iniziale si applica solo al motore GoalBus Classic e serve a garantire che la prima soluzione non venga bloccata se le restrizioni sono troppo rigide fin dall'inizio. Il tempo massimo di calcolo funge da garanzia di consegna e costringe il sistema a restituire la soluzione valida migliore che ha trovato entro il tempo disponibile. filetturn34file0L1-L20 filetturn34file2L1-L20

Per il caso di riferimento:
1. Utilizzare **GoalBus Classic** come motore principale.
2. Riservare il motore di machine learning solo per convalida rapida precedente, non come un motore di calcolo finale.
3. Usare moderata flessibilità iniziale se si sospetta che le restrizioni potrebbero bloccare la prima soluzione.
4. Definisce un tempo massimo realistico per il team di ricevere una soluzione sostenibile entro il tempo atteso. fileciteturn34file0L1-L20fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

Quando si termina questa sezione, si dovrebbe avere il motore Classic configurato con una struttura di calcolo controllata e realistica.

## Controllo il palcoscenico prima di lanciarlo.

Prima di calcolare, è necessario fare una revisione finale dell'intero scenario. L'obiettivo è quello di confermare che non si sta inserendo il calcolo con voci contraddittorie.

Prima di continuare, assicurarsi che:
1. Hai già scelto il corretto servizio convalidato.
2. Hai già selezionato la matrice di viaggio vuota del tipo di giorno giusto.
3. Hai già assegnato i modelli giusti delle regole del veicolo e del turno.
4. Hai già selezionato GoalBus Classic come motore.
5. Hai già regolato la flessibilità e il tempo massimo.

Per rivedere lo scenario prima di avviare il calcolo:
1. Controlla il nome e il tizio della giornata.
2. Conferma che **servizio commerciale** corrisponde esattamente a quello che vuoi programmare.
3. Conferma che **matrice di viaggio vuota** corrisponde allo stesso contesto temporale.
4. Controlla il **modello di norme sui veicoli** e conferma che protegge la logica della flotta.
5. Controlla il **modello di norme sui turni** e conferma che protegge la logica del lavoro umano.
6. Controlla che non stai saltando un modello obbligatorio per il tuo caso.
7. Se tutto è coerente, lasciate lo scenario pronto per il calcolo.

Per il caso di riferimento, non continuare fino a quando non si può dire:
1. Il L1 funzionante utilizza il suo corretto servizio convalidato.
2. La matrice di lavoro è quella giusta.
3. Il modello del veicolo limita realisticamente la flotta.
4. Il modello di turno organizza il lavoro in modo coerente.
5. GoalBus Classic è già stato selezionato.

Quando si termina questa sezione, si dovrebbe avere un pulito, coerente e pronto per il calcolo finale.

## Letture aggiuntive

- [Eseguire e convalidare il primo calcolo della programmazione](P15_Eseguire_E_Convalidare_Il_Primo_Calcolo_Della_Programmazione.md)
