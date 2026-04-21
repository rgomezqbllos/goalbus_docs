---
title: Definire le regole vehicolo per Scheduling
shortTitle: Vehicle rules
intro: 'Scopri come configurare vehicle rules che limitano quali soluzioni di flotta sono valide in Scheduling, così il calcolo rispetta la realtà operativa, l’infrastruttura e l’offerta validata.'
contentType: how-tos
versions:
  - '*'
---

## Preparare la base che useranno le vehicle rules

Prima di abilitare le vehicle rules, devi confermare che la base che queste regole consumeranno sia già pronta. Le vehicle rules non sostituiscono una cattiva parametrizzazione a monte. Il loro scopo è affinare il comportamento del calcolo in modo che il motore scarti combinazioni non fattibili o non desiderate.

Usa questo quick start quando hai già un’offerta validata, una linea con allowed fleet e una struttura operativa coerente e devi preparare il caso prima di creare lo scenario di Scheduling.

Prima di iniziare, assicurati che:
1. Tu abbia già configurato allowed fleet per linea in P4.
2. Tu abbia già definito la time version e i travel times in P9.
3. Tu abbia già creato e validato l’offerta di servizio in P10.
4. Tu abbia già rivisto struttura operativa e status del servizio in P11.
5. Tu sappia quale linea e quale servizio userai come riferimento.

Per questo quick start, usa questo caso di riferimento:

> **Definirò vehicle rules per la linea L1 in modo che Scheduling usi solo una flotta coerente con infrastruttura, offerta validata e vincoli reali del servizio.**

Per preparare la base del caso prima di abilitare le regole:
1. Apri la linea che userai come riferimento.
2. Conferma quali tipi di veicolo sono consentiti.
3. Rivedi da quale depot o parking partiranno le operazioni.
4. Conferma che il servizio di input sia già in stato **Validated**.
5. Conferma che non stai cercando di risolvere con le regole un problema che doveva essere corretto prima in linea, flotta o infrastruttura.
6. Se rilevi un’incoerenza di base, correggila prima di passare alla configurazione delle regole.

Quando termini questa sezione, dovresti avere un quadro chiaro del caso reale che stai cercando di proteggere con le vehicle rules.

## Creare o selezionare il modello/catalogo di vehicle rules

Una volta rivista la base, devi entrare nel modello/catalogo delle vehicle rules. L’obiettivo non è abilitare tutto. L’obiettivo è scegliere o costruire un set di vincoli che rappresenti la logica reale del servizio.

Prima di iniziare questa sezione, assicurati che:
1. Tu sappia quale servizio validato userai come riferimento.
2. Tu abbia confermato quali tipi di veicolo sono validi per la linea.
3. Tu sappia quali problemi reali vuoi evitare.

Per creare o selezionare il rules model:
1. In GoalBus vai su **Configuration** > **Vehicles** > **Vehicle type rules**.
ref: P12_Imagen1.png | compact
2. Verifica se esiste già un rules model adatto al tuo caso.
3. Se esiste, aprilo e rivedi la sua configurazione.
4. Se non esiste, crea un nuovo rules model.
5. Dai al modello un **name** chiaro.
6. Se applicabile, aggiungi una **description** per distinguerne lo scopo.
7. Salva il modello.
ref: P12_Imagen2.png | compact
8. Conferma che il modello sia disponibile così puoi aggiungere regole concrete.

Per il caso di riferimento, opzioni valide potrebbero essere:
- **Vehicles - L1 workday**
- **Fleet rules - L1 workday service**

Quando termini questa sezione, dovresti avere un contenitore chiaro per configurare i vincoli veicolo del caso.

## Abilitare solo le vehicle rules di cui hai davvero bisogno

Ora puoi iniziare ad abilitare le regole. Mantieni un criterio chiaro: una regola dovrebbe rappresentare una necessità reale in operations, sicurezza, infrastruttura o conformità. Se una regola non affronta un problema concreto, è meglio non abilitarla ancora.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia creato o selezionato un rules model.
2. Tu sappia quale flotta è valida per la linea.
3. Tu sappia quali combinazioni devono essere proibite o limitate.

