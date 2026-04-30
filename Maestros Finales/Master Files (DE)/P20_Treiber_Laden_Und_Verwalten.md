---
title: Treiber laden und verwalten
shortTitle: Fahrer
intro: Erfahren Sie, wie Sie die Treiberbasis in GoalBus erstellen, importieren und
  pflegen, Ihr Betriebsprofil überprüfen und eine zuverlässige Vorlage hinterlassen,
  bevor Sie zu Rostering-Abordnung, -Regeln und -Berechnung wechseln.
contentType: how-tos
versions:
- '*'
---
## Erstellen oder Importieren von Treibervorlagen

Bevor Sie über Rostering-Regeln, Abwesenheiten oder Schichtzuweisungen sprechen, benötigen Sie eine zuverlässige Treiberbasis. In GoalBus fungiert das Fahrermanagement als Hauptquelle der Wahrheit für die menschliche Bedienbarkeit: Es ermöglicht die Kombination von manueller Erstellung und Massenladung und konzentriert Identität, Einzahlungszugehörigkeit und Verfügbarkeit im gleichen Verzeichnis. fileciteturn38file2L1-L24

Verwenden Sie diesen schnellen Start, wenn Sie sich über den Übergang von der Scheduling zu Rostering klar sind und müssen die echte Gruppe von Menschen vorbereiten, die an der Aufgabe teilnehmen werden.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben den Übergang von Scheduling bei P19 bereits abgeschlossen.
2. Es ist Ihnen klar, welches Kollektiv von Fahrern an der Berechnung teilnehmen wird.
3. Du weißt, ob du ein paar Fahrer manuell entladen willst oder ob du eine massive Ladung brauchst.
4. Sie haben Zugriff auf die Umgebung mit Berechtigungen zur Verwaltung von Mitarbeitern.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde die Treibervorlage laden und überprüfen, die die L1-Lösung abdecken kann, bevor ich in Abordnung, Regeln und Verfügbarkeit gehe.**

So erstellen oder importieren Sie die Treibervorlage:
1. Gehen Sie in GoalBus zum **Einstellungen** Modul > **Personal** > **Fahrerverwaltung**.
ref: P20_Imagen1.png | compact
2. Prüfen Sie, ob die Falltreiber bereits in der allgemeinen Liste vorhanden sind.
3. Wenn Sie nur wenige Treiber erstellen möchten, klicken Sie auf **Neuer Treiber**.
ref: P20_Imagen2.png | compact(2x)
4. Wenn Sie viele Treiber laden müssen, machen Sie einen massiven Import mit CSV-Datei von **Persönliche Belastung**.
ref: P20_Imagen3.png | compact
5. Wenn Sie Massenimport wählen, bereiten Sie die Datei mit den minimalen Daten vor, die Ihre Operation benötigt, um jede Person korrekt zu identifizieren.
ref: P20_Imagen4.png
6. Führen Sie die Last aus und überprüfen Sie das Ergebnis.
7. Gehen Sie zurück zur allgemeinen Liste und überprüfen Sie, ob Treiber korrekt erscheinen.
8. Wenn Sie Duplikate oder unvollständige Datensätze erkennen, korrigieren Sie diese, bevor Sie fortfahren.

Beenden Sie diesen Abschnitt für den Referenzfall nur, wenn Sie Folgendes angeben können:
1. L1-Treiber werden bereits entladen oder importiert.
2. Die allgemeine Liste enthält eine einzige Referenzvorlage.
3. Sie können nun das Profil eines jeden Treibers öffnen, um dessen Betriebsbedingungen zu überprüfen.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine Treibervorlage geladen und im System sichtbar haben. fileciteturn38file0L1-L7 fileciteturn38file2L1-L24

## Überprüfung des Fahrerprofils und der Strukturdaten

Sobald die Vorlage erstellt ist, müssen Sie die **Fahrerprofil** überprüfen. Das Profil ist nicht nur ein Kontaktblatt: es ist die komplette digitale Datei des Mitarbeiters innerhalb der Operation. Dort existieren sie statische Daten, Betriebskontext und Attribute, die das System später zur Begründung seiner Berechtigung verwenden wird. fileciteturn38file0L8-L20 fileciteturn38file2L25-L40

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits sichtbare Treiber auf der allgemeinen Liste.
2. Sie wissen, welchen Fahrer oder welche Gruppe Sie als Probe benutzen.
3. Sie wollen bestätigen, dass die Aufzeichnung nicht nur verwaltungstechnisch, sondern auch operationell ist.

