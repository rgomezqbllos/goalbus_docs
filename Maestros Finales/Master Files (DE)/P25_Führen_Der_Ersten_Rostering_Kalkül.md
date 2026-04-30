---
title: Führen der ersten Rostering Kalkül
shortTitle: Rostering berechnen
intro: Erfahren Sie, wie Sie die erste Rostering-Berechnung vorbereiten und durchführen,
  ob die Personallösung praktikabel ist, und erkennen Sie, welche Probleme zu Regeln,
  Verfügbarkeit oder Abordnung gehören, bevor Sie die Zuordnung bestätigen.
contentType: how-tos
versions:
- '*'
---
## Vorbereitung der Basis vor dem Start der Rostering-Berechnung

Bevor Sie die Berechnung durchführen, müssen Sie überprüfen, ob die Personalbasis reif genug ist. Das Rostering sollte nicht verwendet werden, um fehlende Stammdaten in letzter Minute zu entdecken. Wenn die Vorlage, die Abordnung, die Regeln oder die Verfügbarkeit nicht gut vorbereitet sind, wird die Berechnung fehlschlagen oder eine irreführende Lösung produzieren.

Nutzen Sie diesen schnellen Start, wenn Sie bereits über eine stabile Scheduling-Lösung verfügen und alle erforderlichen Mitarbeiter vorbereitet haben, um den Fahrern echte Arbeit zuzuordnen.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben den Übergang von Scheduling bei P19 bereits abgeschlossen.
2. Sie haben bereits Treiber auf P20 geladen und überprüft.
3. Sie haben bereits die operative Abordnung nach P21 bestätigt.
4. Sie haben bereits die Regeln für das Rostering auf P22 festgelegt.
5. Sie haben bereits Abwesenheiten, Inaktivität und Verfügbarkeit bei P23 registriert.
6. In P24 haben Sie bereits Zuweisungen, Übertragungen oder Abordnungsänderungen registriert.
7. Sie sind klar, welche Scheduling-Lösung als Input für die Berechnung fungieren wird.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde die erste Rostering-Berechnung für die Linie L1 durchführen, mit einer bereits stabilen Scheduling-Lösung und einer gut vorbereiteten Fahrerbasis.**

Zur Vorbereitung der Grundlage vor der Berechnung:
1. Öffnet die **Einreihung** Umgebung oder das Modul.
ref: P25_Imagen1.png | compact
2. Prüfen Sie, welche Scheduling-Lösung die Eingabe der Berechnung sein wird.
3. Bestätigt, dass das Kollektiv von Fahrern, die teilnehmen werden, verfügbar ist und zu dem richtigen Kontext gehört.
4. Überprüfen Sie, ob die aktiven Rostering-Regeln auf den realen Fall reagieren.
5. Kontrolliert, ob die wichtigsten Abwesenheiten und Inaktivitäten bereits registriert sind.
6. Bestätigt, dass sich relevante Zuweisungen oder Transfers bereits widerspiegeln.
7. Wenn Sie ein Stammdatenproblem erkennen, korrigieren Sie es vor der Berechnung.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Die L1-Lösung braucht keine strukturellen Veränderungen mehr.
2. Das Kollektiv der Fahrer existiert bereits und ist bereit.
3. Regeln und Verfügbarkeit stellen bereits die Realität des Zeitraums dar.
4. Du kannst jetzt eine richtige Arbeitsaufgabe ausprobieren.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine stabile genug Basis haben, um das Rostering zu starten.

## Auswahl des richtigen Eintrags von Scheduling

Das Rostering braucht einen klaren Arbeitseintrag. Dieser Eintrag sollte keine mehrdeutige Mischung aus Szenarien sein, sondern eine bekannte und brauchbare Scheduling-Lösung. In diesem Stadium ist es wichtig, zu bestätigen, dass Sie Menschen dem richtigen Job zuweisen werden.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie wissen, welches Scheduling-Szenario oder welche Lösung Sie verwenden werden.
2. Du weißt, welche Linie, welcher Tag oder welcher Kontext du bedecken wirst.
3. Sie können nun zwischen der aktuellen Lösung und einer unkonsolidierten Iteration unterscheiden.

So wählen Sie die Eingabe der Berechnung richtig aus:
1. Öffnen Sie im Rastering-Modul die Berechnungseinstellungen oder das Mapping-Szenario.
2. Wählen Sie den **Planungslösung**, der als Eintrag fungiert, d.h. welche Lösung für einen Datumsbereich veröffentlicht wird.
3. Überprüfen Sie, ob die Art des Tages mit der Berechnung übereinstimmt, die Sie machen möchten.
4. Überprüfen Sie, ob die Zeile oder der Satz der Zeilen dem Fall entspricht.
5. Wenn es mehrere mögliche Versionen gibt, wählen Sie nur die, die Sie wirklich als Basis verwenden möchten.
6. Speichern Sie die Auswahl.
7. Überprüfen Sie, ob das System bereits deutlich zeigt, welche Arbeit zugewiesen wird.

