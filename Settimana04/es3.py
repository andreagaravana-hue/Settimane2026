# - Contare il numero di lettere maiuscole 
# in una stringa

s = input("Parola: ")

i = 0
maiuscole = 0
while i < len(s):
    if s[i].isupper():
        maiuscole = maiuscole + 1

print(maiuscole)

maiuscole = 0
for i in range(len(s)):
    if s[i].isupper():
        maiuscole = maiuscole + 1

maiuscole = 0
for ch in s:
    if ch.isupper():
        maiuscole = maiuscole + 1
