#Testing toolkit code
from dnatoolkit import *
from utilities import colored
import random

#DNA = open("C:/Users/Brandon/Downloads/rosalind_dna.txt").read()
tempDNA = ''.join([random.choice(nucleotides) for nuc in range (50)])
DNA = validateSequence(tempDNA)

print(f'\nSequence: {colored(DNA)}\n')
print(f'[1] Sequence Length: {len(DNA)}\n')
print(colored(f'[2] Nucleotide Frequency: {countNucleotides(DNA)}\n'))

print(f'[3] DNA/RNA Transcription: {colored(transcribe(DNA))}\n')
print(f"[4] DNA String + Reverse Complement:\n5' {colored(DNA)} 3'")
print(f"   {''.join(['|' for c in range(len(DNA))])}")
print(f"3' {colored(reverse_complement(DNA))} 5'\n")