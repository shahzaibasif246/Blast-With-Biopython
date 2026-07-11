from Bio import SeqIO
from Bio import Blast
import sqlite3
from time import sleep

con = sqlite3.connect("hypothetical-proteins-BLAST.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS status(
            locus_tag TEXT PRIMARY KEY,
            translation_sequence TEXT,
            status TEXT,
            error_msg TEXT,
            xml_path TEXT)""")



for seq_record in SeqIO.parse("./data/Hypothetical-Protein-Sequence/hypothetical-protein-sequences.faa", "fasta"):
    #cur.execute("""INSERT OR IGNORE INTO status(locus_tag, translation_sequence, status) VALUES(?, ?, ?)""", (seq_record.id, str(seq_record.seq), 'pending'))
    #con.commit()
    sleep(10)
    try:
        file_name = f'./data/BLAST-XML-Files/{seq_record.id}.xml'
        print(file_name)
        result_stream = Blast.qblast('blastp', 'swissprot', seq_record.seq)
        with open(file_name, "wb") as out_stream:
            out_stream.write(result_stream.read())
        result_stream.close()
        cur.execute("""UPDATE status SET error_msg = ?, xml_path = ?, status = ? WHERE locus_tag = ?""", ('na', file_name, 'complete', seq_record.id))
        con.commit()
        print("SUCCESS")
    except Exception as e:
        error_msg = str(e)
        print(error_msg)
        cur.execute("""UPDATE status SET error_msg = ? WHERE locus_tag = ?""", (error_msg, seq_record.id))
        con.commit()
        print('FAILURE')




#res = cur.execute("""SELECT * FROM status""")

#print(res.fetchall())