Per abilitare le vehicle rules per il tuo caso:
1. All’interno del rules model, rivedi le regole disponibili facendo clic su **Add New Rule**.
ref: P12_Imagen3.png
2. Identifica quelle che corrispondono a bisogni reali del tuo servizio selezionando il **template** corrispondente.
3. Definisci un **Name** e scrivi una **Description** per ogni nuova regola.
4. Abilita solo le regole realmente necessarie per il caso.
5. Configura i parametri di ciascuna regola quando applicabile.
6. Ripeti finché copri le restrizioni minime necessarie.
7. Salva le modifiche.
8. Rivedi il modello completo e conferma che non sia né troppo restrittivo né troppo permissivo.

Per il caso di riferimento, chiediti:
1. Quali situazioni di flotta dovrebbe prevenire il sistema?
2. Quali combinazioni sono fisicamente possibili ma indesiderate?
3. Quali comportamenti devono essere guidati dalla logica di depot, parking o linea?

Quando termini questa sezione, dovresti avere un primo set di vehicle rules attive e coerenti, simile alla seguente immagine:
ref: P12_Imagen4.png | compact

## Allineare le regole con linea, flotta e infrastruttura

Dopo aver abilitato le regole, devi verificare che siano allineate con la linea e l’infrastruttura che supportano il caso. Una vehicle rule non dovrebbe contraddire l’allowed fleet per linea né la geografia depot/parking.

Prima di continuare, assicurati che:
1. Tu abbia abilitato il set iniziale di regole.
2. Tu abbia rivisto gli allowed vehicle types.
3. Tu sappia la base fisica da cui partono le operazioni.

Per verificare la coerenza delle regole:
1. Rivedi di nuovo la configurazione della linea.
2. Conferma che le regole non contraddicano gli allowed vehicle types.
3. Rivedi la relazione con depot e parking autorizzati.
4. Conferma che le regole rinforzino quella logica invece di romperla.
5. Se una regola rende il servizio non fattibile o contraddice l’infrastruttura, correggila o disabilitala.
6. Salva la versione finale del modello.

Per il caso di riferimento, assicurati che:
1. La linea L1 possa ancora usare la flotta autorizzata.
2. North Depot sia ancora una base di partenza coerente.
3. Nessuna regola blocchi un’operazione che dovrebbe essere valida in base alla base già configurata.

Quando termini questa sezione, dovresti avere regole allineate alle condizioni reali del servizio, non un modello astratto.

## Confermare che l’offerta validata sia ancora calcolabile

L’ultimo passo è confermare che le vehicle rules abilitate consentano ancora di calcolare l’offerta validata. È una cosa limitare con intenzione, un’altra è chiudere così tanto il modello che il servizio diventa non fattibile ancora prima di creare lo scenario.

Prima di concludere, assicurati che:
1. Tu abbia abilitato le regole necessarie.
2. Tu abbia rivisto la relazione con linea, flotta e infrastruttura.
3. Tu sappia quale servizio sarà l’input per Scheduling.

Per validare che il caso sia ancora calcolabile:
1. Rivedi il servizio validato che userai come riferimento.
2. Conferma che la linea abbia ancora accesso alla flotta di cui ha bisogno.
3. Rivedi se le regole abilitate lasciano almeno una soluzione ragionevole per il caso.
4. Chiediti se il sistema potrebbe creare uno scenario di Scheduling senza contraddizioni.
5. Se la risposta è sì, continua con il prossimo quick start.
6. Se la risposta è no, correggi il rules model prima di procedere.

Per il caso di riferimento, non procedere finché puoi affermare:
1. La linea L1 mantiene una flotta valida e autorizzata.
2. Il servizio feriale validato è ancora compatibile con le regole abilitate.
3. Il modello veicolo è pronto per essere usato nello scenario di Scheduling.

Quando termini questa sezione, dovresti poter affermare che la logica veicolo è chiusa e sufficientemente coerente per passare a shift rules e creazione dello scenario.

## Additional reading

- [Definire tipi di turno e regole dei turni](P13_Definire_tipi_di_turno_e_regole_dei_turni.md)

