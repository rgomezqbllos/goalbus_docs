---
title: Leeres Reisen und Reisen laden
shortTitle: Leeres Reisen
intro: Erfahren Sie, wie Sie leere Reise- und Fahrerreisematrizen einrichten, so dass
  GoalBus reale Logistikzeiten nutzt, nichtproduktive Kosten minimiert und realistischere
  Zeitpläne und Verschiebungen erstellt.
contentType: how-tos
versions:
- '*'
---
## Erstellen der richtigen Matrix für den richtigen Tagestyp

Vor der Berechnung von Scheduling müssen Sie festlegen, wie sich die Operation physisch bewegt, wenn sie keine Einnahmen generiert. In GoalBus deckt dieses Modul zwei verschiedene Dinge ab:

1. **Leeres Reisen**, das die Bewegung eines Busses mit einem Fahrer zwischen dem Tank, dem Parkplatz, dem Start der Linie oder zwischen den Linien darstellt.
2. **Fahrerverlagerungen**, die die Bewegung des Fahrers ohne Fahrzeug, z.B. zu Fuß, Taxi oder Shuttle darstellt.

GoalBus behandelt diese Bewegungen nicht als eine einzige und feste Liste. Das Tool macht deutlich, dass sie in **Matrizen nach Art des Tages** organisiert werden müssen, da sich der Verkehr je nach Betriebskontext ändert. Eine Fahrt kann an einem Sonntag 15 Minuten und an einem Montagmorgen 45 Minuten dauern, so dass dieselbe Verbindung nicht immer gleichzeitig wiederverwendet werden sollte.

Nutzen Sie diesen schnellen Start, wenn Sie bereits Parkplätze und Lagerhäuser eingerichtet haben, und Sie müssen die unsichtbare Logistik vorbereiten, die eine realistische Planung ermöglicht.

Bevor Sie beginnen, stellen Sie sicher, dass:

1. Sie haben bereits die Parkplätze und Lagerhäuser bei P5 vorbereitet.
2. Sie sind bereits klar über die Linie oder den Dienst, den Sie als Referenz verwenden werden.
3. Du weißt, was für ein Tag du modelst.
4. Sie verstehen den Unterschied zwischen einer leeren Fahrt und einer Fahrerfahrt.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde die leere Reisematrix für einen Arbeitstag der Linie L1, die Verbindung der North Parking mit dem North Terminal, und auch die Fahrer Reisematrix, wenn für Relais erforderlich.**

So erstellen Sie die richtige Matrix für Ihren Fall:

1. Öffnen Sie in GoalBus das **Unbeladenes Reisen und Reisen** Modul.
ref: P8_Imagen1.png | full
2. Entscheiden Sie zunächst, ob Sie eine **Leerfahrten**-Matrix, eine **Fahrerbewegungen**-Matrix oder beides erstellen möchten.
3. Klicken Sie auf **Neu erstellen**.
ref: P8_Imagen2.png | compact(2x5)
4. Geben Sie eine klare **Bezeichnung** für die Matrix ein.
5. Fügen Sie einen **Beschreibung** hinzu, mit dem Sie den Operationskontext erkennen können.
6. Weist den **Art des Tages** zu, für den diese Matrix gilt.
7. Speichern Sie die Matrix.
ref: P8_Imagen3.png | compact(x8)
8. Überprüfen Sie, ob die Matrix eindeutig mit dem richtigen Kontext und nicht einer generischen Logik verbunden ist.

Für den Referenzfall könnte eine gültige Matrix aufgerufen werden:

- **Leer - Januar 2026**
- **Verdrängungen - Arbeitstage**

Wenn Sie diesen Abschnitt beenden, sollten Sie eine richtig erstellte Matrix haben, die mit dem richtigen Tagestyp verknüpft ist.

## Ladeverbindungen durch Massenimport oder manuelle Bearbeitung

