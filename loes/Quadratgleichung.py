# argv.py
import math
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
print("Argumente", a, b, c )

if a == 0.0:    # b * x + c = 0  = > x = -c / b
    if b == 0.0:  # c = 0
        if  c == 0.0:
            print("Alle x sind Lösungen")
        else:
            print("Kein x erfüllt die Gleichung")
    else:
            print("x ist: ", -c/b)
elif (b * b - 4 * a * c) < 0.0:
    print("Kein x erfüllt die Gleichung")
else:
    x1 = ((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a))
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    print("Hier kommt der erste Wert: " , x1)
    print("Hier kommt der zweite Wert: " , x2)
