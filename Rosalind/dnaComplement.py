DNA = open("C:/Users/Brandon/Downloads/rosalind_revc.txt").read()

reversedDNA = DNA[::-1]
trans1 = str.maketrans("ATCG", "TAGC")

complement = reversedDNA.translate(trans1)
with open("output.txt", "w") as file:
    file.write(complement)