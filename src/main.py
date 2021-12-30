from pathlib import Path

from src import parse_fasta
from src import sam_to_fasta_file

# this method starts the tasks for the whole exercise (1.4 and 2.2 to be precise)

if __name__ == '__main__':
    print(parse_fasta.map_reads(
        str(Path(__file__).parents[1] / "tests/test_files/sequences.fasta"),
        str(Path(__file__).parents[1] / "tests/test_files/genome.fasta"),
    ))
    sam_to_fasta_file.sam_to_fasta_file(
        str(Path(__file__).parents[1] / "tests/test_files/Aligned.out.sam"),
    )
    dict = parse_fasta.map_reads(
        'fasta_converted_from_sam_file.fasta',
        str(Path(__file__).parents[1] / "tests/test_files/genome.fasta"),
    )
    print(dict)

