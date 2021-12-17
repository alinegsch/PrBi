import re


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
    print('A: ' + str(round(float(a)/float(total_sequences), 2)))
    print('C: ' + str(round(float(c)/float(total_sequences), 2)))
    print('G: ' + str(round(float(g)/float(total_sequences), 2)))
    print('T: ' + str(round(float(t)/float(total_sequences), 2)))

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

if __name__ == '__main__':
    map_reads(r"/Users/Aline/Desktop/21HS/21HS PrBi/PrBi Alexander Kanitz/PrBi/RNA-Seq/Test files/sequences.fasta",
              r"/Users/Aline/Desktop/21HS/21HS PrBi/PrBi Alexander Kanitz/PrBi/RNA-Seq/Test files/genome.fasta")