---
title: Kalenderbasis mit Tages- und Feiertagstypen erstellen
shortTitle: Tages- und Feiertagsarten
intro: Erfahren Sie, wie Sie Tagesarten und Feiertage einrichten, damit die Planungslogik das richtige Betriebsmuster anwendet, bevor Sie mit Routen, Fahrzeiten und der Serviceerstellung fortfahren.
contentType: how-tos
versions:
- '*'
---
## Erstellen der Tagesart, die Sie für die Planung verwenden werden

Bevor Sie Dienste erstellen oder Planungsberechnungen starten, müssen Sie die Kalenderlogik definieren, die dem System mitteilt, mit welcher Art von Tag Sie arbeiten. In GoalBus sind Tagesarten die operativen Kategorien, die Tage als Standardarbeitstage, Freitage, Wochenenden oder Sondertage gruppieren, sodass Sie die Planungslogik nicht Datum für Datum erstellen müssen.

Verwenden Sie diesen Schnellstart, wenn Sie Ihren ersten Planungsfall vorbereiten, wenn Sie die Tagesart erstellen oder validieren müssen, die Ihre Phase verwenden wird, oder wenn Sie sicherstellen möchten, dass die Feiertagslogik bereit ist, bevor Sie fortfahren.

Stellen Sie vor dem Start sicher, dass:
1. Sie Zugriff auf die Umgebung mit Berechtigungen zum Anzeigen oder Bearbeiten der Kalendereinstellungen haben.
2. Sie wissen, welchen Planungsfall Sie erstellen möchten.
3. Sie wissen, welchen Zeitraum Sie vorbereiten möchten, zum Beispiel Januar 2026.
4. Sie bereits Ihre Planungsrolle und den allgemeinen Ablauf in P1 überprüft haben.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich bereite die Kalenderbasis für ein Arbeitsszenario vom Januar 2026 vor, einschließlich des korrekten Verhaltens der Feiertage.**

So erstellen oder validieren Sie die Tagesart Ihres Falls:
1. Gehen Sie in GoalBus zu **Einstellungen** > **Zeitmanagement** > **Verwaltung der Tagesarten**.
ref: P2_Imagen1.png | compact
2. Überprüfen Sie vorhandene Tagesarten und sehen Sie nach, ob es bereits eine gibt, die die von Ihnen benötigte operative Logik darstellt.
3. Wenn bereits eine entsprechende Tagesart existiert, bestätigen Sie, dass:
   1. Ihr Name klar ist.
   2. Ihr Kurzname klar ist.
   3. Sie wirklich das von Ihnen benötigte Betriebsmuster darstellt.
4. Wenn keine geeignete Tagesart existiert, klicken Sie auf **Tagestyp erstellen**.
ref: P2_Imagen2.png | compact(2x)
5. Definieren Sie den **Namen** und den **Kurznamen** für die neue Tagesart.
ref: P2_Imagen3.png | compact(8.5x)
6. Wählen Sie die Wochentage aus, die für diese Tagesart gelten.
ref: P2_Imagen4.png | compact(8.5x8)
7. Wenn die Tagesart auch für gesetzliche Feiertage gelten soll, aktivieren Sie die Option zur Anwendung der Tagesart auf gesetzliche Feiertage.
ref: P2_Imagen5.png | compact(8.5x8)
8. Speichern Sie den Tagestyp.
9. Überprüfen Sie das Ergebnis und bestätigen Sie, dass die Tagesart nun den Fall, den Sie vorbereiten, klar darstellt.

Wenn Sie diesen Abschnitt abgeschlossen haben, sollten Sie eine Tagesart haben, die das System als Betriebskategorie für Ihren Planungsfall verwenden kann.

## Aufzeichnen von Feiertagen, die die normale Logik des Kalenders ändern

Nachdem Sie die allgemeine Tagesart definiert haben, müssen Sie dem System mitteilen, was mit den Ausnahmedaten zu tun ist. Feiertage sind wichtig, da der Kalender sagen kann, dass ein Datum ein Dienstag ist, während sich der Betrieb wie ein Sonntag oder wie ein anderes spezielles Muster verhalten sollte. Wenn Sie die Feiertage nicht gut registrieren, kann das System den falschen Plan anwenden, wenn Sie später Szenarien veröffentlichen oder berechnen.

