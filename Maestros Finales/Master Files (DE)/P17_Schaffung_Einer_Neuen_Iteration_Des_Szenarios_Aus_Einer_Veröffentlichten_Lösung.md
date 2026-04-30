---
title: Schaffung einer neuen Iteration des Szenarios aus einer veröffentlichten Lösung
shortTitle: Neue Iteration
intro: Erfahren Sie, wie Sie eine neue Iteration eines bereits veröffentlichten Szenarios
  erstellen, um Verbesserungen zu testen, Parameter anzupassen oder Änderungen einzuführen,
  ohne die bereits in Betrieb befindliche Version zu verändern.
contentType: how-tos
versions:
- '*'
---
## Basierend auf einer veröffentlichten Lösung ohne Änderung der aktuellen Version

Nach der Veröffentlichung einer Lösung ist es normal, dass Sie weiter daran arbeiten müssen. Sie können Regeln anpassen, eine andere Drehlogik ausprobieren, Änderungen anbieten oder eine Verbesserung für einen späteren Zeitraum vorbereiten. In diesem Fall sollten Sie die bereits veröffentlichte Version nicht direkt ändern. Das Richtige ist, eine **Neue Iteration** des Szenarios zu erstellen, um die Rückverfolgbarkeit zu erhalten und die bereits vorhandene Version zu schützen.

Verwenden Sie diesen Schnellstart, wenn Sie bereits eine Stufe mit einer Lösung im **Veröffentlicht**-Status haben und eine neue Variante erzeugen müssen, ohne die historische Referenz der implantierten Lösung zu verlieren.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben das vorherige Szenario bereits auf P16 veröffentlicht.
2. Die Szenario-Lösung, die Sie als Basis nehmen, ist im **Veröffentlicht**-Status.
3. Du weißt, wie du aussehen willst oder wie du die nächste Iteration verbessern willst.
4. Es ist klar, dass die neue Iteration die aktuelle Version erst automatisch ersetzen sollte, wenn sie die Berechnung, Validierung und Veröffentlichung wieder durchlaufen hat.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde eine neue Iteration des veröffentlichten L1-Szenarios erstellen, um Verbesserungen in der Lösung zu testen, ohne die bereits in Betrieb befindliche Version zu berühren.**

Für eine sicher veröffentlichte Lösung:
1. Öffnen Sie in GoalBus das **Planungsszenarien** Modul.
2. Lokalisiert das Szenario, dessen Lösung im **Veröffentlicht**-Status liegt.
3. Überprüfen Sie Ihren Namen, Ihre Beschreibung, Ihren Tagestyp und die zugehörigen Zeilen.
4. Bestätigen Sie, dass es wirklich die Version ist, die Sie als Referenz verwenden möchten.
5. Vermeiden Sie die Bearbeitung dieser Version direkt, als ob es ein neuer Entwurf wäre.
6. Entscheiden Sie, welche Änderungen Sie in der neuen Iteration vornehmen möchten:
   1. Vorschriften,
   2. Parameter,
   3. Angebot,
   4. oder zulässige strukturelle Anpassungen.

Wenn Sie diesen Abschnitt beenden, sollten Sie das veröffentlichte Szenario klar identifiziert haben, das als Grundlage für Ihre neue Iteration dienen wird.

## Erstellen der neuen Iteration aus dem veröffentlichten Szenario

Sobald die Basis identifiziert ist, ist der nächste Schritt, um eine **Neue Iteration** zu erstellen. Ziel ist es, die veröffentlichte Version als historische Referenz zu erhalten und einen neuen kontrollierten Zweig der Arbeit auf der gleichen Betriebslogik zu öffnen.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die richtige Lösung gefunden.
2. Du weißt, warum du eine neue Iteration brauchst.
3. Sie sind sich sicher, dass die neue Iteration deutlich von der vorherigen Version unterschieden werden muss.

So erstellen Sie die neue Iteration:
1. Öffnen Sie aus der Szenariotabelle das Aktionsmenü des veröffentlichten Szenarios.
2. Wählen Sie die Option für **eine neue Iteration erstellen**, indem Sie auf **Duplikat** das Szenario als Arbeitsbasis klicken.
ref: P17_Imagen1.png | compact
3. Geben Sie eine **Neuer Name** für die Iteration ein.
4. Falls zutreffend, aktualisieren Sie die **Beschreibung**, um das Änderungsziel zu reflektieren.
5. Speichern Sie die neue Iteration.
ref: P17_Imagen2.png | compact
6. Prüft, ob das neue Szenario als eigenständige Einheit vom veröffentlichten Szenario erscheint.
ref: P17_Imagen3.png | full
7. Prüfen Sie, ob die ursprünglich veröffentlichte Version intakt bleibt und von der neuen unterscheidet.

Für den Referenzfall könnte eine gültige Option sein:
- **Klassische Berechnung - L1 bearbeitbar - Iteration 2**
- **L1 praktikabel - Verbesserung der Schichtvorschriften**

Wenn Sie diesen Abschnitt beenden, sollten Sie eine neue Iteration erstellen lassen, ohne die Rückverfolgbarkeit der veröffentlichten Version zu verlieren.

## Definieren, welche Änderungen zur neuen Iteration gehören

Nachdem Sie die Iteration erstellt haben, müssen Sie entscheiden, was Sie wirklich ändern werden. Nicht alle Iterationen verfolgen das gleiche Ziel. Einige dienen dazu, Regeln anzupassen, andere, um die Effizienz zu verbessern, andere, um ein neues Angebot oder zukünftige betriebliche Variationen widerzuspiegeln.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Du hast die neue Iteration geschaffen.
2. Sie wissen, welchen Aspekt der oben genannten Lösung Sie überprüfen möchten.
3. Sie sind bereit, den Wechsel auf ein bestimmtes Ziel zu begrenzen, damit Sie nicht zu viele Variablen mischen.

