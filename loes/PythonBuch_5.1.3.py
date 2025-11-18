# Schreibe ein Programm, welches alle Zahlen von 1 bis 100 auf den Bildschirm schreibt,
# ohne dafür eine for Schleife zu verwenden.

i = 1   # Initialisierung

while i <= 100:
    print(i)
    i = i + 1


##############################################################################

# Aus dem Kapitel über die for Schleife kennst du das folgende Beispielprogramm:
#
# for zahl in [4,5,7,11,21]:
#
#     summe = zahl + 2
#
#     print("Wenn ich zu", zahl, "zwei addiere, erhalte ich", summe)
#
# print("Ich bin fertig!")
#
# Schreibe das Programm so um, dass es eine while Schleife anstelle der for Schleife benutzt.

liste = [4,5,7,11,21]

i = 0
while i < len(liste):
    summe = liste[i] + 2
    print("Wenn ich zu", liste[i], "zwei addiere, erhalte ich", summe)
    i = i + 1
print("Ich bin fertig!")

#######################################################################################

# Die Folge aus Fibonacci-Zahlen wird wie folgt gebildet:
#
#     Das erste und das zweite Element sind 0 und 1.
#
#     Jedes folgende Element wird gebildet, in dem die letzten zwei Elemente addiert werden.
#
# Das heisst, die Folge sieht so aus: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Schreibe ein Programm, welches die Fibonacci-Zahlen bis zu einer vom Benutzer gewählten Zahl ausgibt.

limit = int(input("Limit: "))

zahl1 = 0
zahl2 = 1
nextnumber = 0
print(zahl1)
print(zahl2)

while (nextnumber + zahl1) <= limit:
    nextnumber = zahl1 + zahl2
    print(nextnumber)
    zahl1 = zahl2
    zahl2 = nextnumber


############################################################################

# Der Wert einer Immobilie steigt jedes Jahr um Prozent an. Schreibe ein Programm,
# welches den Zeitwert dieser Immobilie so lange berechnet, bis der Zeitwert
# (mehr als) doppelt so gross ist wie der heutige Anfangswert.
# Frag den Benutzer nach dem Prozentsatz.

anfangswert = float(input("Anfangswert der Immobilie: "))
prozentsatz = float(input("Prozentsatz: "))

neuerwert = anfangswert

while neuerwert <= 2 * anfangswert:
    neuerwert = neuerwert * (1 + prozentsatz)
    print("Neuerwert: ", neuerwert)


#############################################################################

# Eine Firma kauft eine Maschine (der Einkaufspreis ist einzugeben), welche innert
# einiger Jahre (die Anzahl Jahre ist einzugeben) linear abgeschrieben wird.
#
# Beispieleingabe:
#     20000 (Fr. Einkaufspreis), 5 (Jahre)
# Beispielausgabe:#
#     Jahr 1: 16000.00 Jahr 2: 12000.00 Jahr 3: 8000.00 Jahr 4: 4000.00 Jahr 5: 0.00

wert = float(input("Einkaufpreis: "))
anzahlJahre = int(input("AnzahlJahre: "))
abschreibung = wert / anzahlJahre

i = 1
while i <= anzahlJahre:
    wert = wert - abschreibung
    print("Jahr " + str(i) + ": ", wert)
    i = i + 1

#########################################################################################

# Herr Spar legt sich jedes Jahr einen festen Betrag (z.B. 800.00 Fr.) auf sein Konto,
# welches beispielsweise Zins trägt. Er tut dies so lange, bis er einen bestimmten Betrag überschreitet.
# Dieser Betrag ist auch einzugeben, z.B. 5000.00. Schreibe dazu ein Programm.

betrag = float(input("Betrag: "))
zins = float(input("Zins: "))
limit = float(input("Limit: "))

guthaben = betrag
while guthaben <= limit:
    guthaben = guthaben * (1 + zins) + betrag
    print("Guthaben: ", guthaben)

######################################################################################

# Ein Gegenstand hat den Wert k (dieser Wert ist Eingabe). Erstelle ein Programm, welches
# für die nächsten Jahre (die Anzahl Jahre ist Eingabewert) den Zeitwert dieses Gegenstands berechnet,
# wenn jedes Jahr p Prozent des Werts abgeschrieben werden. (Der Abschreibungssatz ist auch einzugeben.)
# Diese Art Abschreibung heisst degressive Abschreibung.

wert = float(input("Anfangswert: "))
pozentsatz= float(input("Pozentsatz: "))
jahre = int(input("Jahre: "))

i = 1
while i <= jahre:
    wert = wert - wert * pozentsatz
    print("Jahr", i, "ist der Restwert:", wert)
    i = i + 1

#################################################################################








