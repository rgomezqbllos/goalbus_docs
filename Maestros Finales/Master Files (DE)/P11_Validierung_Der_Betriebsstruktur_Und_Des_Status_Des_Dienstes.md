---
title: Validierung der Betriebsstruktur und des Status des Dienstes
shortTitle: Betriebsstruktur
intro: Erfahren Sie, wie Sie Einzahlungen, Einheiten und Betriebsgruppen überprüfen
  und den Service validieren können, der erstellt wurde, um es wirklich für Scheduling
  geeignet zu machen, bevor Sie zu Regeln und Berechnungen übergehen.
contentType: how-tos
versions:
- '*'
---
## Überprüfung der Betriebsstruktur, die Ihren Service unterstützt

Bevor Sie zu den Regeln und dem Scheduling-Szenario übergehen, müssen Sie prüfen, ob Ihr Angebot nicht nur existiert, sondern durch eine kohärente Betriebsstruktur unterstützt wird. In diesem Stadium müssen Sie prüfen, ob die Leitung, die Einlage, die Betriebseinheit und die zugehörigen Gruppen zum gleichen Geschäfts- und Betriebskontext gehören.

Verwenden Sie diesen Schnellstart, wenn Sie bereits das Basisservice-Angebot erstellt haben und müssen Sie bestätigen, dass die organisatorische Umgebung, die es unterstützt, vor der Berechnung korrekt ist.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Das Serviceangebot haben Sie bereits bei P10 erstellt.
2. Sie haben bereits Parkplätze und Lagerhäuser in P6 eingerichtet.
3. Sie haben bereits Flotten- und Basislinienbeschränkungen bei P8 definiert.
4. Sie sind klar, welche Linie und Dienst Sie als Referenz verwenden werden.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich validiere die Linie L1, das North Depot, die zugehörige Betriebseinheit und die zugehörigen Gruppen bilden eine kohärente Basis, bevor ich den Dienst nach Scheduling annehme.**

Um die Betriebsstruktur Ihres Falls zu überprüfen:
1. Öffnet die Konfiguration oder die Bedienansicht im Zusammenhang mit dem Dienst, den Sie gerade erstellt haben.
2. Identifizieren Sie, welche **Hinterlegung** den Dienst unterstützt.
3. Überprüfen Sie, dass die Einzahlung der physikalischen Grundlage entspricht, die Sie früher definiert haben.
4. Überprüfen Sie, zu welchem **Betriebseinheit** die Linie oder der Dienst gehört.
5. Prüfen Sie, ob diese Einheit der Infrastruktur, Geographie und Organisation des Falles entspricht.
6. Überprüfen Sie den zugehörigen **Gruppen**, der diesen Kontext beeinflusst, falls er existiert.
7. Bestätigt, dass die Linie, Einheit und Einzahlung nicht zu inkompatiblen Strukturen gehören.
8. Wenn Sie eine Inkonsistenz feststellen, korrigieren Sie sie, bevor Sie fortfahren.

Für den Referenzfall ist Folgendes zu prüfen:
1. Diese Linie L1 ist mit dem Norddepot verbunden.
2. Diese Kaution gehört zur richtigen Einheit.
3. Diese verbundenen Gruppen weisen nicht auf einen anderen operativen Bereich hin.

Wenn Sie diesen Abschnitt beenden, sollten Sie klar sein, dass der Service Leben in einer konsistenten Betriebsstruktur bietet.

## Bestätigung, dass der Dienst bereits validiert und programmierbereit ist

Nach der Überprüfung der Betriebsstruktur müssen Sie etwas kritisches bestätigen: dass der in P10 erstellte Dienst bereits im **Validierung**-Status ist. Es reicht nicht aus, Reisen, Intervalle und Routen erstellt zu haben. Damit Scheduling den Dienst lesen und als förderfähig betrachten kann, muss der Dienst die Validierungsaktion durchlaufen haben.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits den kommerziellen Service und ihre P10-Reisen überprüft.
2. Sie haben schon Intervalle, Routen und Dauern überprüft.
3. Sie müssen den Dienst in diesem Stadium nicht mehr bearbeiten.

Um zu bestätigen, dass der Dienst für die Programmierung bereit ist:
1. Öffnen Sie den kommerziellen Dienst, den Sie als Referenz verwenden.
2. Überprüfen Sie Ihre aktuelle **Status**.
3. Wenn der Status bereits **Validierung** ist, bestätigen Sie, dass vor der Fortsetzung nichts ansteht.
4. Wenn der Dienst noch in Bearbeitung oder in einem vorherigen Zustand ist, führen Sie die Aktion **Validierung** aus.
5. Überprüfen Sie, ob sich der Zustand korrekt ändert.
6. Prüfen Sie das:
   1. der Dienst ist kein Entwurf mehr,
   2. die Reise vor zufälligen Veränderungen geschützt ist,
   3. und der Service kann bereits von Scheduling konsumiert werden.
7. Wenn Sie einen Strukturfehler erkennen, korrigieren Sie ihn vor der Revalidierung.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Die Linie L1 hat bereits ihr überarbeitetes, praktikables Angebot.
2. Der Dienst hat sich bereits in **Validierung** Status geändert.
3. Das System kann nun als Programmiereingabe verwendet werden.

Wenn Sie diesen Abschnitt beenden, sollten Sie einen Service haben, der wirklich bereit ist, vom Motor gelesen zu werden.

## Überprüfung der Kohärenz zwischen Struktur, Service und Förderfähigkeit

Jetzt müssen Sie eine abschließende gemeinsame Überprüfung durchführen. Ziel ist es nicht nur, einen validierten Dienst zu haben, sondern zu bestätigen, dass der validierte Dienst in der korrekten Struktur lebt und keine organisatorischen Inkonsistenzen zieht, die dann die Berechnung erschweren.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Sie haben bereits Lager, Einheit und Gruppen überprüft.
2. Sie haben den Dienst bereits validiert oder seine Validierung bestätigt.
3. Du weißt, welchen Fall du als nächstes nehmen wirst.

Um die volle Berechtigung vor der Planung zu validieren:
1. Überprüfen Sie den validierten Service und bestätigen Sie, welche Zeile Sie verwenden.
2. Überprüfen Sie, dass die Zeile immer noch mit der korrekten Einzahlung verbunden ist.
3. Prüfen Sie, ob die operative Einheit und die Gruppen dem Kontext des Dienstes nicht widersprechen.
4. Fragen Sie sich, ob das System diesen Service bereits als gültige und konsistente Eingabe für die Berechnung übernehmen könnte.
5. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
6. Wenn die Antwort nein ist, korrigieren Sie die Struktur oder geben Sie den Dienst nur an die Bearbeitung zurück, wenn Sie einen Teil der Basis vor der Revalidierung wiederholen müssen.

Für den Referenzfall stellen Sie sicher, dass
1. L1 gehört zum richtigen organisatorischen Kontext.
2. Die North Deposit ist wirklich die Basis für den Service.
3. Der bearbeitbare Dienst ist bereits validiert und hat keine Widersprüche mit seiner Struktur.

Wenn Sie diesen Abschnitt beenden, sollten Sie in der Lage sein, zu erklären, dass das Angebot nicht nur erstellt, sondern auch strukturell ausgerichtet und für Scheduling geeignet ist.

## Zusätzliche Messwerte

- [Festlegung von Fahrzeugregeln für die Planung](P12_Festlegung_Von_Fahrzeugregeln_Für_Die_Planung.md)
