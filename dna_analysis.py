Eva = ["TGAAGGACCTTC", "AAAACCTCA", "TTAGCTATCGC", "TTGTGGTGGC", "AGGCCTCA"]
Larisa = ["TGAAGGACCTTC", "AAAACCTCA", "GCCAGTGCCG", "AAGTAGTGAC", "AGGCCTCA"]
Matej = ["TGCAGGAACTTC", "AAAACCTCA", "CCAGCAATCGC", "TTGTGGTGGC", "AGGCCTCA"]
Miha = ["TGCAGGAACTTC", "AAAACCTCA", " GCCAGTGCCG", "GGGAGGTGGC",  "GCCACGG"]

with open('dna.txt', 'r') as dna_file:
    sample = dna_file.read()

while True:
    if Eva[0] and Eva[1] and Eva[2] and Eva[3] and Eva[4] in sample:
        print("Eva did it")
        break
    elif Larisa[0] and Larisa[1] and Larisa[2] and Larisa[3] and Larisa[4] in sample:
        print("Larisa did it")
        break
    elif Matej[0] and Matej[1] and Matej[2] and Matej[3] and Matej[4] in sample:
        print("Matej did it!")
        break
    elif Miha[0] and Miha[1] and Miha[2] and Miha[3] and Miha[4] in sample:
        print("Miha did it!")
        break
