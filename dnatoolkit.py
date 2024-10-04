#DNA Toolkit File
from structures import *

#checks if given sequence is valid, if so returns the sequence with ensured capitalization, if not, returns false
def validateSequence(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            return False
    return tmpseq

#alternative to below function, using dictionary
def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

#From a given dataset containing DNA, generate the counts of ACGT
def countNucleotides(dna_seq):
    ACGTcount = [dna_seq.count("A"), dna_seq.count("C"), dna_seq.count("G"), dna_seq.count("T")]
    return ACGTcount

#Transcribes DNA to RNA
def transcribe(seq):
    return seq.replace("T", "U")

def reverse_complement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

#same function as above but more understandable/readable
def reverse_complement_alt(seq):
    comp = ''
    for nuc in seq:
        comp += (DNA_ReverseComplement[nuc])
    reverseComp = comp[::-1] #reverses a string
    return reverseComp