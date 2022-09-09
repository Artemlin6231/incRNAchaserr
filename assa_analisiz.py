import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file = open('chaserr.txt', 'r')
mouse_align = [line.strip() for line in file]
mouse_align_str = ''.join(mouse_align)
file.close()
def plot_sites_prob(rna_sites_file_csv,chaserr_align,caption_name):
    #rna_sites_file_txt - rnaup sites filename to work with
    #chaserr_align - alignment dictionary, also giving info of isoform/ortolog length
    #caption_name - filename for distribution caption, referring caption name, e.g. "chaserr_sites.png"
    rnaup_df=pd.read_csv(rna_sites_file_csv, sep="\t", header=0)
    print(rnaup_df.columns.tolist())
    #print(len(chaserr_align))
    full_seq=dict()
    #print(len(rnaup_df))
    for i in range(1,len(chaserr_align)+1):
        full_seq[i]=0
    #print(full_seq)
    for i in range(1,len(rnaup_df)):
        #print(i)
        for j in range(rnaup_df["siteStart1"][i],rnaup_df["siteEnd1"][i]):
            full_seq[j]+=(-abs(rnaup_df["deltaG"][i])*np.log(rnaup_df["PValue"][i])/rnaup_df["siteLen"][i])
    print(full_seq)
    f, ax = plt.subplots(figsize=(20,8))
    width=1
    plt.bar(full_seq.keys(), full_seq.values(), width, color='g')
    plt.savefig(caption_name)
plot_sites_prob("sites_all1.txt",mouse_align_str,"CHASERR_08_sites.png")
#print(len(mouse_align_str))


