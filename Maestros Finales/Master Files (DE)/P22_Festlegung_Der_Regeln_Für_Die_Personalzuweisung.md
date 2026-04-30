---
title: Festlegung der Regeln für die Personalzuweisung
shortTitle: Regeln für die Aufstellung
intro: Erfahren Sie, wie Sie grundlegende und erweiterte Regeln für die Dienstordnung
  festlegen, damit die Personalzuweisung die Arbeitsgrenzen, die Eigenkapitalkriterien
  und die tatsächlichen Betriebsbeschränkungen vor der Berechnung der Personaltabelle
  einhält.
contentType: how-tos
versions:
- '*'
---
## Verstehen, was sie unter den Regeln von Rostering kontrollieren

Bevor Sie die Personalzuweisungen berechnen, müssen Sie den **Regeln für die Aufstellung** definieren, der die Zuordnung der Mitarbeiter zu den Schichten regelt. Diese Regeln bauen keine Arbeit, da dieser Schritt bereits durch Scheduling gelöst wurde. Hier steuern Sie, wie diese Arbeit unter realen Menschen geteilt wird, wobei die operativen Richtlinien, die Kriterien für die Gerechtigkeit und die Arbeitsgrenzen eingehalten werden.

Verwenden Sie diesen Schnellstart, wenn Sie bereits über eine stabile Scheduling-Lösung, eine geladene Treibervorlage und eine überarbeitete Betriebsabordnung verfügen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben den Übergang von Scheduling bei P19 bereits abgeschlossen.
2. Sie haben bereits Treiber auf P20 geladen und überprüft.
3. Sie haben bereits die operative Abordnung nach P21 bestätigt.
4. Sie sind bereits klar, welche Scheduling-Lösung als Grundlage dienen wird.
5. Sie wissen, welche kollektiven oder Gruppen von Mitarbeitern von der Berechnung betroffen sind.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde die Rostering-Regeln für die L1-Linie und ihre Fahrergruppe so konfigurieren, dass die Berechnung echte Mitarbeiter unter Einhaltung von Pausen, Arbeitslimits und Betriebskriterien zuweist.**

Um die Rolle dieser Regeln zu verstehen:
1. Es behandelt die Regeln von Rostering als Einschränkungen und Präferenzen für die Zuordnung von Menschen.
2. Verwenden Sie diese Regeln, wenn Sie kontrollieren möchten:
   1. Pausen,
   2. Arbeitszeit,
   3. wöchentliche Muster,
   4. Arbeitsgruppe,
   5. Kombinationen,
   6. und andere Kriterien der Gerechtigkeit oder der Innenpolitik.
3. Verwenden Sie diese Regeln nicht, um folgende Probleme zu beheben:
   1. Angebot,
   2. Zeiten,
   3. Schwimmer,
   4. oder Verschiebungsbasiskonstruktion.
4. Wenn Sie feststellen, dass das Problem strukturell bleibt, gehen Sie zurück nach Scheduling, bevor Sie fortfahren.

Wenn Sie diesen Abschnitt beenden, sollten Sie klar sein, dass die Regeln für das Rostering die Menschen regeln und nicht die Grundstruktur der Arbeit.

## Unterscheidung zwischen Grundregeln und fortgeschrittenen Regeln

Bevor Sie ein Regelmodell erstellen, müssen Sie zwei Konfigurationsebenen unterscheiden:
1. **Grundregeln**
2. **Erweiterte Regeln**

Die Grundregeln sind so konzipiert, dass sie häufige Einschränkungen schnell konfigurieren. Sie sind nützlich, wenn Sie eine agile Parametrierung oder einen ersten Test wünschen. Die erweiterten Regeln sind so konzipiert, dass sie Einschränkungen und Präferenzen durch Limits und Strafen genauer modellieren.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie wissen, ob Ihr Fall Geschwindigkeit oder Präzision braucht.
2. Sie verstehen, dass grundlegende Regeln weniger Flexibilität als fortgeschrittene haben.
3. Du weißt, wenn du je nach Gebrauch verschiedene Modelle brauchst.

Um die richtige Art von Regeln zu wählen:
1. Verwenden Sie **Grundregeln**, wenn Sie häufige Einschränkungen schnell abdecken möchten.
2. Verwenden Sie **fortgeschrittene Vorschriften**, wenn Sie komplexe Richtlinien, Vereinbarungen oder spezifische Betriebsbedingungen im Detail modellieren müssen.
3. Beachten Sie, dass aktive Grundregeln sowohl im täglichen Betrieb als auch in Zuweisungsberechnungsszenarien gelten.
4. Wenn Sie unterschiedliche Modelle für unterschiedliche Kontexte benötigen, zum Beispiel für den täglichen Betrieb und für die zukünftige Berechnung, arbeiten Sie mit erweiterten Regeln.
5. Entscheiden Sie, welchen Ansatz Sie verwenden werden, bevor Sie mit der Parametrierung beginnen.

