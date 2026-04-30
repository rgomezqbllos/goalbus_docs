---
title: Erstellen der Kalenderbasis mit Tages- und Urlaubstypen
shortTitle: Arten von Tagen und Feiertagen
intro: Erfahren Sie, wie Sie Tagestypen und Feiertage so einrichten, dass die Planungslogik
  das richtige Betriebsmuster anwendet, bevor Sie auf Routen, Reisezeiten und Service-Erstellung
  weiterziehen.
contentType: how-tos
versions:
- '*'
---
## Erstellen der Art des Tages, die Sie verwenden, um zu planen

Bevor Sie Dienste erstellen oder Planungsberechnungen starten, müssen Sie die Kalenderlogik definieren, die dem System sagt, mit welcher Art von Tag Sie arbeiten. Bei GoalBus sind die Tagestypen die operativen Kategorien, die Tage als Standardjobs, Freitage, Wochenenden oder Sondertage gruppieren, damit Sie das Planungslogikdatum nicht per Datum erstellen müssen.

Verwenden Sie diesen schnellen Start, wenn Sie Ihren ersten Planungsfall vorbereiten, wenn Sie die Art des Tages erstellen oder validieren müssen, den Ihre Bühne verwenden wird, oder wenn Sie sicherstellen möchten, dass die Urlaubslogik bereit ist, bevor Sie fortfahren.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben Zugriff auf die Umgebung mit Berechtigungen, um die Kalendereinstellungen anzuzeigen oder zu bearbeiten.
2. Du weißt, welchen Planungsfall du bauen willst.
3. Sie wissen, welche Zeit Sie vorbereiten wollen, zum Beispiel Januar 2026.
4. Sie haben bereits Ihre Planungsrolle und den Gesamtfluss in P1 überprüft.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich bereite die Kalenderbasis für ein Arbeitsszenario vom Januar 2026 vor, einschließlich des korrekten Verhaltens der Feiertage.**

So erstellen oder validieren Sie den Tagestyp Ihres Falles:
1. Gehen Sie in GoalBus zu **Einstellungen** > **Zeitmanagement** > **Verwaltung von Tagestypen**.
ref: P2_Imagen1.png | compact
2. Überprüfen Sie bestehende Tagestypen und sehen Sie, ob es bereits eine gibt, die die operative Logik darstellt, die Sie benötigen.
3. Wenn bereits eine geeignete Art von Tag existiert, bestätigt sie:
   1. Sein Name ist klar.
   2. Sein kurzer Name ist klar.
   3. Es stellt wirklich das Betriebsmuster dar, das Sie brauchen.
4. Wenn kein richtiger Tagestyp existiert, klicken Sie auf **Tagestyp erstellen**.
ref: P2_Imagen2.png | compact(2x)
5. Definieren Sie die **Bezeichnung** und **Kurzbezeichnung** für den neuen Tagestyp.
ref: P2_Imagen3.png | compact(8.5x)
6. Wählen Sie die Tage der Woche, die für diese Art von Tag gelten.
ref: P2_Imagen4.png | compact(8.5x8)
7. Sollte die Art des Tages auch für Feiertage gelten, aktivieren Sie die Möglichkeit, die Art des Tages auf Feiertage anzuwenden.
ref: P2_Imagen5.png | compact(8.5x8)
8. Retten Sie den Tag Kerl.
9. Überprüfen Sie das Ergebnis und bestätigen Sie, dass die Art des Tages jetzt eindeutig den Fall darstellt, den Sie vorbereiten.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine Art Tag haben, den das System als Betriebskategorie für Ihren Planungsfall verwenden kann.

## Aufnahme von Feiertagen, die die normale Logik des Kalenders verändern

Nach der Definition des allgemeinen Tagestyps müssen Sie dem System mitteilen, was mit den außergewöhnlichen Daten zu tun ist. Feiertage sind wichtig, weil der Kalender sagen kann, dass ein Datum Dienstag ist, während sich die Operation wie ein Sonntag oder als ein anderes spezielles Muster verhalten sollte. Wenn Sie die Feiertage nicht gut registrieren, kann das System den falschen Plan anwenden, wenn Sie später Szenarien veröffentlichen oder berechnen.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben den Tag geschaffen oder bestätigt, an dem Ihr Fall verwendet wird.
2. Sie wissen, ob der Planungszeitraum Feiertage oder besondere Termine beinhaltet.
3. Sie sind bereit zu entscheiden, welches Betriebsmuster jeder Urlaub folgen sollte.

