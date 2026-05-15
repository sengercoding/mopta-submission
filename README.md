# MOPTA Challenge 2026 Submission

# Prozessbeschreibung
## Anleitung

1. Generieren der Routen mit file `route_generator_three_stops`
  * Hier können Constraints verändert werden (deadhead ratio, dest-miles)
2. Mit `prepare_dex_files` das Einlesen der Daten über DataExchange Library und die dafür erstellten Mappings (.xml-Files) vorbereiten
3. In AIMMS den Prozess `ReadInputData` ausführen, der alle nicht Routen-bezogenen Daten in AIMMS einliest
4. In AIMMS den Prozess `ReadLargeData` ausführen, der alle Routen-bezogenen Daten in AIMMS mittels DataExchange einliest
5. `MainExecution` in AIMMS ausführen - Das Optimierungsprogramm läuft jetzt durch, ein Fenster zeigt den Progress an und die Map der Weboberfläche wird vorbereitet
6. Nachdem der Optimierer durchgelaufen ist, sind alle Variablen (z, r, ExcessCost und die **total_cost**) ausgefüllt
7. Mit dem Prozess `WriteSolution` lassen sich alle Variablenwerte des aktuellsten Durchlaufs in ein .csv-File exportieren
8. Anschließend kann das Python-File `generate_report.py`ausgeführt werden, welche die `solution.csv`einliest und Statistiken zusammenfasst und darstellt: 
   1. report_carriers.csv
   2. report_open_market.csv
   3. report_routes.csv
