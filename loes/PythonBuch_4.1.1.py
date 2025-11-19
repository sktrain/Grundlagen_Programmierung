# Angenommen, du hast pro Semester vier Prüfungen in einem Fach.
# Nun sind drei dieser Prüfungen vorbei und du möchtest wissen,
# welche Note du in der vierten Prüfung haben musst, um deinen
# Wunschschnitt zu erreichen.
#
# Schreibe ein Programm, welches dir diese Frage beantwortet.
# Benutze vier Variablen um die drei Noten und den Wunsch-Durchschnitt
# abzuspeichern und lasse das Programm daraus die letzte Note berechnen,
# welche du brauchst, um den Wunsch-Durchschnitt zu erreichen.
# Diese kannst du mit dem print() Befehl ausgeben.

note1 = 2   # float(input("erste Note: "))
note2 = 3   # float(input("zweite Note: "))
note3 = 4   # float(input("dritte Note: "))
durchschnitt = 3.0 # float(input("gewünschter Durchschnitt: "))

# Formel (note1 + note2 + note3 + x ) / 4 = durchschnitt
x = durchschnitt * 4 - (note1 + note2 + note3)

print("notwendige 4.Note:", x)



# Schreibe ein Programm, welches eine Zeitangabe in Stunden, Minuten und Sekunden
# in die Anzahl Sekunden insgesamt umrechnet
std = 10
min = 30
sek = 30
print("Zeit in Sekunden:", 30 + 30 * 60 + 10 * 60 * 60)


#Eine Werkstatt verlangt für die Benützung einer Maschine eine Grundgebühr
# von 60 Franken sowie 35 Fanken pro Stunde.
# Man überlege sich, welche Daten einzugeben und wel che Daten zu berechnen sind
# und erstelle ein passendes Programm.

stunden = int(input("Anzahl Stunden: "))
print("Preis:", 60 + 35 * stunden, "Franken")


#Ein Kleinunternehmen stellt seinen Kunden für Transporte einen Lieferwagen und
# einen Lastwagen zur Verfügung. Für Transporte mit dem Lieferwagen werden
# Fr. 1.60 pro Kilometer verrechnet, für den Lastwagen beträgt der Tarif
# Fr. 2.80 pro Kilometer. Welche Gebühr hat ein Kunde zu bezahlen, wenn der
# Lieferwagen 85 km und der Lastwagen 120 km zurückgelegt hat?

result = 1.6 + 85 + 2.8 * 120
print("Preis:", result, "Franken")



# Ein Weinhändler verkauft Rotwein zu 18 Franken pro Flasche, Roséwein zu 13
# und Weisswein zu 12 Franken pro Flasche.
# Ein Kunde bestellt (beispielsweise) 12 Flaschen Rotwein, 6 Flaschen Rosé
# und 24 Flaschen Weisswein.
# Schreibe ein Programm, welches den Gesamtpreis berechnet.

result = 12*18 + 6*13 + 24*12
print("Preis:", result, "Franken")



