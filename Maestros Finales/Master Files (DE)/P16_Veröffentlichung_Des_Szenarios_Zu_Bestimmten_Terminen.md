---
title: Veröffentlichung des Szenarios zu bestimmten Terminen
shortTitle: Szenario veröffentlichen
intro: Erfahren Sie, wie Sie ein validiertes Szenario zu bestimmten Terminen veröffentlichen,
  welche Lösung in Betrieb geht, und halten Sie die Rückverfolgbarkeit zwischen Planung,
  Validierung und operativem Einsatz aufrecht.
contentType: how-tos
versions:
- '*'
---
## Vorbereitung des validierten Szenarios vor der Veröffentlichung

Nach der Berechnung und Validierung einer Lösung besteht der nächste Schritt darin, zu entscheiden, dass **wenn** im eigentlichen Betrieb in Kraft treten muss. Bei der Veröffentlichung eines Szenarios geht es nicht nur um die Genehmigung: Es geht darum, die validierte Lösung für ein bestimmtes Datum in den Betriebskalender einzufügen, ohne sie mit einem Entwurf oder einer noch überarbeiteten Version zu verwechseln.

Verwenden Sie diesen Schnellstart, wenn Sie bereits eine Phase mit einer Lösung im **Validierung**-Status haben und diese für einen bestimmten Zeitraum in Betrieb nehmen müssen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben das Szenario bereits auf P15 validiert.
2. Die Szenariolösung, die Sie veröffentlichen möchten, ist im **Validierung**-Status.
3. Du weißt, welche genauen Daten du einplanen willst.
4. Sie sind klar, dass die Veröffentlichung den Betriebszustand der Lösung verändert und als implantierte Version sichtbar macht.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde das validierte Szenario der Linie L1 veröffentlichen, damit es während eines bestimmten Arbeitszeitraums in Kraft tritt, ohne Lösungen zu beeinflussen, die diesen Zeitpunkten nicht entsprechen.**

Vorbereitung der Veröffentlichung des Szenarios:
1. Öffnen Sie das **Planungsszenarien** Modul.
2. Suchen Sie das Szenario, das Sie bereits validiert haben.
3. Überprüfen Sie, ob der aktuelle Zustand der Lösung **Validierung** ist.
4. Prüfen Sie den Namen der Bühne, die Zeile(n) enthalten, den Tagestyp und die Beschreibung.
5. Bestätigen Sie, dass Sie dabei sind, genau die richtige Lösung zu veröffentlichen.
6. Wenn das Szenario noch nicht validiert ist, gehen Sie zurück und beenden Sie P15, bevor Sie fortfahren.
7. Wenn das Szenario richtig ist, fahren Sie mit der Veröffentlichung fort.

Wenn Sie diesen Abschnitt abgeschlossen haben, sollten Sie das validierte Szenario, das Sie implementieren möchten, eindeutig identifiziert haben.

## Auswahl des temporären Veröffentlichungsfensters

Sobald das Szenario bestätigt ist, müssen Sie entscheiden, **zu welchem Zeitpunkt** gilt. Veröffentlichung sollte nicht mehr eindeutig gemacht werden. Es sollte klar sein, wann und wann diese Lösung operative Referenz sein wird.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits bestätigt, welches Szenario Sie veröffentlichen werden.
2. Sie wissen, ob die Veröffentlichung einen Tag, eine Woche, eine kontinuierliche Reichweite oder einen längeren Betriebsblock umfasst.
3. Sie sind bereits klar, dass der gewählte Zeitraum nicht der Art des Tages und der zeitlichen Logik des Szenarios widersprechen sollte.

So wählen Sie das temporäre Veröffentlichungsfenster:
1. Öffnen Sie aus dem validierten Szenario die Aktion **Veröffentlichen**.
ref: P16_Imagen1.png | compact
2. Im Publikationsformular definieren Sie den **Datumsbereich**.
3. Fügen Sie ein weiteres **Datumsbereiche** hinzu, wenn Sie es betrachten und für andere nicht ausgewählte Tage posten (optional).
ref: P16_Imagen2.png | compact(x12)
4. Prüfen Sie, ob die Daten sinnvoll sind für:
   1. der Bühnen-Junge,
   2. die betreffende(n) Leitung(en),
   3. Und das echte Bedienfenster, das Sie decken wollen.
5. Bestätigen Sie, dass Sie einen Bereich nicht zu weit aus Versehen verlassen.
6. Sollte das Szenario nur in kurzer Zeit angewendet werden, begrenzt es das Fenster genau.
7. Bestätigt die Veröffentlichung für das gewählte Datum/den gewählten Bereich/en.

Fragen Sie sich für den Referenzfall:
1. Bezieht sich die Veröffentlichung genau auf die Arbeitstage, die ich umsetzen möchte?
2. Vermeide ich es, mehr Tage zu veröffentlichen, als nötig ist?
3. Entspricht die Lösung wirklich den ausgewählten Daten?

Wenn Sie diesen Abschnitt beenden, sollten Sie ein klares, kontrolliertes Zeitfenster für die Implantation haben.

## Bestätigung der Veröffentlichung und Änderung des Szenariostatus

Nach der Auswahl des Zeitbereichs müssen Sie die Veröffentlichungsaktion bestätigen. An diesem Punkt hört die Lösung auf, nur ein validiertes Szenario zu sein und wird im Kalender einsatzbereit.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Sie haben die Daten bereits richtig ausgewählt.
2. Sie haben das validierte Szenario bereits überprüft.
3. Sie sind bereits bereit für die Lösung, um in ihrem Lebenszyklus voranzukommen.

