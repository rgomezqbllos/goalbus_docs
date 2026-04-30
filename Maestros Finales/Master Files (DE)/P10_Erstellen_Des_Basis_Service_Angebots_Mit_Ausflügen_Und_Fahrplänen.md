---
title: Erstellen des Basis-Service-Angebots mit Ausflügen und Fahrplänen
shortTitle: Serviceangebot
intro: Erfahren Sie, wie Sie einen Business-Service erstellen, Ihre Reisen nach Linien
  und Sinnen überprüfen und ein gültiges und ausführbares Angebot hinterlassen, bevor
  Sie bei GoalBus zu Zeitplan wechseln.
contentType: how-tos
versions:
- '*'
---
## Schaffung der kommerziellen Dienst, der als Container von dem Angebot handeln wird

Bevor Sie einzelne Reisen überprüfen, müssen Sie den **kommerzielle Dienstleistungen** erstellen, der als Container für Ihr Angebot fungiert. In GoalBus sind Business Services die Governance-Ebene des Angebots: Sie verbinden Linien und Routen, Tagestypen und Kalenderlogik und Reisen, die den realen Service definieren. Das Tool macht deutlich, dass diese Struktur verhindert, dass unvollständige oder nicht überarbeitete Zeitpläne operativ genutzt werden.

Verwenden Sie diesen Schnellstart, wenn Sie bereits ein validiertes Netzwerk, eine definierte Zeitbasis, haben und diese Struktur in ein reales Angebot verwandeln müssen, das dann in Scheduling validiert, gemessen und verbraucht werden kann.

Bevor Sie beginnen, stellen Sie sicher, dass:

1. Sie haben bereits Arten von Feiertagen und Tagen in P2 eingerichtet.
2. Sie haben bereits das Betriebsjahr auf P3 validiert.
3. Sie haben bereits das Basis- und Betriebsnetz bei P4 und P5 vorbereitet.
4. Sie haben bereits Parkplätze, Lagerhäuser und Ausflüge in P6 und P7 definiert.
5. Sie haben bereits die in P8 erlaubten Fahrzeugtypen definiert.
6. Sie haben bereits die Zeitversion und die Reisezeiten auf P9 erstellt.
7. Sie sind klar, welche Linie, welche Art von Tag und welches Gefühl Sie als Referenzfall verwenden werden.

Verwenden Sie für diesen Schnellstart diesen Referenzfall:

> **Ich werde den L1-Business-Service erstellen, Ihre Rückfahrten überprüfen und das Angebot validiert lassen, bevor Sie zu Zeitplan wechseln.**

So erstellen Sie den kommerziellen Service Ihres Koffers:

1. Gehen Sie in GoalBus zur **Dienstleistungen** Ansicht.
ref: P10_Imagen1.png | compact
2. Finden Sie heraus, ob bereits ein kommerzieller Service für Ihren Fall geeignet ist.
3. Wenn der Service bereits existiert, öffnen Sie ihn und überprüfen Sie, ob er wirklich der Art des Tages entspricht und das Angebot, das Sie vorbereiten möchten.
4. Wenn es nicht existiert, erstellen Sie eine neue.
ref: P10_Imagen2.png | compact(2x)
5. Definieren:
   1. Eine klare **Bezeichnung** für den Service,
   2. Der anzuwendende **Art des Tages**,
   3. Der **Zeilen**, der Teil dieses Dienstes sein wird.
   4. Der **Beschreibung**-Dienst, wenn Sie mehr Details angeben möchten, obwohl dieses Feld nicht obligatorisch ist.
6. Sparen Sie sich den Service.
ref: P10_Imagen3.png | compact(x8)
7. Bestätigen Sie, dass Sie bereits Ihre Fahrplanansicht oder Ihr Reiseraster eingeben können.

Für den Referenzfall könnte eine gültige Option sein:

- **Standardarbeitstag - L1**

Es ist auch möglich, den neuen Dienst aus dem GTFS Datei laden zu erstellen. Dazu:
1. 1. Gehen Sie in GoalBus zur **Dienstleistungen** Ansicht.
ref: P10_Imagen1.png | compact
2. Importieren Sie GTFS-Dateien von **Einfuhrleistungen**.
ref: P10_Imagen11.png | compact
3. Wenn beim Laden keine Fehler auftreten, wird der Dienst korrekt erstellt.
4. Wenn Sie den Dienst eingeben, können Sie alle Reisen sehen, die mit dem Import erstellt wurden.

Wenn Sie diesen Abschnitt beenden, sollten Sie einen kommerziellen Service haben, der als strukturierter Container des Angebots fungiert.
ref: P10_Imagen4.png  | full



## Zugang zum Reisenetz und wechselnder Kontext

