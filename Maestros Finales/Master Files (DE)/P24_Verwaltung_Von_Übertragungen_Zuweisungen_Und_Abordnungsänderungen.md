---
title: Verwaltung von Übertragungen, Zuweisungen und Abordnungsänderungen
shortTitle: Zuweisungen und Änderungen
intro: Erfahren Sie, wie Sie Änderungen im Betriebsumfeld von Fahrern verwalten können,
  indem Sie zwischen Übertragung, Zuordnung und Änderung der Abordnung unterscheiden,
  so dass Rostering jede Person im richtigen Bereich nutzt, ohne die Rückverfolgbarkeit
  zu verlieren.
contentType: how-tos
versions:
- '*'
---
## Verständnis des Unterschieds zwischen Übertragung, Abtretung und Abordnungsänderung

Vor der Berechnung von Rostering müssen Sie die Bewegungen des Personals korrekt zwischen betrieblichen Kontexten unterscheiden. Nicht alle Situationen bedeuten dasselbe. Ein Fahrer kann noch zu seiner Hauptablage gehören, aber vorübergehend an einem anderen arbeiten. Er kann auch die Abordnung stabiler ändern. Wenn Sie diese Konzepte mischen, wird die Berechtigung des Personals verwirrend und die Berechnung kann Arbeit im falschen Kontext zuweisen.

Verwenden Sie diesen schnellen Start, wenn Sie bereits die Treiber geladen haben, überprüfen Sie ihre Hauptabordnung und modellieren ihre Abwesenheiten und Inaktivität, und Sie müssen reale Bewegungen zwischen Tanks, Gruppen oder Einheiten reflektieren.

Bevor Sie beginnen, stellen Sie sicher, dass:
1. Sie haben bereits Treiber auf P20 geladen und überprüft.
2. Sie haben bereits die operative Abordnung nach P21 bestätigt.
3. Sie haben bereits die Regeln für das Rostering auf P22 festgelegt.
4. Sie haben bereits Abwesenheiten, Inaktivität und Verfügbarkeit bei P23 registriert.
5. Sie wissen, welche Menschen den Kontext verändern und in welcher Zeit.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde aufzeichnen, dass einer der Fahrer, der normalerweise zur North Deposit gehört, vorübergehend in einem anderen Kontext arbeiten wird, und dass ein anderer Fahrer die Abordnung stabiler vor der Rostering-Berechnung ändern wird.**

Um jede Bewegung richtig zu unterscheiden:
1. Er verwendet ein **Zuweisung**, wenn die Person noch zu seinem Hauptkontext gehört, aber vorübergehend an einem anderen arbeiten wird.
2. Verwenden Sie einen **Übertragung**, wenn die Person den Kontext strukturell oder dauerhaft verändert.
3. Verwenden Sie einen **Änderung der Abordnung**, wenn Sie den Tank, die Gruppe oder die Basiseinheit, von der das System den Treiber behandeln soll, offiziell aktualisieren müssen.
4. Verwenden Sie keine Abwesenheit, um eine Änderung des Betriebskontexts zu modellieren.
5. Verwenden Sie keine Zuordnung, um eine fehlerhaft konfigurierte Hauptabordnung zu korrigieren.

Halten Sie diese Fragen als Leitfaden:
1. Wo gehört diese Person normalerweise hin?
2. Wo werden Sie in dieser Zeit wirklich arbeiten?
3. Ist diese Bewegung vorübergehend oder strukturell?

Wenn Sie diesen Abschnitt beenden, sollten Sie klar sein, welche Art von Datensatz jeder Kontextänderung entspricht.

## Aufzeichnung einer vorübergehenden Übertragung des Fahrers

Die Abtretung dient dazu, zu reflektieren, dass ein Fahrer vorübergehend aus seinem gewohnten Kontext herausarbeitet, ohne seine Basisabordnung zu verlieren. Dies ist nützlich, wenn eine Person weiterhin zu ihrer Einzahlung, Einheit oder Hauptgruppe gehört, aber für einige Zeit in einer anderen Umgebung arbeitet.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Person identifiziert, die verlegt wird.
2. Sie wissen, was ihr Hauptkontext ist.
3. Sie kennen bereits den temporären Zielkontext und die Anwendungstermine.

