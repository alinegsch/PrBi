from pathlib import Path

from src.sam_to_fasta_file import sam_to_fasta_file


def test_sam_to_fasta_file():
    """ test for funtion sam_to_fasta_file()
    tests samples if the new created fasta file has correct format
    """
    sam_to_fasta_file(str(Path(__file__).parents[0] / "test_files/Aligned.out.sam"))
    with open(str(Path(__file__).parents[0] / "test_files/fasta_converted_from_sam_file.fasta")) as fh:
        data = fh.readlines()
    assert data[0][0] == '>'
    assert data[12][1:9] == 'NS500637'
    assert data[13][0:4] == 'GTCA'
