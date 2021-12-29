from src import parse_fasta


def sam_to_fasta_file(path):
    # type: (file) -> None
    """ Sheet 2, exercise 2.2: function reads fasta file, writes data to a sam file format
            Args:
                path: fasta file
        """
    converted_fasta = 'fasta_converted_from_sam_file.fasta'
    with open(converted_fasta, 'w') as out:
        with open(path, 'r') as fh:
            data = fh.readlines()
        for line in data:
            if line[0] != '@':
                sam_split = line.split("\t")
                if sam_split[9][0] == 'A' or sam_split[9][0] == 'C' or sam_split[9][0] == 'G' or sam_split[9][0] == 'T':
                    out.write(">" + sam_split[0] + "\n")
                    out.write(sam_split[9] + "\n")
