---
title: Der erste Calculus von Scheduling läuft und validiert
shortTitle: Berechnen und validieren
intro: Erfahren Sie, wie Sie die erste Kalkulation von Scheduling durchführen, den
  Lebenszyklus der Phase überprüfen, die vorbereitete Lösung validieren und das Szenario
  für die Veröffentlichung oder das anschließende Audit bereit lassen.
contentType: how-tos
versions:
- '*'
---
## Berechnung des Szenarios

Nachdem Sie das Szenario mit dem validierten Angebot, den korrekten Matrizen und den Modellen der Fahrzeugregeln und -kurven bereits erstellt und konfiguriert haben, ist der nächste Schritt, die Berechnung durchzuführen.

In dieser Phase nimmt der Motor:
1. das validierte Angebot,
2. aktive Regeln,
3. die Logistik von Leerfahrten,
4. und die Struktur der Bühne,

programmierbare logische Aufgaben zu erstellen.

Verwenden Sie diesen Schnellstart, wenn Sie das geplante Szenario bereit haben und die erste berechnete Lösung vor der Überprüfung und Validierung erhalten müssen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Bühne auf P14 gelegt.
2. Sie haben bereits den korrekt validierten Service ausgewählt.
3. Sie haben bereits die richtige leere Reisematrix zugewiesen.
4. Sie haben bereits das richtige Modell der Fahrzeugregeln gewählt.
5. Sie haben bereits das richtige Modell für Schichtregeln gewählt.
6. Sie haben bereits den Classic Motor und die Berechnungsparameter eingerichtet.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde die erste Berechnung des geplanten Szenarios auf Linie L1 durchführen, überprüfen, ob die Lösung konsistent ist und das Szenario zur Validierung bereit lassen.**

Um die Szenarioberechnung durchzuführen:
1. Öffnen Sie das Szenario, das Sie berechnen möchten.
2. Überprüfen Sie ein letztes Mal, dass die Bühnenkarten korrekt sind.
3. Starten Sie die Aktion **Berechnen** oder **Berechnung starten**.
ref: P15_Imagen1.png | compact(3x)
ref: P15_Imagen2.png | compact
4. Überprüfen Sie, ob sich der Bühnenstatus von **Ausstehende Lösung** auf **Berechnung der Lösung** ändert.
ref: P15_Imagen3.png | full
ref: P15_Imagen4.png | full
5. Warten Sie, bis der Motor den Prozess beendet.
ref: P15_Imagen5.png | compact(1x18)
6. Überprüfen Sie den neuen Bühnenzustand.
7. Wenn die Berechnung richtig schlussfolgert, bestätigt sie, dass das Szenario auf **Zubereitete Lösung** übergeht.
ref: P15_Imagen6.png | compact(x7)
8. Wenn die Lösung manuelle Anpassungen erfordert, geben Sie zur Verfeinerung den **Bearbeiten**-Status ein.
9. Gibt der Motor keine gültige Lösung zurück, überprüfen Sie erneut:
   1. das Angebot,
   2. die leere Reisematrix,
   3. die Regeln,
   4. und die Parameter des Szenarios.

Im Referenzfall bestätigt sie, dass
1. Das L1-Szenario kommt aus dem Ausgangszustand.
2. Der Motor schließt die Berechnung ohne Blockierung ab.
3. Das Szenario kommt zu einer vorbereiteten Lösung oder einer vernünftigen Bearbeitungsphase.

Darüber hinaus, falls die Art des Szenarios gewählt ist für Fahrzeuge und Verschiebungen, können Sie die Lösung aus Verschiebungen aus der Personalansicht generiert sehen.
ref: P15_Imagen12.png | compact

Wenn Sie diesen Abschnitt beenden, sollten Sie eine erste berechnete Lösung oder ein klares Signal haben, welches Teil der Parametrierung korrigiert werden muss.

## Überprüfung des Zustands des Szenarios und des Ergebnisses der Berechnung

Nachdem Sie die Berechnung durchgeführt haben, müssen Sie verstehen, an welchem Punkt im Lebenszyklus das Szenario geblieben ist. Dies ist wichtig, weil jeder Staat eine andere betriebliche Bedeutung hat und Ihnen sagt, welche Aktionen Sie als nächstes tun können.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Du hast schon die Rechnung geführt.
2. Sie kennen den Namen der Bühne, die Sie überprüfen.
3. Sie wissen, ob Sie eine fertige Lösung oder eine Verfeinerungsphase erwartet haben.

