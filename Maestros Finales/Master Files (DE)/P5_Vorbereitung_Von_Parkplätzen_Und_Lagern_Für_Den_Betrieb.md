---
title: Vorbereitung von Parkplätzen und Lagern für den Betrieb
shortTitle: Parkplätze und Lagerhäuser
intro: Erfahren Sie, wie Sie Parkplätze und Lager konsequent einrichten, damit Scheduling
  eine realistische physische Infrastruktur nutzen, Leerkilometer minimieren und die
  korrekte Datenhierarchie respektieren kann.
contentType: how-tos
versions:
- '*'
---
## Konfiguration der Lagerstätte als Betriebs- und Relaisstruktur

Vor der Erstellung des Parkplatzes müssen Sie die **Hinterlegung** überprüfen. In GoalBus ist die Kaution die operative Basis der Organisation und ist die zwingende Verbindung für Fahrzeuge und Fahrer. Darüber hinaus dient seine Konfiguration nicht nur zur Identifizierung der Einheit, sondern auch zu definieren, wo die Verschiebungen beginnen oder enden können, einschließlich autorisierte Header oder Terminals, die effiziente Relais ermöglichen und Vakuum Laufleistung zu reduzieren.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie wissen, welche Kaution für die Leitung oder den Service verantwortlich ist, den Sie vorbereiten.
2. Sie verstehen, dass die Kaution die wichtigste Einheit ist und dass der Parkplatz davon abhängt.
3. Sie haben bereits alle Arten von Fahrzeugen erstellt, die für den Betrieb benötigt werden.

Um Ihre Fall-Einlage zu erstellen oder zu validieren:
1. Öffnen Sie in GoalBus das **Einlagen** Modul.
ref: P5_Imagen3.png | full
2. Sehen Sie, ob die Kaution, die Sie benötigen, bereits vorhanden ist.
3. Wenn die Einzahlung bereits existiert, öffnen Sie sie und überprüfen Sie ihre Einstellungen.
4. Wenn es nicht existiert, erstellen Sie eine neue.
ref: P5_Imagen4.png | compact(2x)
5. Definiert oder validiert diese Felder:
   1. **ANHANG** als eindeutige Kennung.
   2. **Kurzbezeichnung** für kompakte Ansichten.
   3. **Anteil %** als Einlagenanteil an den Gesamtgeschäften. Unter allen Einlagen müssen 100% addiert werden.
   4. **Langer Name** als Hauptname der Einzahlung.
   5. **Externe ID**, wenn der Client mit ERP- oder HR-Integrationen arbeitet.
6. Fügen Sie den **Zugelassene Start- und Endstopps** als Header oder Terminals hinzu, wo Relais oder Ende der Verschiebung erlaubt sind.
7. Sparen Sie die Kaution.
ref: P5_Imagen5.png | compact(8.5x)
8. Bestätigt, dass die Kaution bereits operativ den Fall, den Sie gebaut haben, aufrecht erhalten kann.

Für den Referenzfall ist Folgendes zu prüfen:
1. Die North Deposit ist die richtige organisatorische Einzahlung.
2. Relevante L1-Header oder Terminals werden bei der Anwendung als Start- oder Endstandorte autorisiert.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine korrekt identifizierte Einzahlung mit Ihren autorisierten Betriebsstandorten verbunden haben.

## Konfigurieren des Parkens als physischer Knoten des Netzwerks

Nachdem Sie die Einzahlung definiert haben und vor dem Gehen auf leeren Reisen, Flotte oder Scheduling Regeln, müssen Sie die **Parken** gut konfiguriert verlassen, die Ihren Fall halten wird. In GoalBus, ein Parkplatz ist nicht nur ein administratives Tag. Es ist ein geolozierter physischer Knoten des Netzwerks, und wenn Sie es erstellen, erzeugt das System automatisch einen zugehörigen Stopp an diesen Koordinaten, so dass der Motor Distanzen, Eingangszeiten und Ausgabezeiten konsistent berechnen kann. Darüber hinaus muss jeder Parkplatz mit einer organisatorischen Kaution verknüpft werden.

Verwenden Sie diesen Schnellstart, wenn Sie bereits das Basisnetz erstellt haben und dieses Netzwerk mit der tatsächlichen physischen Infrastruktur verbinden müssen, bevor Sie weiterfahren und planen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie sind klar, welche Linie oder Dienst Sie als Referenzfall verwenden werden.
2. Sie wissen, von welcher physischen Grundlage diese Operation ausgehen sollte.
3. Sie haben bereits die operativen Einlagen eingerichtet.
4. Sie haben bereits alle notwendigen Arten von Fahrzeugen erstellt.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde den North Depot Parkplatz vorbereiten und bestätigen, dass Ihre Beziehung mit der Kaution und Linie L1 konsistent ist, bevor Sie mit leeren Reisen und Scheduling fortfahren.**