Für den Referenzfall verwenden Sie diese Logik:
1. Wenn Sie beginnen und eine erste Ebene der Kontrolle wollen, beginnen Sie mit grundlegenden Regeln.
2. Wenn Sie bereits wissen, dass Sie Präferenzen, Strafen oder Modelle nach Kontext anpassen müssen, fahren Sie mit fortgeschrittenen Regeln fort.

Wenn Sie diesen Abschnitt beenden, sollten Sie klar sein, ob Ihr Fall mit grundlegenden, fortgeschrittenen Regeln oder einer kontrollierten Kombination von beiden gelöst wird.

## Aktivieren Sie die häufigsten Grundregeln für eine erste Zuweisung

Wenn Ihr Fall ein schnelles erstes Setup benötigt, können Sie mit dem **Grundregeln** beginnen. Diese decken die häufigsten Einschränkungen ab und ermöglichen es Ihnen, die Berechnung auf einer vernünftigen Basis zu starten, bevor Sie feinere Kontrollstufen eingeben.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits beschlossen, mit grundlegenden Regeln zu beginnen.
2. Sie wissen, welche Mindestbeschränkungen Sie auferlegen wollen.
3. Sie sind sich sicher, dass nicht alle Regeln standardmäßig aktiviert werden müssen.

Um grundlegende Regeln zu aktivieren:
1. Gehen Sie in GoalBus zu **Einstellungen** > **Zuweisungsregeln**.
ref: P22_Imagen1.png | compact
2. Öffnen Sie den **Grundregeln** Abschnitt.
3. Prüfen Sie den Katalog der verfügbaren Grundregeln.
ref: P22_Imagen2.png | full
4. Aktivieren Sie nur diejenigen, die dem Fall entsprechen, den Sie bauen.
5. Sätze bei der Anwendung:
   1. allgemeine Grenzwerte,
   2. spezifische Grenzen für Mitarbeitereigenschaften,
   3. oder Ausnahmen für bestimmte Arbeitnehmer.
6. Speichern Sie die Änderungen.
7. Überprüfen Sie, dass aktive Regeln wirklich die Richtlinien widerspiegeln, die Sie auferlegen wollen.

Eine erste Grundlage für die Grundregeln kann sein:
1. **Arbeitsmuster**
2. **Ruhe zwischen den Tagen**
3. **Monatliche Arbeitszeit**
4. **Wöchentliche Arbeitszeit**
5. **Freie Tage pro Woche**
6. **Erste Lösung veröffentlicht**
7. **Arbeitsgruppe**
8. **Paarung**
9. **Vereinbarkeit der Zuteilung**
10. **Streckenanbindung**
11. **Drehung der ersten Lösung veröffentlicht**
12. **Konsekutive Arbeitstage**, wenn angewendet

Für den Referenzfall aktivieren Sie keine Regel, nur weil sie existiert. Aktivieren Sie sie nur, wenn:
1. reagiert auf ein wirkliches Bedürfnis,
2. Du kannst erklären, warum du es brauchst.
3. Und du weißt, wie das den Auftrag beeinflussen wird.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine erste Kontrollbasis für die Personalzuweisung haben.

## Erstellen eines Modells von fortgeschrittenen Regeln, wenn Sie mehr Präzision benötigen

Wenn die Grundregeln nicht genug sind, ist der nächste Schritt, um eine **Modell fortgeschrittener Regeln** zu erstellen. Dieser Ansatz ermöglicht es Ihnen, genau zu kontrollieren, wie Aufträge generiert werden, Anpassung von Grenzen und Präferenzen nach Unternehmenspolitiken, Arbeitsvereinbarungen und realen Betriebsbedingungen.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits erkannt, welcher Teil des Falles nicht gut mit grundlegenden Regeln gelöst werden kann.
2. Sie wissen, welches Verhalten obligatorisch sein sollte und welches nur bevorzugt wird.
3. Sie benötigen bereits ein feineres Modell, das nach Szenario oder Kontext wiederverwendet werden kann.

So erstellen Sie ein Modell von fortgeschrittenen Regeln:
1. Öffnen Sie in **Einstellungen** > **Zuweisungsregeln** den Abschnitt **Modellregeln**.
2. Erstellt ein neues Modell von Regeln.
3. Weist dem Modell einen klaren **Bezeichnung** zu.
4. Fügen Sie einen **Beschreibung** hinzu, mit dem Sie ihn von anderen Modellen unterscheiden können.
5. Speichern Sie das Modell.
ref: P22_Imagen3.png | compact
6. Fangen Sie an, erweiterte Regeln nacheinander hinzuzufügen.
7. Entscheiden Sie für jede Regel:
   1. wenn sie als verbindliche Grenze gilt,
   2. oder wenn es als eine Vorliebe durch Strafe.
