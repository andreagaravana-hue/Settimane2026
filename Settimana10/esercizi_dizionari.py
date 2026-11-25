numeri = {
    1 : "primo",
    2 : "secondo",
    3 : "terzo"
}

print(numeri[1]) #1 non è l'indice ma la chiave

if 0 in numeri.keys():
    print(numeri[0])
else:
    print("Chiave non presente")

print(numeri.get(0, "chiave mancante"))

for elemento in numeri.items(): #dict.items() per stamapare tutte le tuple
    print(elemento)

for chiave, valore in numeri.items(): 
    print(valore)
    