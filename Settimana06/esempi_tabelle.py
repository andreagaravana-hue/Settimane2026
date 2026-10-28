

tabella_medaglie = [
    [0, 3, 0],
    [0, 0, 1],
    [1, 0, 0],
    [3, 1, 1],
    [0, 1, 0]
]

prima_medaglia = tabella_medaglie[1][2]

print(prima_medaglia)


numero_righe = 5
numero_colonne = 5

tabella_zeri =[]

for riga in range(numero_righe):
    tabella_zeri.append([0] * numero_colonne)

tabella_zeri[2][2] = 1

for riga in tabella_zeri:
    print(riga)


#somma della riga i

i = 2
rowtotal = 0
for j in range (len(tabella_medaglie[0])):
    rowtotal = rowtotal + tabella_medaglie[i][j]
print(rowtotal)
