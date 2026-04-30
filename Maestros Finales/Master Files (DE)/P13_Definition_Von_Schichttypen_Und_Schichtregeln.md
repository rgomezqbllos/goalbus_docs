---
title: Definition von Schichttypen und Schichtregeln
shortTitle: Arten und Regeln
intro: Erfahren Sie, wie Sie Schichttypen erstellen, innerhalb von Regelmodellen organisieren
  und die Einschränkungen oder Sanktionen aktivieren können, die Scheduling benötigt,
  um rechtsgültige und operationell kohärente Aufgaben aufzubauen.
contentType: how-tos
versions:
- '*'
---
## Schaffung der Arten von Verschiebungen, die die Arbeit strukturieren

Bevor Sie Schichtregeln festlegen, müssen Sie die **Art der Schicht** definieren, die das System verwendet, um Reisen in kohärente menschliche Arbeit zu gruppieren. Ein Schichttyp ist nicht nur ein visuelles Tag. Es ist die logische Kategorie, die den Motor führt, um erkennbare und nutzbare Aufgaben später in Listen, täglichen Betrieb und Integration mit anderen Systemen zu erstellen.

Verwenden Sie diesen Schnellstart, wenn Sie bereits ein validiertes Angebot, eine definierte Fahrzeuglogik, haben, und Sie müssen dem System mitteilen, welche Formen der Arbeit für Ihren Fall gültig sind.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben das Serviceangebot bei P10 bereits erstellt und validiert.
2. Sie haben die Betriebsstruktur in P11 bereits validiert.
3. Sie haben bereits die Fahrzeugregeln in P12 definiert.
4. Sie sind klar, welchen Service und Betrieb Kontext Sie als Referenz verwenden werden.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde die Verschiebungstypen der Linie L1 definieren, damit Scheduling kohärente Aufgaben aufbauen kann, bevor das Berechnungsszenario erstellt wird.**

So erstellen Sie die Shift-Typen Ihres Gehäuses:
1. Gehen Sie in GoalBus zu **Einstellungen** > **Personal** > **Schichtarbeitsarten**.
ref: P13_Imagen1.png | compact
2. Prüfen Sie, ob es bereits geeignete Arten von Schichten für Ihren Fall gibt.
3. Wenn der Typ bereits existiert, öffnen Sie ihn und überprüfen Sie, ob er noch gültig ist.
4. Wenn es nicht existiert, erstellen Sie eine neue.
5. Definiert diese Felder:
   1. **Vollständiger Name**, mit einem klaren und beschreibenden Namen.
   2. **Kurzbezeichnung**, für kompakte Ansichten und Betriebskarten.
   3. **Externe ID**, wenn der Client eine Integration in HR-Systeme oder Lohnabrechnung benötigt.
ref: P13_Imagen2.png | compact
6. Markiert den Typ als **Forderungen**, wenn Sie an zukünftigen Berechnungen teilnehmen müssen.
7. Rette den Schichtmann.
8. Wiederholen Sie den Prozess für jede Kategorie von Arbeit, die Sie wirklich brauchen in Ihrem Fall.

Für den Referenzfall können Sie Typen wie z.B.:
1. **Morgen umdrehen**
2. **Late turn**
3. **Gebrochene Wendung**, falls der Betrieb erforderlich ist

Wenn Sie diesen Abschnitt beenden, sollten Sie die Arten von Verschiebungen haben, die als DNA's der Aufgaben dienen, die Scheduling aufbauen wird.

## Erstellen oder Auswählen des Drehregelmodells

Nach der Erstellung der Shift-Typen müssen Sie den Container definieren, in dem die Regeln leben. Turn-Regeln werden nicht als flache Liste verwaltet, sondern innerhalb von **Modelle**, die eine kohärente Gruppe von Einschränkungen für eine Phase, einen Zeitraum oder eine konkrete Simulation. Dies ermöglicht es Ihnen, mehrere Konfigurationen zu halten, ohne historische Regeln mit aktiven Regeln zu mischen.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Arten von Schichten erstellt oder validiert, die Sie verwenden werden.
2. Sie wissen, welchen Service oder welche Simulation Sie als Referenz verwenden.
3. Sie sind bereits klar, ob dieses Modell wiederverwendbar oder fallspezifisch sein wird.

