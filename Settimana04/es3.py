#- Contare il numero di lettere maiuscole in una stringa

i = 0
m = 0
stringa = input("Inserire una stringa: ")

while i < len(stringa):
    if stringa[i].isupper():
        m = m + 1
    i += 1

print ("Il numero di lettere maiuscole nella stringa è: ", m)

#oppure con for

for i in range (len(stringa)):
    if stringa[i].isupper():
        m = m + 1

print ("Il numero di lettere maiuscole nella stringa è: ", m)