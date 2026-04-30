---
title: Überprüfung des Betriebsnetzes mit Sequenzen und Schlüsselpunkten
shortTitle: Betriebsnetz
intro: Erfahren Sie, wie Sie validieren, wie sich Ihr Netzwerk wirklich im Betrieb
  verhält, Sequenzen überprüfen, Berechtigungen und Relaispunkte stoppen, bevor Sie
  zu Zeiten und Diensten wechseln.
contentType: how-tos
versions:
- '*'
---
## Überprüfung der Betriebsfolge der Strecken

Nun, da Sie bereits das Basisnetz (Stopps, Linien und Routen) erstellt haben, ist der nächste Schritt, um zu bestätigen, dass dieses Netzwerk aus operativer Sicht ordnungsgemäß funktioniert.

An diesem Punkt schaffen Sie keine Struktur mehr, Sie bestätigen, wie sie sich in der Praxis verhält.

Bevor Sie beginnen:
1. Sie haben bereits Stops, Linien und Routen auf P6 erstellt.
2. Sie haben mindestens eine Route pro Sinn.
3. Du weißt, welche Linie du vorbereitest.

Fall:
> Validierung dieser Route L1 hat eine kohärente und operative Reihenfolge vor der Festlegung von Zeiten.

Schritte:
1. Mach die Leitung auf, an der du arbeitest.
2. Zugriff auf die Routenansicht.
ref: P7_Imagen1.png | full
3. Wählen Sie einen Sinn aus.
4. Überprüfen Sie die Stoppsequenz.
5. Prüft, dass
   - Es gibt keine fehlenden Schlüsselstopps.
   - Es gibt keine unnötigen Duplikate.
   - Die Reihenfolge ist korrekt.
6. Wiederholen Sie für den anderen Sinn.

Erwartetes Ergebnis:
- Eine saubere und logische Reihenfolge, die die tatsächliche Route darstellt.

## Validierung von Stop-Genehmigungen

Nicht alle stoppt arbeiten gleich. Einige erlauben Klettern, andere niedriger, und andere beide.

Bevor Sie fortfahren:
1. Sie haben die Sequenz bestätigt.
2. Du weißt, wie jeder Stopp in der Realität funktioniert.

Schritte:
1. Innerhalb der Route, überprüfen Sie jede Haltestelle.
2. Konfigurieren Sie, wenn Sie erlauben:
   - Aufstieg
   - Nach unten
   - Beides
ref: P7_Imagen2.png | compact
3. Stellen Sie sicher, dass:
   - Terminals erlauben beides.
   - Zwischenstopps spiegeln den tatsächlichen Betrieb wider.
4. Speichern Sie die Änderungen.

Erwartetes Ergebnis:
- Jeder Stop hat ein Verhalten, das mit der Operation übereinstimmt.

## Festlegung von Relaispunkten

Die Relaispunkte sind entscheidend für Röstung und Betrieb.

Bevor Sie beginnen:
1. Sie haben bereits eine validierte Sequenz.
2. Sie wissen, wo Relais bei der eigentlichen Operation passieren.

Schritte:
1. Identifizieren stoppt, wo Fahreränderungen vorgenommen werden.
2. Markieren Sie die Stopps als Relaispunkte.
ref: P7_Imagen3.png | compact
3. Prüft, dass
   - Sie sind gut platziert.
   - Das reicht für die Operation.
4. Wache.

Erwartetes Ergebnis:
- Das Netzwerk überlegt bereits, wo Treiberänderungen vorgenommen werden können.

## Endgültige Validierung des Betriebsnetzes

Vor dem Fortschreiten:

1. Überprüfen Sie die gesamte Route noch einmal.
2. Bestätigt:
   - Genaue Reihenfolge.
   - Kohärente Genehmigungen.
   - Determinierte Relais.
3. Fragen Sie sich:
   - Könnten Sie diese Linie im wirklichen Leben betreiben?
   - Fehlt ein operatives Detail?

Wenn die Antwort ja ist, können Sie fortfahren.

## Zusätzliche Messwerte

- P8 Leeres Reisen und Reisen laden
