# Modul mit simplen mathematischen Funktionen

# Berechnung der Summe natürlicher Zahlen via Schleife
def gauss_1(n):
    if n<0 :
        raise Exception("keine nagativen Ganzzahlen erlaubt")
    else:
        result = 0
        for i in range(1, n+1):
            result = result+i
    return result


# Berechnung der Summe natürlicher Zahlen via Formel nach Gauss
def gauss_2(n):
    if n<0 :
        raise Exception("keine nagativen Ganzzahlen erlaubt")
    else:
       return int(n * (n+1) / 2)


# Berechnung des Produkts natürlicher Zahlen (Fakultaet) via Schleife
def fak(n):
    if n<1 :
        raise Exception("keine Ganzzahlen < 1 erlaubt")
    else:
        result = 1
        for i in range(1, n + 1):
            result = result * i
    return result


# Berechnung des Produkts natürlicher Zahlen (Fakultaet) via Rekursion
def fakrek(n):
    if n<1 :
        raise Exception("keine Ganzzahlen < 1 erlaubt")
    elif n == 1:
        return 1
    else:
        return n * fakrek(n-1)


print(gauss_1(10))
print(gauss_2(10))
# print(gauss_2(-10))
print(fak(5))
print(fakrek(5))