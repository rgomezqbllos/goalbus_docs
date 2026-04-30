---
title: Validierung des Betriebsjahres vor der Planung
shortTitle: Operationelles Jahr
intro: Erfahren Sie, wie Sie das Betriebsjahr validieren können, um Lücken, Überschneidungen
  oder künstliche Datenkürzungen zu vermeiden, bevor Sie zu Netzwerk, Infrastruktur
  und Dienstleistungen wechseln.
contentType: how-tos
versions:
- '*'
---
## Erstellung oder Validierung des Betriebsjahres, das Ihre Planung nutzt

Bevor Sie mit Netzwerk, Zeiten, Dienstleistungen oder Regeln fortfahren, müssen Sie überprüfen, ob der Zeitraum, den Sie planen möchten, innerhalb des **korrektes Betriebsjahr** fällt. In GoalBus existiert das Betriebsjahr, um die zeitliche Logik des Systems an die Realität des Geschäfts anzupassen. Dies ist wichtig, da viele Operationen nicht dem Kalenderjahr von Januar bis Dezember folgen. Zum Beispiel kann ein Schulbetrieb von September bis August arbeiten, und ein Steuer- oder Gewerkschaftsvertrag kann einen anderen Rang benötigen.

Verwenden Sie diesen Schnellstart, wenn Sie bereits die Logik von Tages- und Urlaubstypen definiert haben, wenn Sie Ihren ersten realen Planungsfall vorbereiten möchten oder wenn Sie bestätigen müssen, dass der Zeitraum, den Sie verwenden werden, von einer gültigen Timeline unterstützt wird.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Rolle des Planers in P1 überprüft.
2. Sie haben bereits die Arten von Feiertagen und Tagen in P2 festgelegt oder validiert.
3. Sie wissen genau, welche Periode Sie planen wollen.
4. Sie haben Zugriff auf die Umgebung mit Berechtigungen zur Abfrage oder Bearbeitung der temporären Einstellungen.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde den Januar 2026 planen und muss bestätigen, dass diese Frist innerhalb des korrekten Betriebsjahres fällt, bevor ich mit meiner ersten Planung fortfahre.**

Um das Betriebsjahr Ihres Falles zu erstellen oder zu validieren:
1. Gehen Sie in GoalBus zu **Einstellungen**.
2. Öffnet den **Zeitmanagement** Abschnitt > **Betriebsjahre**.
ref: P3_Imagen1.png | compact
3. Prüfen Sie bestehende Betriebsjahre und finden Sie, welche Sie den gewünschten Zeitraum abdecken sollten.
4. Wenn es kein geeignetes Betriebsjahr gibt, klicken Sie auf die Option, um ein neues zu erstellen, indem Sie auf **Operatives Jahr erstellen** klicken.
ref: P3_Imagen2.png | full
5. Definieren Sie einen **Eindeutiger Name** und, falls nötig, einen **Warenbezeichnung**.
6. Passen Sie die **Anfangsdatum** und **Enddatum** an die operative oder fiskalische Realität Ihres Gehäuses an.
7. Verbinden Sie die **Geschäftseinheiten** falls vorhanden.
8. Sparen Sie das Betriebsjahr.
ref: P3_Imagen3.png | compact(x10)
9. Bestätigen Sie, dass der Zeitraum, den Sie planen möchten, für dieses Jahr vollständig abgedeckt ist.
10. Wenn das Jahr bereits existiert, überprüfen Sie auch, dass es immer noch das richtige für Ihren Fall ist und dass seine Daten nicht Anlass zu Zweifeln geben.

Wenn Sie diesen Abschnitt beenden, sollten Sie das Betriebsjahr identifiziert oder erstellt haben, das Ihren Planungsfall wirklich unterstützt.

## Überprüfung der Zeitkontinuität und Vermeidung von Lücken oder Überschneidungen

