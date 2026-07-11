from Bio import Blast
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

import os

#os.chdir("/home/shahzaib/Desktop/Functional-Annotation")

translation_sequences = list()

for seq_record in SeqIO.parse("./data/Original-Sequences/genomic.gbff", "genbank"):
    for feature in seq_record.features:
        if feature.type == "CDS" and feature.qualifiers["product"][0] == "hypothetical protein":
            rec = SeqRecord(
                Seq(feature.qualifiers['translation'][0]),
                id=str(feature.qualifiers['locus_tag'][0]))
            translation_sequences.append(rec)

SeqIO.write(translation_sequences, './data/Hypothetical-Protein-Sequence/hypothetical-protein-sequences.faa', "fasta")




