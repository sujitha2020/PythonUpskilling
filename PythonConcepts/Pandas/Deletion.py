import pandas as pd

# creating a data frame.
dataFrame = pd.DataFrame([
    {
        "Person": "James",
        "Sales": 1000,
        "LastName": "Taylor",
    },
    {
        "Person": "Clara",
        "Sales": 3000,
        "LastName": "Brown"
    }
])

del dataFrame['LastName']
print(dataFrame)

dataFrame.drop(columns=["Person"], inplace=True)

print(dataFrame)

# importing necessary modules.
import pandas as pd

# importing necessary modules.
import pandas as pd

# creating a data frame.
dataFrame = pd.DataFrame([
    {
        "Person": "James",
        "Sales": 1000
    },
    {
        "Person": "Clara",
        "Sales": 3000
    },
    {
        "Person": "John",
        "Sales": 2000
    },
    {
        "Person": "Rhea",
        "Sales": 5000
    }
])


dataFrame.drop(columns=["Person"], inplace=True)

print(dataFrame)

# importing necessary modules.
import pandas as pd

# creating a data frame.
dataFrame = pd.DataFrame([
    {
        "Person": "James",
        "Sales": 1000
    },
    {
        "Person": "Clara",
        "Sales": 3000
    },
    {
        "Person": "John",
        "Sales": 2000
    },
    {
        "Person": "Rhea",
        "Sales": 5000
    }
])


dataFrame.drop([0, 1], inplace=True)

print(dataFrame)


# importing necessary modules.
import pandas as pd

# creating a data frame.
dataFrame = pd.DataFrame([
    {
        "Person": "James",
        "Sales": 1000
    },
    {
        "Person": "Clara",
        "Sales": 3000
    },
    {
        "Person": "John",
        "Sales": 2000
    },
    {
        "Person": "Rhea",
        "Sales": 5000
    }
])


dataFrame.drop([0, 1], inplace=True)

print(dataFrame)
