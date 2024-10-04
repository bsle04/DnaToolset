#DNA Toolkit File

nucleotides = ["A", "C", "G", "T"]

#checks if given sequence is valid, if so returns the sequence with ensured capitalization, if not, returns false
def validateSequence(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in nucleotides:
            print("Invalid DNA Sequence: " + nuc)
            return False
    print("Valid DNA Sequence.")
    return True

#From a given dataset containing DNA, generate the counts of ACGT
def countNucleotides(dna_seq):
    ACGTcount = [dna_seq.count("A"), dna_seq.count("C"), dna_seq.count("G"), dna_seq.count("T")]
    return ACGTcount

#Transcribes DNA to RNA
def transcribe(seq):
    return seq.replace("T", "U")