So erstellen oder wählen Sie das Regelmodell:
1. Gehen Sie in GoalBus zu **Einstellungen** > **Personal** > **Schichtregeln**.
2. Prüfen Sie, ob bereits ein **Musterregeln** für Ihren Koffer vorhanden ist.
3. Wenn das Modell bereits existiert, öffnen Sie es und überprüfen Sie, ob es noch gültig ist.
4. Falls es sie nicht gibt, erstellen Sie ein neues Modell, indem Sie auf **Neues Modell hinzufügen** klicken.
5. Weist dem Modell einen klaren **Bezeichnung** zu.
6. Falls zutreffend, fügen Sie eine **Warenbezeichnung** hinzu, die ihre Verwendung identifiziert.
7. Speichern Sie das Modell.
ref: P13_Imagen3.png | compact
8. Bestätigen Sie, dass Sie bereits Regeln in diesem Container hinzufügen können.

Für den Referenzfall könnte eine gültige Option sein:
- **Drehungen - L1**
- **Schichtregeln**

Wenn Sie diesen Abschnitt beenden, sollten Sie ein Modell von Regeln bereit sein, spezifische Einschränkungen und Sanktionen zu erhalten.

## Turn-Regeln wie Einschränkungen oder Sanktionen aktivieren

Jetzt können Sie beginnen, die Regeln zu setzen. Hier ist es wichtig, zwei Logiken zu unterscheiden:
1. **Einschränkungen**, die obligatorisch sind und ungültige Aufgaben blockieren.
2. **Sanktionen**, die nicht blockieren, aber drücken Sie den Optimierer auf bevorzugte Lösungen.

Dieser Unterschied ist entscheidend, weil nicht alles, was Sie in der Operation wollen, ein absolutes Verbot werden muss.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits ein Modell von Regeln erstellt oder ausgewählt.
2. Du weißt, welches Arbeitsverhalten du beenden willst.
3. Sie wissen, welches Verhalten Sie bevorzugen möchten, ohne es zwingend zu machen.

Um die Turn-Regeln Ihres Falles zu verwalten:
1. Wenn Sie eine neue Regel erstellen möchten, tippen Sie auf **Neue Regel hinzufügen**.
2. Überprüfen Sie im Regelmodell die verfügbare **Vorlagen für Regeln** und geben Sie der neuen Regel einen **Bezeichnung** und einen **Warenbezeichnung**.
3. Wählen Sie die Vorlage, die der Steuerung entspricht, die Sie anwenden möchten.
4. Erstellen Sie einen **Sonderregelung** aus dieser Vorlage, indem Sie auf **Bestätigen** klicken.
ref: P13_Imagen4.png | compact
6. Entscheiden Sie sich für **Für welche Arten von Verschiebungen jede Regel gilt**. Nicht alle Regeln sollten für alle Typen gelten. Einige können global sein und andere sollten bestimmte Kategorien ansprechen, wie morgen, Nachmittag oder Match.
7. Geben Sie die spezifischen Parameter der Regel ein.
8. Behalten Sie die Regel.
9. Wiederholen Sie den Vorgang nur für die Regeln, die Ihr Fall wirklich braucht.
10. Prüfen Sie, ob die Regeln, die Sie anwenden müssen, aktiv sind oder nicht. Um eine Regel zu starten, muss sie mindestens einer Drehung zugeordnet worden sein.
ref: P13_Imagen5.png | compact(x19)

Für den Referenzfall, denken Sie an Beispiele wie:
1. Die Schicht von morgen sollte in einem bestimmten Fenster beginnen.
2. Eine geteilte Drehung sollte eine bestimmte Amplitude nicht überschreiten.
3. Eine unerwünschte Sequenz kann bestraft und nicht verboten werden.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine erste Reihe von Regeln haben, die sowohl verbindliche Grenzen als auch operative Präferenzen widerspiegeln.

## Überprüfung, ob die Regeln dem korrekten Verschiebungstyp zugeordnet sind

