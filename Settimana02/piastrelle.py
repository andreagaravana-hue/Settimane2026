# Esercizio "Piastrelle"

"""
Ipotesi aggiuntive:
    Le piastrelle sono quadrate
    Piastrelle bianche e nere hanno la stessa dimensione
    In senso verticale c'è abbastanza spazio

Valori in INPUT:
    Lunghezza totale del muro (lun_muro)
    Lunghezza della piastrella (lun_piast)

Valori in OUTPUT:
    Numero di piastrelle bianche e numero di piastrelle nere (bianche, nere)
    Margine laterale tra le piastrelle all'estremità e il muro (margine)

Vincoli:
    Prima e ultima piastrella nere
    Piastrelle di colore alternato
    Margine uguale alle due estremità (può anche essere 0.0)
"""

"""
ESEMPIO

Muro: 100 cm
Piastrella: 33 cm

2 nere, 1 bianca, margine 0.5 cm

Muro: 100 cm
Piastrella: 25 cm

2 nere, 1 bianca, margine 12.5 cm

Muro: 100 cm
Piastrella: 20 cm

3 nere, 2 bianche, margine 0.0 cm

Muro: 100 cm
Piastrella: 80 cm

1 nera, 0 bianche, margine 10.0 cm

Muro: 50 cm
Piastrella: 80 cm

Impossibile
"""

"""
ALGORITMO

quante = int(lun_muro / lun_piast)

if quante è dispari:
    quante è giusto
else:
    quante viene decrementato di 1

NOTA: di sicuro 'quante' è dispari

bianche = int(quante/2) 
nere = bianche+1

margine = (lun_muro - (lun_piast * quante))/2

"""

print("Problema delle piastrelle")

lun_muro = float(input("Lunghezza del muro (cm): "))
lun_piast = float(input("Lunghezza piastrella (cm): "))

if lun_muro <= 0 :
    print("Il muro deve avere lunghezza positiva")
elif lun_piast <=0:
    print("La piastrella deve avere lunghezza positiva")
elif lun_piast>lun_muro:
    print("La piastrella non può essere più lunga del muro")
else:
    quante = int(lun_muro/lun_piast)
    # print(quante)

    if quante % 2 == 0 :  # è pari
        quante = quante - 1

    # print(quante)

    bianche = int(quante/2) 
    nere = bianche+1

    margine = (lun_muro - (lun_piast * quante))/2

    print("Numero di piastrelle bianche: ", bianche)

    print("Numero di piastrelle nere: ", nere)

    print("Margine da lasciare su ogni lato: ", margine, "cm")

