---
title: Umzug von Scheduling nach Rostering
shortTitle: Vom Scheduling zum Rostering
intro: Erfahren Sie, was in Scheduling bereit sein sollte, bevor Sie Rostering eingeben,
  welche Informationen die Mitarbeiterzuteilung erben und welche Probleme vor der
  Berechnung realer Treiber gelöst werden sollten.
contentType: how-tos
versions:
- '*'
---
## Bestätigung, dass sie in Scheduling geschlossen werden sollte, bevor sie nach Rostering verlegt wird

Vor dem Einsteigen ins Rostering müssen Sie prüfen, ob Scheduling bereits eine ausreichend stabile Basis hinterlassen hat. Das Rostering ersetzt das Scheduling nicht. Ein Teil der bereits gebauten Arbeit wird zusammengestellt und entscheidet, wie man es echten Menschen zuordnet.

Verwenden Sie diesen Schnellstart, wenn Sie bereits eine berechnete und validierte Scheduling-Lösung haben, und Sie müssen entscheiden, ob Sie mit echten Mitarbeitern arbeiten können.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben bereits Schedulings Szenario erstellt, berechnet und validiert.
2. Sie haben bereits das Serviceangebot und seine Gesamtkonsistenz überprüft.
3. Sie wissen, welche Linien, welche Art von Tag und welche Lösung Sie als Referenz verwenden werden.
4. Sie sind sich sicher, dass Rostering nicht der Ort ist, um eine schlechte strukturelle Basis für Scheduling zu reparieren.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde bestätigen, dass die validierte Lösung von Scheduling für die L1-Linie reif genug ist, um nach Rostering zu ziehen und damit zu beginnen, echte Fahrer zu beauftragen.**

Um zu bestätigen, dass Scheduling bereit ist:
1. Öffnen Sie das Scheduling-Szenario, das Sie als Referenz verwenden werden.
2. Prüfen Sie, ob Ihr Zustand bereits korrekt ist, um ihn nicht mehr als Arbeitsentwurf zu behandeln.
3. Überprüfen Sie, ob das Angebot immer noch das richtige ist.
4. Prüfen Sie, ob die Logik der Fahrzeuge und die Logik der Verschiebungen bereits angewandt wurden.
5. Sie bestätigt, dass es keine offensichtlichen strukturellen Inkonsistenzen in der Lösung gibt.
6. Wenn Sie noch die Fahrzeugbasis, Zeiten, Dienste oder Regeln neu erstellen müssen, gehen Sie zurück nach Scheduling, bevor Sie folgen.
7. Wenn die Lösung bereits stabil ist, gehen Sie weiter zum nächsten Schritt.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Die L1-Lösung wurde bereits berechnet.
2. Es wurde überprüft.
3. Sie brauchen keine strukturellen Korrekturen mehr von Scheduling.
4. Sie kann nun als Arbeitsgrundlage für das Personal behandelt werden.

Wenn Sie diesen Abschnitt fertig stellen, sollten Sie klar sein, ob Scheduling bereits eine nutzbare Basis für das Rostering geliefert hat.

## Verstehen, was Rostering von Scheduling erbt

Sobald die Basis bestätigt ist, müssen Sie verstehen, welche Informationen von Scheduling zu Rostering passieren. Hier ist der Schlüssel nicht zu denken, dass Rostering von Grund auf beginnt. Rostering erbt die bereits strukturierte Arbeit und von dort entscheidet, welche reale Person es annehmen kann.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Scheduling-Lösung identifiziert, die Sie verwenden werden.
2. Sie wissen, welcher Teil der Lösung stabil bleiben sollte.
3. Sie verstehen, dass Rostering an der bereits gebauten Arbeit arbeitet, nicht an einem unstrukturierten Angebot.

Um zu verstehen, was Rostering erbt:
1. Prüfen Sie die validierte Scheduling-Lösung.
2. Identifizieren Sie die Aufgaben, Blöcke oder Arbeitsstrukturen, die als Grundlage dienen.
3. Prüfen Sie, ob die Lösung bereits eine operationell erkennbare Form hat.
4. Denken Sie daran, dass das System durch den Umzug nach Rostering nicht mehr abstrakte Arbeit schafft, sondern versucht, diese Arbeit wirklichen Menschen zuzuordnen.
5. Verwenden Sie diese Leseregel:
   1. Scheduling definiert **welche Arbeit existiert**.
   2. Das Rostering definiert **Wer wird den Job machen?**.

Fragen Sie sich für den Referenzfall:
1. Hat die L1-Lösung bereits klar genug Arbeit, um sie zuzuordnen?
2. Sind die Arbeitsblöcke erkennbar und nutzbar?
3. Ist das Problem, das noch zu lösen ist, schon von Menschen und nicht von Struktur?

Wenn Sie diesen Abschnitt beenden, sollten Sie verstehen, was Rostering erbt und was dort nicht noch einmal neu definiert werden sollte.

## Unterscheiden, welche Probleme in Scheduling gelöst werden und welche in Rostering

Bevor Sie schließlich auf die Personalschicht übergehen, müssen Sie sehr gut Aufgaben trennen. Diese Unterscheidung ist grundlegend, weil viele Fehler auftreten, wenn Sie versuchen, in der Rostering etwas zu korrigieren, das früher in Scheduling hätte aufgelöst werden müssen.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Sie wissen, welche Etappe Scheduling an der Basis sein wird.
2. Sie verstehen, dass Rostering eine vorherige Lösung verbraucht.
3. Sie sind bereit, strukturelle Probleme von Personalproblemen zu unterscheiden.

