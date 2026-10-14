#- Inserire 10 numeri interi. 
# Calcolare il valore dato dalla somma di tutti i numeri pari, meno la somma di tutti i numeri dispari

i = 0
somma_pari = 0
somma_dispari = 0

while i < 10:
    x = int (input ("Inserire un numero intero: "))
    if x % 2 == 0:
        somma_pari = somma_pari + x
    else: 
        somma_dispari = somma_dispari + x
    i = i + 1


differenza = somma_pari - somma_dispari
print ("Il valore della differenza tra la somma dei numeri pari e la somma dei numeri dispari è: ", differenza)