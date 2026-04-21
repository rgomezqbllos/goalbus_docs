---
title: Definire tipi di turno e regole dei turni
shortTitle: Tipi e regole
intro: 'Scopri come creare tipi di turno, organizzarli dentro modelli di regole e abilitare i vincoli o le penalità necessarie affinché Scheduling costruisca duties legalmente valide e operative.'
contentType: how-tos
versions:
  - '*'
---

## Creare i tipi di turno che struttureranno il lavoro

Prima di configurare le shift rules, devi definire i **shift types** che il sistema userà per raggruppare i trips in lavoro umano coerente. Uno shift type non è solo un’etichetta visiva. È la categoria logica che guida il motore a costruire duties riconoscibili e utilizzabili in seguito in Rostering, daily operations e integrazioni.

Usa questo quick start quando hai già un’offerta validata, una logica veicolo definita e devi indicare al sistema quali pattern di lavoro sono validi per il tuo caso.

Prima di iniziare, assicurati che:
1. Tu abbia già creato e validato l’offerta di servizio in P10.
2. Tu abbia già validato la struttura operativa in P11.
3. Tu abbia già definito vehicle rules in P12.
4. Tu sappia quale servizio e contesto operativo userai come riferimento.

Per questo quick start, usa questo caso di riferimento:

> **Definirò shift types per la linea L1 in modo che Scheduling possa costruire duties coerenti prima di creare lo scenario di calcolo.**

Per creare shift types per il tuo caso:
1. In GoalBus, vai su **Configuration** > **Staff** > **Shift types**.
ref: P13_Imagen1.png | compact
2. Verifica se esistono già shift types adatti al tuo caso.
3. Se un tipo esiste, aprilo e conferma che sia ancora valido.
4. Se non esiste, creane uno nuovo.
5. Definisci questi campi:
   1. **Full name**, chiaro e descrittivo.
   2. **Short name**, per viste compatte e schede operative.
   3. **External ID**, se il cliente necessita integrazione con sistemi HR o payroll.
ref: P13_Imagen2.png | compact
6. Marca il tipo come **Active** se deve partecipare a calcoli futuri.
7. Salva lo shift type.
8. Ripeti per ogni categoria di lavoro di cui hai davvero bisogno nel tuo caso.

Per il caso di riferimento, potresti creare tipi come:
1. **Morning shift**
2. **Afternoon shift**
3. **Split shift**, se richiesto dall’operatività

Quando termini questa sezione, dovresti avere shift types che agiranno come “DNA” delle duties che Scheduling costruirà.

## Creare o selezionare il modello di shift rules

Dopo aver creato shift types, devi definire il contenitore in cui vivranno le regole. Le shift rules non sono gestite come una lista piatta, ma dentro **models** che raggruppano un set coerente di vincoli per uno scenario, un periodo o una simulazione. Questo ti consente di mantenere più configurazioni senza mescolare regole storiche con quelle attive.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già creato o validato gli shift types che userai.
2. Tu sappia quale servizio o simulazione userai come riferimento.
3. Tu sappia se questo modello sarà riutilizzabile o specifico del caso.

Per creare o selezionare il rules model:
1. In GoalBus, vai su **Configuration** > **Staff** > **Shift rules**.
2. Verifica se esiste già un **rules model** adatto al tuo caso.
3. Se esiste, aprilo e conferma che sia ancora valido.
4. Se non esiste, crea un nuovo modello facendo clic su **Add New Model**.
5. Dai al modello un **Name** chiaro.
6. Se applicabile, aggiungi una **Description** che ne identifichi l’uso.
7. Salva il modello.
ref: P13_Imagen3.png | compact
8. Conferma di poter aggiungere regole dentro quel contenitore.

Per il caso di riferimento, opzioni valide potrebbero essere:
- **Shifts - L1**
- **Shift rules**

Quando termini questa sezione, dovresti avere un rules model pronto a ricevere vincoli e penalità specifiche.

## Abilitare shift rules come vincoli o penalità

Ora puoi iniziare a configurare le regole. È importante distinguere due logiche:
1. **Constraints**, che sono obbligatorie e bloccano duties non valide.
2. **Penalties**, che non bloccano, ma spingono l’ottimizzatore verso soluzioni preferite.

Questo è importante perché non tutto ciò che desideri in operations deve diventare una proibizione assoluta. Alcune condizioni dovrebbero guidare, non chiudere.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia creato o selezionato un rules model.
2. Tu sappia quale comportamento lavorativo vuoi impedire.
3. Tu sappia quale comportamento vuoi incoraggiare senza renderlo obbligatorio.

