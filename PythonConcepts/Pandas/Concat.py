import pandas as pd
import numpy as np


df1 = pd.DataFrame({'employee': ['Gauri', 'Keshav', 'Harshit', 'Komal'],
                    'group': ['Chemical', 'Engineering', 'Chemical', 'HR']})
                    
df2 = pd.DataFrame({'employee': ['Gauri', 'Keshav', 'Harshit', 'test'],
                    'hire_date': [2004, 2008, 2012, 2014]})

df3 = pd.concat([df1, df2])
print(df3)


res2 = pd.concat([df1, df2], axis=1, join='inner')
print(res2)