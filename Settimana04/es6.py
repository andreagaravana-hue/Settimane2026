#Dire se una stringa contiene almeno una lettera maiuscola

i = 0
stringa = input("Inserire una stringa: ")
maiuscola = False

while i < len(stringa):
    if stringa[i].isupper():
        print ("La stringa contiene almeno una lettera maiuscola")
        maiuscola = True
        break
    i += 1

if maiuscola == False:
    print ("La stringa non contiene lettere maiuscole")
