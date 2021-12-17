import parse_fasta
import sam_to_fasta_file

if __name__ == '__main__':
    print(parse_fasta.map_reads(
        r"/Users/Aline/Desktop/21HS/21HS PrBi/PrBi Alexander Kanitz/PrBi/RNA-Seq/Test files/sequences.fasta",
        r"/Users/Aline/Desktop/21HS/21HS PrBi/PrBi Alexander Kanitz/PrBi/RNA-Seq/Test files/genome.fasta"))
    sam_to_fasta_file.sam_to_fasta_file('Aligned.out.sam')
    dict = sam_to_fasta_file.parse_fasta.map_reads(
        'fasta_converted_from_sam_file.fasta',
        r"/Users/Aline/Desktop/21HS/21HS PrBi/PrBi Alexander Kanitz/PrBi/RNA-Seq/Test files/genome.fasta")
    print(dict)