Um den Status und das Ergebnis zu überprüfen:
1. Gehen Sie zurück zum Hauptszenario Tisch oder bleiben Sie auf der Bühne.
2. Überprüfen Sie den aktuellen Zustand.
3. Er interpretiert den Zustand nach dieser Logik:
   1. **Ausstehende Lösung**: Das Szenario wurde noch nicht berechnet.
   2. **Berechnung der Lösung**: Der Motor verarbeitet die Lösung.
   3. **Bearbeiten**: Ein Benutzer stellt die Lösung manuell ein.
   4. **Zubereitete Lösung**: Die Berechnungs- oder Bearbeitungsphase ist beendet und das Szenario ist zur Revision bereit.
   5. **Validierung**: Die Lösung wurde bereits genehmigt und blockiert.
   6. **Veröffentlichung**: Die Lösung wird in den Betriebskalender integriert.
   7. **Veröffentlicht**: Die Lösung wurde bereits in der Operation implantiert.
4. Wenn das Szenario in **Zubereitete Lösung** ist, fahren Sie mit der Konsistenzüberprüfung fort.
5. Wenn das Szenario in **Bearbeiten** ist, beenden Sie zuerst die notwendigen manuellen Einstellungen.
6. Wenn das Szenario noch zu lange in **Berechnung der Lösung** ist, überprüfen Sie, ob es eine zu restriktive technische Inzidenz oder Konfiguration gab.

Für den Referenzfall sollten Sie erwarten, dass das Szenario mindestens in folgenden Bereichen endet:
1. **Zubereitete Lösung**, wenn Sie die Struktur nicht mehr berühren müssen,
2. oder **Bearbeiten**, wenn Sie noch manuell verfeinern möchten.

Wenn Sie diesen Abschnitt beenden, sollten Sie klar verstehen, was der aktuelle Stadium Zustand bedeutet und welche Aktion folgt.

## Überprüfung von KPI, Fehlern und Konsistenz vor der Validierung

Bevor Sie das Szenario validieren, müssen Sie es überprüfen. Validierung ist kein einfacher administrativer Klick. Es ist die formale Zulassungstür, die die Lösung einfriert und versehentliche Folgeänderungen verhindert.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Die Bühne ist bereits in **Zubereitete Lösung** oder Sie haben die **Bearbeiten** Phase beendet.
2. Nach der Validierung ist das Szenario nicht mehr editierbar.
3. Sie sind bereit für eine abschließende Überprüfung vor der Genehmigung.

Um die Lösung vor der Validierung zu überprüfen:
1. Sie öffnet die Bühne in ihrem gegenwärtigen Zustand.
2. Überprüfen Sie die verfügbaren KPIs.
ref: P15_Imagen7.png | full
3. Prüfen Sie auf sichtbare Fehler, Warnungen oder Widersprüche.
ref: P15_Imagen8.png | compact(x7)
4. Verwenden Sie die verfügbaren Filter, um die Lösung aus verschiedenen Blickwinkeln zu prüfen.
ref: P15_Imagen9.png | compact(3x)
5. Überprüft, ob die Kartierungen und die Szenariostruktur einen operativen Sinn ergeben.
6. Wenn Sie ein kleines Problem erkennen und das Szenario noch editierbar ist, korrigieren Sie es, bevor Sie fortfahren.
7. Wenn Sie ein großes Problem erkennen, nachdem Sie es später blockiert haben, müssen Sie es mit entsprechenden Berechtigungen freischalten oder zu einem editierbaren Szenario zurückkehren.

Für den Referenzfall stellen Sie sicher, dass
1. Die L1-Lösung KPIs sind vernünftig.
2. Es gibt keine schwerwiegenden Fehler, die die Lösung ungültig machen.
3. Die Lösung kann nun von der technischen Überprüfung zur formalen Genehmigung übergehen.

Wenn Sie diesen Abschnitt beenden, sollten Sie genug Vertrauen haben, um das Szenario zu validieren.

## Validierung der Stufe und Blockierung der Lösung

