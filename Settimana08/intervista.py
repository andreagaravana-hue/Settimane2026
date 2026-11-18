#conteggiare il numero di parole nel file intervistalinus.txt
#printare le domande fatte nell'intervista

infile = open ("intervistalinus.txt", "r", encoding="utf-8")
tot_parol=0
for riga in infile:
    parole=riga.split()
    print (len(parole))
    tot_parole = tot_parole + len(parole)
infile.close()


