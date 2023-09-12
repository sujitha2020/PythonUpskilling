import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")

# using []
print(data["Team"])

print(data[["Team","Number"]])
  
# retrieving multiple rows by loc method
first = data.loc[["Avery Bradley", "R.J. Hunter"]]
  
print(first)

# retrieving two rows and three columns by loc method
first = data.loc[["Avery Bradley", "R.J. Hunter"],
                   ["Team", "Number", "Position"]]
  
print(first)

# retrieving all rows and some columns by loc method
first = data.loc[:, ["Team", "Number", "Position"]]
  
print(first)

data = pd.read_csv("nba.csv", index_col ="Name")
# retrieving rows by iloc method 
row2 = data.iloc[[2,1]]
  
print(row2)

r = data.iloc[:3, [1, 3]]
print(r)

s= data.reindex(['test'])
print(s)