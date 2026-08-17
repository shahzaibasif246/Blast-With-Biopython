#!/usr/bin/bash

blastp -db swissprot/swissprot -query ./data/Hypothetical-Protein-Sequence/hypothetical-protein-sequences.faa -out ./data/Blast-result-loweval-title.tsv -evalue 1e-10 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qcovs stitle" -num_threads 8
