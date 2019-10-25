def to_rna(dna_strand):
    dna_in = str(dna_strand.upper())
    nucleotides = {"G": "C", "C": "G", "T": "A", "A": "U"}

    try:
        return "".join([nucleotides[s] for s in dna_in])
    except KeyError:
        raise ValueError("Invalid DNA strand provided: %s" % dna_in)