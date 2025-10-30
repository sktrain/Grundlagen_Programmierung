# Gegeben ist der folgende Anfang eines Programms:

animals = ["tiger", "mouse", "bird", "python", "elephant", "monkey"]

# Ergänze das Programm so, dass für jedes Tier aus der Liste animals
# der Satz „… ist ein Tier“ in der Konsole
# ausgegeben wird. Benutze dafür die print() Funktion.

for animal in animals:
    print(animal, "ist ein Tier")

########################################################################

# Mit append() kannst du einer Liste ein Element hinten anfügen.
# Schreibe ein Programm, welches den Benutzer mit input() fünf mal nach
# einem Wort fragt und alle diese Worte in einer Liste abspeichert.
# Anschliessend werden alle Worte aus der Liste mit print() zurückgegeben.
#
# Erweiterung: Frage den Benutzer zuerst, wie viele Worte er eingeben will
# und frage dann genau so viel mal nach einem Wort.

liste = []
anzahl = int(input("Gewünschte Anzahl: "))
for x in range(anzahl):
    zahl = int(input("Zahl: "))
    liste.append(zahl)

# jetzt Ausgabe
print(liste)
# oder
for x in liste:
    print(x)

########################################################################

# Schreibe ein Programm welches n! für ein vom Benutzer vorgegebenes n berechnet.
# Benutze dafür eine for Schleife.

n = int(input("Für welche Zahl soll die Fakultät berechnet werden: "))
result = 1
for i in range(1,n+1):
    result = result * i
print("Fakultät von", n, "ist:", result)


###############################################################################

# Schreibe ein Programm, welches die folgende Ausgabe bis zu einer vom
# Benutzer gewählten Zahl fortsetzt:
#
# 1*
# 2**
# 3***
# 4****

anzahl = int(input("Anzahl: "))

for i in range(0,anzahl+1):
    s ="*"*i
    print(s)

