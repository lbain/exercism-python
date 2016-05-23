def distance(dna_1, dna_2):
    mutation_count = 0
    for nucleotide_1, nucleotide_2 in zip(dna_1, dna_2):
        if nucleotide_1 != nucleotide_2:
            mutation_count += 1
    return mutation_count
