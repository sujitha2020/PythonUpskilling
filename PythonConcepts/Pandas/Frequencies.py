import pandas as pd
import numpy as np

# Write a Pandas program to display most frequent value in a given series and replace everything else as ‘Other’ in the series.
num_series = pd.Series(np.random.randint(1, 5, [15]))
# print("Original Series:")
print(num_series)
print("Top 2 Freq:", num_series.value_counts())
print(num_series.value_counts().index[:1]);
result = num_series[~num_series.isin(num_series.value_counts().index[:0])] = 'Other'
print(num_series)


import pandas as pd

# Making a list and then converting it to dataframe
data1 = [[1,'A'], [2,'B'], [3,'C']]
df1 = pd.DataFrame(data1, columns=['Col1', 'Col2'])

# Printing Dataframe 1
print(df1.head())

# Making a second list and then converting it to dataframe
data2 = [[4,'D'], [5,'E'], [6,'F'], [7,'G']]
df2 = pd.DataFrame(data2, columns=['Col3', 'Col4'])

# Printing Dataframe 2
print(df2.head())
print(df2.index)


technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
    'Discount':[1000,2300,1200,2000]
              }
index_labels=['r1','r2','r3','r4']
df = pd.DataFrame(technologies,index=index_labels)
print(df.index)

df = pd.DataFrame(technologies).set_index('Courses')
print(df)