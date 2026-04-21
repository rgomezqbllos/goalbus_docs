---
title: Creare la base del calendario con tipi di giorno e festività
shortTitle: Tipi di giorno e festività
intro: 'Scopri come configurare tipi di giorno e festività in modo che la logica di planning applichi il corretto pattern operativo prima di passare a percorsi, tempi di viaggio e creazione dei servizi.'
contentType: how-tos
versions:
  - '*'
---

## Creare il tipo di giorno che userai per la pianificazione

Prima di creare servizi o eseguire calcoli di planning, devi definire la logica di calendario che indica al sistema con quale tipo di giorno sta lavorando. In GoalBus, i tipi di giorno sono categorie operative che raggruppano giorni come feriali standard, venerdì, weekend o giorni speciali, così non devi costruire la logica di planning data per data.

Usa questo quick start quando stai preparando il tuo primo caso di planning, quando devi creare o validare il tipo di giorno che userà il tuo scenario, oppure quando vuoi assicurarti che la logica delle festività sia pronta prima di continuare.

Prima di iniziare, assicurati che:
1. Tu abbia accesso all’ambiente con permessi per visualizzare o modificare la configurazione del calendario.
2. Tu sappia già quale caso di planning vuoi costruire.
3. Tu sappia già quale periodo vuoi preparare, ad esempio gennaio 2026.
4. Tu abbia già rivisto il tuo ruolo di planner e il flusso complessivo in P1.

Per questo quick start, usa questo caso di riferimento:

> **Sto preparando la base del calendario per uno scenario feriale per gennaio 2026, includendo il corretto comportamento delle festività.**

Per creare o validare il tipo di giorno per il tuo caso:
1. In GoalBus, vai su **Configuration** > **Time Management** > **Day type management**.
ref: P2_Imagen1.png | compact
2. Rivedi i tipi di giorno esistenti e verifica se uno rappresenta già la logica operativa di cui hai bisogno.
3. Se esiste già un tipo di giorno adatto, conferma che:
   1. Il suo nome sia chiaro.
   2. Il suo nome breve sia chiaro.
   3. Rappresenti davvero il pattern operativo di cui hai bisogno.
4. Se non esiste un tipo di giorno adatto, fai clic su **Create day type**.
ref: P2_Imagen2.png | full
5. Definisci il **name** e lo **short name** per il nuovo tipo di giorno.
ref: P2_Imagen3.png | compact
6. Seleziona i giorni della settimana che si applicano a quel tipo di giorno.
ref: P2_Imagen4.png | compact
7. Se il tipo di giorno deve applicarsi anche alle festività, abilita l’opzione per applicare il tipo di giorno alle festività.
ref: P2_Imagen5.png | compact
8. Salva il tipo di giorno.
9. Rivedi il risultato e conferma che il tipo di giorno rappresenti ora chiaramente il caso che stai preparando.

Quando termini questa sezione, dovresti avere un tipo di giorno che il sistema può usare come categoria operativa per il tuo caso di planning.

## Registrare le festività che modificano la normale logica di calendario

Dopo aver definito il tipo di giorno generale, devi indicare al sistema cosa fare con le date eccezionali. Le festività sono importanti perché il calendario può dire che una data è martedì, mentre l’operatività dovrebbe comportarsi come una domenica o seguire un altro pattern speciale. Se le festività non vengono registrate correttamente, il sistema potrebbe applicare il piano sbagliato quando in seguito pubblichi o calcoli scenari.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già creato o confermato il tipo di giorno che userà il tuo caso.
2. Tu sappia se il periodo di planning include festività o date speciali.
3. Tu sia pronto a decidere quale pattern operativo deve seguire ogni festività.

Per registrare e validare le festività per il tuo caso:
1. Nella stessa sezione di gestione dei tipi di giorno, passa alla scheda **Holidays**.
ref: P2_Imagen6.png | compact
2. Verifica se la festività di cui hai bisogno esiste già nel sistema.
3. Se la festività non esiste, crea un nuovo record di festività.
4. Se la festività esiste già, aprila e rivedi la sua configurazione.
5. Inserisci o conferma il **name** della festività.
6. Assegna il corretto **day type** a quella festività.
ref: P2_Imagen7.png | compact
7. Salva il record della festività.
8. Ripeti questo processo per qualsiasi altra festività che impatta il periodo che stai preparando.
9. Rivedi l’elenco delle festività e conferma che ogni data eccezionale punti al corretto pattern operativo.

Per il caso di riferimento, chiediti:
1. Gennaio 2026 include una festività che dovrebbe comportarsi diversamente da un normale giorno feriale?
2. Quella festività dovrebbe comportarsi come una domenica, un sabato o un altro tipo di giorno speciale?
3. Se pubblicassi uno scenario per questo periodo, il sistema saprebbe esattamente quale pattern applicare in quella data?

Quando termini questa sezione, il sistema dovrebbe essere in grado di sovrascrivere il comportamento normale del calendario nelle date festive rilevanti per il tuo caso.

## Verificare che la base del calendario sia pronta per la pianificazione

Ora che hai definito il tipo di giorno generale e le eccezioni delle festività, devi confermare che la base del calendario sia effettivamente utilizzabile. Qui verifichi che la struttura creata possa supportare i prossimi quick start senza introdurre errori evitabili.

Prima di continuare, assicurati che:
1. Il tipo di giorno esista e abbia la corretta logica settimanale.
2. Le festività rilevanti siano registrate.
3. Ogni festività sia collegata al tipo di giorno corretto.
4. Il tuo caso di planning sia ancora chiaro e specifico.

Per validare la base del calendario prima di passare al prossimo quick start:
1. Rivedi il caso di planning che hai definito all’inizio di questo articolo.
2. Conferma che il tipo di giorno che hai creato o validato corrisponda a quel caso.
3. Conferma che qualsiasi festività nel periodo di planning sia stata registrata e associata al tipo di giorno corretto.
4. Verifica che l’opzione di applicazione alle festività che hai abilitato nel tipo di giorno rifletta davvero il comportamento desiderato.
5. Chiediti se il sistema potrebbe già distinguere:
   1. i giorni normali del periodo, e
   2. le date eccezionali che devono seguire un pattern operativo diverso.
6. Se la risposta è sì, continua con il prossimo quick start.
7. Se la risposta è no, torna indietro e correggi le associazioni del tipo di giorno o delle festività prima di procedere.

Quando termini questa sezione, dovresti poter affermare che il tuo caso di planning ha una base di calendario affidabile e che i prossimi quick start possono costruire su di essa senza ereditare un errore di logica temporale.

## Additional reading

- [Validare l’anno operativo prima di pianificare](P3_Valider_l_anno_operativo_prima_di_pianificare.md)
