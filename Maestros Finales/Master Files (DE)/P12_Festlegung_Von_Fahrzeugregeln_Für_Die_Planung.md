---
title: Festlegung von Fahrzeugregeln für die Planung
shortTitle: Fahrzeugvorschriften
intro: Erfahren Sie, wie in Scheduling Fahrzeugregeln festgelegt werden, die die Gültigkeit
  von Flottenlösungen begrenzen, so dass die Berechnung die betriebliche Realität,
  Infrastruktur und validiertes Angebot berücksichtigt.
contentType: how-tos
versions:
- '*'
---
## Vorbereitung der Basis, die die Fahrzeugregeln verwenden wird

Bevor Sie Fahrzeugregeln aktivieren, müssen Sie überprüfen, ob die Grundlage, auf der diese Regeln konsumieren, bereits fertig ist. Fahrzeugregeln ersetzen keine vorherige schlechte Parametrierung. Ihre Funktion ist es, das Berechnungsverhalten so zu verfeinern, dass der Motor unerreichbare oder unerwünschte Kombinationen zurückwirft.

Verwenden Sie diesen Schnellstart, wenn Sie bereits ein validiertes Serviceangebot, eine Linie mit erlaubter Flotte und eine kohärente Betriebsstruktur haben, und Sie müssen den Fall vorbereiten, bevor Sie das Scheduling-Szenario erstellen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Flotte pro Linie erlaubt auf P8 eingerichtet.
2. Sie haben bereits die Zeitversion und die Reisezeit in P9 definiert.
3. Sie haben das Serviceangebot bei P10 bereits erstellt und validiert.
4. Sie haben bereits die Betriebsstruktur und den Status des Dienstes bei P11 überprüft.
5. Sie sind klar, welche Linie und Dienst Sie als Referenz verwenden werden.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde die Fahrzeugregeln für die Linie L1 definieren, so dass Scheduling nur eine Flotte verwendet, die mit Infrastruktur, validiertem Angebot und tatsächlichen Servicebeschränkungen übereinstimmt.**

Zur Vorbereitung der Fallbasis vor Aktivierung der Regeln:
1. Öffnen Sie die Zeile, die Sie als Referenz verwenden.
2. Prüfen Sie, welche Fahrzeugtypen zulässig sind.
3. Überprüfen Sie, von welcher Anzahlung oder Parkplatz die Operation geht.
4. Bestätigen Sie, dass der Dienst, den Sie als Eingabe verwenden, bereits **Validierung** ist.
5. Prüfen Sie, ob Sie nicht versuchen, mit Regeln ein Problem zu lösen, das früher online, Flotte oder Infrastruktur hätte korrigiert werden sollen.
6. Wenn Sie eine Inkonsistenz auf dieser Basis erkennen, korrigieren Sie diese, bevor Sie zu den Regeln wechseln.

Wenn Sie diesen Abschnitt beenden, sollten Sie sich darüber im Klaren sein, welchen realen Fall Sie versuchen, durch Fahrzeugregeln zu schützen.

## Erstellung oder Auswahl des Modells der Fahrzeugregeln

Sobald Sie die Basis überprüft haben, müssen Sie das Modell oder den Katalog der Fahrzeugregeln eingeben. An dieser Stelle geht es nicht darum, alles zu aktivieren. Es geht um die Auswahl oder den Aufbau einer Reihe von Einschränkungen, die die reale Logik des Dienstes darstellt.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie wissen, welchen validierten Service Sie als Referenz verwenden werden.
2. Sie haben bereits bestätigt, welche Fahrzeugtypen für die Linie gültig sind.
3. Du weißt, welche Probleme du vermeiden willst.

So erstellen oder wählen Sie das Regelmodell:
1. In GoalBus siehe **Einstellungen** > **Fahrzeuge** > **Vorschriften für den Fahrzeugtyp**.
ref: P12_Imagen1.png | compact
2. Prüfen Sie, ob es bereits ein richtiges Modell von Regeln für Ihren Fall gibt.
3. Wenn das Modell bereits existiert, öffnen Sie es und überprüfen Sie seine Konfiguration.
4. Wenn sie nicht existiert, erstellen Sie ein neues Modell von Regeln.
5. Weist dem Modell einen klaren **Bezeichnung** zu.
6. Falls zutreffend, fügen Sie einen **Beschreibung** hinzu, mit dem Sie seinen Zweck unterscheiden können.
7. Speichern Sie das Modell.
ref: P12_Imagen2.png | compact
8. Bestätigt, dass das Modell bereits verfügbar ist, um konkrete Regeln hinzuzufügen.

Für den Referenzfall könnte eine gültige Option sein:
- **Fahrzeuge - L1 bearbeitbar**
- **Flottenregeln - L1 Workable Service**

Wenn Sie diesen Abschnitt beenden, sollten Sie einen klaren Behälter haben, um die Fahrzeugbeschränkungen des Falles einzurichten.

## Aktiviere nur die Fahrzeugregeln, die du wirklich brauchst

Jetzt können Sie mit der Aktivierung von Regeln beginnen. Hier ist es wichtig, ein klares Kriterium zu halten: Eine Regel muss einen echten Bedarf an Betrieb, Sicherheit, Infrastruktur oder Compliance darstellen. Wenn eine Regel nicht auf ein bestimmtes Problem reagiert, ist es noch nicht angebracht, sie zu aktivieren.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits ein Modell von Regeln erstellt oder ausgewählt.
2. Sie wissen, welche Flotte für die Linie gültig ist.
3. Sie wissen, welche Kombinationen verboten oder begrenzt werden sollten.

