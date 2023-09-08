import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

#Create Labels

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

#accessing the item by label
print(myvar["y"])