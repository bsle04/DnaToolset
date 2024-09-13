#Testing toolkit code
from dnatoolkit import *

DNA = open("C:/Users/Brandon/Downloads/rosalind_dna.txt").read()

if validateSequence(DNA):
    ACGTcount = countNucleotides(DNA)

for i in ACGTcount:
    print(i)