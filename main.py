import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#task 1
df=pd.read_csv('data.csv')
names=df.columns.tolist()
#print(names)
types=df.dtypes
print(types)
#task2
count_of_nan=df.shape[0]*0.3
df = df.loc[:, (df.isnull().sum(axis=0) <= count_of_nan)]
names=df.columns.tolist()
print(df)

#task3
x=df['SalePrice']
print(x)
y=df.shape[0]
plt.plot(x)
plt.show()
#task4
df.dtypes.unique()
df['MasVnrArea'].hist(figsize=(15,10), bins=10)
plt.show()
#task5
corr_df = df.select_dtypes(include=['float64', 'int64']).corr(method='pearson')
corr_df = corr_df.iloc[:-1,:]
corr_df = corr_df[corr_df.SalePrice > 0.5]['SalePrice']
print(corr_df)
#task6
for feature in corr_df.index:
    df[feature].hist(figsize=(10,5))
    plt.show()
    print(feature)
#task7
plt.figure(figsize=(40,40))
sns.heatmap(corr_df, annot=True)
plt.show()
#task8
plt.figure(figsize=(40,40))
for i, feature in enumerate(corr_df.index):
    plt.subplot(3, 4, i + 1)
    df[feature].hist(figsize=(10,5))
#task9
def correlation(categoria, measure):
    faccat, _ = pd.factorize(categoria)
    num = np.max(faccat)+1
    array = np.zeros(num)
    n_array = np.zeros(num)
    for i in range(0,num):
        cat_measure = measure[np.argwhere(faccat == i).flatten()]
        n_array[i] = len(cat_measure)
        array[i] = np.average(cat_measure)
    y_total_avg = np.sum(np.multiply(array,n_array))/np.sum(n_array)
    numer = np.sum(np.multiply(n_array,np.power(np.subtract(array,y_total_avg),2)))
    denumer = np.sum(np.power(np.subtract(measure,y_total_avg),2))
    if numer == 0:
        delta = 0.0
    else:
        delta = np.sqrt(numer/denumer)
    return delta
