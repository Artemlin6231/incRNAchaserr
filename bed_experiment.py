import pandas as pd
df = pd.read_csv('sorted_results.csv')
for i in range(len(df)):
    a=df['name2'][i].split(':')
    b=a[1]
    if 'c' in b:
        b=b.replace('c',"")
        b=b.split('-')
        c=int(b[1])
        c1=int(b[0])
    else:
        b = b.split('-')
        c = int(b[0])
        c1 = int(b[1])
    #print(c)
    df['len1'][i]=c
    df['len2'][i]=c1
    df['name2'][i]=a[0]
del df["name1"]
del df['Unnamed: 0']
df.to_csv('bed_transcripts.txt',  sep="\t")
df=pd.read_csv('bed_transcripts.txt', sep="\t", header=0)
for i in range(len(df)):
    if ((df['len2'][i]-df['len1'][i]) < 0):
        print('Big_Error')
#print(df['siteStart2'])