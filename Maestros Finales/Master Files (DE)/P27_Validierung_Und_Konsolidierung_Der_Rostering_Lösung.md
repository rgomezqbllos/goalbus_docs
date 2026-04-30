---
title: Validierung und Konsolidierung der Rostering-Lösung
shortTitle: Protokollierung bestätigen
intro: Erfahren Sie, wie Sie die Überprüfung der Rostering-Lösung abschließen, die
  Personalzuweisung validieren, wenn sie bereits betriebssicher ist, und sie als Ready-Referenz
  für den späteren Einsatz oder die Integration in den Betrieb zu konsolidieren.
contentType: how-tos
versions:
- '*'
---
## Bestätigung, dass die Lösung zur Validierung bereit ist

Nach Überprüfung der Reichweite, der Konflikte und der Machbarkeit soll im nächsten Schritt entschieden werden, ob die Rostering-Lösung bereits als stichhaltig genug angesehen werden kann. Validierung bedeutet nicht nur eine administrative Freigabe. Es bedeutet, dass die Zuordnung von Personal bereits konsequent, verständlich und als genehmigte Basis nutzbar ist.

Verwenden Sie diesen Schnellstart, wenn Sie bereits die Berechnung des Rasters durchgeführt haben, dessen Ergebnis analysiert haben und die Lösung formal schließen müssen, bevor Sie mit der Konsolidierung fortfahren.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Rostering-Berechnung auf P25 durchgeführt.
2. Sie haben bereits Konflikte, Berichterstattung und Lebensfähigkeit bei P26 überprüft.
3. Sie haben bereits die Hauptprobleme korrigiert oder verstehen bereits, warum die verbleibenden Konflikte akzeptabel sind.
4. Sie wissen, welche konkrete Lösung Sie validieren werden.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde die Rostering-Lösung der Linie L1 validieren, weil die Zuordnung die Arbeit bereits zuverlässig genug abdeckt und ich sie als genehmigte Referenz konsolidieren möchte.**

Um zu bestätigen, dass die Lösung zur Validierung bereit ist:
1. Öffnen Sie die Rostering-Lösung, die Sie als Referenz verwenden.
2. Überprüfen Sie die Job-Berichterstattung ein letztes Mal.
3. Bestätigt, dass die Hauptkonflikte bereits gelöst oder diagnostiziert wurden.
4. Überprüfung, ob die sich daraus ergebende Zuteilung mit folgenden Grundsätzen vereinbar ist:
   1. Die Regeln von Rostering,
   2. tatsächliche Verfügbarkeit des Personals,
   3. operative Abordnung,
   4. und die von Scheduling geerbte Lösung.
5. Wenn Sie ein ungelöstes Hauptproblem erkennen, validieren Sie die Lösung noch nicht.
6. Wenn die Basis bereits stabil ist, gehen Sie weiter zum Validierungsschritt.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Die Arbeit von L1 ist bereits abgedeckt oder die restlichen Lücken werden verstanden.
2. Die Lösung ist operativ vertretbar.
3. Sie müssen keine strukturellen Änderungen mehr vornehmen, bevor Sie sie weitergeben.

Wenn Sie diesen Abschnitt beenden, sollten Sie klar sein, ob die Lösung bereits eine formale Validierung verdient.

## Durchführung der Validierung der Personallösung

Sobald die Lösung stabil genug ist, müssen Sie die Validierung durchführen. Dieser Schritt markiert das Schließen der Berechnungs- und Überprüfungsphase für das Rostering und verwandelt die Lösung in eine genehmigte Referenz innerhalb des Workflows.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits entschieden, dass die Lösung gültig ist.
2. Sie müssen die Regeln nicht mehr neu berechnen oder anpassen, bevor Sie passieren.
3. Sie wissen, dass Validierung bedeutet, die Lösung als genehmigte Referenz einzufrieren.

Zur Validierung der Rostering-Lösung:
1. Öffnen Sie aus der Sicht der Lösung oder aus der Haupttabelle das entsprechende Aktionsmenü.
ref: P27_Imagen1.png | full
2. Wählen Sie die Aktion **Validierung** aus.
3. Überprüfen Sie die endgültige Zusammenfassung der Lösung vor der Bestätigung.
4. Bestätigen Sie die Validierung, wenn das System sie verlangt.
5. Überprüft, ob der Status der Lösung den entsprechenden Zulassungsstatus ändert.
6. Prüfen Sie, ob die Lösung nicht mehr als vorläufige Version der Arbeit behandelt wird.
7. Wenn Ihr Stream bestimmte Berechtigungen verwendet, um zu genehmigen, bestätigen Sie, dass die Validierung korrekt aufgezeichnet wurde.

Für den Referenzfall stellen Sie sicher, dass
1. Die L1-Lösung ändert nach der Validierung den Status.
2. Das System erkennt es bereits als genehmigte Version an.
3. Die Lösung wird nicht mehr als noch offene Iteration behandelt.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine formal validierte Rostering-Lösung haben.

## Konsolidierung der Lösung als operative Referenz

Nach der Validierung müssen Sie die Lösung konsolidieren. Konsolidieren bedeutet, diese Version als genehmigte Referenz für die nächste Stufe des Prozesses zu behandeln. Von hier aus sollte die Lösung nicht mehr als Test, sondern als ernsthafte und rückverfolgbare Basis für die Personalzuweisung verwaltet werden.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Die Lösung ist bereits validiert.
2. Sie wissen, ob dies die aktuelle Referenz oder eine genehmigte Version bis zu einer späteren Verwendung sein wird.
3. Sie können nun eine zugelassene Lösung von einer geprüften Lösung unterscheiden.

