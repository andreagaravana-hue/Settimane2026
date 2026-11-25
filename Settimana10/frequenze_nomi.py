nomi = ["Anna", "Mario", "Marta", "Andrea", "Anna", "Mario", "Gino", "Andrea"]

#insieme_nomi = set()
#conta_anna = 0

conte_nomi = dict()

for nome in nomi:
    #if nome == "Anna"   HARD CODED
    #conta_anna += 1
    #insie_nomi.append(nome)
    #nome=nome.lower() per avere i nomi minuscoli
    if nome in conte_nomi.keys():
        conte_nomi[nome] = conte_nomi[nome] + 1
    else:
        conte_nomi[nome] = 1

print(conte_nomi)