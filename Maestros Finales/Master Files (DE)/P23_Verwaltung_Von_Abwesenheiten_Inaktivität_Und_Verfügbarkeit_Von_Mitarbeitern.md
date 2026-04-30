---
title: Verwaltung von Abwesenheiten, Inaktivität und Verfügbarkeit von Mitarbeitern
shortTitle: Persönliche Verfügbarkeit
intro: Erfahren Sie, wie Sie Abwesenheiten, Inaktivitäts- und Verfügbarkeitsbeschränkungen
  registrieren können, so dass Rostering nur wirklich förderungsberechtigten Personen
  zuweist und nicht versucht, die Arbeit mit nicht verfügbaren Treibern abzudecken.
contentType: how-tos
versions:
- '*'
---
## Den Unterschied zwischen Abwesenheit, Inaktivität und Verfügbarkeit verstehen

Vor der Berechnung der Rostering, müssen Sie steuern, welche Menschen wirklich zur Verfügung stehen, um zu arbeiten. In dieser Ebene ist es nicht mehr genug für den Fahrer zu existieren, werden an den richtigen Kontext und haben anwendbare Regeln. Sie müssen auch das System sagen, wenn diese Person:
1. verfügbar ist,
2. abwesend ist,
3. Es ist inaktiv.
4. oder über eine teilweise oder eingeschränkte Verfügbarkeit verfügt.

Verwenden Sie diesen Schnellstart, wenn Sie bereits die Treiber geladen haben, überprüfen Sie ihre operative Abordnung und bereiten Sie die Rostering-Regel-Basis vor, und Sie müssen verhindern, dass die Berechnung versucht, Arbeit für nicht förderungsberechtigte Menschen zuzuweisen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben bereits Treiber auf P20 geladen und überprüft.
2. Sie haben bereits seine operative Abordnung nach P21 bestätigt.
3. Sie haben bereits Rosterings Regelbasis in P22 definiert.
4. Es ist Ihnen klar, welche Mitarbeitergruppe an der Berechnung teilnehmen wird.
5. Sie wissen, ob Sie in Ihrer Operation Ferien, Verluste, Genehmigungen, teilweise Nichtverfügbarkeiten oder nicht-operative Zustände registrieren müssen.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde Fehlzeiten, Inaktivitäts- und Verfügbarkeitsbeschränkungen für Fahrer aufzeichnen, die die Linie L1 abdecken, um sicherzustellen, dass Rostering nur wirklich förderungsberechtigten Personen Arbeit zuweist.**

Um diese Konzepte richtig zu verstehen:
1. Verwenden Sie einen **Abwesenheit**, wenn die Person existiert und zum Kollektiv gehört, aber für einen bestimmten Zeitraum nicht verfügbar ist.
2. Verwenden Sie einen **Nichterwerbstätigkeit**, wenn die Person für einen strukturierteren Zeitraum außer Betrieb gelassen werden muss oder nicht an der Berechnung teilnehmen darf.
3. Verwenden Sie eine **Beschränkung der Verfügbarkeit**, wenn die Person arbeiten kann, aber nicht zu allen Zeiten oder nicht unter allen Bedingungen.
4. Mischen Sie diese Konzepte nicht so, als wären sie dieselben.
5. Verwenden Sie diese Leseregel:
   1. **Abwesenheit** = kann nicht für einen bestimmten Zeitraum arbeiten,
   2. **Nichterwerbstätigkeit** = sollte in diesem Zusammenhang oder in diesem Zeitraum nicht als Betriebsressource behandelt werden —
   3. **eingeschränkte Verfügbarkeit** = kann funktionieren, aber mit Grenzen.

Zur Erfassung der Arten von Abwesenheiten, Inaktivitäten oder Nichtverfügbarkeiten:
1. In GoalBus müssen Sie **Einstellungen** > **Personal** > **Einstellungen für die Abwesenheit** öffnen.
ref: P23_Imagen1.png | compact
2. Prüfen Sie, ob alle Arten von Abwesenheit, die Sie benötigen, erstellt werden.
3. Wenn es keine Abwesenheit gibt oder Sie eine neue erstellen müssen, klicken Sie auf die Schaltfläche **Neue Abwesenheit erstellen**.
ref: P23_Imagen2.png | compact(2x)
4. Um einen neuen Typ der Abwesenheit zu erstellen, müssen folgende Felder ausgefüllt werden:
   1. **Name der Abwesenheit**: Name des zu erstellenden Abwesenheitstyps.
   2. **Kurzbezeichnung**: für kompakte Ansichten.
   3. **Zielfahrer-ID**: interner Code, wenn Sie mit Integrationen arbeiten.
   4. **Abwesenheitskategorie**: Es kann **Rein**, **Frei** oder **Arbeit** sein. Je nach Ihrer Wahl sollte eine Dauer (**Zeit** oder **Ganzer Tag**) einer Dauer von **Arbeitszeit** oder **Höchsttage** zugewiesen werden.
   5. **Förderfähigkeit für die Zuweisung von Arbeiten**: Ob Sie den Treiber wählen können, um Ihnen Arbeit zuzuweisen oder nicht, trotz Ihrer Abwesenheit.
   6. Wählen Sie, ob diese Art der Abwesenheit **Vom Fahrer angefordert** ist.