Sobald der Dienst erstellt ist, ist der nächste Schritt, um das Reiseraster. Diese Ansicht ist ein zentralisierter Kontrollturm für alle geplanten Reisen innerhalb des Dienstes. Von hier aus können Sie Linie ändern, ändern Service und wechseln zwischen **Sentido 1** und **Sentido 2**, ohne den Betrieb Kontext zu verlieren.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:

1. Sie haben den kommerziellen Dienst bereits erstellt oder validiert.
2. Du weißt, welche Linie du zuerst überprüfen willst.
3. Sie wissen, welchen Sinn oder Richtung Sie als Ausgangspunkt benutzen werden.

Zugang und Änderung des Kontexts im Reiseraster:

1. Klicken Sie in der Serviceliste auf die Service-Kennung oder das **Zeitpläne anzeigen**-Symbol.
2. Verwenden Sie den Zeilenauswahlschalter, um zwischen den im Service enthaltenen Linien zu wechseln.
3. Verwenden Sie das Dropdown-Menü, wenn Sie mit einem anderen kommerziellen Dienst vergleichen möchten.
4. Wechseln Sie zwischen **Sentido 1** und **Sentido 2**, um Rundfahrten separat zu überprüfen.
5. Halten Sie den Fokus auf eine einzige Linie und einen Sinn beim Aufbau Ihres Basisgehäuses.

Für den Referenzfall:

1. Öffnen Sie den **Standardarbeitstag - L1**-Dienst.
2. Geben Sie zuerst **Sentido 1** ein.
3. Überprüfen Sie **Sentido 2** später.
ref: P10_Imagen5.png  | full

Wenn Sie diesen Abschnitt beenden, sollten Sie in der Lage sein, das Angebot zu navigieren, ohne den Kontext von Linie, Service und Adresse zu verlieren.

## Erstellung oder Überprüfung von Dienstreisen

Nun ja, geben Sie das Detail des **Reise** ein. Das Dokument erklärt, dass ein Zeitplan eine Abfolge von Ereignissen ist und dass jede Reise verknüpft werden muss mit:

1. eine spezifische Streckenänderung,
2. einer Abfolge von Stopps,
3. und eine temporäre Referenz.

Dies sorgt dafür, dass Ausgänge und Ankünfte physikalisch ausführbar sind. Darüber hinaus zeigt das Raster standardmäßig nur die wichtigsten Stopps oder Zeitpunkte an, um eine klare Ansicht zu behalten, obwohl Sie alle Zwischenprodukte einzoomen können.

Bevor Sie diesen Abschnitt beginnen, stellen Sie sicher, dass:

1. Sie haben bereits eine gültige Zeitversion in P9.
2. Sie wissen, welche Routenvariation der Reise entspricht, die Sie erstellen oder überprüfen möchten.
3. Du weißt, welche Linie und was für ein Gefühl du redigierst.

Um Dienstreisen zu erstellen oder zu überprüfen:

1. Wählen Sie innerhalb des Dienstes eine Linie und einen Sinn aus.
2. Überprüfen Sie die Reisen, die bereits im Raster vorhanden sind.
3. Wenn Sie eine neue Reise erstellen müssen, verwenden Sie die entsprechende Aktion, um einen neuen Ausgang hinzuzufügen.
ref: P10_Imagen9.png | compact
4. Weist die Reise an:
   1. die richtige **Pfad oder Variation**,
   2. die **Uhrzeit der Abreise**,
   3. und die **Vorübergehende Bezugnahme** in Übereinstimmung mit der in P9 erstellten Version.
ref: P10_Image10.png
5. Wenn die Reise bereits existiert, übergeben Sie den Cursor über Ihren Identifier, um zu überprüfen, welche Routenvariation Sie verwenden.
6. Prüfen Sie, ob die berechnete Gesamtdauer im Vergleich zu den definierten Fahrzeiten sinnvoll ist.
7. Erweitern Sie die Sequenz, wenn Sie alle Zwischenstopps überprüfen müssen.
8. Wiederholen Sie den Vorgang, bis Sie eine minimale Basis von Reisen pro Sinn haben.

Für den Referenzfall können Sie mit einer minimalen Struktur wie folgt beginnen:

1. L1 - Sentido 1
   1. Reise 1: Abreise 06:00
   2. Reise 2: Ausfahrt 06:20
2. L1 - Sentido 2
   1. Reise 1: Ausfahrt 06:10
   2. Reise 2: Abreise 06:30 Uhr

Wenn Sie diesen Abschnitt beenden, sollten Sie ein grundlegendes Reiseangebot haben, das bereits mit Route, Sinn und Zeitbezug verknüpft ist.

## Überprüfungsintervalle, Gesamtdauer und Versorgungsbilanz

Nach der Erstellung oder Überprüfung von Reisen, müssen Sie überprüfen, ob das Angebot als Ganzes sinnvoll ist. Das Raster ermöglicht es Ihnen, ein Auge auf:

