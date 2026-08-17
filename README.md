# BLAST on hypothetical proteins in Acidobacterium genome found on NCBI

This was a script I wrote to become more familiar with Biopython  

Parse-Annotated-Genbank gets the hypothetical proteins translation sequences in the Genbank file. They are used to create SeqRecord Objects. This object is stored in a list, which is Used to create a FASTA file.  

Blastp.sh is used to run the BLAST+ command line tool using swissprot database.  

I had also tried to use Biopython to directly BLAST the proteins and store the results in a SQL database. However, this turned out to be very slow, so I used BLAST+ instead.