Um eine befristete Aufgabe zu registrieren:
1. Öffnen Sie das Fahrerprofil auf der allgemeinen Liste.
2. Gehen Sie zum Abschnitt **Bewegungen**, **befristete Abordnung** oder **Zuweisungen**, je nach verfügbarer Ansicht.
3. Erstellt einen neuen Zuweisungs-Record.
4. Definieren:
   1. die **Herkunftskontext**,
   2. die **Zielkontext**,
   3. die **Anfangsdatum**,
   4. die **Enddatum**,
   5. und alle notwendigen Beobachtungen.
5. Behalten Sie das Protokoll.
6. Prüfen Sie, ob der Fahrer immer noch seine Hauptabordnung behält.
7. Sie stellt fest, dass das System während der Zuweisungszeit im richtigen Zeitrahmen damit umgehen kann.

Für den Referenzfall wäre eine gültige Zuordnung wie folgt:
1. Fahrer am Norddepot angebracht,
2. für zwei Wochen an die South Deposit abgetreten,
3. ohne seine historische Hauptabordnung zu ändern.

Wenn Sie diesen Abschnitt beenden, sollten Sie eine temporäre Zuordnung korrekt modelliert haben, ohne die strukturelle Rückverfolgbarkeit zu verlieren.

## Aufnahme einer stabileren Übertragung oder Änderung

Im Gegensatz zur Abtretung reagiert ein Transfer auf eine strukturellere Bewegung. Hier geht es nicht mehr nur darum, vorübergehend in einem anderen Kontext zu arbeiten, sondern die betriebliche Zugehörigkeit des Fahrers stabiler zu bewegen.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:
1. Sie haben bereits die Person identifiziert, die den Kontext nachhaltig verändern wird.
2. Sie wissen, welche Einzahlung, Einheit oder Gruppe zu ihrem neuen Hauptkontext werden wird.
3. Sie sprechen nicht mehr von einer vorübergehenden oder außergewöhnlichen Notwendigkeit.

Um einen Transfer oder Strukturwandel aufzuzeichnen:
1. Öffnen Sie das Fahrerprofil.
2. Überprüfen Sie Ihre aktuelle Hauptabordnung.
3. Erstellen Sie die Übertragungsbewegung oder aktualisieren Sie die Hauptabordnung, je nach dem Fluss, den Ihre Umgebung verwendet.
4. Definieren:
   1. die neue **Haupteinlage**,
   2. die neue **Geschäftsbereich**,
   3. die neue **Arbeitsgruppe**, falls geändert,
   4. und das Datum der Wirksamkeit.
5. Speichern Sie die Änderungen.
6. Überprüfen Sie, ob das Profil bereits den neuen Hauptkontext widerspiegelt.
7. Kontrolliert, dass die Änderung keine widersprüchlichen Daten zwischen Hauptabordnung und Ratings hinterlassen hat.

Für den Referenzfall wäre eine gültige Übertragung:
1. Fahrer, der nicht mehr zum Norddepot gehört,
2. wird ein stabiles Mitglied der South Deposit,
3. und ab diesem Zeitpunkt sollte sie als Beschwerde gegen diese neue Grundlage behandelt werden.

Wenn Sie diesen Abschnitt abgeschlossen haben, sollten Sie eine strukturelle Kontextänderung korrekt modelliert haben.

## Überprüfung der Auswirkungen von Bewegungen auf Ratings und Förderfähigkeit

Nach der Registrierung von Zuweisungen oder Transfers müssen Sie die Auswirkungen auf den Betrieb überprüfen. Das Verschieben einer Person zwischen Kontexten ist nutzlos, wenn ihre Bewertungen oder Berechtigungen die Änderung nicht begleiten. Hier müssen Sie bestätigen, dass der Fahrer nicht nur den Kontext im Profil verändert hat, sondern auch in dieser neuen Umgebung korrekt verwendet werden kann.

