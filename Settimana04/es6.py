# Dire se una stringa contiene almeno una 
# lettera maiuscola 

s = input()

maiuscola = False
for ch in s:
    if ch.isupper():
        maiuscola = True

if maiuscola:
    print("esiste una maiuscola")
else:
    print("non ci sono maiuscole")


# Dire se una stringa contiene al suo interno 
# due spazi consecutivi

spaziodoppio = False
for i in range(len(s)):
    if i>0 and s[i] == ' ' and s[i-1] == ' ':
        spaziodoppio = True

if spaziodoppio:
    print("Ci sono spazi doppi")

for i in range(1, len(s)):
    if s[i] == ' ' and s[i-1] == ' ':


if s[i:i+2] == "  "
if s[i-1:i+1] == "  "



import string
if ch is string.punctuation: 