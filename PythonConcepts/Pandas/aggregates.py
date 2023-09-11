# The agg() method allows you to apply a function or a list of function names to be executed along one of the axis of the DataFrame, default 0, which is the index (row) axis.
import pandas as pd
import numpy as np
# # Creating a new dataframe
# df = pd.DataFrame([[100, 95, 87],[94, 92, 81],[75,84,91]],columns=['Maths', 'English','Science'])
# print(df)
# print(df.agg(['sum'],1)) # row
# print(df.agg(['average'],0)) # column 
# print(df.agg(['average','min','max'],0))

# # Performing different aggregations per column.
# print(df.agg(Average_Score=('Maths','average'),Minimum_Score=('English','min'),Maximum_Score=('Science','max')))

# # Creating a series
# score = {'Harsh': 97, 'Manish': 86, 'Dev': 76}
# series = pd.Series(data=score)
# print(series)
# print("-----------------------")
# # Running Aggregate Function on Series
# print(series.agg({'average'}))

df = pd.DataFrame({'A': [1, 2, 2, 1,3],'B': [1, 2, 3, 4, 5],'C': np.random.randn(5)})
print(df)
print("----------------------")
result =df.groupby('A')
# agg({'C':{'min','max'}})
for name,group in result:
    print("\nGroup:")
    print(name)
    print(group)
    
print(df.groupby('A').agg({'C':{'min','max'}}))