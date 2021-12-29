import re


def parse_fasta(path):
    # type: (file) -> (list[str], list[str])
    """ Sheet 1, exercise 1.1: function reads fasta file and sorts sequences headers and actual sequence
        Args:
            path: fasta file
        Returns:
            two lists - first: headers, second: actual sequences
    """
    with open(path) as fh:
        data = fh.readlines()
    headers = []
    sequences = []
    sequence = []
    for line in data:
        line = line.replace('\n', "")
        if line.startswith(">"):
            line = line.replace('>', "")
            headers.append(line)
            sequences.append(''.join(sequence))
            sequence = []
        else:
            sequence.append(line)
    sequences.append(''.join(sequence))
    sequences.pop(0)
    return headers, sequences


def discard_ambiguous_seqs(strings):
    # type: (list[str]) -> (list[str])
    """ Sheet 1, exercise 1.2: function sorts not-dna-letter-strings out and replaces it with a space
            Args:
                strings: list of strings
            Returns:
                list of strings that only contains dna-letters
    """
    not_dna = []
    dna_letters = ['A', 'a', 'C', 'c', 'G', 'g', 'T', 't']
    for s in strings:
        for k in s:
            if not k in dna_letters:
                not_dna.append(strings.index(s))
                continue
            continue
    for i in reversed(not_dna):
        strings[i] = " "
    return strings


def nucleotide_frequencies(strings):
    # type: (list[str]) -> None
    """ Sheet 1, exercise 1.3: function counts total amount of each dna-letter and divides it with the total amount of
    letters to calculate the frequency to be printed out.
            Args:
                strings: list of strings
    """
    a = 0
    c = 0
    g = 0
    t = 0
    for s in strings:
        for k in s:
            if k == 'A' or k == 'a':
                a += 1
            elif k == 'C' or k == 'c':
                c += 1
            elif k == 'G' or k == 'g':
                g += 1
            elif k == 'T' or k == 't':
                t += 1
    total_sequences = a + c + g + t
    print('A: ' + str(round(float(a) / float(total_sequences), 2)))
    print('C: ' + str(round(float(c) / float(total_sequences), 2)))
    print('G: ' + str(round(float(g) / float(total_sequences), 2)))
    print('T: ' + str(round(float(t) / float(total_sequences), 2)))


def map_reads(FASTA_1, FASTA_2):
    # type: (file, file) -> dict
    """ Sheet 1, exercise 1.4: function runs previous functions, uses the data to create a dictionary of dictionaries,
    where the outer dictionary uses the names of query sequences as its keys, and the inner dictionary uses reference
    sequence names as keys and a list of 1-based indices indicating at which position (counting from left to right) in
    the reference sequence the query sequence occurs
            Args:
                FASTA_1: fasta file with short read sequences
                FASTA_2: fasta file with containing reference sequences
            Returns:
                dictionary
    """
    sequences = parse_fasta(FASTA_1)

    genomes = parse_fasta(FASTA_2)
    sequences_dna = discard_ambiguous_seqs(sequences[1])

    print('short read sequences: ')
    nucleotide_frequencies(genomes[1])
    print('reference sequences: ')
    nucleotide_frequencies(sequences_dna)

    dict = {}
    for s in range(len(sequences[1])):
        dict[sequences[0][s]] = {}
        for g in range(len(genomes[0])):
            index_list = [m.start() + 1 for m in re.finditer(sequences[1][s].upper(), genomes[1][g].upper())]
            if index_list:
                dict[sequences[0][s]].update({genomes[0][g]: index_list})
    return dict
