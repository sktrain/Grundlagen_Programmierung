# Für Vergleiche, ob etwas grösser oder kleiner ist, können die in der Mathematik üblichen Zeichen
# < und > benutzt werden.
# Schreibe ein Programm, welches die folgenden Schritte ausführt:
#
#     Es wird vom Benutzer per input() eine Zahl eingelesen.
#
#     Es wird geprüft, ob die Zahl grösser oder kleiner als 10 ist.
#
#     Mit dem Befehl print() wird entsprechend entweder „Die Zahl ist grösser als 10“
#     oder „Die Zahl ist kleiner als 10“ ausgegeben.

eingabe = float(input("Zahl: "))

if eingabe >= 10:
    print("Die Zahl ist grösser oder gleich 10")
else:
    print("Die Zahl ist kleiner 10")



####################################################################################################

# Schreibe ein Programm, welches vom Benutzer 10 Zahlen einliest und diese in einer Liste speichert.
# Anschliessend soll das Minimum und das Maximum der Zahlen aus der liste bestimmt und ausgegeben werden.

liste = []
for i in range(10):
    liste.append(float(input("Zahl: ")))

# manuell
minimum = liste[0]
maximum = liste[0]
for zahl in liste:      # ein wenig ineffizient
    if zahl < minimum:
        minimum = zahl
    elif zahl > maximum:
        maximum = zahl
print("das Minimum ist:", minimum, "Das Maximum ist:",maximum)

# einfacher mit den fertigen Funktionen für max und min
print("das Minimum ist:", min(liste), "Das Maximum ist:",max(liste))



###################################################################################################

# Ob ein Jahr im Gregorianischen Kalender ein Schaltjahr ist, kann nach den folgenden Regeln entschieden werden:
#
#     Jahre sind Schaltjahre, falls ihre Jahrzahl durch 400 teilbar ist.
#
#     Jahre sind Schaltjahre, falls ihre Jahrzahl durch 4 teilbar ist, ausser die Jahrzahl ist durch 100 teilbar.
#
# Schreibe ein Programm, welches den Benutzer nach einer Jahreszahl fragt und anschliessend prüft,
# ob es sich um ein Schaltjahr handelt.

jahr = int(input("Jahr: "))

if jahr % 400 == 0:
    print(jahr, "ist Schaltjahr")
elif jahr % 4 == 0:
    if jahr % 100 == 0:
        print(jahr, "ist kein Schaltjahr")
    else:
        print(jahr, "ist Schaltjahr")
else:
    print(jahr, "ist kein Schaltjahr")


# oder besser und kompakter
jahr = int(input("Jahr: "))

if jahr % 400 == 0 or (jahr % 4 == 0 and jahr % 100 != 0):
    print(jahr, "ist Schaltjahr")
else:
    print(jahr, "ist kein Schaltjahr")