Sobald die Matrix erstellt ist, müssen Sie sie mit den eigentlichen Verbindungen zwischen Ursprung und Bestimmungsort füllen. Das Dokument zeigt an, dass GoalBus zwei Formen der Arbeit erlaubt:

1. **Massenimport CSV**, empfohlen für große Netzwerke.
2. **Manuelle Eingabe**, nützlich für kleine Fälle oder Punktanpassungen abzuschließen.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:

1. Sie haben bereits die richtige Matrix erstellt.
2. Sie haben bereits die relevanten Herkunfts- und Zielorte identifiziert.
3. Sie wissen, ob Ihr Fall manuell geladen werden kann oder ob ein massiver Import wünschenswert ist.

Zum Laden von Daten durch Massenimport:

1. Bereiten Sie eine CSV-Datei mit dem Standard-GoalBus-Format vor.
2. Stellen Sie sicher, dass Sie mindestens:
   1. Ursprung
   2. Zielorte
   3. Entfernungen
   4. Zeitnischen, wenn angewendet.
   5. Dauer
3. Wählen Sie in GoalBus die Option **Belastung** oder **Einfuhr** aus.
ref: P8_Imagen4.png | compact
4. Wählen Sie die CSV-Datei.
5. Überprüfen Sie die **Vorvalidierung**, die das System macht.
6. Prüfen Sie, ob das System:
   1. erkennt Fehler,
   2. gibt an, wie viele Datensätze erstellt werden.
ref: P8_Imagen5.png |compact
7. Wenn die Validierung korrekt ist, bestätigen Sie die Last.
8. Überprüfen Sie, ob das Gitter mit den erwarteten Datensätzen gefüllt ist.

Wenn alles korrekt ist, wird das Array ähnlich dem des folgenden Bildes angezeigt:
ref: P8_Imagen6.png |full

Zum manuellen Laden von Daten:

1. Öffnen Sie das Raster der Matrix.
2. Fügen Sie einen neuen Datensatz hinzu, indem Sie auf **Neue Beziehung** klicken.
ref: P8_Imagen7.png | compact
3. Definieren Sie die **Ursprung**.
4. Definieren Sie die **Bestimmung**.
5. Geben Sie die entsprechende Zeit oder Entfernung ein.
6. Falls zutreffend, definieren Sie den Zeitnischen.
ref: P8_Imagen8.png | compact(15x)
7. Behalten Sie das Protokoll.
8. Wiederholen Sie den Vorgang, bis Sie die für Ihren Fall erforderlichen minimalen Verbindungen abschließen.

Beginnen Sie für den Referenzfall mit Verbindungen wie diesen:

1. Parken im Norden → Terminal im Norden
2. Süd Terminal → Nord Parken

Wenn Sie diesen Abschnitt beenden, sollten Sie eine Matrix mit echten Verbindungen haben, entweder per Datei geladen oder manuell eingegeben.

## Unterscheidung von Leerfahrten von Fahrerreisen

Jetzt müssen Sie überprüfen, dass Sie nicht zwei verschiedene Logiken mischen. Das Dokument hebt hervor, dass GoalBus **Leerfahrten** und **Fahrerbewegungen** ähnlich in der Konfiguration behandelt, aber mit einem anderen Geschäftszweck:

1. Die Leerfahrt nutzt **Bus + Fahrer** und modelliert die Logistik, ein Fahrzeug dort zu bewegen, wo es gebraucht wird.
2. Die Scroll verwendet **Nur Fahrer** und modelliert, wie lange eine Person ein Relais oder einen Startpunkt erreichen muss, ohne die Flotte zu bewegen.

Bevor Sie fortfahren, stellen Sie sicher, dass:

1. Sie haben bereits mindestens die wesentlichen Verbindungen zu Ihrem Fall geladen.
2. Sie können erkennen, ob jede Verbindung einem Fahrzeug oder nur einer Person entspricht.
3. Sie haben nicht beide Logiken in dieselbe falsche Matrix gemischt.

