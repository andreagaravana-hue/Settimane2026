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


#per dire se ci sono 2 segni di punteggiatura consecutivi
i = 0
punteggiatura = False

while i < len(stringa) - 1:
    if stringa[i] in ".,;:!?":
        if stringa[i + 1] in ".,;:!?":
            print ("La stringa contiene 2 segni di punteggiatura consecutivi")
            punteggiatura = True
            break
    i += 1

if punteggiatura == False:
    print ("La stringa non contiene 2 segni di punteggiatura consecutivi")