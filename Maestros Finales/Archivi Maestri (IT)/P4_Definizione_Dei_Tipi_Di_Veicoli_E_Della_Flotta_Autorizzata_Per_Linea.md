---
title: Definizione dei tipi di veicoli e della flotta autorizzata per linea
shortTitle: Flotta per linea
intro: Scopri come configurare i tipi di veicoli e le restrizioni del parco veicoli
  consentite per linea in modo che GoalBus blocchi incarichi non fattibili, rispetti
  i limiti fisici e ambientali e prepari una base coerente prima di definire orari
  e servizi.
contentType: how-tos
versions:
- '*'
---
## Definizione dei tipi di veicolo consentiti per una linea

Come primo passo, è necessario chiarire quale **tipo di veicolo** può utilizzare ogni linea. In GoalBus, questa restrizione non è decorativa: agisce come un filtro di sicurezza, conformità e vitalità fisica. L'obiettivo è quello di evitare che il sistema di proporre un veicolo che non si inserisce in una strada, che non rispetta una restrizione ambientale, o che non dovrebbe circolare in quel servizio.

Usa questo avvio rapido quando devi chiudere la base della flotta che il tuo caso userà prima di definire i tempi e l'offerta di servizio.

Prima di iniziare, assicurati che:
1. Sei chiaro che linea userai come caso di riferimento.
2. Sapete, almeno a livello di base, quali restrizioni fisiche o ambientali influiscono su questa linea.

Per questo avvio rapido, utilizzare questo caso di riferimento:

> **Ho intenzione di definire quali tipi di veicolo possono utilizzare la linea L1 per assicurarmi che la mia prima pianificazione utilizzi solo una flotta coerente con la realtà fisica e regolamentare del servizio.**

Per definire i tipi di veicolo consentiti del vostro caso:
1. In GoalBus, se esiste già una linea, apri la configurazione **riga** che stai per usare come riferimento.
2. Trova la sezione **Tipi di veicoli ammessi**.
3. Controllare se la riga ha già assegnato i tipi.
4. Se la riga ha già definito i tipi, conferma che sono ancora corretti per il caso.
5. Se non sono ancora definiti, controllare prima se il **Tipo di veicolo** è già necessario esistere nella configurazione generale del veicolo.
6. Se digitare **Sì, esiste davvero.**, selezionare come consentito per quella riga.
7. Se digitare **non esiste**, uscire dalle impostazioni di riga e andare alle impostazioni generali **veicoli** per creare o completare prima il catalogo di tipo disponibile dal pannello **Tipi di veicoli**.
ref: P4_Imagen1.png | full
8. Crea il tipo di veicolo di cui hai bisogno utilizzando una categoria chiara e comprensibile per l'azienda, ad esempio:
   1. Minibus
   2. Standard elettrico
   3. Diesel articolato
ref: P4_Imagen2.png | compact(2x5)
9. Salva il nuovo tipo di veicolo.
ref: P4_Imagen3.png | compact(x9)
10. Torna alle impostazioni di riga.
11. Segnare i tipi specifici di veicolo che sono autorizzati a funzionare su tale linea.
ref: P4_Imagen4.png | compact(8x)
12. Lasciate senza segnali i ragazzi che non devono operare quel servizio.
13. Salva le impostazioni.
14. Ricontrollare la riga (se esiste già) e confermare che il filtro rappresenta già correttamente la realtà operativa.

Per il caso di riferimento, chiedetevi:
1. La linea L1 supporta un autobus standard, un minibus o entrambi?
2. Esiste un tipo di veicolo da escludere per dimensioni o per ambiente?
3. Se non c'era il tipo di cui avevi bisogno, l'hai creato prima di cercare di assegnarlo alla linea?
4. Il sistema dovrebbe bloccare una mappatura manuale se si cerca di utilizzare un veicolo non autorizzato?

Quando si conclude questa sezione, si dovrebbe avere definito una restrizione flotta per linea che già serve come base per ulteriori calcoli.

## Relazione della linea con i magazzini o i parcheggi autorizzati

Dopo aver definito quale flotta si adatta o non si adatta alla linea, è necessario controllare da quali basi fisiche che il servizio può uscire. GoalBus consente di definire **parcheggi o magazzini autorizzati** per linea per forzare il sistema a iniziare il servizio da posizioni geograficamente corrette e ridurre il chilometraggio vuoto.

Prima di iniziare questa sezione, assicurarsi che:
1. Hai già configurato i tipi di veicolo autorizzati della linea.
2. Sai da che base operativa dovrebbe davvero iniziare il servizio.

Per collegare la linea ai vostri magazzini o parcheggio autorizzati:
1. All'interno della stessa configurazione di linea, individuare la sezione **Parcheggio consentito** o **Depositi ammissibili**.
2. Controllare se la linea ha già autorizzato depositi.
3. Selezionare solo i magazzini o i garage che sono geograficamente autorizzati a iniziare i servizi su quella linea.
4. Lascia fuori le basi che non hanno senso operativo per quel broker.
5. Salva le impostazioni.
6. Verificare che la linea ora ha una logica coerente di uscita dalla base più ragionevole.

Per il caso di riferimento, ritiene che:
1. La linea L1 può uscire dal North Depot.
2. Il parcheggio principale associato è quello giusto.
3. Non permettete un deposito distante che vi costringe a percorrere molte miglia in un vuoto per iniziare il primo viaggio.

Quando si termina questa sezione, si dovrebbe avere la linea (se esiste già), la flotta ammessa e la geografia di uscita di servizio allineata.

## Convalidare che la linea ha già una base di flotta coerente

Ora che avete già definito i tipi di veicolo consentiti e i magazzini autorizzati o i posti auto, è necessario effettuare una validazione finale.

Prima di continuare, assicurarsi che:
1. La linea ha già i tipi di veicolo ammessi.
2. Se il tipo di veicolo richiesto non esisteva, è stato precedentemente creato nella configurazione generale.
3. La linea ha già autorizzato magazzini o parcheggio.
4. La configurazione riflette la realtà del caso che stai costruendo.

Per convalidare che la base della flotta è già pronta:
1. Controlla di nuovo la configurazione completa della linea.
2. Conferma che i tipi di veicolo selezionati rappresentano la flotta che dovrebbe effettivamente operare tale servizio.
3. Conferma che magazzini autorizzati o parcheggi minimizzano il chilometraggio vuoto.
4. Chiedetevi se il sistema, con questa configurazione, avrebbe già evitato:
   1. incarichi fisicamente impossibili,
   2. le inosservanze ambientali,
   3. divieti da basi geograficamente inefficienti.
5. Se la risposta è sì, continuare con il prossimo inizio rapido.
6. Se la risposta è no, correggere la linea o creare il tipo di veicolo mancante prima di continuare.

Quando si conclude questa sezione, si dovrebbe essere in grado di affermare che si dispone di tutti i tipi di veicolo e flotta necessari per la pianificazione della vostra linea.

## Letture aggiuntive

- [Preparazione di parcheggi e magazzini](P5_Preparazione_Di_Parcheggi_E_Magazzini_Per_Loperazione.md)
