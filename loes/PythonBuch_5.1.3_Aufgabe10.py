# Der Computer „würfelt“ eine Zufallszahl zwischen 1 und 6 (Grenzen inklusive).
# Der Spieler versucht nun, die gewürfelte Zahl zu erraten.
# Bestimme mit einem Programm, wie viele Versuche dazu nötig sind.

import random

geraten = int(input("Geben Sie eine ganze Zahl zwischen 1 und 6 ein: "))
anzahlWuerfe = 0
zahl = 0

while zahl != geraten:
    zahl = random.randint(1, 6)
    anzahlWuerfe = anzahlWuerfe + 1
    print("Aktuelle Zahl:", zahl, "mit Wurf Nr.", anzahlWuerfe)

print("Diesmal haben wir", anzahlWuerfe, "Würfe für die geratene Zahl", geraten, "benötigt")