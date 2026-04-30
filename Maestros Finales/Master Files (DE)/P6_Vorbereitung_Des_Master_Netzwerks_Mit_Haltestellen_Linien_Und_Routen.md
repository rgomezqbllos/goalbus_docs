---
title: Vorbereitung des Master-Netzwerks mit Haltestellen, Linien und Routen
shortTitle: Hauptnetz
intro: Erfahren Sie, wie Sie die Netzwerkbasis erstellen und validieren können, die
  Ihre Planung, einschließlich Stopps, Linien und Routen, nutzt, so dass die nächsten
  Schritte in Zeiten, Diensten und Terminplanung von einer kohärenten Struktur abweichen.
contentType: how-tos
versions:
- '*'
---
## Erstellen oder Validieren der Stopps, die Ihr Netzwerk verwendet

Bevor Sie Linien oder Routen erstellen, müssen Sie sicherstellen, dass der **stoppt**, den Sie verwenden, bereits existiert und korrekt definiert ist. In GoalBus ist ein Stop nicht nur ein geographischer Punkt. Es ist auch eine Einheit mit operativer Identität und mehreren Namensebenen, die verschiedenen Zielgruppen dienen, wie Planer, Passagiere und interne Geräte. Darüber hinaus ermöglicht das System, Haltestellen zu deaktivieren, anstatt sie abrupt zu entfernen, so dass keine aktiven Routen oder Reisen zu brechen.

Verwenden Sie diesen Schnellstart, wenn Sie die Zeitbasis in P2 und P3 bereits geschlossen haben, und Sie müssen mit dem Aufbau des Basisnetzes beginnen, auf dem Sie dann Routen, Reisezeiten und Dienste definieren.

Bevor Sie beginnen, stellen Sie sicher, dass:

1. Sie haben bereits die Arten von Feiertagen und Tagen in P2 eingerichtet.
2. Sie haben bereits das Betriebsjahr auf P3 validiert.
3. Sie haben Zugriff auf die Umgebung mit Berechtigungen, um die Netzwerkinfrastruktur zu konsultieren oder zu bearbeiten.
4. Sie sind klar, welche Linie oder Korridor Sie als ersten Fall vorbereiten wollen.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde Linie L1 vorbereiten, Ihre Basisstopps erstellen oder validieren und Ihre Hin- und Rückwege für spätere Verwendung in meinem ersten Fall von Scheduling auflisten.**

So erstellen oder validieren Sie die Stops Ihres Falles:

1. Gehen Sie in GoalBus innerhalb der Service-Einstellungen zum **Einstellungen beenden**-Modul.
ref: P6_Imagen1.png
2. Finden Sie heraus, ob die Basis auf Ihrem Fall bereits existiert.
3. Wenn ein Stop bereits existiert, öffnen Sie ihn und bestätigen Sie, dass Ihre Identität korrekt ist.
4. Wenn ein Stop nicht existiert, klicken Sie auf **Neuer Stop**.
5. Diese Felder eingeben oder validieren:
   1. **ANHANG** als eindeutige Kennung.
   2. **Handelsbezeichnung** als sichtbarer Passagiername.
   3. **Langer Name** als interne beschreibende Referenz.
   4. **Kurzbezeichnung** wenn Sie es für kompakte Ansichten benötigen.
6. Definieren Sie die Position des Stopps durch Koordinaten oder Richtung.
7. Fügen Sie eine **Externe ID** hinzu, wenn Sie eine zusätzliche Kennung wünschen.
8. Sparen Sie sich den Halt.
ref: P6_Imagen2.png | compact(20x)
9. Wiederholen Sie den Vorgang, bis Sie die für Ihren Fall notwendigen Mindeststopps haben.
10. Wenn Sie einen alten Stop erkennen, der bei der Neuplanung nicht mehr verwendet werden soll, schalten Sie ihn auf **Nichterwerbstätig** um, anstatt ihn zu löschen.

Verwenden Sie für den Referenzfall eine Logik wie diese:

1. Nord-Terminal
2. Zentrum
3. Krankenhaus
4. Hochschule
5. Süd-Terminal

Wenn Sie diesen Abschnitt beenden, sollten Sie die Base Stops bereit und in einem konsistenten Zustand haben, um die Linie und Routen zu bauen.

## Erstellen oder Validieren der Linie als Bediencontainer

Nachdem Sie die Basisstopps haben, müssen Sie die **Zeile** überprüfen. In GoalBus ist eine Linie mehr als nur eine Servicenummer. Es ist ein Operationslogik-Container. Durch die richtige Konfiguration definieren Sie physikalische und logistische Grenzen des Dienstes, wie die Art der Flotte erlaubt oder die operative Geographie von Ablagerungen und Parkplätzen, die dann die Optimierung beeinflussen.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:

