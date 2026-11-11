durate = []
velocita = []
infile = open ("allenamenti.txt", "r", encoding = "utf-8")
for riga in infile: 
    riga_s = riga.split()
    durate.append(float(riga_s[1]))
    velocita.append(float(riga_s[2]))
infile.close()

print(durate)
print(velocita)

print("In totale questa settimana ti sei allenato ", str(sum(durate)), " minuti")

numeratore = 0
for i in range (len(durate)):
    numeratore = numeratore + durate[i] + velocita [i]

media_p = numeratore/sum(durate)

print(media_p)