Sobald die Regeln aktiviert sind, müssen Sie **für welche Schichttypen jeweils** überprüfen. Nicht alle Regeln sollten für alle Typen gelten. Einige können global sein und andere sollten auf bestimmte Kategorien gerichtet sein, wie morgen, spät oder passend.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Sie haben bereits mindestens eine Regel innerhalb des Modells aktiviert.
2. Sie haben bereits die Arten von Schichten definiert, die in den Fall involviert sind.
3. Sie wissen, ob die Regel global oder spezifisch sein sollte.

Um den Anwendungsbereich angemessen zu überprüfen:
1. Wählen Sie jede von Ihnen erstellte Regel aus.
2. Überprüfen Sie den **Anwendbare Arten von Schichten** Abschnitt.
3. Wählen Sie die spezifischen Typen aus, für die die Regel gelten soll.
4. Wenn die Regel alle Arten des Szenarios beeinflussen muss, setzen Sie diese als global, indem Sie **alle Arten von Schichtarbeit** auswählen.
5. Prüfen Sie, ob es keine zwei aktiven Regeln der gleichen Vorlage gibt, die für dieselbe Art von Verschiebung gelten, wenn dies einen logischen Konflikt erzeugen würde.
6. Speichern Sie die Einstellungen.
7. Wiederholen Sie die Revision für jede Modellregel.

Für den Referenzfall:
1. Ein frühes Startfenster kann nur auf **Morgen umdrehen** angewendet werden.
2. Eine Ruheregel kann auf mehrere Typen angewendet werden.
3. Eine allgemeine Präferenz könnte global sein.

Wenn Sie diesen Abschnitt beenden, sollten Sie Regeln mit einem klaren Umfang und keine logischen Konflikte miteinander haben, ähnlich wie das folgende Bild:
ref: P13_Imagen6.png | compact(x19)

## Überprüfung, ob die Schaltlogik mit dem Dienst kompatibel bleibt

Der letzte Schritt ist zu überprüfen, dass die Arten von Verschiebungen und die Regeln, die Sie gerade definiert haben, immer noch kompatibel mit dem validierten Angebot und mit der Logik der Fahrzeuge, die Sie bereits geschlossen haben. Es ist nicht hilfreich, die Regeln zu haben, wenn das Ergebnis den Service ohne eine realistische Möglichkeit, programmiert zu werden verlässt.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Du hast bereits die Art von Schichten geschaffen, die du brauchst.
2. Sie haben bereits die entsprechenden Regeln aktiviert und zugewiesen.
3. Sie wissen genau, wie der Eingang zur Scheduling-Bühne sein wird.

Um zu bestätigen, dass der Fall noch praktikabel ist:
1. Überprüfen Sie den validierten Dienst, den Sie als Referenz verwenden.
2. Prüfen Sie, ob die Arten von Schichten, die Sie erstellt haben, diese Arbeit arrangieren können.
3. Prüfen Sie, ob irgendwelche Shift-Regeln den Fall zu starr lassen.
4. Prüft, ob es keinen starken Widerspruch zu den bereits aktivierten Fahrzeugregeln gibt.
5. Fragen Sie sich, ob das System bereits Aufgaben legal und operativ mit dieser Basis in Einklang bringen könnte.
6. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
7. Wenn die Antwort nein ist, korrigieren Sie die Typen oder Regeln, bevor Sie folgen.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Das validierte L1-Angebot bleibt mit den definierten Schichttypen kompatibel.
2. Regeln blockieren den Fall nicht unnötig.
3. Das Modell ist bereits bereit, die Etappe des Scheduling zu betreten.

Wenn Sie diesen Abschnitt beenden, sollten Sie in der Lage sein zu sagen, dass die Logik der Verschiebungen bereits genug geschlossen ist, um zur Erstellung des Scheduling-Szenarios überzugehen.

## Zusätzliche Messwerte

- [Erstellung der ersten Etappe des Scheduling](P14_Erstellen_Der_Ersten_Etappe_Von_Scheduling_Mit_Dem_Classic_Motor.md)