1. die **Gesamtdauer** für jede Reise,
2. die **Intervall** in Bezug auf die vorherige Reise,
3. und globale KPIs pro Linie, wie z.B. Reiseanzahl, Gesamtdistanz und Gesamtfahrzeit. Damit lässt sich beurteilen, ob das Angebot ausgewogen, symmetrisch und wirtschaftlich rentabel ist.

Bevor Sie fortfahren, stellen Sie sicher, dass:

1. Sie haben bereits mindestens einige Reisen erstellt oder überprüft.
2. Sie können bereits die Gesamtlänge dieser Reisen sehen.
3. Sie können bereits Sinne und Frequenzen vergleichen.

Zur Validierung der Versorgungsbilanz:

1. Überprüfen Sie im Raster die **Gesamtdauer** für jede Reise.
2. Prüfen Sie, ob es vernünftigerweise zu den erwarteten Reisezeiten passt.
3. Überprüfen Sie die **Intervall** in Bezug auf die vorherige Reise und sehen Sie, ob es übermäßige Lücken oder Ausgänge zu nah zusammen.
4. Vergleichen Sie die Anzahl der **Sentido 1** Reisen zum **Sentido 2**.
5. Überprüfen Sie die globalen KPIs der Linie:
   1. **Reisekonto**,
   2. **Gesamtentfernung**,
   3. **Gesamtzeit**. - Nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein, nein.
ref: P10_Imagen6.png | compact
6. Korrigiert jedes offensichtliche Ungleichgewicht, bevor der Service für bereit.

Fragen Sie sich für den Referenzfall:

1. Ist die Rundreise und die Rundreise ausgewogen?
2. Entsprechen die Reiseintervalle dem Niveau des Angebots, das Sie erstellen möchten?
3. Ist die Gesamtdauer jeder Reise mit der Zeitangabe vereinbar?
4. Erscheint das Angebot wirtschaftlich vernünftig oder ist es überdimensioniert?

Wenn Sie diesen Abschnitt beenden, sollten Sie ein Angebot nicht nur erstellt haben, sondern auch aus der Sicht von Frequenz, Dauer und Balance überarbeitet.

## Validierung des Dienstes, um ihn zur Berechnung bereit zu lassen

Der letzte Schritt ist der **Validierung**-Dienst. Die Validierung blockiert die Reisedaten und ermöglicht die Programmierung, während ein nicht validierter Dienst noch in der Bearbeitungsphase ist und noch nicht kalkulierbar ist. Er zeigt auch an, dass ein validierter Dienst für die Bearbeitung eingeschränkt wird, nicht mehr herausnehmbar ist und für die Programmierung bereit ist.

Bevor Sie fertig sind, stellen Sie sicher, dass:

1. Sie haben die Dienstreisen bereits überprüft.
2. Sie haben bereits Routen, Dauern und Intervalle überprüft.
3. Sie haben bereits bestätigt, dass das Angebot auf den Fall reagiert, den Sie bauen möchten.

Um den Service zu validieren und ihn für Scheduling bereit zu lassen:

1. Überprüfen Sie das Reiseraster des Dienstes ein letztes Mal.
2. Bestätigen Sie, dass Sie den Dienst nicht mehr bearbeiten müssen.
3. Führen Sie die Aktion **Validierung** auf dem Dienst oder auf dem entsprechenden Reiseset aus.
ref: P10_Imagen7.png | full
4. Überprüfen Sie, ob sich der Status des Dienstes in **Validierung** ändert.
ref: P10_Imagen8.png | compact(2x)
5. Bestätigt, dass:
   1. die Reise wird für versehentliche Änderungen gesperrt,
   2. der Dienst ist jetzt **kalkulierbar**,
   3. und Scheduling kann es in den nächsten Schritten lesen.
6. Wenn Sie noch Änderungen vornehmen müssen, verwenden Sie die **Nicht validieren**-Logik, um den Dienst zurückzugeben, um ihn zu bearbeiten und zu beenden, bevor Sie ihn erneut validieren.

Für den Referenzfall, nicht weiter zu Zeitplan, bis Sie angeben können:

1. Linie L1 hat ein konsistentes, praktikables Angebot.
2. Reisen sind mit der korrekten Routenvariation verbunden.
3. Die Gesamtdauer und die Intervalle sind sinnvoll.
4. Der Dienst befindet sich bereits im **Validierung**-Status.

Wenn Sie diesen Abschnitt beenden, sollten Sie ein bereits strukturiertes, überarbeitetes und validiertes Geschäftsangebot haben, das für Scheduling konsumierbar ist.

## Zusätzliche Messwerte

- [Validierung der operativen Struktur: Lager, Einheiten und Gruppen](P11_Validierung_Der_Betriebsstruktur_Und_Des_Status_Des_Dienstes.md)
