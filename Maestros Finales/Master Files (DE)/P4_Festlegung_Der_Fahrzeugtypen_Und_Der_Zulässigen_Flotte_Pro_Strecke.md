---
title: Festlegung der Fahrzeugtypen und der zulässigen Flotte pro Strecke
shortTitle: Flotte je Strecke
intro: Erfahren Sie, wie Sie die pro Zeile zulässigen Fahrzeugtypen und Flottenbeschränkungen
  so konfigurieren, dass GoalBus undurchführbare Zuweisungen blockiert, physische
  und ökologische Grenzen beachtet und eine kohärente Basis vor der Festlegung von
  Zeiten und Diensten vorbereitet.
contentType: how-tos
versions:
- '*'
---
## Festlegung der zulässigen Fahrzeugtypen für eine Strecke

In einem ersten Schritt müssen Sie klarstellen, welche **Fahrzeugtypen** jede Linie bedienen kann. In GoalBus ist diese Beschränkung nicht dekorativ: sie fungiert als Sicherheits-, Compliance- und physische Lebensfähigkeitsfilter. Ziel ist es, zu verhindern, dass das System ein Fahrzeug vorschlägt, das nicht auf eine Straße passt, das einer Umweltbeschränkung nicht entspricht oder das in diesem Dienst nicht zirkulieren sollte.

Verwenden Sie diesen schnellen Start, wenn Sie die Flottenbasis schließen müssen, die Ihr Fall vor der Festlegung von Zeiten und Serviceangebot verwenden wird.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie sind klar, welche Linie Sie als Referenzfall verwenden werden.
2. Wissen Sie, zumindest auf der grundlegenden Ebene, welche physischen oder ökologischen Einschränkungen diese Linie beeinflussen.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde definieren, welche Fahrzeugtypen die L1-Linie bedienen können, um sicherzustellen, dass meine erste Planung nur eine Flotte nutzt, die mit der physischen und regulatorischen Realität des Dienstes übereinstimmt.**

Um die zulässigen Fahrzeugtypen Ihres Gehäuses zu definieren:
1. Öffnen Sie in GoalBus, falls bereits eine Zeile existiert, die **Zeile**-Konfiguration, die Sie als Referenz verwenden werden.
2. Finden Sie den **zulässige Fahrzeugtypen** Abschnitt.
3. Prüfen Sie, ob die Zeile bereits Typen zugewiesen hat.
4. Wenn die Zeile bereits Typen definiert hat, bestätigt sie, dass sie für den Fall immer noch korrekt sind.
5. Wenn sie noch nicht definiert sind, überprüfen Sie zuerst, ob der **Fahrzeugtyp**, den Sie benötigen, bereits in der allgemeinen Fahrzeugkonfiguration vorhanden ist.
6. Wenn Typ **Ja, es existiert.**, wählen Sie es wie für diese Zeile erlaubt.
7. Wenn Typ **existiert nicht**, verlassen Sie die Zeileneinstellungen und gehen Sie zu den allgemeinen **Fahrzeuge**-Einstellungen, um zuerst den Typkatalog aus dem **Fahrzeugtypen**-Panel zu erstellen oder abzuschließen.
ref: P4_Imagen1.png | full
8. Erstellen Sie den Fahrzeugtyp, den Sie benötigen, indem Sie eine klare und verständliche Kategorie für das Unternehmen verwenden, zum Beispiel:
   1. Kleinbus
   2. Elektrischer Standard
   3. Artikulierter Diesel
ref: P4_Imagen2.png | compact(2x5)
9. Speichern Sie den neuen Fahrzeugtyp.
ref: P4_Imagen3.png | compact(x9)
10. Gehen Sie zurück zu den Zeileneinstellungen.
11. Markieren Sie die spezifischen Fahrzeugtypen, die auf dieser Strecke betrieben werden dürfen.
ref: P4_Imagen4.png | compact(8x)
12. Lassen Sie die Männer unbemerkt, die diesen Dienst nicht bedienen müssen.
13. Speichern Sie die Einstellungen.
14. Überprüfen Sie die Zeile (falls vorhanden) und bestätigen Sie, dass der Filter bereits die Betriebsrealität korrekt darstellt.

