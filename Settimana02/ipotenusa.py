# Calcolo ipotenusa

from math import sqrt

sa = input("Cateto 1: ")
a = float(sa)

b = float(input("Cateto 2: "))

c = sqrt ( a*a + b*b )

print(a, b, c)
