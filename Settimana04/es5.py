# Acquisire 10 numeri interi.
#  Dopo averli acquisiti tutti, 
# dire se erano TUTTI PARI. 

conta = 0
for i in range(10):
    x = int(input("Numero: "))

    if x%2 == 0:
        conta = conta + 1 # conta quanti sono i pari

if conta==10:
    print("Tutti pari")
else:
    print("Qualche dispari")

##############

tutti_pari = True  # Flag

for i in range(10):
    x = int(input("Numero: "))

    if x%2 != 0:
        tutti_pari = False

if tutti_pari:
    print("Tutti pari")
else:
    print("Qualche dispari")