Für den Referenzfall stellen Sie sicher, dass
1. Der Eintrag entspricht L1 bearbeitbar.
2. Sie mischen keine veröffentlichte Version mit einer nicht genehmigten Iteration.
3. Der Job, der zu Rostering kommt, ist genau das, was Sie abdecken wollen.

Wenn Sie diesen Abschnitt beenden, sollten Sie einen genau definierten Scheduling-Eintrag für die Personalberechnung haben.

## Konfigurieren der Rostering-Berechnung mit den richtigen Regeln und Kollektiven

Sobald der Eintrag ausgewählt ist, müssen Sie überprüfen, ob die Berechnung das Kollektiv und die korrekten Regeln verwendet. In Rostering kann eine schlechte Kombination aus Kollektiv, Regeln und Verfügbarkeit eine Lösung machen, die in Scheduling korrekt unerreichbar war.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits den Eintrag von Scheduling ausgewählt.
2. Sie wissen, welche Mitarbeitergruppe teilnehmen wird.
3. Sie haben bereits definiert, ob Sie grundlegende, erweiterte Regeln oder eine kontrollierte Kombination verwenden.

So konfigurieren Sie die Rostering-Berechnung:
1. Beginnt die Konfiguration der Mapping-Berechnung durch die Erstellung eines neuen Röstszenarios.
2. Wählen Sie die folgenden Eingabedaten:
   1. Die **Einlagen**, die teilnehmen wird.
   2. Wählen Sie den **Datteln** aus dem neuen Röstszenario.
   3. Überprüfen Sie, welche **Musterregeln** für die Berechnung gilt. Bestätigen Sie, dass die aktiven Regeln der korrekten Gruppe entsprechen.
   4. Fügen Sie ein **Beschreibung** hinzu, wenn Sie es genauer beschreiben möchten.
3. Speichern Sie die Einstellungen.
ref: P25_Imagen2.png | compact(x10)
4. Prüfen Sie, ob die Berechnung Folgendes berücksichtigt:
   1. Abwesenheiten,
   2. Nichterwerbstätigkeit,
   3. Zuweisungen,
   4. und Verfügbarkeitsbeschränkungen.
5. Prüfen Sie, ob die Berechnung bereits vorliegt:
   1. Aufnahmearbeiten,
   2. förderungsberechtigte Kollektive,
   3. anwendbare Vorschriften.

Im Referenzfall bestätigt sie, dass
1. Die L1-Treibergruppe ist die zu verwendende.
2. Die aktiven Regeln entsprechen dieser Gruppe.
3. Die Konfiguration zieht keine Einschränkungen aus einem anderen Kontext.

Wenn Sie diesen Abschnitt beenden, sollten Sie die Berechnung für das Raster korrekt parametrieren lassen, bevor Sie sie ausführen.

## Durchführung der ersten Zuweisungsberechnung

Jetzt können Sie die Berechnung starten. An dieser Stelle wird das System versuchen, echte Menschen zuzuordnen, um von Scheduling geerbt zu arbeiten, unter Einhaltung von Regeln, Abordnung und Verfügbarkeit.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits den richtigen Eintrag gewählt.
2. Sie haben das Kollektiv und die Regeln aufgestellt.
3. Sie haben bereits die Verfügbarkeitsbasis und Kontextänderungen überprüft.
4. Es fehlen Ihnen nicht mehr wesentliche Stammdaten.

So führen Sie die Berechnung für das Rostering aus:
1. Von der Rostering-Stufe oder Modul, es startet die **Berechnen** oder **Berechnung starten** Aktion.
ref: P25_Imagen3.png | compact(3x)
2. Überprüfen Sie, ob das System mit der Bearbeitung der Zuordnung beginnt.
3. Warte, bis die Kalküle vorbei ist.
4. Überprüfen Sie, ob das System zurückkommt:
   1. eine zugewiesene Lösung,
   2. Teillösung,
   3. oder ein klares Zeichen von Konflikten.
5. Wenn die Berechnung keine brauchbare Lösung generiert, gehen Sie nicht sofort davon aus, dass Sie persönlich fehlen. Prüfen Sie zuerst:
   1. Vorschriften zu restriktiv,
   2. falsche Abordnung,
   3. Fehlbelegungen,
   4. o unterschiedliche Aufgaben und Ratings.

