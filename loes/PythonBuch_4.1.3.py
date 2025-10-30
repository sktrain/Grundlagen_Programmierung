# Lies das folgende Programm und versuche zu erraten, was die Ausgabe ist.
# Probiere es anschliessend aus und suche nach einer Erklärung des Verhaltens.

liste_a = ['Hallo', 'schönes', 'Wetter']
liste_b = liste_a   # beide Variablen zeigen auf das gleiche Objekt im Speicher !!

# Ändert man das Objekt anhand der einen Variablen,
# ist die Änderung auch über die andere Variable sichtbar!
liste_b[1] = 'schlechtes'
print(liste_a[0], liste_a[1], liste_a[2])

# Das nennt man Referenz-Semantik!!

#####################################################################################

# In einer früheren Aufgabe hast du ein Programm erstellt, welches eine feste Anzahl
# Noten einliest und anschliessend die notwendige Berechnung macht.
# Wir möchten dieses Programm nun anpassen, so dass die Noten in einer Liste gespeichert werden.

liste = []
note1 = float(input("erste Note: "))
note2 = float(input("zweite Note: "))
note3 = float(input("dritte Note: "))
liste.extend([note1, note2, note3])

durchschnitt = float(input("gewünschter Durchschnitt: "))

# Formel (note1 + note2 + note3 + x ) / 4 = durchschnitt
x = durchschnitt * 4 - (note1 + note2 + note3)

print("notwendige 4.Note:", x)


# Es geht auch folgende Variante
eingabe = input("Gib die bisherigen Noten als Liste ein: ")  # z.Bsp. [ 2.0, 2.0, 3.4 ]
noten = eval(eingabe)
# nur zum Test: print(noten)
durchschnitt = float(input("gewünschter Durchschnitt: "))

# Formel (note1 + note2 + note3 + x ) / 4 = durchschnitt
x = durchschnitt * 4 - sum(noten)

print("notwendige 4.Note:", x)
