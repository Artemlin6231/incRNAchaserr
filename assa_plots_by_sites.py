import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file = open('chaserr.txt', 'r')
mouse_align = [line.strip() for line in file]
mouse_align_str = ''.join(mouse_align)
file.close()
file = open('выравненный chaserr.txt', 'r')
mouse_conserve = []
for line in file:
    line=line.split()
    line.pop(5)
    line=''.join(line)
    mouse_conserve.append(line)
mouse_conserve = ''.join(mouse_conserve)
file.close()
def plot_sites_prob(rna_sites_file_csv,chaserr_align,mouse_conserve,caption_name):
    #rna_sites_file_txt - rnaup sites filename to work with
    #chaserr_align - alignment dictionary, also giving info of isoform/ortolog length
    #caption_name - filename for distribution caption, referring caption name, e.g. "chaserr_sites.png"
    rnaup_df=pd.read_csv(rna_sites_file_csv, sep="\t", header=0)
    #print(len(chaserr_align))
    full_seq=dict()
    full_seq1=dict()
    #print(len(rnaup_df))
    for i in range(1,len(chaserr_align)+1):
        full_seq[i]=0
        full_seq1[i]=0
    #print(full_seq)
    for i in range(1,len(rnaup_df)):
        #print(i)
        for j in range(rnaup_df["siteStart1"][i],rnaup_df["siteEnd1"][i]):
            full_seq[j]+=1
    for i in range(len(mouse_conserve)):
        if mouse_conserve[i].isupper():
            full_seq1[i]=200

    f, ax = plt.subplots(figsize=(20,8))
    width=1
    plt.bar(full_seq1.keys(), full_seq1.values(), width, color='b')
    plt.bar(full_seq.keys(), full_seq.values(), width, color='g')
    ax.set_xlabel('координаты chaserr')
    ax.set_ylabel('количество сайтов связывания координату')
    plt.savefig(caption_name)
plot_sites_prob("sites_all_to_make_plot.txt",mouse_align_str,mouse_conserve,"CHASERR_08_sites.png")
#print(len(mouse_align_str))
file = open('chaserr_gene', 'r')
chaserr_gene = [line.strip() for line in file]
chaserr_gene_str = ''.join(chaserr_gene)
file.close()
file = open('выровненый ген chaserr', 'r')
mouse_gen_conserve = []
for line in file:
    line=line.split()
    line.pop(5)
    line=''.join(line)
    mouse_gen_conserve.append(line)
mouse_gen_conserve = ''.join(mouse_gen_conserve)
file.close()
full_seq2=dict()
for i in range(len(mouse_gen_conserve)):
    if mouse_gen_conserve[i].isupper():
        full_seq2[i] = 200

f, ax = plt.subplots(figsize=(20, 8))
width = 1
plt.bar(full_seq2.keys(), full_seq2.values(), width, color='g')
ax.set_xlabel('координаты chaserr гена')
ax.set_ylabel('места консервативности ')
plt.savefig('консервативность chaserr.png')