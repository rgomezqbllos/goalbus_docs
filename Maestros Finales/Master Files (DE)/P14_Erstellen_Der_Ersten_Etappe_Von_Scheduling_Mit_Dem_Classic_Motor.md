---
title: Erstellen der ersten Etappe von Scheduling mit dem Classic-Motor
shortTitle: Klassische Bühne
intro: Erfahren Sie, wie Sie Ihr erstes Scheduling-Szenario mit dem GoalBus Classic-Motor
  erstellen, die Kalküleinträge korrekt auswählen und unterscheiden, wann Sie Fahrzeugregeln
  anwenden und wann Sie Schichtregeln anwenden.
contentType: how-tos
versions:
- '*'
---
## Erstellen des Szenarios mit dem validierten Angebot als Ausgangspunkt

Jetzt, da Sie bereits das validierte Angebot, Fahrzeuglogik und Drehlogik haben, ist der nächste Schritt, um die **Planungsphase** zu erstellen, die diese Basis verwenden wird, um eine ausführbare Lösung zu berechnen.

Dieses Szenario ist die kontrollierte Umgebung, in der Sie kombinieren werden:
1. die **validiertes Angebot**,
2. die **Leere Reisematrix**,
3. die **Modell der Fahrzeugregeln**,
4. und der **Modell der Schichtregeln**.

Verwenden Sie diesen Schnellstart, wenn Sie bereits die Basis-Parametrierung geschlossen haben und das endgültige Szenario für die Berechnung mit dem Classic-Motor vorbereiten möchten.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben das Serviceangebot in P10 bereits konfiguriert und validiert.
2. Sie haben die Betriebsstruktur bei P11 bereits überprüft.
3. Sie haben bereits die Fahrzeugregeln in P12 definiert.
4. Sie haben bereits die Arten von Schichten und die Regeln von Schichten in P13 definiert.
5. Sie haben bereits die leere Reisematrix für P7 vorbereitet.
6. Sie wissen, welcher Tag und welche Linien Teil der Berechnung sein werden.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde das erste Szenario von Schedule für Linie L1 erstellen, mit dem validierten praktikablen Angebot, der entsprechenden Leerlaufmatrix und den korrekten Modellen von Fahrzeug- und Schaltregeln, um die endgültige Berechnung mit GoalBus Classic zu starten.**

Um das Grundszenario Ihres Falles zu erstellen:
1. Öffnen Sie in GoalBus das **Planung** Modul.
ref: P14_Imagen1.png | compact
2. Klicken Sie auf **Neues Szenario**.
ref: P14_Imagen2.png | compact(2x)
3. Einführung der grundlegenden Szenario-Identität:
   1. **Bezeichnung**
   2. **Art des Tages**
   3. **Warenbezeichnung** wenn Sie mehr Details geben möchten.
   4. **Nur für Fahrzeuge**-Szenario oder nicht.
ref: P14_Imagen3.png | compact(x10)
4. Wählen Sie die Grundelemente des Szenarios:
   1. Die **validierter kommerzieller Dienst**, die Sie abdecken möchten.
   2. Wählen Sie die **Modell der Drehregeln**.
   3. Wählen Sie die **Muster der Vorschriften für den Fahrzeugtyp** (optional).
   4. Wählen Sie die **Leere Reisematrix** entsprechend dem gleichen Tagestyp aus.
   5. Wählen Sie die **Fahrerverdrängungsmatrix**, die Teil der Bühne sein wird.
ref: P14_Imagen4.png | compact(x10)
5. Wählen Sie die Zeile.
ref: P14_Imagen5.png | compact(x12)
6. Rettet oder vervollständigt die Erstellung der Bühne.
7. Prüfen Sie, ob das Szenario in der Hauptplanungstabelle erscheint.

Für den Referenzfall könnte eine gültige Option sein:
- **Scheduling Classic - L1 bearbeitbar**

Wenn Sie diesen Abschnitt beenden, sollten Sie ein Szenario mit seiner richtigen Logistik und kommerziellen Inputs erstellt haben, wie im folgenden Bild:
ref: P14_Imagen6.png | full

