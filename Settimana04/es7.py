# Cancellare tutte le lettere maiuscole da una stringa

s = input("Stringa: ")
# ciaOOOOO a tuttiiIIII
# cia a tuttii

nuova = ""
for ch in s:
    if not ch.isupper():
        nuova = nuova + ch

print(nuova)