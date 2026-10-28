n_righe = 10
n_colonne = 10

griglia = []

for riga in range (n_righe):        #usando append che funziona nelle liste non potevo fare il contrario quindi si passa dalle righe
    griglia.append([0] * n_colonne)

for i in range (4,8):
    griglia[3][i] = 1

for riga in range (n_righe):
    for colonna in range (n_colonne):
        print(griglia[riga][colonna], end = " ")
    print()

i_elemento = 4
j_elemento = 5

conta_vivi = 0
for delta_i in range (-1, 2):  #-1  0  1
    for delta_j in range (-1,2):
        #print (griglia[i_elemento + delta_i][j_elemento + delta_j])
        if griglia[i_elemento + delta_i][j_elemento + delta_j] == 1:
            if not (delta_i == 0 and delta_j == 0):   #esclude l'elemento centrale
                conta_vivi += 1
print (conta_vivi)

