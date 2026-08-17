from Bio import SearchIO

data = './data/Blast-Result-title.tsv'

columns = "qseqid sseqid length qstart qend sstart send evalue bitscore"

for result in SearchIO.parse(data, 'blast-tab'):
    for hit in result:
        print(hit)
    break

