from parse_fasta import parse_fasta, discard_ambiguous_seqs, nucleotide_frequencies, map_reads


def test_parse_fasta():
    """ test for funtion parse_fasta()
    tests if it returns right headers
    """
    arr = parse_fasta(r"/Users/Aline/Desktop/21HS/21HS PrBi/PrBi Alexander Kanitz/PrBi/RNA-Seq/Test files/genome.fasta")
    assert arr[0][0] == 'chr1'
    assert arr[0][1] == 'chr2'
    assert arr[0][2] == 'chr3'
    assert arr[0][3] == 'chr4'


def test_discard_ambiguous_seqs():
    """ test for funtion discard_ambiguous_seqs()
    tests if function recognizes wrong letters and is able to check capitalized and lowercase letters
    """
    wrong_letters = discard_ambiguous_seqs(['TAT', 'SSSSSSSNAKE', 'GACCTATGTGTCCGGTAAC', 'GAGA'])
    assert wrong_letters == ['TAT', ' ', 'GACCTATGTGTCCGGTAAC', 'GAGA']

    capitalized_lowercase = discard_ambiguous_seqs(['ccCcT', 'GCtAtTgTTAG', 'ATAgccca', 'GooooOoAt'])
    assert capitalized_lowercase == ['ccCcT', 'GCtAtTgTTAG', 'ATAgccca', ' ']


def test_nucleotide_frequencies(capsys):
    """ test for funtion nucleotide_frequencies()
    tests if function prints corr calculated frequencies out
    """
    nucleotide_frequencies(['TAT', 'GACCTATGTGTCCGGTAAC', 'GAGA'])
    captured = capsys.readouterr()
    assert captured.out == 'A: 0.27\nC: 0.19\nG: 0.27\nT: 0.27\n'


def test_map_reads():
    """ test for funtion map_reads()
    tests if function returns correct index of the position of the substring
    """
    dic = map_reads(r"/Users/Aline/Desktop/21HS/21HS PrBi/PrBi Alexander Kanitz/PrBi/RNA-Seq/Test files/sequences.fasta",
                    r"/Users/Aline/Desktop/21HS/21HS PrBi/PrBi Alexander Kanitz/PrBi/RNA-Seq/Test files/genome.fasta")
    assert dic['sequence1']['chr1'] == [759]
    assert dic['sequence2']['chr2'] == [1422]
    assert dic['sequence4']['chr2'] == [1039]
    assert dic['sequence4']['chr3'] == [1422]
    assert dic['sequence4']['chr4'] == [1455]


if __name__ == '__main__':
    test_parse_fasta()
    test_discard_ambiguous_seqs()
    test_nucleotide_frequencies()
    test_map_reads()
