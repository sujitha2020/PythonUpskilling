import pandas as pd
import numpy as np

df1 = pd.DataFrame({'employee': ['Gauri', 'Keshav', 'Harshit', 'Komal'],
                    'group': ['Chemical', 'Engineering', 'Chemical', 'HR']})
                    
df2 = pd.DataFrame({'employee': ['Gauri', 'Keshav', 'Harshit', 'test'],
                    'hire_date': [2004, 2008, 2012, 2014]})

# df3 = pd.merge(df1, df2)
# print(df3) 

# df4 = pd.merge(df1, df2,on='employee')
# print(df4) 

# df3 = pd.DataFrame({'name': ['Gauri', 'Keshav', 'Harshit', 'test'],
#                     'salary': [70000, 80000, 120000, 90000]})
# df9=pd.merge(df1, df3, left_on="employee", right_on="name")
# print(df9)

# df10 = pd.merge(df1,df2,indicator=True)
# print(df10)

# df11 = pd.merge(df1,df2,sort=True)
# print(df11)

# print(df1.join(df2.set_index('employee'), on='employee'))