5. Sparen Sie sich die neue Art der Abwesenheit.
ref: P23_Imagen3.png | compact(x10)
6. Sie zeichnet weiterhin alle notwendigen Arten von Abwesenheit auf.
7. Bestätigen Sie, dass Sie alle Arten von Abwesenheit für Ihre Planung benötigt haben.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine klare Ansicht darüber haben, welche Art von Abwesenheiten Sie in Ihrer Röstplanung verwenden können und dass Sie in der Lage sein werden, unterschiedlichen Treibern zuzuordnen. fileciteturn22file3L1-L20 fileciteturn22file2L1-L18

## Aufzeichnung geplanter Fehlzeiten des Fahrers

Geplante Abwesenheiten sind einer der ersten Elemente, die vor der Berechnung des Dienstplans geladen werden. Hier kommt Urlaub, Genehmigungen, Behinderungen, Lizenzen oder jede andere Zeit, in der eine Person keinen Job erhalten sollte.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie wissen, welche Treiber innerhalb des Berechnungshorizonts Abwesenheiten haben werden.
2. Sie kennen die genauen oder ungefähren Daten dieser Abwesenheiten.
3. Sie wollen das System eindeutig verlassen, an welchen Tagen eine Person nicht benutzt werden kann.
4. Sie haben bereits alle notwendigen Arten von Abwesenheit geschaffen.

Zum Aufzeichnen von Abwesenheiten aus dem Fahrerprofil:
1. In GoalBus müssen Sie **Einstellungen** > **Personal** > **Fahrerverwaltung** öffnen.
ref: P23_Imagen4.png | compact
2. Klicken Sie auf die Schaltfläche in der oberen Leiste, um die Abwesenheitsdaten zu laden.
ref: P23_Imagen5.png | compact(3x)
3. Wählen Sie die Aktion **Fehlzeiten des gebührenpflichtigen Personals** aus.
ref: P23_Imagen6.png | compact
4. Laden Sie die Abwesenheits-Datei im Pop-up-Fenster. In diesem Fenster können Sie das Format der Abwesenheits-Datei überprüfen, entweder indem Sie die Anweisungen lesen oder eine Beispielvorlage herunterladen.
ref: P23_Imagen7.png | full
5. Bestätigt das Laden der Datei.
6. Behalten Sie das Protokoll.
7. Jetzt können Sie die geladenen Abwesenheiten im Profil jedes Treibers überprüfen.

Für den Referenzfall könnte eine Mindestlogik sein:
1. Fahrer A: Urlaub von 10 bis 20
2. Fahrer B: Genehmigung am 14.
3. Fahrer C: Invalidität für eine bestimmte Woche

Wenn Sie diesen Abschnitt beendet haben, sollten Sie die Hauptausfälle, die die Berechnung der Liste beeinflussen, aufgezeichnet haben.

## Prüfen, dass Rostering die tatsächliche Berechtigung bereits richtig sieht

Der letzte Schritt besteht darin, zu bestätigen, dass die Kombination zwischen Fahrern, Abordnung, Regeln und Verfügbarkeit bereits die Realität der Berechnung widerspiegelt. Ziel ist es hier sicherzustellen, dass Rostering nicht versucht, abwesende, inaktive oder schlecht eingeschränkte Personen zuzuweisen, noch wird es Menschen, die förderfähig sein sollten, auslassen.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie haben bereits relevante Abwesenheiten registriert.
2. Sie haben bei Bedarf bereits Teilverfügbarkeiten konfiguriert.
3. Sie wissen, welches Kollektiv die folgende Berechnung verwendet.

Um zu überprüfen, ob die tatsächliche Verfügbarkeit bereits gut modelliert ist:
1. Gehen Sie zurück zur allgemeinen Liste der Fahrer.
2. Überprüfen Sie mehrere repräsentative Profile des Kollektivs.
3. bestätigt, dass abwesende Personen ihre Fristen korrekt registriert haben.
4. Bestätigt, dass Teilbeschränkungen nicht aus Versehen als totale Abwesenheiten modelliert werden.
5. Fragen Sie sich, ob das System schon:
   1. schließen diejenigen aus, die nicht arbeiten sollten,
   2. einschließlich derjenigen, die arbeiten können,
   3. und teilweise Beschränkungen einhalten, ohne die Berechnung zu brechen.
6. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
7. Wenn die Antwort nein ist, korrigieren Sie die Aufzeichnungen, bevor Sie fortfahren.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. L1-Treiber haben ihre reale Verfügbarkeit bereits gut reflektiert.
2. Die Abwesenheiten sind geladen.
3. Inaktivität wird differenziert.
4. Teilweise Einschränkungen wurden nicht mit vollständigen Abwesenheiten verwechselt.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine hinreichend zuverlässige Verfügbarkeitsbasis haben, um zu Zuweisungen, Transfers und Abordnungsänderungen zu wechseln.

## Zusätzliche Messwerte

- [Verwaltung von Übertragungen, Zuweisungen und Abordnungsänderungen](P24_Verwaltung_Von_Übertragungen_Zuweisungen_Und_Abordnungsänderungen.md)