Um das Fahrerprofil zu überprüfen:
1. Klicken Sie in der allgemeinen Liste auf den Namen eines Treibers.
ref: P20_Imagen5.png | full
2. Überprüfen Sie die statische Daten-Seitenleiste.
3. Prüfen Sie mindestens diese Informationsgruppen:
   1. Grunddaten wie Name und Code,
   2. Betriebsdaten, wie z. B. Tarifvertrag oder Vertragsart,
   3. Betriebsverbindungen wie Hauptlager, Arbeitsgruppe, Bereich oder Arten zugelassener Fahrzeuge.
4. Wenn wichtige strukturelle Daten fehlen, füllen Sie sie aus, bevor Sie fortfahren.
5. Speichern Sie alle notwendigen Änderungen.
6. Wiederholen Sie die Überprüfung auf mehreren Treibern, um die Konsistenz in der Vorlage zu bestätigen.

Für den Referenzfall ist mindestens Folgendes zu prüfen:
1. Der Code des Fahrers.
2. Ihr Hauptlagerhaus.
3. Ihre Task Force.
4. Die operativen Eigenschaften, die Ihre nachfolgende Zuordnung erfordern.

Wenn Sie diesen Abschnitt beenden, sollten Sie klar sein, dass jeder Treiber eine konsistente und nutzbare Bediendatei hat. fileciteturn38file0L8-L20

## Überprüfung des Betriebskontexts und dynamischer Treiberdaten

Neben strukturellen Daten enthält das Treiberprofil dynamische Daten, die direkt beeinflussen, wie das System Gründe für die Person. In der Registerkarte Verwaltung können Sie Zähler und Arbeitsmuster, die Teil des Betriebskontexts später von der Mapping-Logik verwendet sind überprüfen. fileciteturn38file0L12-L17

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die statischen Daten auf dem Profil überprüft.
2. Sie wissen, ob Ihre Operation Zähler oder zyklische Muster verwendet.
3. Sie wollen überprüfen, ob der Treiber nicht nur existiert, sondern einen interpretierbaren Operationskontext hat.

Zur Überprüfung des dynamischen Betriebszusammenhangs:
1. Öffnen Sie im Fahrerprofil die Registerkarte **Einzelheiten zur Verwaltung**.
2. Überprüfen Sie die **Zähler** oder KPI, die mit dem Treiber verbunden sind, wenn sie vorhanden sind.
3. Prüfen Sie, ob der Treiber mit einem beliebigen **Arbeitsmuster** verknüpft ist.
4. Wenn Ihre Operation zyklische Muster verwendet, überprüfen Sie auch die aktuelle Verzögerung oder Position des Treibers innerhalb des Musters.
5. Bestätigt, dass diese Daten für den realen Kontext sinnvoll sind.
6. Wenn dynamische Informationen nicht korrekt sind, passen Sie sie an, bevor Sie zu Regeln oder Berechnungen wechseln.

Fragen Sie sich für den Referenzfall:
1. Hat dieser Fahrer das Muster, das er haben sollte?
2. Sind Ihre Zähler oder KPIs verfügbar, wenn der Prozess sie benötigt?
3. Könnte das System diese Person in einer Zuweisungsberechnung richtig begründen?

Wenn Sie diesen Abschnitt abgeschlossen haben, sollten Sie nicht nur die Identität des Treibers, sondern auch seinen dynamischen Betriebskontext validiert haben. fileciteturn38file0L12-L17

## Validierung von Bewertungen vor Verwendung des Treibers in Rostering

