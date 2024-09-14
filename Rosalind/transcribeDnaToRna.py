DNA = open("C:/Users/Brandon/Downloads/rosalind_rna.txt").read()
RNA = DNA.replace('T', 'U')

with open("output.txt", "w") as file:
    file.write(RNA)