Nachdem Sie das richtige Betriebsjahr identifiziert haben, müssen Sie überprüfen, ob die Zeitabfolge konsistent ist. In GoalBus ist die Kontinuität zwischen den Betriebsjahren nicht optional. Das System soll verhindern, dass **Lücken** oder **Überschneidungen** zwischen den Jahren existieren, da sich diese Fehler auf kumulierte Metriken, jährliche KPIs und spätere Berechnungen auswirken würden.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits das Betriebsjahr gefunden, das Ihren Fall abdecken sollte.
2. Du kennst sein Startdatum und sein Enddatum.
3. Sie wissen, ob es frühere oder spätere Jahre gibt, die Teil derselben Sequenz sind.

Zur Überprüfung der Zeitkontinuität des Betriebsjahres:
1. Öffnen Sie das Detail des Betriebsjahres, das Sie als Referenz verwenden werden.
2. Überprüfen Sie die **Anfangsdatum** und die **Enddatum**.
3. Prüfen Sie, ob der Zeitraum, den Sie planen möchten, in diesen eindeutigen Bereich fällt.
4. gegebenenfalls Überprüfung des vorhergehenden oder nachfolgenden Betriebsjahres, um sicherzustellen, dass
   1. Lücken zwischen einem Jahr und einem anderen oder
   2. Überlappungen zwischen zwei Zeitbereichen.
5. Wenn Sie ein neues Jahr am Ende der Sequenz erstellen müssen, fügen Sie es nur am Ende hinzu und überprüfen Sie, wo genau das vorangegangene endet.
6. Wenn Sie eine Inkonsistenz bemerken, korrigieren Sie die Daten, bevor Sie fortfahren.
7. Bestätigt, dass das System erlaubt, die Sequenz zu speichern, ohne den Speicher aufgrund von Kontinuitätsfehlern zu blockieren.

Stellen Sie sich für den Referenzfall folgende Fragen:
1. Ist der Januar 2026 vollständig in einem gültigen Betriebsjahr?
2. Verbindet sich dieses Jahr korrekt mit dem Vorjahr und dem nächsten Jahr?
3. Könnte das System Daten sammeln, ohne die Kontinuität der Periode zu brechen?

Wenn Sie diesen Abschnitt beenden, sollten Sie sicher sein, dass es keine Lücken oder Überschneidungen gibt, die Ihren Fall betreffen.

## Überprüfung des Verhältnisses zwischen dem Betriebsjahr und der Kalenderlogik

Nun, da Sie das Betriebsjahr und seine Kontinuität validiert haben, müssen Sie es mit dem verbinden, was Sie in P2 definiert haben. Es ist nicht hilfreich, gut konfigurierte Urlaubs- und Tagestypen zu haben, wenn der Zeitrahmen, in dem diese Daten leben, nicht gut gebaut ist.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Das richtige Betriebsjahr ist bereits identifiziert.
2. Die Arten von Tagen und Feiertagen des Gehäuses sind bereits konfiguriert.
3. Die Zeit, die Sie planen, ist noch klar und begrenzt.

Um zu überprüfen, dass das operative Jahr bereit ist, die Planung zu stützen:
1. Überprüfen Sie den Planungsfall, den Sie am Anfang dieses Artikels definiert haben.
2. Bestätigt, dass diese Frist innerhalb des korrekten Betriebsjahres endet.
3. Überprüft, ob die in P2 definierte Kalenderlogik auch innerhalb des gleichen Zeitrahmens gilt.
4. Fragen Sie sich, ob das System bereits gleichzeitig verwendet werden könnte:
   1. die korrekte Kategorie des Tagestyps,
   2. die richtigen Feiertage und
   3. das richtige Betriebsjahr.
5. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
6. Wenn die Antwort nein ist, korrigieren Sie das Betriebsjahr oder überprüfen Sie die Konsistenz mit dem Kalender, bevor Sie fortfahren.

Am Ende dieses Abschnitts sollten Sie angeben können, dass Ihr Fall eine Vollzeitbasis hat: korrekter Kalender und korrektes Betriebsjahr.

## Zusätzliche Messwerte

- [Vorbereitung des Master-Netzwerks: Haltestellen, Linien und Routen](P4_Festlegung_Der_Fahrzeugtypen_Und_Der_Zulässigen_Flotte_Pro_Strecke.md)
