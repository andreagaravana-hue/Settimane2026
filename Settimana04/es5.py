#Acquisire 10 numeri interi. e verificare se erqno Tutti Pari

i = 0
risultato = True #Flag per verificare se tutti i numeri sono pari

while i < 10:
    x = int (input("Inseirire un numero intero: "))
    if x % 2 == 0:
        risultato = True
    else:
        risultato = False
        break
    i += 1
if risultato == True:
    print ("Tutti i numeri inseriti sono pari")
else:
    print ("Non tutti i numeri inseriti sono pari")