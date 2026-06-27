def dna_to_rna(dna_sequence):
    rna_sequence = dna_sequence.upper().replace('T', 'U')
    return rna_sequence


DNA = input("Enter the DNA sequence: ")
RNA = dna_to_rna(DNA)

print("your DNA: ", DNA)
print("your RNA: ", RNA)