Um den Umfang der Iteration zu definieren:
1. Öffne die neue Bühne.
2. Prüfen Sie, welche Elemente Sie genau wie in der veröffentlichten Version behalten möchten.
3. Entscheiden Sie, welches Element Sie zuerst ändern werden:
   1. **Fahrzeugvorschriften**,
   2. **Schichtregeln**,
   3. **Motorparameter**,
   4. **Serviceangebot**,
   5. **Logistische Matrizen**. - Nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein.
4. Vermeiden Sie, in der ersten Iteration zu viele Dinge gleichzeitig zu ändern, es sei denn, es ist unbedingt notwendig.
5. Dokument in der Bezeichnung oder Beschreibung der Zweck der Iteration.
6. Speichern Sie die beschreibenden Änderungen, bevor Sie zur Berechnung gehen.

Verwenden Sie für den Referenzfall eine Logik wie diese:
1. Halten Sie das gleiche L1 praktikable Angebot.
2. Nur das Modell der Schichtregeln anpassen.
3. Berechnen, um die neue Lösung mit der veröffentlichten zu vergleichen.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine neue Iteration mit einem klaren, eingeengten Ziel haben.

## Die Iteration neu berechnen und mit der vorherigen Version vergleichen

Sobald der Bereich definiert ist, müssen Sie die Iteration neu berechnen. Hier ist der Vorteil, dass Sie nicht mehr von Grund auf verlassen: Teile aus einer bekannten Lösung und Sie können besser die Auswirkungen der Änderung vergleichen.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Du hast die neue Iteration geschaffen.
2. Sie haben bereits das Ziel des Wandels definiert.
3. Sie haben bereits geprüft, welche Regeln, Parameter oder Einträge Sie ändern werden.

Um die neue Iteration neu zu berechnen:
1. Prüfen Sie das iterierte Szenario und bestätigen Sie, dass seine Einträge konsistent bleiben.
2. Passen Sie das Element an, das Sie ändern möchten.
3. Speichern Sie die Einstellungen.
4. Führen Sie die Berechnung des neuen Szenarios aus.
5. Warten Sie, bis das Szenario die Berechnungsphase beendet.
6. Überprüfen Sie, ob die Iteration auf **Zubereitete Lösung** oder **Bearbeiten** übergeht.
7. Vergleichen Sie das Ergebnis mit der vorherigen Version mit:
   1. KPI,
   2. allgemeine Struktur,
   3. Aufgabenlogik,
   4. und operative Kohärenz.
8. Wenn die Änderung das Ergebnis verbessert, fahren Sie mit der formalen Überprüfung fort.
9. Wenn die Änderung das Ergebnis verschlimmert, behalten Sie die veröffentlichte Version als Referenz und entscheiden Sie, ob Sie diese Iteration korrigieren oder verwerfen möchten.

Für den Referenzfall ist zu vergleichen:
1. Die veröffentlichte L1-Lösung.
2. Die neue Iteration mit Anpassung der Regeln.
3. Was sich in Qualität, Lebensfähigkeit oder Gleichgewicht verändert hat.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine neue berechnete Lösung und eine klare Grundlage haben, um sie mit der bereits veröffentlichten Version zu vergleichen.

## Entscheiden, ob die neue Iteration die aktuelle Version ersetzen wird

Der letzte Schritt besteht darin zu entscheiden, ob diese Iteration die neue Betriebsversion verdient. Eine neue Iteration ersetzt nicht automatisch die vorherige Veröffentlichung. Um zur Produktion zu gelangen, müssen Sie durch Revision, Validierung und Veröffentlichung mit Ihrem eigenen Lebenszyklus zurück gehen.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie haben die neue Iteration bereits berechnet.
2. Sie haben das Ergebnis bereits mit der veröffentlichten Lösung verglichen.
3. Sie wissen, ob die Änderung eine echte Verbesserung bringt oder nur eine Variante ohne Betriebswert.

Zum Abschluss der Entscheidung über die Iteration:
1. Prüfen Sie die neue Lösung aus technischer und operativer Sicht.
2. Wenn die Iteration die aktuelle Lösung deutlich verbessert, bereiten Sie sie auf:
   1. Validierung,
   2. und anschließende Veröffentlichung.
3. Wenn die Iteration das Ergebnis nicht verbessert, behält sie die aktuelle veröffentlichte Version als aktuelle Referenz bei.
4. Löschen Sie die vorherige Veröffentlichung nicht, nur weil es eine neue Iteration gibt.
5. Halten Sie beide Versionen für Audit und historischen Vergleich gut identifiziert.
6. Wenn Sie sich entscheiden, vorwärts zu gehen, behandeln Sie Iteration als ein neues Szenario, das seinen eigenen Fluss reisen muss, bis es **Veröffentlicht** erreicht.

Für den Referenzfall beenden Sie diesen schnellen Start nur, wenn Sie eines dieser beiden Dinge bestätigen können:
1. Die neue L1-Iteration verbessert die veröffentlichte Version und verdient es, ihren Zyklus fortzusetzen.
2. Die aktuelle veröffentlichte Version bleibt besser und die Iteration bleibt nur als Test oder Referenz.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine neue Iteration berechnen lassen, vergleichen und bereit sein, eine neue Version zu werden oder als Analysevariante beibehalten zu werden.

## Zusätzliche Messwerte

- [Der erste Calculus von Scheduling läuft und validiert](P15_Der_Erste_Calculus_Von_Scheduling_Läuft_Und_Validiert.md)