Um zu validieren, dass jede Matrix die richtige Ressource darstellt:

1. Überprüfen Sie eine **Leerfahrt**-Verbindung und bestätigen Sie, dass ihre Logik reagiert auf:
   1. ein Fahrzeug von einem Tank oder Parkplatz in Richtung der Linie zu bewegen, oder
   2. ein Fahrzeug zwischen den Linien bewegen.
2. Überprüfen Sie eine **Verdrängung**-Verbindung und bestätigen Sie, dass ihre Logik reagiert auf:
   1. einen Fahrer ohne Fahrzeug bewegen oder
   2. ein Relais in einem Terminal oder Header zulassen.
3. Überprüfen Sie, ob die leere Reisematrix verkehrsabhängige Zeiten modelliert.
4. Überprüfen Sie, ob die Fahrerreisematrix den tatsächlichen Transfermodus widerspiegelt, wie z.B. Gehen, Taxi oder Shuttle.
5. Korrigieren Sie jede falsche Verbindung, bevor Sie fortfahren.

Fragen Sie sich für den Referenzfall:

1. Ich modelliere hier einen Bus, der den Parkplatz verlässt oder nur einen Fahrer, der zu einem Header fährt?
2. Entspricht die Zeit, die ich eingestellt habe, dem tatsächlichen Verkehr oder der Fahrweise des Fahrers?
3. Würde der Motor diese Informationen korrekt verwenden, wenn er den Zeitplan und die Verschiebungen erstellt?

Wenn Sie diesen Abschnitt beenden, sollten Sie klar sein, welcher Teil Ihrer Konfiguration zur Fahrzeuglogistik gehört und welcher Teil zur Fahrerlogistik gehört.

## Überprüfen, ob die Matrix bereit für Scheduling ist

Das letzte Ziel dieses schnellen Starts ist nicht nur, einen Tisch zu füllen, sondern eine Logistikbasis vorzubereiten, die Scheduling verbrauchen kann. Das Dokument erklärt, dass eine präzise Modellierung dieser Matrizen drei Dinge verbessert:

1. die **Kostentransparenz**,
2. die **realistische Gestaltung von Verschiebungen**,
3. und der **Optimierungsgenauigkeit**.

Bevor Sie fertig sind, stellen Sie sicher, dass:

1. Die richtige Matrix existiert.
2. Es ist mit dem richtigen Tag verbunden.
3. Die minimalen Anschlüsse im Fall sind bereits geladen.
4. Sie haben leeres Reisen und Fahrerreisen richtig getrennt.

Um zu bestätigen, dass die Matrix bereits bereit für den nächsten Schritt ist:

1. Sieh dir den Referenzfall an, den du gebaut hast.
2. Bestätigt, dass GoalBus bereits weiß:
   1. von dem aus das Fahrzeug physisch herauskommt,
   2. wo sie in die Linie eintritt,
   3. wie es zurückkommt, wenn es fällig ist,
   4. und wie sich ein Fahrer für ein Relais bewegen würde, wenn es angewendet wird.
3. Fragen Sie sich, ob das System in diesem Fall bereits unproduktive Zeiten und Entfernungen minimieren könnte.
4. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
5. Wenn die Antwort nein ist, gehen Sie zurück und fügen oder korrigieren Sie Verbindungen hinzu, bevor Sie fortfahren.

Wenn Sie diesen Abschnitt beenden, sollten Sie in der Lage sein zu behaupten, dass Ihre Logistikbasis realistisch genug ist, um Zeiten, Dienstleistungen und Terminplanung zu erhalten.

## Zusätzliche Messwerte

- [Festlegung der Fahrzeugtypen und der zulässigen Flotte pro Strecke](P4_Festlegung_Der_Fahrzeugtypen_Und_Der_Zulässigen_Flotte_Pro_Strecke.md)