Im Referenzfall bestätigt sie, dass
1. Die Berechnung von L1 erfolgt auf dem erwarteten Kollektiv.
2. Das System versucht, echte Arbeit den wirklichen Menschen zuzuordnen.
3. Das Ergebnis ermöglicht es Ihnen, die Machbarkeit zu überprüfen oder spezifische Konflikte zu erkennen.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine erste Rostering-Lösung oder ein klares Zeichen dafür haben, wo das Schloss ist.

## Dolmetschen, ob es sich um Regeln, Verfügbarkeit oder Abordnung handelt

Nach der Berechnung müssen Sie das Ergebnis richtig interpretieren. Nicht alle Fehler bedeuten dasselbe. Wenn Sie die Ursache nicht gut unterscheiden, können Sie sie in der falschen Ebene korrigieren.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Du hast schon die Rechnung geführt.
2. Sie haben gesehen, ob die Lösung vollständig, teilweise oder widersprüchlich war.
3. Sie sind bereit, zu diagnostizieren, bevor Sie Daten berühren.

Um das Ergebnis korrekt zu interpretieren:
1. Wenn viele Aufgaben fehlen, überprüfen Sie zuerst das Notensystem **Verfügbarkeit**.
2. Wenn das System Leute auslässt, die gültig sein sollten, überprüfen Sie ihre **Abordnung** und ihre **Ratings**.
3. Wenn die Zuordnung zu starr oder unmöglich erscheint, überprüfen Sie die **Regeln für die Aufstellung**.
4. Wenn Legacy-Arbeit für eine Gruppe nicht praktikabel erscheint, überprüfen Sie erneut, ob das Problem von **Planung** kommt.
5. Korrigieren Sie nicht durch Intuition. Finden Sie zuerst heraus, ob das Problem zu gehört:
   1. Vorschriften,
   2. Verfügbarkeit,
   3. Abordnung,
   4. oder vererbte Struktur.

Stellen Sie sich für den Referenzfall folgende Fragen:
1. Werden Menschen wirklich vermisst oder falsch konfiguriert?
2. Die Regel, die ich aktiviert habe, machte den Auftrag unmöglich?
3. Versuche ich, einen Treiber in einem Kontext zu benutzen, in den er nicht gehört oder nicht aktiviert ist?
4. Gab es das Problem schon vor der Einreise ins Verzeichnis?

Wenn Sie diesen Abschnitt beenden, sollten Sie ein erstes diagnostisches Lesen des Ergebnisses der Berechnung haben.

## Die Lösung für die funktionale Überprüfung bereit lassen

Ziel dieses Schnellstarts ist es, die Lösung noch nicht endgültig zu genehmigen. Ziel ist es, die erste Berechnung durchzuführen und eine funktionsgerechte Überprüfungsgrundlage zu schaffen: Abdeckung, Konflikte, Gleichgewicht und Lebensfähigkeit.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Du hast schon die Rechnung geführt.
2. Sie haben bereits geprüft, ob die Lösung vollständig oder teilweise ist.
3. Sie haben bereits festgestellt, ob die Probleme zu Regeln, Verfügbarkeit, Abordnung oder Scheduling gehören.

Um diese erste Berechnung sinnvoll zu schließen:
1. Sie behält das Ergebnis der Berechnung als Grundlage für die Überprüfung bei.
2. Machen Sie keine massiven Änderungen, ohne zuerst die Ursache des Problems zu identifizieren.
3. beschließt, dass der nächste Schritt sein wird:
   1. Überprüfung von Deckungskonflikten,
   2. Regeln anpassen,
   3. Korrektur der Personaldaten,
   4. oder zurück zu Scheduling, wenn das Problem strukturell ist.
4. Es behandelt diese erste Ausführung als Validierung des gesamten Mapping-Modells.
5. Wenn die Grundlage angemessen ist, setzen Sie die Überprüfung der Abdeckung und Konflikte fort.

Für den Referenzfall, beenden Sie diesen schnellen Start nur, wenn Sie sagen können:
1. Sie haben bereits die erste Rostering-Berechnung für L1 durchgeführt.
2. Sie wissen, ob die Lösung praktikabel oder teilweise ist.
3. Sie haben bereits eine klare Hypothese darüber, wo die Hauptkonflikte sind.
4. Sie sind bereit, Berichterstattung und Konflikte im Detail zu überprüfen.

Wenn Sie diesen Abschnitt abgeschlossen haben, sollten Sie die erste Rostering-Berechnung und eine klare Grundlage für die nächste Überprüfungsphase ausgeführt haben.

## Zusätzliche Messwerte

- [Überprüfung von Konflikten, Abdeckung und Machbarkeit des Personals](P26_Überprüfung_Von_Konflikten_Abdeckung_Und_Machbarkeit_Des_Personals.md)
