---
title: Definieren von Versionen von Zeit und Fahrzeiten für den Betrieb
shortTitle: Versionen und Zeiten
intro: Erfahren Sie, wie Sie Zeitversionen erstellen, Reise- und Dauerzeiten nach
  Tagestyp und Zeitschlitz definieren und eine zuverlässige Zeitreferenz hinterlassen,
  bevor Sie Dienste in GoalBus erstellen oder anpassen.
contentType: how-tos
versions:
- '*'
---
## Erstellen der Version der Zeit, die Ihr Fall verwenden wird

Bevor Sie die Reisezeit definieren, müssen Sie eine **Zeit-Version** erstellen. In GoalBus ist eine Version nicht nur ein Tag: Es ist die Zeitbibliothek, die die Zeitlogik zusammengruppiert, die für bestimmte Routen und bestimmte Tagestypen gilt. Dies ist wichtig, weil sie sich an einem Montagmorgen nicht wie ein Sonntagmorgen verhält, und das System sollte keine einzelnen Zeiten für das ganze Jahr wiederverwenden.

Verwenden Sie diesen Schnellstart, wenn Sie bereits eine Linie und ihre definierten Routen haben, und Sie müssen die Zeitbasis erstellen, die dann verwendet wird, um Reisen zu berechnen, Dauern zu validieren und Abweichungen mit dem Standard zu vergleichen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben bereits das Master-Netzwerk bei P6 vorbereitet.
2. Sie haben bereits das Betriebsnetzwerk bei P7 überprüft.
3. Sie haben bereits die Zeitbasis der Tagestypen auf P2 gesetzt.
4. Sie haben bereits das Betriebsjahr auf P3 validiert.
5. Sie wissen, welche Linie, welche Routen und welche Art von Tag Sie als Referenz benutzen werden.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde eine Zeitversion für die L1-Linie an Werktagen erstellen und sie als temporäre Referenz verwenden, bevor ich Dienste erstelle oder anpasse.**

So erstellen Sie die Zeit-Version Ihres Gehäuses:
1. Öffnen Sie in GoalBus die **Ansicht der Pfade** der Zeile, die Sie als Referenz verwenden.
2. Wählen Sie das **Verwaltung von Fahrt- und Haltezeiten**-Symbol oder die Option.
ref: P9_Imagen1.png | compact
3. Erstellen Sie oben in der Ansicht eine neue Version, indem Sie **Neue Zeitpläne** auswählen.
ref: P9_Imagen2.png | compact
4. Definiert eine klare **Bezeichnung** für die Version.
5. Fügen Sie einen **Beschreibung** hinzu, um den Operationskontext zu unterscheiden.
6. Wählen Sie den **Art des Tages**, für den diese Version gilt, zum Beispiel **Arbeitstage**.
7. Verknüpfen Sie die **Streckenänderungen** oder bestimmte Sequenzen, die Teil dieser temporären Version sein werden.
8. Speichern Sie die Version.
ref: P9_Imagen3.png | compact(x8)
9. Überprüfen Sie, ob die Version bereits als temporäre Referenz für diese Zeile verfügbar ist.

Für den Referenzfall könnte eine gültige Version aufgerufen werden:
- **Arbeitstage des Winters**
- **L1 Arbeitsbasis**

Wenn Sie diesen Abschnitt beenden, sollten Sie eine Zeitversion erstellt haben, die das System als temporäre Referenz für die Dienste dieser Zeile verwenden kann, ähnlich der des untenstehenden Bildes.
ref: P9_Imagen4.png | full

## Festlegung der Fahrzeiten zwischen den Haupthaltestellen

Nachdem Sie die Version erstellt haben, müssen Sie die **Fahrtzeiten** eingeben. In GoalBus sind diese Zeiten hauptsächlich zwischen **Hauptstopps** oder **Zeitpunkte** definiert, nicht zwischen allen Zwischenstopps. Header sind standardmäßig die Hauptübergänge, und von dort aus bauen Sie die temporäre Logik, die dann die Dienste füttern wird.

