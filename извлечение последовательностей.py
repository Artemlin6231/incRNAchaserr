import pandas as pd
df = pd.read_csv('mouse_chaserr_test.csv')
out_handle = open("example.txt", "w")
import re
from Bio import Entrez
from Bio import SeqIO

for rx in range(3,len(df['ID'])):
    print(df['ID'][rx])
    Entrez.email = "angeran73@gmail.com"
    in_handle = Entrez.efetch(db="gene", rettype="fasta", id=df['ID'][rx])
    print(in_handle)
    record = SeqIO.parse(in_handle, "fasta")
    SeqIO.write(record, out_handle, "fasta")
    in_handle.close()
out_handle.close()