Um die Fahrzeugregeln des Falles zu aktivieren:
1. Überprüfen Sie im Regelmodell den verfügbaren Regelkatalog, indem Sie auf **Neue Regel hinzufügen** klicken.
ref: P12_Imagen3.png
2. Identifizieren Sie, welche auf die tatsächlichen Bedürfnisse Ihres Dienstes reagieren, indem Sie das entsprechende **Meldebogen** auswählen.
3. Definieren Sie einen **Bezeichnung** und geben Sie für jede neue Regel einen **Warenbezeichnung** ein.
4. Aktiviere nur die Regeln, die du für den Fall wirklich brauchst.
5. Konfigurieren Sie die spezifischen Parameter jeder Regel bei der Anwendung.
6. Wiederholen Sie den Prozess, um die erforderlichen Mindestbeschränkungen zu decken.
7. Speichern Sie die Änderungen.
8. Überprüfen Sie das komplette Modell und bestätigen Sie, dass es nicht sehr restriktiv oder zu offen ist.

Fragen Sie sich für den Referenzfall:
1. Welche Flottensituationen sollte das System verhindern?
2. Welche Kombinationen wären physisch möglich, aber nicht wünschenswert?
3. Welches Verhalten sollte von der Logik der Kaution, des Parkens oder der Leitung geleitet werden?

Wenn Sie diesen Abschnitt beenden, sollten Sie eine erste Reihe von aktiven und konsistenten Fahrzeugregeln haben, ähnlich der im folgenden Bild:
ref: P12_Imagen4.png | compact(20x)

## Vorschriften für Strecken, Flotten und Infrastruktur

Nach der Aktivierung der Regeln, müssen Sie überprüfen, ob sie wirklich mit der Linie und Infrastruktur, die den Fall stützt ausgerichtet sind. Eine Fahrzeug-Regel sollte nicht der Flotte durch Linie oder die Geographie von Lagern und Parkplätzen erlaubt widersprechen.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Sie haben bereits die ersten Regeln aktiviert.
2. Sie haben bereits die zulässigen Fahrzeugtypen überprüft.
3. Sie kennen die physische Basis, von der die Operation ausgeht.

Überprüfung der Kohärenz der Regeln:
1. Überprüfen Sie die Zeileneinstellungen erneut.
2. bestätigt, dass die Vorschriften nicht den zulässigen Fahrzeugtypen widersprechen.
3. Überprüfen Sie die Beziehung mit dem Lager und dem autorisierten Parkplatz.
4. Es beweist, dass die Regeln diese Logik verstärken, anstatt sie zu brechen.
5. Wenn eine Regel den Dienst unbrauchbar macht oder der Infrastruktur widerspricht, korrigieren Sie ihn oder deaktivieren Sie ihn.
6. Speichern Sie die endgültige Version des Modells.

Für den Referenzfall stellen Sie sicher, dass
1. Die Linie L1 kann weiterhin die autorisierte Flotte nutzen.
2. Der North Depot bleibt ein kohärenter Ausgang für den Service.
3. Keine Regel blockiert eine Operation, die entsprechend der bereits konfigurierten Basis gültig sein sollte.

Wenn Sie diesen Abschnitt beenden, sollten Sie Regeln haben, die mit der Realität des Dienstes abgestimmt sind, nicht mit einem abstrakten oder generischen Modell.

## Bestätigung, dass das validierte Angebot noch kalkulierbar ist

Der letzte Schritt ist zu überprüfen, dass die gerade aktivierten Fahrzeugregeln weiterhin die Berechnung des validierten Angebots ermöglichen. Es ist eine Sache, mit Kriterien zu beschränken, und eine andere ist, das Modell so sehr zu schließen, dass der Service nicht mehr lebensfähig ist, bevor überhaupt das Szenario erstellt wird.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie haben bereits die notwendigen Regeln aktiviert.
2. Sie haben bereits seine Beziehung zu Linie, Flotte und Infrastruktur überprüft.
3. Sie wissen genau, wie der Eingang von Scheduling sein wird.

Um zu bestätigen, dass der Fall noch praktikabel ist:
1. Überprüfen Sie erneut den validierten Dienst, den Sie als Referenz verwenden.
2. Überprüfen Sie, ob die Linie noch Zugang zu der Flotte hat, die sie braucht.
3. Prüfen Sie, ob die aktivierten Regeln mindestens eine vernünftige Lösung für den Fall hinterlassen.
4. Fragen Sie sich, ob das System schon ein Scheduling-Szenario schaffen könnte, ohne in Widerspruch zu geraten.
5. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
6. Wenn die Antwort nein ist, korrigieren Sie das Regelmodell, bevor Sie folgen.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Die Linie L1 unterhält eine gültige und autorisierte Flotte.
2. Der validierte praktikable Dienst bleibt mit den aktivierten Regeln kompatibel.
3. Das Fahrzeugmodell ist nun im Rahmen des Scheduling-Szenarios einsatzbereit.

Wenn Sie diesen Abschnitt beenden, sollten Sie in der Lage sein zu sagen, dass die Logik der Fahrzeuge bereits geschlossen ist und konsistent genug ist, um zur Definition der Verschiebungsregeln und zur Erstellung des Szenarios zu gelangen.

## Zusätzliche Messwerte

- [Definition von Schichttypen und Schichtregeln](P13_Definition_Von_Schichttypen_Und_Schichtregeln.md)
