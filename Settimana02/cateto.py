# Calcolo ipotenusa

from math import sqrt

a = float(input("Cateto 1: "))

c = float(input("Ipotenusa: "))

if a>0 and c>0:

    if a > c:
        print("Il cateto non deve essere più lungo dell'ipotenusa")
        print("Non è un triangolo valido")

    if a<=c:
        b = sqrt(c*c - a*a)
        print(a, b, c)

else:
    print("Il cateto deve essere un valore positivo")