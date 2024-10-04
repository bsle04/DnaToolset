#Testing toolkit code
from dnatoolkit import *

DNA = open("C:/Users/Brandon/Downloads/rosalind_dna.txt").read()

print(f'\nSequence: {DNA}\n')
print(f'[1] + Sequence Length: {len(DNA)}\n')
print(f'[2] + Nucleotide Frequency: {countNucleotides(DNA)}\n')

print(f'[3] + DNA/RNA Transcription: {transcribe(DNA)}\n')