Um die Feiertage Ihres Falles zu registrieren und zu validieren:
1. Wechseln Sie im gleichen Tages-Management-Bereich auf die Registerkarte **Feiertage**.
ref: P2_Imagen6.png | compact
2. Prüfen Sie, ob der gewünschte Urlaub bereits im System vorhanden ist.
3. Wenn der Urlaub nicht existiert, erstellen Sie einen neuen Urlaubsrekord.
4. Wenn der Urlaub bereits existiert, öffnen Sie ihn und überprüfen Sie seine Einstellungen.
5. Geben Sie die **Bezeichnung** des Feiertags ein oder bestätigen Sie diese.
6. Schicken Sie dem Urlaub den richtigen **Art des Tages** zu.
ref: P2_Imagen7.png | compact
7. Halten Sie die Aufzeichnungen über den Feiertag.
8. Wiederholen Sie diesen Prozess für jeden anderen Feiertag, der den Zeitraum betrifft, den Sie vorbereiten.
9. Überprüfen Sie die Liste der Feiertage und bestätigen Sie, dass jedes außergewöhnliche Datum auf das korrekte Betriebsmuster hinweist.

Stellen Sie sich für den Referenzfall folgende Fragen:
1. Enthält der Januar 2026 einen Feiertag, der sich anders als ein Standard-Arbeitsfähig verhalten sollte?
2. Sollte dieser Feiertag sich wie Sonntag, wie Samstag oder wie eine andere Art von besonderen Tag verhalten?
3. Wenn Sie ein Szenario für diesen Zeitraum veröffentlicht haben, würde das System genau wissen, welches Muster zu diesem Zeitpunkt anzuwenden ist?

Wenn Sie diesen Abschnitt beenden, sollte das System in der Lage sein, das normale Kalenderverhalten an den für Sie wichtigen Feiertagen zu ersetzen.

## Überprüfen, ob Ihre Kalender-Basis bereit ist, zu planen

Nachdem Sie bereits den allgemeinen Tagestyp und die Urlaubsausnahmen definiert haben, müssen Sie bestätigen, dass die Kalenderbasis wirklich nutzbar ist. Dies ist der Schritt, in dem Sie überprüfen, dass die von Ihnen erstellte Struktur die folgenden schnellen Starts ohne die Einführung vermeidbarer Fehler halten kann.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Die Art des Tages existiert und hat die richtige wöchentliche Logik.
2. Die entsprechenden Feiertage sind registriert.
3. Jeder Urlaub ist mit der richtigen Art des Tages verbunden.
4. Ihr Planungsfall bleibt klar und konkret.

Um Ihre Kalenderbasis zu validieren, bevor Sie zum nächsten Schnellstart übergehen:
1. Überprüfen Sie den Planungsfall, den Sie am Anfang dieses Artikels definiert haben.
2. Bestätigen Sie, dass der Tag, an dem Sie diesen Fall erstellt oder validiert haben.
3. Bestätigen Sie, dass jeder Urlaub innerhalb des Planungszeitraums registriert wurde und mit dem richtigen Tagestyp verbunden ist.
4. Prüfen Sie, ob die Urlaubs-App-Option, die Sie im Tagestyp aktiviert haben, wirklich das gewünschte Verhalten widerspiegelt.
5. Fragen Sie sich, ob das System bereits unterscheiden könnte:
   1. normale Tage des Zeitraums und
   2. die außergewöhnlichen Daten, die von einem anderen Betriebsmuster gefolgt werden müssen.
6. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
7. Wenn die Antwort nein ist, gehen Sie zurück und korrigieren Sie die Art des Tages oder des Ferienvereins, bevor Sie fortfahren.

Am Ende dieses Abschnitts sollten Sie in der Lage sein zu sagen, dass Ihr Planungsfall über eine zuverlässige Kalenderbasis verfügt und dass die folgenden Schnellstarts sich darauf verlassen können, ohne einen temporären Logikfehler zu erben.

## Zusätzliche Messwerte

- [Validierung des Betriebsjahres vor der Planung](P3_Validierung_Des_Betriebsjahres_Vor_Der_Planung.md)
