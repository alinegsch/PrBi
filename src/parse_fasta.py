import re


# Sheet 1
# Ex 1.1:
# input: fasta file, output: list of headers and list of sequences
def parse_fasta(path):
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


# Ex 1.2:
# input: list of strings, output: list of strings but only with dna-letters
def discard_ambiguous_seqs(strings):
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


# Ex 1.3:
# input: list of strings, output: prints frequency of each dna-letter
def nucleotide_frequencies(strings):
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


# Ex 1.4:
# input: two fasta files, first -> short read sequences, second -> containing reference sequences
# output: dictionary of dictionaries, where the outer dictionary uses the names of query sequences as its keys, and the
# inner dictionary uses reference sequence names as keys and a list of 1-based indices indicating at which position
# (counting from left to right) in the reference sequence the query sequence occurs
def map_reads(FASTA_1, FASTA_2):
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


# local main method
# input: two fasta files
# output: prints frequency of dna-letters
if __name__ == '__main__':
    map_reads(r"/Users/Aline/Desktop/21HS/21HS PrBi/PrBi Alexander Kanitz/PrBi/RNA-Seq/Test files/sequences.fasta",
              r"/Users/Aline/Desktop/21HS/21HS PrBi/PrBi Alexander Kanitz/PrBi/RNA-Seq/Test files/genome.fasta")
