# - Inserire 10 numeri interi positivi.
#  Calcolare il valore dato dalla somma
#  di tutti i numeri in posizione pari, 
# meno la somma di tutti i numeri in 
# posizione dispari

somma = 0
for i in range(10):

    x = int(input("Numero: "))
    while x <= 0:
        print("Dovevi inserire un numero positivo")
        x = int(input("Numero: "))

    if i%2 == 0:
        somma = somma + x
    else:
        somma = somma - x

print(somma)