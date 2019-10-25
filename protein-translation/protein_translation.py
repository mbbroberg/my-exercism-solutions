from textwrap import wrap

def proteins(strand):

    condons = {
        "AUG": "Methionine",
        "UUC": "Phenylalanine",
        "UUU": "Phenylalanine",
        "UUG": "Leucine",
        "UUA": "Leucine",
        "UCU": "Serine",
        "UCG": "Serine",
        "UCA": "Serine",
        "UCC": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
    }

    to_analyze = wrap(strand, 3)  # chunk strand into condons
    to_return = []  # build the response

    for sequence in to_analyze:
        if sequence in condons.keys():
            if condons[sequence] != "STOP":
                to_return.append(condons[sequence])
            else:
                return to_return            
    return to_return