---
title: Preparare la rete maestra con fermate, linee e percorsi
shortTitle: Rete maestra
intro: "Scopri come creare e validare la rete di base che userà la tua pianificazione, incluse fermate, linee e percorsi, in modo che i passaggi successivi per tempi, servizi e Scheduling partano da una struttura coerente."
contentType: how-tos
versions:
  - "*"
---

## Creare o validare le fermate che userà la tua rete

Prima di creare linee o percorsi, devi assicurarti che le **stops** che userai esistano già e siano definite correttamente. In GoalBus, una stop non è solo un punto geografico. È anche un’entità operativa con più livelli di naming per audience diverse come planner, passeggeri e dispositivi interni. Inoltre, il sistema ti permette di disattivare le stop invece di eliminarle bruscamente, così non interrompi route o trip attivi.

Usa questo quick start quando hai già chiuso la base temporale in P2 e P3 e devi iniziare a costruire la rete di base su cui in seguito definirai routes, tempi di viaggio e servizi.

Prima di iniziare, assicurati che:
1. Tu abbia già configurato tipi di giorno e festività in P2.
2. Tu abbia già validato l’anno operativo in P3.
3. Tu abbia accesso all’ambiente con permessi per visualizzare o modificare l’infrastruttura di rete.
4. Tu sappia quale linea o corridoio vuoi preparare come primo caso.

Per questo quick start, usa questo caso di riferimento:

> **Preparerò la linea L1, creerò o validerò le sue fermate di base e renderò pronti i percorsi di andata e ritorno per usarli più avanti nel mio primo caso di Scheduling.**

Per creare o validare le fermate per il tuo caso:
1. In GoalBus, vai al modulo **Stop Configuration** nella configurazione del servizio.
ref: P6_Imagen1.png
2. Verifica se le fermate di base per il tuo caso esistono già.
3. Se una fermata esiste già, aprila e conferma che la sua identità sia corretta.
4. Se una fermata non esiste, fai clic su **New Stop**.
5. Inserisci o valida questi campi:
   1. **Code** come identificatore univoco.
   2. **Commercial name** come nome per i passeggeri.
   3. **Long name** come riferimento descrittivo interno.
   4. **Short name** se ti serve per viste compatte.
6. Definisci la posizione della fermata usando coordinate o un indirizzo.
7. Aggiungi un **External ID** se vuoi un identificatore aggiuntivo.
8. Salva la fermata.
ref: P6_Imagen2.png | compact
9. Ripeti fino ad avere le fermate minime necessarie per il tuo caso.
10. Se trovi una fermata vecchia che non dovrebbe più essere usata in nuove pianificazioni, impostala su **Inactive** invece di eliminarla.

Per il caso di riferimento, usa una logica come:
1. North Terminal
2. Downtown
3. Hospital
4. University
5. South Terminal

Quando termini questa sezione, dovresti avere le fermate di base pronte e in uno stato coerente per costruire la linea e i percorsi.

## Creare o validare la linea come contenitore operativo

Dopo aver preparato le fermate di base, devi rivedere la **line**. In GoalBus, una line è più di un semplice numero di servizio. È un contenitore di logica operativa. Configurandola correttamente, definisci confini fisici e logistici come tipi di flotta consentiti e geografia depot/parking che in seguito influenzerà l’ottimizzazione.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già rivisto o creato le fermate di base per il tuo caso.
2. Tu sappia quale servizio vuoi rappresentare.
3. Tu capisca che la line è il contenitore amministrativo, non ancora il percorso fisico dettagliato.

Per creare o validare la linea per il tuo caso:
1. In GoalBus, vai su **Network Configuration**.
ref: P6_Imagen3.png
2. Verifica se la linea di cui hai bisogno esiste già.
3. Se la linea esiste già, aprila e rivedi la sua configurazione.
4. Se non esiste, crea una nuova linea facendo clic su **Create line**.
5. Definisci o valida:
   1. **Line name** per la denominazione interna.
   2. **Short name** per viste compatte.
   3. **Commercial name**, se applicabile.
   4. **Parkings** associati alla linea. **Nota: i parkings devono essere creati prima.**
   5. **Vehicle types** per associare i tipi di veicolo disponibili per la linea. **Nota: i tipi di veicolo devono essere creati prima.**
   6. **External ID** per aggiungere un identificatore aggiuntivo.
   7. **Color** per assegnare un colore specifico alla linea.
6. Conferma che la linea rappresenti davvero il servizio corretto.
7. Salva la linea.
ref: P6_Imagen4.png
8. Conferma che la linea possa ora essere usata come contenitore per creare percorsi specifici.

Per il caso di riferimento, puoi pensare a una linea come:
- **L1**
- **L1: North Terminal - South Terminal**

Quando termini questa sezione, dovresti avere una linea chiara e utilizzabile su cui in seguito potrai definire percorsi per direzione.

## Creare o validare i percorsi di andata e ritorno

Con la linea pronta, ora puoi lavorare con le **routes**. In GoalBus, una route è il vero percorso fisico che un veicolo percorre. Una singola linea può avere più routes valide, come short turn, deviazioni o ingressi al depot. Il sistema organizza queste variazioni per direzione e protegge le routes “in use” per evitare modifiche rischiose a servizi già attivi.

Prima di iniziare questa sezione, assicurati che:
1. Tu abbia già creato o validato la linea.
2. Tu abbia già le fermate di base da usare in sequenza.
3. Tu sappia se creerai una sola route per direzione o se il tuo caso richiede già varianti.

Per creare o validare le routes per il tuo caso:
1. Nella tabella principale delle linee, fai clic sulla linea che hai appena creato o validato per accedere alla vista routes.
ref: P6_Imagen5.png
2. Usa le schede/controlli di direzione per lavorare su **Direction 1** e **Direction 2**.
3. Verifica se esiste già una route appropriata per la direzione di cui hai bisogno.
4. Se la route non esiste, crea una nuova variazione di route per quella direzione.
5. Definisci la sequenza di fermate nell’ordine corretto.
6. Conferma il terminale di partenza e quello di arrivo.
7. Salva la route.
8. Ripeti per la direzione opposta.
9. Se trovi una route marcata come **In use**, non provare a modificarne la geometria principale senza verificare prima se esiste un’alternativa sbloccata.

Per il caso di riferimento:
1. Definisci la route di andata:
   1. North Terminal
   2. Downtown
   3. Hospital
   4. University
   5. South Terminal
2. Definisci la route di ritorno:
   1. South Terminal
   2. University
   3. Downtown
   4. North Terminal

Quando termini questa sezione, dovresti avere una linea con le sue routes principali per direzione, pronta in modo che nel prossimo quick start tu possa validare sequenze, permessi sulle fermate e logica operativa in maggiore dettaglio.

## Additional reading

- [Verificare la rete operativa con sequenze e punti chiave](P7_Verificare_la_rete_operativa.md)