Per gestire shift rules per il tuo caso:
1. Se vuoi creare una nuova regola, fai clic su **Add New Rule**.
2. Dentro il modello, rivedi i **rule templates** disponibili e dai alla nuova regola un **Name** e una **Description**.
3. Seleziona il template che corrisponde al controllo che vuoi applicare.
4. Crea una **specific rule** da quel template facendo clic su **Confirm**.
ref: P13_Imagen4.png | compact
6. Decidi **a quali shift types si applica ciascuna regola**. Non tutte le regole devono applicarsi a tutti i tipi.
7. Inserisci i parametri concreti per la regola.
8. Salva la regola.
9. Ripeti solo per le regole realmente necessarie nel tuo caso.
10. Conferma che le regole necessarie siano attive. Per attivare una regola, deve essere assegnata ad almeno uno shift type.
ref: P13_Imagen5.png | compact

Per il caso di riferimento, pensa a esempi come:
1. Morning shifts devono iniziare dentro una finestra oraria specifica.
2. Split shifts non devono superare un massimo di spread.
3. Una sequenza indesiderata può essere penalizzata invece che proibita.

Quando termini questa sezione, dovresti avere un primo set di regole che riflette sia limiti obbligatori sia preferenze operative.

## Rivedere che le regole siano assegnate ai corretti shift types

Una volta abilitate le regole, devi rivedere **a quali shift types si applica ogni regola**. Alcune regole possono essere globali, altre devono mirare a categorie specifiche come morning, afternoon o split.

Prima di continuare, assicurati che:
1. Tu abbia abilitato almeno una regola nel modello.
2. Tu abbia definito gli shift types che partecipano al caso.
3. Tu sappia se la regola deve essere globale o specifica.

Per rivedere correttamente lo scope:
1. Seleziona ciascuna regola che hai creato.
2. Rivedi la sezione **Applicable shift types**.
3. Seleziona i tipi specifici a cui la regola deve applicarsi.
4. Se la regola deve impattare tutti i tipi nello scenario, configurala come globale selezionando **tutti gli shift types**.
5. Conferma che non ci siano due regole attive dallo stesso template applicate allo stesso shift type se ciò creerebbe un conflitto logico.
6. Salva la configurazione.
7. Ripeti per ogni regola nel modello.

Per il caso di riferimento:
1. Una finestra di inizio anticipato può applicarsi solo a **Morning shift**.
2. Una regola di pausa può applicarsi a più tipi.
3. Una preferenza generale può essere globale.

Quando termini questa sezione, dovresti avere regole con scope chiaro e senza conflitti logici, simili alla seguente immagine:
ref: P13_Imagen6.png | full

## Verificare che la logica dei turni sia ancora compatibile con il servizio

L’ultimo passo è confermare che shift types e regole definiti siano ancora compatibili con l’offerta validata e con la logica veicolo già chiusa. Non serve avere regole “belle” se il risultato lascia il servizio senza un modo realistico di essere schedulato.

Prima di concludere, assicurati che:
1. Tu abbia creato i tipi di turno necessari.
2. Tu abbia abilitato e assegnato le regole rilevanti.
3. Tu sappia quale servizio sarà l’input per lo scenario di Scheduling.

Per validare che il caso sia ancora calcolabile:
1. Rivedi il servizio validato che userai come riferimento.
2. Conferma che gli shift types creati possano davvero organizzare quel lavoro.
3. Rivedi se qualche shift rule rende il caso troppo rigido.
4. Conferma che non ci sia una forte contraddizione con le vehicle rules già abilitate.
5. Chiediti se il sistema potrebbe costruire duties legali e operative con questa base.
6. Se la risposta è sì, continua con il prossimo quick start.
7. Se la risposta è no, correggi tipi o regole prima di procedere.

Per il caso di riferimento, non procedere finché puoi affermare:
1. L’offerta validata di L1 è ancora compatibile con gli shift types definiti.
2. Le regole non bloccano inutilmente il caso.
3. Il modello è pronto per entrare nello scenario di Scheduling.

Quando termini questa sezione, dovresti poter affermare che la logica turni è sufficientemente chiusa per passare alla creazione dello scenario di Scheduling.

## Additional reading

- [Creare il primo scenario di Scheduling](P14_Creare_il_primo_scenario_di_Scheduling.md)

