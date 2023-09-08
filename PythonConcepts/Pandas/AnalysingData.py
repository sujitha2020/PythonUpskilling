import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
print(df.tail()) 
print(df.info()) 
new_df = df.dropna()

print(new_df.to_string())
df.dropna(inplace = True)

print(df.to_string())
df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)
df["Calories"].fillna(130, inplace = True)
df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
df = pd.read_csv('data.csv')

x = df["Calories"].median()


df["Calories"].fillna(x, inplace = True)

df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())
df.loc[7, 'Duration'] = 45
print(df.to_string())

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
print(df.to_string())
df.drop_duplicates(inplace = True)
print(df.to_string())

df = pd.read_csv('data.csv')
print(df.corr())

import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()