Bevor Sie fortfahren, stellen Sie sicher, dass:
1. Sie haben bereits mindestens einen Transfer oder Transfer registriert.
2. Sie wissen, in welchem operativen Kontext die Person von jetzt an gesehen werden sollte.
3. Sie verstehen, dass eine Kontextänderung eine Überprüfung der aktuellen Ratings erfordern kann.

Überprüfung der operativen Auswirkungen der Bewegung:
1. Gehen Sie zurück zur Registerkarte **Ratings/Qualifikationen** des Treibers.
2. Prüft die aktuellen Bewertungen für den Zielkontext.
3. Wenn fehlt, fügen Sie sie mit korrekten Daten vor der Berechnung hinzu.
4. Überprüft, ob die Person aufgrund eines Konfigurationsfehlers nicht gleichzeitig in inkompatiblen Kontexten sichtbar ist.
5. prüft, ob das System die förderfähige Person im richtigen Bereich während des betreffenden Zeitraums berücksichtigen kann.
6. Wenn Sie Widersprüche erkennen, korrigieren Sie sie, bevor Sie zur Berechnung gehen.

Für den Referenzfall stellen Sie sicher, dass
1. der übertragene Fahrer kann im Bestimmungskontext rechtlich oder technisch arbeiten;
2. der übertragene Fahrer hat bereits seine Ratings nach dem neuen Kontext,
3. Anspruchsberechtigung fällt mit der eingetragenen Bewegung zusammen.

Wenn Sie diesen Abschnitt beenden, sollten Sie Personalbewegungen haben, die auch operativ nutzbar sind.

## Bestätigen, dass Kontextänderungen bereits für die Rostering-Berechnung bereit sind

Der letzte Schritt besteht darin, zu prüfen, ob die Kombination zwischen Hauptabordnung, Zuweisungen, Transfers und Ratings bereits klar genug ist, um die Berechnung zu füttern. Ziel ist es, zwei Fehler zu vermeiden:
1. eine Person in einem Kontext zuweisen, in dem sie nicht erscheinen sollte,
2. oder lassen Sie eine Person aus, die für eine bereits registrierte Änderung in Frage kommen sollte.

Bevor Sie fertig sind, stellen Sie sicher, dass:
1. Sie haben bereits die notwendigen zeitlichen oder strukturellen Bewegungen aufgenommen.
2. Sie haben bereits ihre Auswirkungen auf die Förderfähigkeit überprüft.
3. Sie wissen, welches Kollektiv an der folgenden Berechnung teilnehmen wird.

Um zu bestätigen, dass diese Ebene bereits fertig ist:
1. Gehen Sie zurück zur allgemeinen Liste der Fahrer.
2. Überprüfen Sie verschiedene Profile, die von Kontextänderungen betroffen sind.
3. Prüft, dass
   1. die Zuweisungen werden als temporär betrachtet,
   2. Übertragungen spiegeln sich in strukturellen Veränderungen wider,
   3. und die Hauptabordnung bleibt gegebenenfalls konsistent.
4. Fragen Sie sich, ob das System schon:
   1. den richtigen Treiber im richtigen Kontext verwenden,
   2. während des korrekten Zeitraums,
   3. ohne Verwirren struktureller Zugehörigkeit mit vorübergehender Verdrängung.
5. Wenn die Antwort ja ist, fahren Sie mit dem nächsten Schnellstart fort.
6. Wenn die Antwort nein ist, korrigieren Sie Bewegungen oder Bewertungen, bevor Sie fortfahren.

Für den Referenzfall dürfen Sie erst dann fortfahren, wenn Sie Folgendes angeben können:
1. Die Kontextänderungen von L1-Treibern werden bereits korrekt aufgezeichnet.
2. Sie wissen, wer abgetreten ist, wer verlegt wurde und wer ihre ursprüngliche Abordnung behält.
3. Die Basis ist bereits bereit, die erste Rostering-Berechnung durchzuführen.

Wenn Sie diesen Abschnitt beenden, sollten Sie den organisatorischen Kontext des Personals klar genug haben, um zur Zuweisungsberechnung überzugehen.

## Zusätzliche Messwerte

- [Führen der ersten Rostering Kalkül](P25_Führen_Der_Ersten_Rostering_Kalkül.md)
