a = [3, 5, 12, -5, 8, 44, -12, 0, 1]

print (len(a))

print ()

print (a)

print ()

for i in range (len(a)):
    print (a[i])

print () 

for v in a:
    print ("*", v)

for i, v in enumerate(a):
    print ("Alla posizione ", i, " c'è il valore ", v)

#incremento tutti i numeri della lista "a" di 1 unità

print ("Lista dopo l'incremento:")

for i in range (len(a)):
    a[i] += 1

print (a)

