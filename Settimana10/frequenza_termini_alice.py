import string

conta_parole = dict()

def conta_occorrenze(file):
    with open ("alice_in_wonderland.txt", "r", encoding = "utf-8") as f:
        dizionario_righe = dict()
        riga = f.readline()
        while riga != "":
            riga = riga.replace("--", " ")
            riga = riga.replace("-", " ")
            riga = riga.lower()
            
            parole_riga = riga.lower().strip(string.punctuation).rstrip().split()
            for parola in parole_riga:
                if parola not in conta_parole.keys():
                    conta_parole[parola] = 1
                else:
                    conta_parole[parola] += 1
            
            riga = f.readline()
        print (conta_parole)
        return conta_parole

conta_occorrenze ("alice_in_wonderland.txt")