## Verständnis für die Anwendung von Fahrzeugregeln und für die Anwendung von Schichtregeln

Vor dem Einrichten des Motors müssen Sie eine wichtige Unterscheidung machen: **Fahrzeugregeln und Schaltregeln lösen nicht dasselbe Problem.**.

Verwenden Sie **Fahrzeugvorschriften**, wenn Sie Flottenverhalten steuern möchten. Dies sind die richtigen Regeln, wenn Sie modellieren müssen:
1. physikalische Verträglichkeit von Fahrzeugen,
2. Kapazitäts- oder Entfernungsgrenzwerte,
3. Infrastrukturbeschränkungen,
4. oder operative Maßnahmen im Zusammenhang mit der Nutzung der Flotte.

Verwenden Sie **Schichtregeln**, wenn Sie steuern möchten, wie menschliche Arbeit organisiert ist. Es ist die richtigen Regeln, wenn Sie modellieren müssen:
1. Arbeitszeit,
2. Brüche und Brüche,
3. Stunden des Beginns und des Endes,
4. Amplitude,
5. oder Unterschiede zwischen Schichttypen, wie morgens, nachmittags oder abends.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Sie wissen, welche Einschränkungen zum Fahrzeug gehören.
2. Du weißt, welche Einschränkungen der Schicht gehören.
3. Sie versuchen nicht, ein Personalproblem mit Flottenregeln oder umgekehrt zu lösen.

Zu entscheiden, welches Modell in jedem Fall zu verwenden ist:
1. Fragen Sie sich, ob sich die Beschränkung auf **Bus** oder **Fahrer** auswirkt.
2. Wenn es **Bus** betrifft, verwenden Sie **Modell der Fahrzeugregeln**.
3. Wenn es den **Menschliche Arbeit** oder den Verschiebungstyp betrifft, verwenden Sie den **Modell der Schichtregeln**.
4. Wenn eine Regel für alle Arten von Verschiebungen gelten sollte, überprüfen Sie sie als globale Regel oder mit dem größten Umfang zur Verfügung.
5. Wenn eine Regel nur für eine bestimmte Art von Verschiebung gilt, ordnet sie nur diesem Typ zu.

Für den Referenzfall:
1. Wenn Sie begrenzen möchten, welche Flotte den L1 abdecken kann, verwenden Sie **Fahrzeugvorschriften**.
2. Wenn Sie steuern möchten, wie eine Schicht morgen oder Nacht gebaut wird, verwenden Sie **Schichtregeln**.
3. Wenn eine Einschränkung beides mischt, trennen Sie sie und konfigurieren Sie sie im richtigen Modell.

Wenn Sie diesen Abschnitt beenden, sollten Sie sich darüber im Klaren sein, welches Modell auf jeden Bedarf reagiert und Kreuz- oder widersprüchliche Konfigurationen vermeiden.

## Auswahl des GoalBus Classic Motors zur endgültigen Berechnung

Für diesen schnellen Start steht die Arbeit mit **GoalBus Classic** als Haupt-Engine der Bühne im Vordergrund. Dies ist die tiefe Optimierungs-Engine, die darauf abzielt, die beste Endlösung zu erhalten, wenn die Parametrierung reif genug ist. fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Bühne geschaffen.
2. Sie haben Service, Linien und leere Reisematrix richtig ausgewählt.
3. Sie wissen schon, welche Regelmodelle Sie benutzen werden.
4. Du bist bereit für eine finale oder fast endgültige Berechnung, nicht nur für einen schnellen taktischen Test.