Darüber hinaus arbeitet GoalBus nicht mit einem einzigen Wert pro Segment. Der Motor verwendet eine **minimal, optimal und maximal**-Logik, um der Berechnung die Flexibilität der Steuerung zu geben:
1. **Mindestgehalt**: die schnellste Zeit möglich.
2. **Optimal**: die Zielzeit, auf die der Motor eingestellt wird.
3. **Höchstmenge**: die langsamste Zeit, die es gibt.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Zeit-Version erstellt.
2. Du weißt, was für wichtige Punkte du als Referenz benutzen wirst.
3. Sie haben bereits die Richtung identifiziert, die Sie zuerst konfigurieren möchten.

Um die Fahrzeiten Ihres Falles zu definieren:
1. Wählen Sie innerhalb des Zeitrasters den **Segment** zwischen zwei Hauptstopps aus.
ref: P9_Imagen5.png | full
2. Erstellen Sie eine oder mehrere **Zeitnischen**, um die betriebliche Realität widerzuspiegeln.
3. Geben Sie für jeden Streifen ein:
   1. die Zeit **mindestens**,
   2. die Zeit **optimal**,
   3. Zeit **Höchstens**.
ref: P9_Imagen6.png | compact
4. Speichern Sie das Segment.
5. Wiederholen Sie den Vorgang für das nächste Hauptsegment.
6. Wenn Sie einen Sinn beenden, wiederholen Sie die gleiche Logik für den entgegengesetzten Sinn.

Die erstellten Streifen sollten keine Lücken oder Überschneidungen zwischen ihnen haben. Im Falle gab es, wird es nicht möglich sein, die Zeit zu sparen.

Für den Referenzfall könnte eine grundlegende Logik sein:
1. **Terminal Nord → Zentrum**
   1. 07:00–09:00
      1. Mindestens: 12 min
      2. Optimal: 15 min
      3. Maximal: 18 min
   2. 09:00-22:00 Uhr
      1. Mindestens: 5 min
      2. Optimal: 5 min
      3. Maximal: 5 min
   3. 22:00–06:00 Uhr
      1. Mindestens: 8 min
      2. Optimal: 10 min
      3. Maximal: 12 min
2. **Zentrum → Krankenhaus**
3. **Krankenhaus → Universität**
4. **Universität → Süd-Terminal**

Wenn Sie diesen Abschnitt beenden, sollten Sie elastische Fahrzeiten zwischen den wichtigsten Zeitpunkten der Route definiert haben.

## Festlegung von Retentionszeiten für Regulierung und Verwertung

Neben der Fahrzeit muss GoalBus wissen, wie lange ein Fahrzeug an einer Haupthaltestelle bleiben kann. Diese **Zeitskala** sind wichtig, weil sie es Ihnen ermöglichen, den Ausgang zu regulieren, frühzeitige Ankünfte aufzunehmen und Raum für die Erholung an Terminals oder Anschlusspunkten zu lassen.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Reisezeiten zwischen den Hauptsegmenten definiert.
2. Sie wissen, welche Terminals oder wichtige Punkte reguliert werden müssen.
3. Sie haben bereits erkannt, wo wirklicher Einsatzraum benötigt wird.

Um die Skalierungszeit zu definieren:
1. Wählen Sie im Zeitraster den **Spalte** von einem Hauptstopp aus.
ref: P9_Imagen7.png | full
2. Wählen Sie einen wichtigen Terminal, Header oder Verbindungspunkt.
3. Definieren:
   1. **Mindestgehalt**, als obligatorische Wartezeit.
   2. **Höchstmenge**, als zulässige Marge für Regulierung oder Synchronisation.
4. Speichern Sie die Einstellungen.
5. Wiederholen Sie den Prozess für andere Hauptstopps, wo Sie kontrollierte Dauerhaftigkeit benötigen.

Für den Referenzfall wäre eine mögliche Logik:
1. **Nord-Terminal**
   1. Mindestens: 4 min
   2. Maximal: 10 min
2. **Süd-Terminal**
   1. Mindestens: 5 min
   2. Maximal: 12 min

Wenn Sie diesen Abschnitt beenden, sollten Sie die Ränder definiert haben, die der Motor verwenden kann, um sich zu erholen oder zu regulieren, ohne die Logik des Zeitplans zu deformieren.

## Check-Slots, erweiterte Ansicht und visuelle Konsistenz

