# Sostituire, in una stringa tutte le cifre 
# numeriche con il numero successivo 
# (es. ogni 3 diventa 4, il 9 diventa 0)

# abc4!56kk
# abc5!67kk

s = input("Stringa: ")

nuova = ""

for ch in s:
    if ch.isdigit():
        if ch=='9':
            nch = '0'
        else:
            nch = str(int(ch) + 1)
            nch = str((int(ch) + 1)%10)

    else:
        nch = ch

    nuova = nuova + nch

