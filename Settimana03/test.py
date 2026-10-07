totale = 0
numero = float(input("Dammi un numero: "))
contatore = 0

while totale >= 0:
    contatore += 1
    
    totale = totale + numero
    
    print (totale)
    
    numero = float(input("Dammi un numero: "))

#secondo test while metti numero negativo per accedere

finito = False
totale = 0
nunmero = float(input("Dammi un numero: "))
contatore = 0
if numero < 0:
    finito = True
    while not finito:
        contatore += 1
        totale = totale + numero
        print (totale)
        numero = float(input("Dammi un numero: "))
        if numero < 0:
            finito = True