Um die validierte Lösung zu konsolidieren:
1. Überprüfen Sie den Namen und die Beschreibung der Lösung.
2. Falls erforderlich, aktualisieren Sie die Beschreibung, um Folgendes klarzustellen:
   1. welchen Kontext er abdeckt,
   2. welche Periode sie darstellt,
   3. und warum es genehmigt wurde.
3. prüft, ob die validierte Lösung eindeutig von früheren Entwürfen, Tests oder Iterationen zu unterscheiden ist.
4. Wenn Ihr interner Prozess es erfordert, notieren Sie, dass diese Version die Referenz für den nächsten Schritt wird.
5. Es behält frühere Versionen als historisch, aber vermeidet, sie als gleichwertig mit der genehmigten Lösung zu behandeln.

Für den Referenzfall stellen Sie sicher, dass
1. Die validierte L1-Lösung unterscheidet sich deutlich von Tests oder Zwischenversionen.
2. Das Team kann es als die richtige Referenz identifizieren.
3. Die Rückverfolgbarkeit der Genehmigung ist eindeutig.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine genehmigte und erkennbare Lösung als seriöse Rostering Referenz haben.

## Überprüfung, was blockiert ist und was eine neue Iteration erfordern würde

Bevor Sie schließen, müssen Sie klar sein, dass die Validierung einer Lösung nicht bedeutet, dass die Möglichkeit der Verbesserung sie verschwindet. Es bedeutet, dass diese bestimmte Version bereits geschlossen wurde. Wenn Sie eine Verbesserung oder eine Hintergrundanpassung später benötigen, wird die richtige Sache sein, eine neue Iteration oder eine neue Arbeitslösung zu öffnen, nicht die genehmigte Version zu deaktivieren.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Die Lösung ist bereits validiert.
2. Du weißt, welche Teile des Jobs geschlossen wurden.
3. Es ist Ihnen klar, dass zukünftige Verbesserungen als neue Iterationen zurückverfolgt werden müssen.

Um die Governance nach der Validierung deutlich zu machen:
1. Behandeln Sie die validierte Lösung als geschlossene Referenz.
2. Vermeiden Sie es direkt zu ändern, als ob es noch ein Entwurf wäre.
3. Wenn Sie eine zukünftige Verbesserung bemerken:
   1. erzeugt eine neue Iteration,
   2. oder eröffnet einen neuen Berechnungs- und Überprüfungszyklus.
4. Es behält die validierte Version als einen Punkt des historischen Vergleichs.
5. Wenn Ihr Team Entscheidungen prüfen muss, verwenden Sie diese Lösung als genehmigte Basislösung.

Beenden Sie diesen Abschnitt für den Referenzfall nur, wenn Sie Folgendes angeben können:
1. Die validierte Version von L1 ist nun geschlossen.
2. Jede künftige Verbesserung wird durch eine neue Iteration erfolgen.
3. Die Rückverfolgbarkeit zwischen Berechnung, Überprüfung und Genehmigung bleibt erhalten.

Wenn Sie diesen Abschnitt beenden, sollten Sie sich darüber im Klaren sein, was es bedeutet, eine Lösung zu konsolidieren und wie Sie vermeiden, die Kontrolle über die Versionen zu verlieren.

## Die Lösung für die nächste Stufe des Prozesses bereit zu lassen

Der letzte Schritt ist die mentale Vorbereitung des Übergangs. Von hier aus befindet sich die Rostering-Lösung nicht mehr in der technischen Berechnungsphase, sondern befindet sich in der Phase des Einsatzes, der Konsolidierung oder der Übertragung auf den nächsten geeigneten Betriebsprozess.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie haben die Lösung bereits validiert.
2. Sie haben sie bereits als konsolidierte Referenz behandelt.
3. Sie wissen, ob der nächste Schritt sein wird:
   1. sie zu kommunizieren,
   2. sie zu integrieren,
   3. sie zu prüfen,
   4. oder bereiten Sie eine neue zukünftige Iteration vor.

Um diesen Schnellstart richtig zu schließen:
1. Überprüfen Sie den Zustand der Lösung ein letztes Mal.
2. Sie bestätigt, dass dies keine vorläufige Berechnung mehr ist.
3. Überprüfen Sie, ob der Computer diese Version als genehmigt identifizieren kann.
4. Wenn Ihr Prozess es erfordert, notieren Sie den Übergang zur nächsten Betriebsebene.
5. Sie behält die Lösung als stabile Referenz für den zukünftigen Vergleich.

Für den Referenzfall, beenden Sie diesen schnellen Start nur, wenn Sie sagen können:
1. Die L1-Rostering-Lösung ist bereits validiert.
2. Sie wurde bereits als genehmigte Referenz konsolidiert.
3. Der nächste Schritt ist nicht mehr zu berechnen, sondern diese Basis auf kontrollierte Weise zu nutzen, zu überprüfen oder zu entwickeln.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine validierte, konsolidierte und fertige Rostering-Lösung haben, um als stabile Prozessreferenz zu dienen.

## Zusätzliche Messwerte

- [Verwalten von Versionen und Iterationen der Rostering-Lösung](P28_Gestionando_versiones_e_iteraciones_de_la_solucion_de_Rostering.md)