Fragen Sie sich für den Referenzfall:
1. Unterstützt die Linie L1 einen Standardbus, einen Minibus oder beides?
2. Gibt es einen Fahrzeugtyp, der je nach Größe oder Umgebung ausgeschlossen werden muss?
3. Wenn es nicht den Kerl gab, den Sie brauchten, haben Sie ihn erstellt, bevor Sie versuchten, ihn der Linie zuzuweisen?
4. Sollte das System ein manuelles Mapping blockieren, wenn Sie versuchen, ein unbefugtes Fahrzeug zu verwenden?

Wenn Sie diesen Abschnitt abgeschlossen haben, sollten Sie eine Fuhrpark-by-Line-Beschränkung definiert haben, die bereits als Grundlage für eine weitere Berechnung dient.

## Über die Leitung zu den zulässigen Lagern oder Parkplätzen

Nachdem Sie definiert haben, welche Flotte in die Linie passt oder nicht passt, müssen Sie prüfen, aus welchen physischen Basen dieser Dienst aussteigen kann. GoalBus ermöglicht es Ihnen, **Zulässige Parkplätze oder Lagerhäuser** pro Zeile zu definieren, um das System zu zwingen, den Service von geografisch korrekten Standorten aus zu starten und Leerkilometer zu reduzieren.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die zulässigen Fahrzeugtypen der Linie konfiguriert.
2. Sie wissen, von welcher operativen Basis der Dienst wirklich beginnen sollte.

Um die Leitung auf Ihre zulässigen Lagerhäuser oder Parkplätze zu beziehen:
1. Suchen Sie innerhalb derselben Zeilenkonfiguration den Abschnitt **Parken erlaubt** oder **Zulässige Einlagen**.
2. Prüfen Sie, ob die Leitung bereits autorisierte Einlagen hat.
3. Wählen Sie nur die Lager oder Garagen, die geographisch autorisiert sind, um Dienste auf dieser Linie zu starten.
4. Lassen Sie die Basen aus, die für diesen Broker keinen operativen Sinn ergeben.
5. Speichern Sie die Einstellungen.
6. Überprüfen Sie, ob die Linie jetzt eine kohärente Logik des Austritts von der vernünftigsten Basis hat.

Für den Referenzfall stellt sie fest, dass
1. Die Linie L1 kann aus dem North Depot aussteigen.
2. Der Hauptparkplatz ist der richtige.
3. Du lässt nicht zu, dass eine weit entfernte Lagerstätte dich zwingt, viele Meilen in einem Vakuum zu reisen, um die erste Reise zu beginnen.

Wenn Sie diesen Abschnitt beenden, sollten Sie die Linie haben (wenn sie bereits existiert), die Flotte erlaubt und der Dienst verlassen Geographie ausgerichtet.

## Validierung, dass die Strecke bereits über eine kohärente Flottenbasis verfügt

Nachdem Sie die zulässigen Fahrzeugtypen und die autorisierten Lager oder Parkplätze bereits definiert haben, müssen Sie eine abschließende Validierung vornehmen.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Die Linie hat bereits Fahrzeugtypen erlaubt.
2. Wenn der erforderliche Fahrzeugtyp nicht existierte, wurde er zuvor in der allgemeinen Konfiguration erstellt.
3. Die Linie hat bereits autorisierte Lager oder Parkplätze.
4. Die Konfiguration spiegelt die Realität des Falles wider, den Sie bauen.

Um zu bestätigen, dass die Flottenbasis bereits bereit ist:
1. Überprüfen Sie erneut die komplette Linienkonfiguration.
2. bestätigt, dass die ausgewählten Fahrzeugtypen die Flotte darstellen, die diesen Dienst tatsächlich betreiben sollte.
3. Bestätigt, dass autorisierte Lager oder Parkplätze Leerkilometer minimieren.
4. Fragen Sie sich, ob das System mit dieser Konfiguration bereits vermeiden würde:
   1. physisch unmögliche Aufgaben,
   2. Verstöße gegen die Umweltvorschriften,
   3. Abweichungen von geografisch ineffizienten Grundlagen.
5. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
6. Wenn die Antwort nein ist, korrigieren Sie die Zeile oder erstellen Sie den fehlenden Fahrzeugtyp, bevor Sie fortfahren.

Wenn Sie diesen Abschnitt beenden, sollten Sie in der Lage sein zu erklären, dass Sie alle Arten von Fahrzeugen und Flotte für die Planung Ihrer Linie notwendig haben.

## Zusätzliche Messwerte

- [Vorbereitung von Parkplätzen und Lagern](P5_Vorbereitung_Von_Parkplätzen_Und_Lagern_Für_Den_Betrieb.md)