Um Ihren Fallparkplatz zu erstellen oder zu validieren:
1. Öffnen Sie in GoalBus das **Parkplätze** oder **Parkplätze** Modul innerhalb der Netzwerkinfrastruktur.
ref: P5_Imagen1.png | full
2. Sehen Sie, ob der Parkplatz, den Sie benötigen, bereits vorhanden ist.
3. Wenn der Parkplatz bereits existiert, öffnen Sie ihn und überprüfen Sie seine Konfiguration.
4. Wenn der Parkplatz nicht existiert, erstellen Sie einen neuen.
ref: P5_Imagen2.png | compact(2x)
5. Definiert oder validiert diese Felder:
   1. **ANHANG** als kurze Kennung für kompakte Ansichten.
   2. **Kurzbezeichnung** für kompakte Ansichten.
   3. **Langer Name** als beschreibender Name der Garage oder Terrasse.
   4. **Koordinaten** um das Parken auf der Karte korrekt zu lokalisieren.
   5. **Externe ID**, wenn der Client mit ERP- oder HR-Integrationen arbeitet.
6. Überprüfen Sie, ob der Parkplatz mit dem zuvor erstellten **Hinterlegung** verknüpft ist.
ref: P5_Imagen6.png | compact(8.5x)
7. Klicken Sie auf **Nächster**, um die Parkkapazität und die zulässigen Fahrzeugtypen zu konfigurieren. Diese können Sie in Zukunft bearbeiten, wenn sich die Bedingungen ändern.
ref: P5_Imagen7.png | compact(8.5x)
8. Prüfen Sie visuell die Karte, dass Ihr Standort für den eigentlichen Betrieb sinnvoll ist.
9. Bestätigt, dass das System das Parken bereits als Quelle oder logistisches Ziel des Betriebes behandeln kann.

Wenn Sie diesen Abschnitt beenden, sollten Sie einen ordnungsgemäß geolokalisierten und ordnungsgemäß untergeordneten Parkplatz dem richtigen Lager haben.

## Validierung der Konsistenz zwischen Parkplatz, Kaution und Leitung

Jetzt, da Sie bereits Parkplätze und Lagerung eingerichtet haben, müssen Sie überprüfen, ob diese Infrastruktur der Linienlogik und logistischen Effizienz entspricht, die GoalBus erwartet. Das Linienmodell selbst ermöglicht es Ihnen, **Zulässige Parkplätze oder Lagerhäuser** zu definieren, um das System zu zwingen, den Service von den geografisch korrekten Basen zu starten und Leerkilometer zu minimieren.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Der Parkplatz ist bereits mit der richtigen Kaution verbunden.
2. Das Lager hat bereits seine autorisierten Standorte.

Um die vollständige Kohärenz der Infrastruktur zu validieren (wenn Sie bereits eine Zeile haben):
1. Öffnen Sie die **Zeile**-Konfiguration, die Sie als Referenz verwenden.
2. Überprüfen Sie den Abschnitt **Zulässige Parkplätze** oder **Zulässige Einlagen**.
3. Überprüfen Sie, ob die richtige Kaution berechtigt ist, die Dienste auf dieser Linie zu starten.
4. Wenn die richtige Einzahlung nicht genehmigt ist, fügen Sie sie hinzu.
5. Bestätigen Sie, dass Sie nicht aktivierte Einlagen hinterlassen, die keine geografische Bedeutung für diese Zeile haben.
6. Prüfen Sie, ob das Verhältnis zwischen Linie, Kaution und Parkplatz das Fahren ohne Einkommen minimiert.
7. Bestätigen Sie, dass die physische Infrastruktur, die Sie gerade vorbereitet haben, den Service unterstützen könnte, den Sie später erstellen oder berechnen werden.
8. Wenn Sie Unstimmigkeiten feststellen, korrigieren Sie sie, bevor Sie fortfahren.

Fragen Sie sich für den Referenzfall:
1. Ist die Linie L1 berechtigt, vom Norddepot aus zu fahren?
2. Benutzt das Lager das North Parking als seine physische Basis?
3. Verringert die daraus resultierende Logik Meilen in einem Vakuum, anstatt sie zu erhöhen?

Wenn Sie diesen Abschnitt beenden, sollten Sie in der Lage sein zu sagen, dass die Leitung, die Kaution und der Parkplatz die gleiche operative und logistische Logik bilden.

## Zusätzliche Messwerte

- [Hauptnetz](P6_Vorbereitung_Des_Master_Netzwerks_Mit_Haltestellen_Linien_Und_Routen.md)
