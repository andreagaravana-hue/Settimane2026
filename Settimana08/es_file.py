outfile = open("output.txt", "w") #w : write
print(outfile)
outfile.write("Hello World!\n")
outfile.close()
#bisogna sempre chiudere perchè altrimenti non lo si può modificare in futuro perchè lo considera aperto


infile = open("output.txt", "r", encoding = "utf-8")
content = infile.read()
print(content)
infile.close()