Zur Veröffentlichung des Szenarios:
1. Überprüfen Sie die Zusammenfassung der Veröffentlichungen zum letzten Mal.
2. Bestätigt:
   1. Name der Bühne,
   2. den Zeitbereich,
   3. und den operativen Kontext, auf den sie Anwendung finden wird.
3. Führen Sie die Aktion **Veröffentlichen** aus.
4. Überprüfen Sie, ob sich der Bühnenstatus auf **Veröffentlichung** ändert, während das System die Implantation verarbeitet.
5. Warten Sie, bis der Prozess vorbei ist.
6. Überprüfen Sie, ob sich der Endzustand der Lösung auf **Veröffentlicht** ändert.
ref: P16_Imagen3.png | compact
7. Wenn sich der Zustand nicht wie erwartet ändert, überprüfen Sie, ob es eine technische Inzidenz oder ein Problem mit der Förderfähigkeit des Szenarios gab.

Beenden Sie die Veröffentlichung für den Referenzfall erst, wenn Sie Folgendes angeben können:
1. Die L1-Szenario-Lösung ist bereits aus **Validierung** herausgekommen.
2. Die Plattform bearbeitete die Publikation.
3. Die finale Zustandslösung ist **Veröffentlicht**.

Wenn Sie diesen Abschnitt beenden, sollten Sie ein Szenario bereits im Betriebskalender für den ausgewählten Zeitraum implantiert haben.

## Überprüfung, dass die veröffentlichte Lösung in Kraft ist

Nach der Veröffentlichung müssen Sie überprüfen, ob die aktive Lösung wirklich die richtige ist. Publishing sollte kein blinder Schritt sein. Sie sollten in der Lage sein zu überprüfen, welches Szenario für die gewählten Daten gültig war und die Rückverfolgbarkeit auf der implementierten Lösung zu halten.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Die Szenariolösung hat bereits den **Veröffentlicht**-Status erreicht.
2. Du weißt, was da drin ist.
3. Sie wissen, welcher Dienst oder welche Leitung von der Veröffentlichung betroffen sein sollte.

Zur Überprüfung der Implementierung der Lösung:
1. Geh zurück zum Hauptszenario-Tisch.
2. Filtern oder überprüfen Sie die Szenarien nach Status.
3. Bestätigt, dass die veröffentlichte Szenariolösung als **Veröffentlicht** erscheint.
4. Überprüfen Sie Ihre Bewerbungstermine, wenn die Ansicht dies erlaubt.
5. Überprüfen Sie, ob Sie dieses Szenario nicht mit einem anderen validierten verwechseln, aber nicht implantiert.
6. Wenn Ihr interner Prozess dies erfordert, registrieren Sie sich oder kommunizieren Sie, dass diese Version bereits die aktuelle Betriebslösung ist.
7. Sie behält den Namen, die Beschreibung und den Zeitraum als Rückverfolgbarkeitsgrundlage für die anschließende Prüfung.

Für den Referenzfall stellen Sie sicher, dass
1. Das veröffentlichte Szenario entspricht L1 praktikabel.
2. Die Termine entsprechen dem Zeitraum, den Sie umsetzen wollten.
3. Kein anderes Szenario wurde versehentlich aktiviert.

Wenn Sie diesen Abschnitt beenden, sollten Sie sicher sein, welche Lösung vorhanden war und für welchen genauen Zeitraum.

## Beibehaltung der Rückverfolgbarkeit und Vorbereitung der nächsten Iteration

Sobald das Szenario veröffentlicht ist, verschwindet das Werk nicht: es verändert den Fokus. Von hier aus kann die implementierte Lösung zum Referenz für Audit, Vergleich oder zukünftige Iteration werden. Es ist nicht ratsam, ohne Kontrolle ein bereits veröffentlichtes Szenario wiederzuverwenden, um strukturelle Veränderungen zu durchlaufen; am sichersten ist es, eine neue Iteration zu erstellen, wenn Sie eine Verbesserung oder eine Variante vorschlagen müssen.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Das Szenario ist bereits veröffentlicht.
2. Es ist klar, welchen Zeitbereich er abdeckt.
3. Sie wissen, ob die nächste Sache sein wird, die Ergebnisse zu prüfen oder eine neue Iteration vorzubereiten.

Beibehaltung der Rückverfolgbarkeit nach Veröffentlichung:
1. Es bewahrt das veröffentlichte Szenario mit einem ausreichend klaren Namen und Beschreibung.
2. Verwenden Sie den **Veröffentlicht**-Status als Referenz, um ihn von Szenarien in Entwurf, Berechnung oder Validierung zu unterscheiden.
3. Wenn Sie eine Verbesserung vorschlagen müssen, erstellen Sie ein neues Szenario, anstatt die historische Logik des implantierten Szenarios zu verändern.
4. Wenn Ihr Team mit einer späteren Revision arbeitet, verwenden Sie diese veröffentlichte Version als Vergleichsbasis.
5. Halten Sie eine interne Aufzeichnung von:
   1. was veröffentlicht wurde,
   2. als sie veröffentlicht wurde,
   3. und für welche Daten es gültig war.

Für den Referenzfall, beenden Sie diesen schnellen Start nur, wenn Sie sagen können:
1. Die L1-Lösung ist bereits veröffentlicht.
2. Sie wissen genau, wann es in Kraft trat.
3. Sie können diese veröffentlichte Version von jeder zukünftigen Iteration unterscheiden.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine veröffentlichte, rückverfolgbare und fertige Lösung haben, um als operative Referenz oder als Ausgangspunkt für eine neue Iteration zu dienen.

## Zusätzliche Messwerte

- [Schaffung einer neuen Iteration des Szenarios aus einer veröffentlichten Lösung](iteracion-del-escenario)
