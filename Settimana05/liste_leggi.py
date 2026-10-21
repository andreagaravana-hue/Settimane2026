#Inserisci 4 numeri interi e memorizzali in una lista

numeri = []  #lista vuota

for i in range (4):
    n = int (input ("Inserisci un numero intero: "))
    numeri.append (n)  #aggiungo il numero alla lista

print (numeri)

#calcola una lista che contenga il doppio dei valori appena letti

doppi =[]

for v in numeri:
    doppi.append (v * 2)

print ("Lista dei doppi: ", doppi)