Bevor Sie einen Treiber als berechtigt betrachten, müssen Sie Ihre **Ratings** überprüfen. Diese Bewertungen beantworten die Frage      .Kann diese Person rechtlich oder technisch an dieser Einzahlung, Gruppe oder Einheit arbeiten? . Sie werden in einer Zeitlinie mit Start- und Enddatum verwaltet, und das System zeigt Zustände als aktiv, zukunftsfähig, abgelaufen oder in der Nähe des Ablaufs, um das Lesen zu erleichtern. Wenn eine Person für den erforderlichen Kontext nicht aktiviert ist, erzeugt die Engine einen Fehler, wenn sie versucht, es zuzuordnen. fileciteturn38file0L17-L34

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits das Fahrerprofil überprüft.
2. Sie wissen, welche Einzahlung, Gruppe oder Einheit Sie für Ihren Fall benötigen.
3. Sie verstehen, dass eine Ermächtigung nicht dasselbe ist wie eine vorübergehende Zuweisung oder Abordnung.

Überprüfung und Validierung der Ratings:
1. Öffnen Sie im Treiberprofil die Registerkarte **Ermöglichung/Qualifizierung**.
2. Prüfen Sie nach bestehenden Aufzeichnungen für:
   1. Einlagen,
   2. Arbeitsgruppen,
   3. Geschäftseinheiten.
3. Überprüfen Sie den visuellen Status jeder Bewertung:
   1. aktiv,
   2. Zukunft,
   3. unmittelbar vor Ablauf der Frist,
   4. ist abgelaufen.
4. Wenn eine notwendige Bewertung fehlt, fügen Sie sie mit ihren korrekten Daten hinzu.
5. Wenn eine Habilitation abgelaufen ist und nicht verwendet werden sollte, lassen Sie sie als historisch, ohne zu versuchen, die Vergangenheit neu zu schreiben.
6. Speichern Sie die Änderungen.
7. Bestätigen Sie, dass der Treiber bereits für den Kontext aktiviert ist, in dem Sie ihn verwenden wollen.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Der Treiber ist für die korrekte Einzahlung aktiviert.
2. Die erforderliche Arbeitsgruppe ist abgedeckt.
3. Es gibt keine Ablauffristen, die die aktuelle Berechtigung brechen.

Wenn Sie diesen Abschnitt beenden, sollten Sie Treiber haben, die nicht nur in der Vorlage existieren, sondern auch aus operativer und regulatorischer Sicht förderfähig sind. fileciteturn38file0L17-L34

## Bestätigung, dass die Vorlage bereits bereit für die nächste Ebene von Rostering ist

Der letzte Schritt besteht darin, zu überprüfen, ob die Treiberbasis bereit ist, die folgende Ebene einzugeben: Betriebsabordnung, Regeln, Abwesenheiten und Berechnung. Hier ist es nicht nur das Ziel, Namen geladen zu haben, sondern eine kohärente, rückverfolgbare und nutzbare Vorlage durch den Motor.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie haben die Vorlage bereits geladen oder importiert.
2. Sie haben bereits die Hauptprofile überprüft.
3. Sie haben bereits strukturelle und dynamische Daten überprüft.
4. Sie haben bereits wesentliche Bewertungen bestätigt.

Um zu bestätigen, dass die Vorlage bereits fertig ist:
1. Gehen Sie zurück zur allgemeinen Liste der Fahrer.
2. Überprüfen Sie, ob das für Ihren Fall benötigte Kollektiv vorhanden ist.
3. Prüfen Sie, dass kritische Profile keine wichtigen Informationslücken aufweisen.
4. Stellen Sie sicher, dass die Personen, die Sie erwarten, für den richtigen Kontext aktiviert sind.
5. Fragen Sie sich, ob das System diese Basis bereits als Ausgangspunkt für:
   1. operative Abordnung,
   2. Regeln für die Aufstellung,
   3. und tatsächliche Verfügbarkeit.
6. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
7. Wenn die Antwort nein ist, korrigieren Sie die Fahrerbasis, bevor Sie fortfahren.

Für den Referenzfall, beenden Sie diesen schnellen Start nur, wenn Sie sagen können:
1. Die Treibervorlage L1 ist bereits geladen.
2. Schlüsselprofile wurden bereits überprüft.
3. Wesentliche Bewertungen sind bereits vorhanden.
4. Die Basis ist nun für die operative Abordnung bereit.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine starke genug Treiber-Vorlage haben, um mit der nächsten Schicht von Rostering fortzufahren.

## Zusätzliche Messwerte

- [Verwaltung der operativen Abordnung des Fahrers](P21_Verwaltung_Der_Operativen_Abordnung_Des_Fahrers.md)
