# Ein Würfel wird so lange geworfen, bis die Summe aller Würfe 100 oder mehr beträgt.
# Zum simulieren eines Würfels kannst du die Funktion randrange() aus dem Modul random benutzen.


#     b) Schreibe ein Programm, welches mit Hilfe einer Liste zählt, wie oft
#        welche Augenzahl geworfen wurde. Am Ende soll die Liste mit print() ausgegeben werden.
#
#     c) Ändere das Programm so ab, dass so lange gewürfelt wird, bis zum
#        ersten Mal eine Zahl 50 Mal geworfen wurde.
#        Gib an, wie oft die anderen Zahlen geworfen wurden.

import random
# besser randint() statt randrange() benutzen, da es um Ganzzahlen geht!

#------------------------------------------------------------------------------
# a) Bestimme mit einem Programm, wie viele Würfe dazu nötig sind.

anzahlWuerfe = 0
summe = 0

while summe < 100:
    zahl = random.randint(1, 6)
    summe = summe + zahl
    anzahlWuerfe = anzahlWuerfe + 1

print("Diesmal haben wir", anzahlWuerfe, "Würfe für eine Summe >=100 benötigt")

#-----------------------------------------------------------------------------
#   b) Schreibe ein Programm, welches mit Hilfe einer Liste zählt, wie oft
#      welche Augenzahl geworfen wurde. Am Ende soll die Liste mit print() ausgegeben werden.

# Idee: die Elemente der Liste sind die Zähler!
liste =  [0, 0, 0, 0, 0, 0]
summe = 0

while summe < 100:
    zahl = random.randint(1, 6)
    summe = summe + zahl
    liste[zahl - 1] = liste[zahl - 1] + 1    #Index von 0 - 5, zahl von 1 - 6

print(liste)

# anschaulicher:
for i in range(1,7):
    print("Zahl", i, "wurde so oft gewürfelt:", liste[i-1] )

#-------------------------------------------------------------------------------------
#     c) Ändere das Programm so ab, dass so lange gewürfelt wird, bis zum
#        ersten Mal eine Zahl 50 Mal geworfen wurde.
#        Gib an, wie oft die anderen Zahlen geworfen wurden.

# Idee: die Elemente der Liste sind die Zähler!
liste =  [0, 0, 0, 0, 0, 0]

while True:
    zahl = random.randint(1, 6)
    liste[zahl - 1] = liste[zahl - 1] + 1    #Index von 0 - 5, zahl von 1 - 6
    if liste[zahl - 1] == 50:
        break;

print(liste)

# anschaulicher:
for i in range(1,7):
    print("Zahl", i, "wurde so oft gewürfelt:", liste[i-1] )