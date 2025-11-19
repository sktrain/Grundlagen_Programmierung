# Schreibe ein Programm, welches mit input() zwei Zahlen vom Benutzer einliest und den
# grössten gemeinsamen Teiler der beiden Zahlen mit print() ausgibt.
# Dazu kannst du den Euklidischen Algorithmus benutzen, welchen du entweder aus dem
# Mathematikunterricht kennst oder sonst sicher im Internet findest.
from contextlib import nullcontext

# GGT nach Euklid:
# Eingabe: a, b ∈ N
# 1 solange b ≠ 0
# 2     wenn a > b
# 3         dann a = a - b
# 4         sonst b = b - a
# Ausgabe: a

# die zusätzlichen Variablen braucht man nur, um am Ende noch die eingegebenen Werte zu haben
zahl1 = int(input("Gib erste Ganzzahl ein: "))
zahl2 = int(input("Gib zweite Ganzzahl ein: "))

a = zahl1
b = zahl2
while b != 0:
    if a > b:
        a = a-b
    else:
        b = b-a

print("Der GGT von", zahl1, "und ", zahl2, "ist:", a)
