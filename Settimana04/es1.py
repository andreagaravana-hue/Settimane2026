#Inserire un numero intero positivo. 
#Se non fosse positivo, ripetere la richiesta.

x = int (input("Inserire un numero intero positivo: "))
while x <= 0:
    x = int (input("Il numero inserito non è positivo. Inserire un numero intero positivo: "))