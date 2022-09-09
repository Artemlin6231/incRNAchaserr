import pandas as pd
df = pd.read_csv('sites_all.txt', sep="\t", header=0)
df_sort = pd.read_csv('sorted_results.csv')
df['PValue'] = ''
df['Padj'] = ''
#print(df_sort['name2'][0])
#print(df_sort.head())

for i in range(len(df_sort['name2'])):
    ##print(i)
    name=df_sort['name2'][i]
    #print(name)
    Pvalue=df_sort['Pvalue'][i]
    #print(Pvalue)
    Padj=df_sort['Padj'][i]
    #print((df['name2'][i])==name)
    df.loc[(df['name2'] == name), 'PValue'] = Pvalue
    df.loc[(df['name2'] == name), 'Padj'] = Padj
print(df.head())
del df['Unnamed: 0']
df.to_csv('sites_all1.txt',sep="\t")
#df.loc[(df['Name'] == 'tom') & (df['Age'] == 10), 'foo'] = 'x1'
#for j in range(len(df['name2'])):
        #if (df['name2'][j]==df_sort['name2'][i]):
           # df['PValue'][j]=df_sort['Pvalue'][i]
            #df['Padj'][j]=df_sort['Padj'][i]