Sobald Sie bereits Reisen und Dauerzeiten haben, müssen Sie überprüfen, ob das Grid eine realistische Logik widerspiegelt. Das Dokument hebt hervor, dass GoalBus visuelle Hilfsmittel zur Fehlererkennung enthält, wenn Sie viele Datenpunkte, viele Streifen oder mehrere Pfade bearbeiten.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Sie haben mindestens einen Steckplatz eingerichtet.
2. Sie haben bereits minimale, optimale und maximale Werte eingeführt.
3. Sie haben bereits an den relevanten Punkten Retentionszeiten hinzugefügt.

Um die Konsistenz der Konfiguration visuell zu überprüfen:
1. Überprüfen Sie das Raster und bestätigen Sie, dass jedes Hauptsegment einen gültigen Zeitschlitz hat.
2. Verwenden Sie verfügbare visuelle Hilfsmittel, um abnorme Werte zu erkennen.
3. Prüfen Sie, ob Spitzenzeiten zeigen Zeiten höher als Talstunden.
4. Erweitern Sie die Ansicht, wenn Sie mehr Details oder Zwischenstopps sehen müssen.
5. Korrigiert jeden anomalen Wert direkt aus der Ansicht oder aus dem Bearbeitungsfeld.
6. Wiederholen Sie die Überprüfung, bis die Zeitlogik eine glaubwürdige Operation widerspiegelt.

Fragen Sie sich für den Referenzfall:
1. Zeigt sich die Stoßzeit mit Zeiten höher als die Nacht?
2. Haben die minimalen, optimalen und maximalen Zeiten eine logische Beziehung?
3. Haben Terminals einen realistischen Regulierungsraum?
4. Stellt das Netz bereits einen vollen Arbeitstag dar?

Wenn Sie diesen Abschnitt beenden, sollten Sie eine visuell überarbeitete Zeitbasis frei von großen Inkonsistenzen haben.

## Anwendung der Zeitversion als Referenz für Dienstleistungen

Das ultimative Ziel dieses Schnellstarts ist nicht nur, temporäre Daten zu erstellen, sondern eine Referenz zu hinterlassen, die dann beim Erstellen oder Ändern von Diensten verwendet werden kann. Das Dokument zeigt an, dass jede Reise an einem **Vorübergehende Referenzversion** gemessen werden muss und dass diese Referenz automatisch verwendet wird, wenn Sie neue Reisen erstellen oder die Route einer Reise ändern. Es ermöglicht auch Abweichungen zu erkennen, wenn eine Reise außerhalb des Standards importiert oder geändert wurde.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie haben bereits eine gültige temporäre Version erstellt.
2. Sie haben bereits Reise- und Aufenthaltszeiten definiert.
3. Sie haben bereits die Konsistenz des Rasters überprüft.
4. Sie wissen, welche Linie und welchen Fall Sie benutzen, um Dienste zu schaffen.

Um zu überprüfen, ob Ihre temporäre Basis für die Dienste bereit ist:
1. Überprüfen Sie die Version der Zeit, die Sie gerade erstellt haben.
2. Bestätigt, dass es mit der richtigen Art des Tages verknüpft ist.
3. Bestätigen Sie, dass es die Routen oder Variationen enthält, die Sie verwenden werden.
4. überprüft, ob eine solche Version bereits als temporäre Referenz für:
   1. neue Reisen zu schaffen,
   2. Neuberechnung der Ankunfts- und Abfahrtszeiten,
   3. Prüfungsfehler gegenüber dem Standard.
5. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
6. Wenn die Antwort nein ist, gehen Sie zurück und korrigieren Sie die Version oder ihre Zeiten, bevor Sie fortfahren.

Wenn Sie diesen Abschnitt beenden, sollten Sie in der Lage sein zu sagen, dass die Zeile bereits über eine Referenzzeitversion verfügt, die ausreichend ist, um Dienstleistungen in kohärenter Weise zu schaffen.

## Zusätzliche Messwerte

- [Erstellen des Basis-Service-Angebots: Reise- oder Servicegruppen nach Linie, Route und Bedeutung](P10_Erstellen_Des_Basis_Service_Angebots_Mit_Ausflügen_Und_Fahrplänen.md)