Um beide Bereiche richtig zu trennen:
1. Es behandelt wie ein **Planung**-Problem jede Angelegenheit im Zusammenhang mit:
   1. Struktur des Dienstes,
   2. Flottenlogik,
   3. Zeiten,
   4. Fahrzeugregeln,
   5. Arten von Schichten und deren Grundkonstruktion.
2. Es behandelt wie ein **Einreihung**-Problem jede Angelegenheit im Zusammenhang mit:
   1. tatsächliche Verfügbarkeit des Fahrers,
   2. Abordnung zur Einlage oder Gruppe,
   3. Abwesenheiten,
   4. Nichterwerbstätigkeit,
   5. Übertragungen oder Übertragungen,
   6. realer Anspruch auf eine Schicht.
3. Wenn Sie eine Arbeitsunstimmigkeit erkennen, die die gesamte Struktur beeinflusst, gehen Sie zurück zu Scheduling.
4. Wenn Sie die Inkohärenz einer Person feststellen, lösen Sie sie in der Liste.

Für den Referenzfall verwenden Sie diese Logik:
1. Wenn das Problem ist, dass L1's Arbeit schlecht gebaut wurde, gehen Sie zurück nach Scheduling.
2. Wenn das Problem ist, dass du nicht weißt, welcher echte Fahrer diesen Job annehmen kann, dann steigst du richtig ins Rostering ein.

Wenn Sie diesen Abschnitt beenden, sollten Sie in der Lage sein, klar zu erklären, was korrigiert werden sollte, bevor Sie zum Stab übergehen und was zum nächsten Modul gehört.

## Bestätigung, was auf der Seite des Personals bereit sein sollte, vor der Berechnung von Rostering

Nun, da Sie wissen, was Rostering erhält, müssen Sie überprüfen, was auf der Seite des Personals vorhanden sein muss, so dass die folgende Berechnung Sinn macht. Es reicht nicht aus, einen guten Zeitplan zu haben, wenn Sie noch nicht über eine Mindestbasis von Personen, Abordnungen und Verfügbarkeit verfügen.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits eine gültige Basis von Scheduling.
2. Sie wissen, welche Gruppen, Einlagen oder operativen Kontexte Menschen betreffen.
3. Sie sind bereit, die Personalschicht zu überprüfen.

Um zu bestätigen, dass die Stabbasis bereit ist:
1. Prüft, ob es bereits eine Personalgruppe gibt, die den Job erhalten kann.
2. Prüfen Sie, ob Personen beim Bewerben mit dem richtigen Kontext verbunden sind.
3. Prüfen Sie, ob Sie Rostering nicht ohne Mindestverfügbarkeitsinformationen eingeben.
4. Prüfen Sie, ob die erforderliche Struktur bereits vorhanden ist für:
   1. Regeln für die Aufstellung,
   2. Abwesenheiten,
   3. Nichterwerbstätigkeit,
   4. gegebenenfalls Übertragungen oder Übertragungen.
5. Wenn Sie diese Basis noch nicht haben, starten Sie die Personalberechnung nicht.
6. Wenn die Basis bereits existiert oder zumindest auf Kurs ist, fahren Sie mit den folgenden schnellen Starts von Rostering fort.

Fragen Sie sich für den Referenzfall:
1. Gibt es bereits Mitarbeiter, die die L1-Lösung erhalten können?
2. Gehört dieser Stab zum richtigen Bereich?
3. Ist die Basis der Verfügbarkeit und Abordnung bereits minimal vorbereitet?

Wenn Sie diesen Abschnitt beenden, sollten Sie klar sein, ob die Stabseite bereits bereit ist, die Liste zu betreten.

## Den Übergangspunkt zwischen Scheduling und Rostering klarstellen

Der letzte Schritt ist, den Übergang geistig zu schließen. Dieser schnelle Start hat noch nicht die Absicht, die Personalzuweisung zu berechnen. Er zielt darauf ab, sehr deutlich zu machen, wann das Scheduling endet und wann das Rostering beginnt, damit Sie nicht beide Domains mischen.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie haben Schedulings Lösung bereits überprüft.
2. Sie verstehen, was Rostering erbt.
3. Sie haben bereits strukturelle Probleme von Personalproblemen getrennt.
4. Sie haben schon nachgeprüft, ob es einen Mindeststab gibt.

Um den Übergang richtig zu schließen:
1. Behandelt die validierte Scheduling-Lösung als formale Rostering-Eingabe.
2. Ändern Sie diese Basis nicht weiter, es sei denn, Sie erkennen ein echtes strukturelles Problem.
3. Verwenden Sie die folgenden Schnellstarts zur Vorbereitung:
   1. Regeln für die Aufstellung,
   2. Abwesenheiten und Untätigkeit,
   3. Übertragungen, Zuweisungen und Abordnungsänderungen.
4. Er ist der Auffassung, dass sich das Ziel von hier aus ändert:
   1. Es geht nicht mehr ums Bauen.
   2. Jetzt geht es darum, es echten Menschen zuzuordnen.
5. Wenn Sie das klar sagen können, ist der Übergang gut gemacht.

Für den Referenzfall, beenden Sie diesen schnellen Start nur, wenn Sie sagen können:
1. Scheduling hat bereits eine stabile L1-Lösung hinterlassen.
2. Das nächste Problem ist nicht mehr die Struktur, sondern die Personalzuweisung.
3. Sie können nun die Regelebene "Rostering" eingeben.

Wenn Sie diesen Abschnitt beenden, sollten Sie einen klaren und kontrollierten Übergang zwischen Scheduling und Rostering haben.

## Zusätzliche Messwerte

- [Festlegung der Regeln für die Personalzuweisung](P20_Treiber_Laden_Und_Verwalten.md)