1. Sie haben bereits die Base Stops auf Ihrem Fall überprüft oder erstellt.
2. Du weißt, welchen Dienst du darstellen willst.
3. Sie sind klar, dass die Linie ist der administrative Container und noch nicht der detaillierte physische Weg.

Um Ihre Fallzeile zu erstellen oder zu validieren:

1. Gehen Sie in GoalBus zum **Netzwerkeinstellungen** Modul.
ref: P6_Imagen3.png
2. Sehen Sie, ob die Linie, die Sie benötigen, bereits existiert.
3. Wenn die Zeile bereits existiert, öffnen Sie sie und überprüfen Sie ihre Einstellungen.
4. Wenn sie nicht existiert, erstellen Sie eine neue Zeile, indem Sie auf **Zeile erstellen** klicken.
5. Definiert oder validiert:
   1. **Name der Zeile** für den internen Namen.
   2. **Kurzbezeichnung** für kompakte Ansichten.
   3. **Handelsbezeichnung**, falls zutreffend.
   4. **Parken** mit der Linie verbunden. **EJE: die vorherige Einrichtung von Parkplätzen ist notwendig.**
   5. **Fahrzeugtypen** zur Zuordnung der für die Linie verfügbaren Fahrzeugtypen. **EJE: Vor der Erstellung von Fahrzeugtypen ist notwendig.**
   6. **Externe ID** um eine zusätzliche Kennung hinzuzufügen.
   7. **Farbe** um der Zeile eine bestimmte Farbe zuzuweisen.
6. Überprüfen Sie, ob die Linie wirklich den richtigen Service darstellt.
7. Sparen Sie sich die Leitung.
ref: P6_Imagen4.png | compact(8.5x)8. Confirma que la línea ya puede usarse como contenedor para crear rutas específicas.

Für den Referenzfall können Sie sich eine Zeile wie:

- **L1**
- **L1: Nordterminal - Südterminal**

Wenn Sie diesen Abschnitt beenden, sollten Sie eine klare und nutzbare Linie haben, über die Sie dann Pfade durch Bedeutung definieren können.

## Erstellen oder Validieren der Hin- und Rückwege

Mit der bereits fertigen Linie können Sie nun mit dem **Strecken** arbeiten. In GoalBus ist eine Route der wahre physische Weg, der ein Fahrzeug fährt. Dieselbe Linie kann mehrere gültige Routen haben, z.B. kurze Kurven, Umwege oder Lagereingänge. Das System organisiert diese Variationen nach Richtung oder Sinn, und schützt Routen im Einsatz, um gefährliche Veränderungen in bereits aktiven Dienstleistungen zu vermeiden.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:

1. Sie haben bereits die Zeile erstellt oder validiert.
2. Sie haben bereits die Base Stops, die Sie in der Sequenz verwenden werden.
3. Sie wissen, ob Sie einen einzigen Pfad durch Bedeutung erstellen wollen oder ob Ihr Fall bereits Varianten benötigt.

So erstellen oder validieren Sie die Routen Ihres Falles:

1. Klicken Sie in der Hauptzeilentabelle auf die gerade erstellte oder validierte Zeile, um auf die Pfadansicht zuzugreifen.
ref: P6_Imagen5.png
2. Verwenden Sie die Tabs oder Steuerungen, um mit **Sentido 1** und **Sentido 2** zu arbeiten.
3. Prüfen Sie, ob es bereits einen geeigneten Weg für den Sinn gibt, den Sie brauchen.
4. Wenn die Route nicht existiert, erstellen Sie eine neue Route Variation für diesen Sinn.
5. Definiert die Reihenfolge der Stops in der richtigen Reihenfolge.
6. Bestätigt den Start-Header und den End-Header.
7. Sparen Sie sich die Route.
8. Wiederholen Sie die Logik für den anderen Sinn.
9. Wenn Sie einen Pfad finden, der als **In Gebrauch** markiert ist, sollten Sie nicht versuchen, seine grundlegende Geometrie zu ändern, ohne vorher zu überprüfen, ob es eine entsperrte Alternative gibt.


Für den Referenzfall:
1. Definiert die Einbahnstrecke:
   1. Nord-Terminal
   2. Zentrum
   3. Krankenhaus
   4. Hochschule
   5. Süd-Terminal
2. Definiert den Pfad zurück:
   1. Süd-Terminal
   2. Hochschule
   3. Zentrum
   4. Nord-Terminal

Wenn Sie diesen Abschnitt beenden, sollten Sie eine Linie mit seinen Hauptrouten nach Richtung haben, bereit für Sie, Sequenzen, relevante Punkte und Betriebslogik im nächsten schnellen Start zu überprüfen.

## Zusätzliche Messwerte

- [Überprüfung des Betriebsnetzes: Sequenzen, Stoppberechtigungen und Relaispunkte]
