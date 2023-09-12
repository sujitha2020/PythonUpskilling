import pandas as pd
data = {'Book_Name': ['Oxford', 'Arihant', 'Pearson', 'Disha', 'Cengage'],
        'Author': ['Jhon Pearson', 'Madhumita Pattrea', 'Oscar Wilde', 'Disha', 'G Tewani'],
         'Price': [350,880,490,1100,450]} 
df = pd.DataFrame(data)
for i, j in df.iterrows():
    print(i, j)
    print()
    
# i and j pointers are used to iterate over a row. 
# First, i iterate over the row index i.e 0,1,2 etc., 
# and then j iterate over row data like we have the first-row containing 
# Book_Name Oxford, Author Jhon Pearson, and Price 350

for i, j in df.iterrows():
    print(i," Book_Name=", j['Book_Name'],";", "Author=", j['Author'],";", "Price=", j['Price'])
    
# for i, j in df.iteritems():
#   print(i,j)
#   print()
  
for i in df.itertuples():
  print(i)
  
for i in df.index:
  print(df['Book_Name'][i], df['Author'][i], df['Price'][i] )
  
  
for i in range(len(df)):
  print(df.loc[i,'Book_Name'], df.loc[i,'Author'], df.loc[i,'Price'] )
  
  
data = {'First_Name': ['Robert', 'Maxx', 'Harry', 'Howard', 'Sheldon'],
                'Last_Name': ['Copper', 'Koothrappali', 'Hofstadter', 'Wolowitz', 'Fowler'],
                'age': [22, 28, 26, 31, 29],
                'Score': [7, 9, 5, 8, 7],
                'Rating': [74, 92, 83, 78, 64]}

df = pd.DataFrame(data)
print("Given Data\n",df)
print()
print("Iterating over rows using apply function :")
print(df.apply(lambda row: row['Last_Name'] + " " +str(row["Score"]), axis=1))