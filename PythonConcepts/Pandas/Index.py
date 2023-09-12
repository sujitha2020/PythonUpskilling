import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
    'Discount':[1000,2300,1200,2000]
              }
index_labels=['r1','r2','r3','r4']
df = pd.DataFrame(technologies,index=index_labels)
print(df)

# Get name of the index column of DataFrame.
df.index.name
'Index'
df.index.name='Index1'
print(df)

# Get pandas index/name by set_index.
df = pd.DataFrame(technologies).set_index('Courses')
print(df)

# To get Index and Column names.
print (df.index.name)
print (df.columns.name)

# Rename a column by rename_axis method.
df = df.rename_axis('Courses1')
print(df)

# Rename index column by rename_axis() method
df = pd.DataFrame(technologies).set_index('Courses').rename_axis('Courses_Name', axis=1)
print(df)

# Get pandas index title/name by index and Column parameter.
df = df.rename_axis(index='RowNumber', columns="Row")
print(df)

# Removing index and columns names to set it none.
df = df.rename_axis(index=None, columns=None)
print(df)

# Using de.indx.rename get pandas index title/name.
df.index.rename('Row', inplace=True)
print(df)

# Add Multilevel index using set_index() 
df = pd.DataFrame(technologies,index=index_labels)
df2 = df.set_index(['Courses', 'Duration'], append=True)
print(df2)

# Rename Single index from multi Level
df2.index = df2.index.set_names('Courses_Duration', level=2)
print(df2)

# Rename All indexes
df2.index=df2.index.rename(['Row','Courses_Name','Courses_Duration'])
print(df2)

