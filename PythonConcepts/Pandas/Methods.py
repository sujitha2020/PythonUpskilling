# importing necessary module.
import pandas as pd

dataFrame = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                         columns=['A', 'B', 'C'])


# Printing the current dataFrame.
print("The DataFrame formed is: \n", dataFrame)


print("Getting the first value present in the B-column: ",
      dataFrame.at[1, 'B'])

# Changing the first value present in the C-column:
dataFrame.at[1, 'C'] = 15

# Printing the current dataFrame.
print("The updated DataFrame is: \n", dataFrame)

data = {'First_Name': ['Ishan', 'Aryan', 'Priya', 'Veer', 'Akash', 'Chirag', 'Mahi', 'Veer', 'Manthan', 'Sonia', 'Akash'],
        'Last_Name': ['Malhotra', 'Khurana', 'Sharma', 'Rathore', 'Mudgal', 'Sharma', 'Khurana', 'Malhotra', 'Jamwal', 'Mudgal', 'Jamwal'],
            'Age': [29,27,24,25,29,24,31,26,32,35,22,],
            'Salary':[67000,60000,56000,62000,52000,67000,72000,67000,56000,72000,68000]
}
df = pd.DataFrame(data)
Grouped_Salary=df.groupby('Salary')
print(Grouped_Salary.groups)
Grouped_price = df.groupby(['Salary'])['Salary'].count()
print("Grouped data:\n",Grouped_price)# initialise data of lists.
Data = {'Products':['Box','Color','Pencil',
                    'Eraser','Color',
                    'Pencil','Eraser','Color',
                    'Color','Eraser','Eraser','Pencil'],
 
       'States':['Jammu','Kolkata','Bihar',
                 'Gujarat','Kolkata',
                 'Bihar','Jammu','Bihar','Gujarat',
                 'Jammu','Kolkata','Bihar'],
 
       'Sale':[14,24,31,12,13,7,9,31,18,16,18,14]}
 
# Create DataFrame
df = pd.DataFrame(Data, columns=['Products',
                                 'States','Sale'])