# inserito il vlore di -1
#calcola e stampa una lista ottenuta 
# cancellando dalla lista di partenza tutti i numeri maggiori di 5

numeri = []

dato = int (input ("Dato: "))
while dato != -1:
    numeri.append (dato)
    dato = int (input ("Dato: "))

print (numeri)

i = 0

while i < len(numeri):
    if numeri[i] > 5:
        print ("Devo cancellare il numero ", numeri[i], " alla posizione ", i)
        numeri.pop(i) #comando per cancellare un elemento dalla lista
    else:
        i += 1
print (numeri)

#oppure per aggirare il problema di cambiare la lunghezza della lista 
#durante l'iterazione, si può fare così:

i = len(numeri) - 1
while i >= 0:
    if numeri[i] > 5:
        print ("Devo cancellare il numero ", numeri[i], " alla posizione ", i)
        numeri.pop(i) #comando per cancellare un elemento dalla lista
    i -= 1
print (numeri)

#con il for

for i in range (len(numeri) - 1, -1, -1):
    if numeri[i] > 5:
        print ("Devo cancellare il numero ", numeri[i], " alla posizione ", i)
        numeri.pop(i) #comando per cancellare un elemento dalla lista
print (numeri)

#oppure...

altri = []

for v in numeri:
    if v <= 5:
        altri.append (v)    
print (altri)  