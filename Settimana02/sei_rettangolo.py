import math

a = float(input("Cateto numero 1: "))
b = float(input("Cateto numero 2: "))
c = float(input("Ipotenusa: "))


print(a*a + b*b)
print(c*c)
if math.isclose(a*a + b*b, c*c):
    print("È un triangolo rettangolo ")
else:
    print("Non è un triangolo rettangolo")