Stellen Sie vor dem Start dieses Abschnitts sicher, dass:
1. Sie die Tagesart erstellt oder bestätigt haben, die Ihr Fall verwenden wird.
2. Sie wissen, ob der Planungszeitraum Feiertage oder spezielle Daten enthält.
3. Sie bereit sind zu entscheiden, welchem Betriebsmuster jeder Feiertag folgen soll.

So registrieren und validieren Sie die Feiertage Ihres Falls:
1. Wechseln Sie im selben Abschnitt der Tagesarten-Verwaltung auf die Registerkarte **Feiertage**.
ref: P2_Imagen6.png | compact
2. Prüfen Sie, ob der von Ihnen benötigte Feiertag bereits im System vorhanden ist.
3. Wenn der Feiertag nicht existiert, erstellen Sie einen neuen Feiertagsdatensatz.
4. Wenn der Feiertag bereits existiert, öffnen Sie ihn und überprüfen Sie seine Einstellungen.
5. Geben Sie den **Namen** des Feiertags ein oder bestätigen Sie ihn.
6. Weisen Sie diesem Feiertag die korrekte **Tagesart** zu.
ref: P2_Imagen7.png | compact
7. Speichern Sie den Datensatz des Feiertags.
8. Wiederholen Sie diesen Vorgang für jeden anderen Feiertag, der den von Ihnen vorbereiteten Zeitraum betrifft.
9. Überprüfen Sie die Liste der Feiertage und bestätigen Sie, dass jedes Ausnahmedatum auf das richtige Betriebsmuster verweist.

Stellen Sie sich für den Referenzfall diese Fragen:
1. Enthält der Januar 2026 einen Feiertag, der sich anders verhalten sollte als ein Standardarbeitstag?
2. Sollte sich dieser Feiertag wie ein Sonntag, wie ein Samstag oder wie eine andere Art von Sondertag verhalten?
3. Wenn Sie ein Szenario für diesen Zeitraum veröffentlichen würden, wüsste das System genau, welches Muster an diesem Datum anzuwenden ist?

Wenn Sie diesen Abschnitt beendet haben, sollte das System in der Lage sein, das normale Kalenderverhalten an den für Sie wichtigen Feiertagsdaten zu ersetzen.

## Überprüfen, ob Ihre Kalenderbasis bereit für die Planung ist

Nun, da Sie bereits die allgemeine Tagesart und die Feiertagsausnahmen definiert haben, müssen Sie bestätigen, dass die Kalenderbasis wirklich nutzbar ist. Dies ist der Schritt, in dem Sie prüfen, ob die von Ihnen erstellte Struktur die folgenden Schnellstarts aufnehmen kann, ohne vermeidbare Fehler einzuführen.

Stellen Sie vor dem Fortfahren sicher, dass:
1. Die Tagesart existiert und die korrekte wöchentliche Logik hat.
2. Die relevanten Feiertage registriert sind.
3. Jeder Feiertag mit der richtigen Tagesart verknüpft ist.
4. Ihr Planungsfall klar und konkret bleibt.

So validieren Sie Ihre Kalenderbasis, bevor Sie zum nächsten Schnellstart übergehen:
1. Überprüfen Sie den Planungsfall, den Sie am Anfang dieses Artikels definiert haben.
2. Bestätigen Sie, dass die von Ihnen erstellte oder validierte Tagesart mit diesem Fall übereinstimmt.
3. Bestätigen Sie, dass jeder Feiertag innerhalb des Planungszeitraums registriert und der korrekten Tagesart zugeordnet wurde.
4. Prüfen Sie, ob die Option für die Feiertagsanwendung, die Sie in der Tagesart aktiviert haben, wirklich das von Ihnen gewünschte Verhalten widerspiegelt.
5. Fragen Sie sich, ob das System bereits unterscheiden kann zwischen:
   1. normalen Tagen des Zeitraums; und
   2. den Ausnahmedaten, denen ein anderes Betriebsmuster folgen soll.
6. Wenn die Antwort ja lautet, fahren Sie mit dem nächsten Schnellstart fort.
7. Wenn die Antwort nein lautet, gehen Sie zurück und korrigieren Sie die Tagesart oder die Feiertagszuordnung, bevor Sie fortfahren.

Am Ende dieses Abschnitts sollten Sie in der Lage sein festzustellen, dass Ihr Planungsfall über eine zuverlässige Kalenderbasis verfügt und dass die folgenden Schnellstarts darauf aufbauen können, ohne einen temporären Logikfehler zu übernehmen.

## Zusätzliche Lektüre

- [Validierung des Betriebsjahres vor der Planung](P3_Validating_The_Operating_Year_Before_Planning.md)