8. Speichert die Modelleinstellungen.
9. Aktiviert das erstellte Regelmodell.
10. Prüfen Sie, ob das Modell bereits der richtigen Rostering-Berechnung zugeordnet werden kann.

Für den Referenzfall könnte eine gültige Option sein:
- **Aufbau L1 bearbeitbar**
- **L1 Fahrerzuweisung - Erweiterte Regeln**

Wenn Sie diesen Abschnitt beenden, sollten Sie ein erweitertes Modell bereit haben, komplexere Einschränkungen und Präferenzen darzustellen.

## Über die Regeln auf das richtige Kollektiv und auf die tatsächliche Berechnung

Nach Aktivierung der Grundregeln oder der Erstellung eines fortgeschrittenen Modells müssen Sie überprüfen, ob die Regeln für das richtige Kollektiv gelten und dass Sie keine abstrakten Beschränkungen im Zusammenhang mit der tatsächlichen Berechnung auferlegen.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Sie haben bereits Grundregeln aktiviert oder ein fortgeschrittenes Modell erstellt.
2. Sie wissen, welche Mitarbeiter, Gruppen oder Einlagen an der Berechnung teilnehmen.
3. Sie sind klar, welche Scheduling-Lösung als Input dienen wird.

Um die Regeln korrekt auf den Berechnungskontext zu beziehen:
1. Überprüfen Sie die Personalgruppe, für die sich Rostering bewerben wird.
2. Prüfen Sie, ob die Regeln Auswirkungen haben:
   1. das gesamte beteiligte Personal,
   2. für eine bestimmte Gruppe,
   3. oder Mitarbeiter mit spezifischen Eigenschaften.
3. Bestätigen Sie, dass Sie keine Regeln für Menschen, die nicht einmal an dieser Berechnung teilnehmen werden.
4. Prüfen Sie, ob die Logik des Scheduling-Szenarios noch mit diesen Regeln vereinbar ist.
5. Wenn eine Regel die Arbeitsteilung undurchführbar macht, passt sie ihre Grenze oder ihren Anwendungsbereich an.
6. Speichert die endgültige Version der Konfiguration.

Fragen Sie sich für den Referenzfall:
1. Sind diese Regeln für Fahrer bestimmt, die tatsächlich L1 abdecken?
2. Ist die Arbeitsgruppe die richtige?
3. Ist der Auftrag nach Aktivierung dieser Regeln noch praktikabel?

Wenn Sie diesen Abschnitt beenden, sollten Sie eine Reihe von Regeln mit echten Menschen und mit einer bestimmten Rostering Berechnung verbunden haben.

## Bestätigung, dass die Regelbasis bereits bereit für die Berechnung von Rostering ist

Der letzte Schritt ist, sicherzustellen, dass Ihre Einstellungen bereit sind, die Personalberechnung zu füttern. Es geht nicht nur um die Aktivierung von Regeln, sondern eine kohärente, verständliche und anwendbare Basis verlassen.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie haben bereits zwischen grundlegenden und fortgeschrittenen Regeln gewählt, wie der Fall sein mag.
2. Sie haben die notwendigen Einschränkungen bereits aktiviert oder modelliert.
3. Du hast bereits Logik mit dem rechten Kollektiv verknüpft.
4. Sie haben bereits überprüft, dass die Aufgabe noch lebensfähig ist.

Um zu bestätigen, dass die Regelbasis bereits fertig ist:
1. Prüfen Sie den endgültigen Satz aktiver Regeln.
2. Bestätigt, dass jeder auf ein wirkliches Bedürfnis reagiert.
3. Fragen Sie sich, ob das System schon:
   1. Blockieren ungültiger Zuweisungen,
   2. Einhaltung von Resten und Grenzen,
   3. die Eigenkapitalkriterien und die Arbeitsgruppe widerspiegeln,
   4. und weiterhin eine brauchbare Lösung zu erzeugen.
4. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
5. Wenn die Antwort nein ist, passen Sie die Regeln an, bevor Sie folgen.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Die Regeln für die Aufstellung von L1 sind jetzt klar.
2. Du weißt, warum du jede Regel aktiviert hast.
3. Das System kann immer noch echte Leute mit dieser Konfiguration zuweisen.
4. Die Basis ist bereits bereit, mit der Verfügbarkeit von Personal und Ausnahmen umzugehen.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine starke genug Rostering Regel Basis haben, um auf die Behandlung von Abwesenheiten, Inaktivität und Verfügbarkeit zu bewegen.

## Zusätzliche Messwerte

- [Verwaltung von Abwesenheiten, Inaktivität und Verfügbarkeit von Mitarbeitern](P23_Verwaltung_Von_Abwesenheiten_Inaktivität_Und_Verfügbarkeit_Von_Mitarbeitern.md)
