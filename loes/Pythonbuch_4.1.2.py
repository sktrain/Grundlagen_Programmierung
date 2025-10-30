# Benutzereingaben: Das folgende Programm liest eine Eingabe vom Benutzer
# ein und speichert dies in der Variable eingabe.
# Der Befehl input() liest immer Zeichenketten – nicht etwa Zahlen – ein.

eingabe = input("Gib einen Text ein: ")

# Erweitere das Programm so, dass auch die folgenden Schritte ausgeführt werden:
# Der erste Buchstabe der Benutzereingabe wird in Grossbuchstaben konvertiert.
# Dem Text wird ein Ausrufezeichen angehängt.
# Ergebnis wird mit print() auf dem Bildschirm ausgegeben.

ergebnis = eingabe.upper()+"!"
print(ergebnis)

##################################################################################

# Schreibe ein Programm, welches vom Benutzer zwei ganze Zahlen einliest
# und anschliessend die Summe der beiden Zahlen ausgibt.

zahl1 = int(input("Gib Zahl1 ein: "))
zahl2 = int(input("Gib Zahl2 ein: "))
print("Ergebnis ist:", zahl1+zahl2)

#################################################################################

#Eine Werkstatt verlangt für die Benützung einer Maschine eine Grundgebühr
# von 60 Franken sowie 35 Fanken pro Stunde.
# Man überlege sich, welche Daten einzugeben und wel che Daten zu berechnen sind
# und erstelle ein passendes Programm.

stunden = int(input("Anzahl Stunden: "))
print("Preis:", 60 + 35 * stunden, "Franken")