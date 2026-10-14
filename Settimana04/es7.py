#Cancellare tutte le lettere maiuscole dalla stringa inserita dall'utente

stringa = input("Inserire una stringa: ")

i = 0


while i < len(stringa):
    if stringa[i].isupper():
        stringa[i] = str ("")
    i += 1

print ("La stringa senza lettere maiuscole è: ", stringa)




#Sostituire  tutte le cifre numeriche con il numero successivo

i = 0

while i < len(stringa):
    if stringa[i].isdigit():
        stringa[i] = str (int (stringa[i]) + 1)
    i += 1