So wählen Sie den Classic-Motor:
1. Öffnen Sie das Szenario, das Sie gerade erstellt haben, indem Sie es drücken.
2. Klicken Sie in der oberen Leiste auf **Berechnungseinstellungen**.
ref: P14_Imagen7.png | compact
3. Wählen Sie auf der Seite **GoalBus Classic Engine** aus.
4. Bestätigt, dass das Szenario nicht mehr mit der Machine Learning Engine konfiguriert ist.
5. Ermittelt den **Programmierflexibilität für die erste Lösung** (Standard 0).
6. Verwenden Sie einen umsichtigen Wert, der Ihnen erlaubt, eine erste Lösung zu finden, ohne den Fall zu verzerren.
7. Wählen Sie den **Maximale Berechnungszeit**, den der Motor für neue Lösungen haben wird.
ref: P14_Imagen8.png | compact(x8)
8. Speichern Sie die Einstellungen.

Die anfängliche Flexibilität gilt nur für den GoalBus Classic Motor und sorgt dafür, dass die erste Lösung nicht blockiert wird, wenn die Einschränkungen von Anfang an zu starr sind. Die maximale Berechnungszeit dient als Liefergarantie und zwingt das System, die beste gültige Lösung zurückzugeben, die es innerhalb der verfügbaren Zeit gefunden hat. filetturn34file0L1-L20 filetturn34file2L1-L20

Für den Referenzfall:
1. Verwenden Sie **GoalBus Classic** als Hauptmotor.
2. Reservieren Sie die Maschine nur für frühere schnelle Validierungen, nicht als finale Berechnungsmaschine.
3. Verwenden Sie moderate anfängliche Flexibilität, wenn Sie vermuten, dass Einschränkungen die erste Lösung blockieren könnten.
4. Definiert eine realistische maximale Zeit für das Team, um eine praktikable Lösung innerhalb der erwarteten Zeit zu erhalten. fileciteturn34file0L1-L20fileciteturn34file0L1-L20 fileciteturn34file2L1-L20

Wenn Sie diesen Abschnitt beenden, sollten Sie den Classic-Motor mit einem kontrollierten und realistischen Berechnungsrahmen konfigurieren lassen.

## Überprüfen Sie die Bühne, bevor Sie sie starten.

Bevor Sie berechnen, müssen Sie eine abschließende Überprüfung des gesamten Szenarios. Ziel ist es, zu bestätigen, dass Sie nicht in die Berechnung mit widersprüchlichen Einträgen.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Sie haben bereits den korrekt validierten Dienst gewählt.
2. Sie haben bereits die leere Reisematrix des richtigen Tagestyps ausgewählt.
3. Sie haben bereits die richtigen Modelle von Fahrzeug- und Schichtregeln zugewiesen.
4. Sie haben GoalBus Classic bereits als Motor ausgewählt.
5. Sie haben bereits Flexibilität und maximale Zeit angepasst.

Um das Szenario zu überprüfen, bevor die Berechnung gestartet wird:
1. Prüfen Sie den Namen und den Bühnentag-Typen.
2. Bestätigen Sie, dass der **kommerzielle Dienstleistungen** genau dem entspricht, den Sie programmieren möchten.
3. Bestätigt, dass der **Leere Reisematrix** dem gleichen Zeitkontext entspricht.
4. Überprüfen Sie die **Modell der Fahrzeugregeln** und bestätigen Sie, dass sie Flottenlogik schützt.
5. Überprüfen Sie die **Modell der Schichtregeln** und bestätigen Sie, dass sie menschliche Arbeitslogik schützt.
6. Prüfen Sie, ob Sie kein obligatorisches Modell für Ihren Fall überspringen.
7. Wenn alles konsistent ist, lassen Sie das Szenario zur Berechnung bereit.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Die arbeitende L1 nutzt ihren korrekt validierten Service.
2. Die Arbeitsmatrix ist die richtige.
3. Das Fahrzeugmodell schränkt die Flotte realistisch ein.
4. Das Schichtmodell organisiert die Arbeit auf kohärente Weise.
5. GoalBus Classic ist bereits ausgewählt.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine saubere, kohärente und fertige Berechnung haben.

## Zusätzliche Messwerte

- [Der erste Calculus von Scheduling läuft und validiert](P15_Der_Erste_Calculus_Von_Scheduling_Läuft_Und_Validiert.md)
