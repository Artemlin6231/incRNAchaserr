import pandas as pd
df=pd.read_csv('sites_all_to_make_plot.txt', sep="\t", header=0)

for i in range(len(df)):
    a=df['name2'][i].split(':')
    b=a[1]
    if 'c' in b:
        b=b.replace('c',"")
        b=b.split('-')
        c=int(b[1])
    else:
        b = b.split('-')
        c = int(b[0])
    #print(c)
    df['siteStart2'][i]=int(df['siteStart2'][i])+c
    df['siteEnd2'][i]=int(df['siteEnd2'][i])+c
    df['name2'][i]=a[0]
    if ((df['siteEnd2'][i]-df['siteStart2'][i]) < 0):
        print('Big_Error')
del df['Unnamed: 0']
df.to_csv('bed_modificated_u.txt',  sep="\t")
df=pd.read_csv('bed_modificated.txt', sep="\t", header=0)
for i in range(len(df)):
    if ((df['siteEnd2'][i]-df['siteStart2'][i]) < 0):
        print('Big_Error')
#print(df['siteStart2'])