Nun können Sie den **Validierung des Szenarios** ausführen. Dieser Schritt markiert den offiziellen Abschluss der Berechnungs- und Bearbeitungsphase. Ab hier wird die Lösung geschützt, das Szenario wird nicht mehr editierbar und kann nicht mehr neu berechnet werden, solange es validiert bleibt.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Die Bühne ist auf **Zubereitete Lösung**.
2. Sie haben den KPI-Bericht und Fehler abgeschlossen.
3. Sie müssen keine manuellen Anpassungen mehr vornehmen, bevor Sie die Lösung genehmigen.

Zur Validierung des Szenarios:
1. Öffnen Sie aus der Szenariotabelle das Aktionsmenü der Bühne.
2. Wählen Sie **Validierung**.
3. Wenn Sie es lieber von der Bühne aus tun, verwenden Sie die **Validierung**-Taste am oberen Rand des Bildschirms.
ref: P15_Imagen10.png | compact(2x)
4. Bestätigen Sie die Validierung, wenn das System sie verlangt.
5. Überprüfen Sie, ob sich der Status der Bühnenlösung auf **Validierung** ändert.
ref: P15_Imagen11.png | compact(2x)
6. Prüfen Sie das:
   1. das Szenario ist nicht mehr editierbar,
   2. kann nicht mehr neu berechnet werden,
   3. und ihre wichtigsten Daten sind geschützt.
7. Wenn Sie nach der Validierung einen Last-Minute-Fehler entdecken, verwenden Sie den Freischaltstrom nur mit den richtigen Berechtigungen.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Die L1-Lösung wurde bereits überprüft.
2. Die Szenariolösung änderte sich in **Validierung**-Status.
3. Die Organisation kann dieses Szenario bereits als genehmigte Version behandeln.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine formal genehmigte und blockierte Lösung haben, um versehentliche Änderungen zu vermeiden.

## Lassen Sie das Szenario bereit für die Veröffentlichung oder anschließende Prüfung

Nach der Validierung ist das Szenario für zwei Wege bereit:
1. **Veröffentlichung**, wenn Sie es zum tatsächlichen Betriebskalender bringen möchten,
2. oder **Prüfung**, wenn Sie es noch vor der Veröffentlichung überprüfen müssen.

An dieser Stelle bleibt das Szenario eine anerkannte und geschützte Lösung. Sie können es noch konsultieren, KPI überprüfen, Informationen filtern und als Referenz verwenden, aber Sie sollten es nicht mehr als Arbeitsentwurf behandeln.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Die Bühnenlösung befindet sich bereits im **Validierung**-Status.
2. Sie kennen den Unterschied zwischen Validierung und Veröffentlichung.
3. Sie wissen, ob Ihr nächster Schritt darin besteht, die Lösung zu implantieren oder weiter zu auditieren.

Um die Bühne für den nächsten Schritt zu verlassen:
1. Überprüfen Sie die Szenariotabelle und bestätigen Sie den **Validierung**-Status.
2. Wenn der Plan bereits für die Umsetzung genehmigt ist, bereiten Sie den **Veröffentlichen**-Flow vor.
3. Wenn Sie noch interne Überprüfung benötigen, halten Sie das validierte Szenario als Prüfungsgrundlage.
4. Verwenden Sie Filter, Informationssymbole und staatliche Überprüfung, um zu kontrollieren, welche Szenarien noch ausstehen, validiert oder bereits veröffentlicht werden.
5. Wenn Sie eine neue Version iterieren müssen, erwägen Sie, das Szenario zu duplizieren, anstatt eine bereits genehmigte zu ändern.

Für den Referenzfall, beenden Sie diesen schnellen Start nur, wenn Sie sagen können:
1. Das L1-Szenario wurde bereits berechnet.
2. Die Lösung wurde überprüft.
3. Die Bühnenlösung ist **Validierung**.
4. Der nächste Schritt ist nicht mehr zu berechnen, sondern zu entscheiden, ob es veröffentlicht oder geprüft wird.

Wenn Sie diesen Abschnitt beenden, sollten Sie ein berechnetes, überarbeitetes und validiertes Szenario haben, bereit für die Produktion oder die endgültige Revision.

## Zusätzliche Messwerte

- [Veröffentlichung des Szenarios zu bestimmten Terminen](publicacion-del-escenario)
