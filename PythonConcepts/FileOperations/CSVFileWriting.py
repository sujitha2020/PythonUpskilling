# import
import csv
 
# Create header and data variables
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path) 
os.chdir(dir_path)
header = ['last_name', 'first_name', 'zip_code', 'spending']
data = ['Doe', 'John', 546000, 76]
 
with open('./customers.csv', 'w', encoding='UTF8', newline='') as file:
    # Create a writer object
    writer = csv.writer(file)
    # Write the header
    writer.writerow(header)
    # Write the data
    writer.writerow(data)
    
# Create header and data variables
header = ['last_name', 'first_name', 'zip_code', 'spending']
data = [
    ['Smith', 'Nicholas', 453560, 82],
    ['Thompson', 'Julia', 326908, 143],
    ['French', 'Michael', 678321, 189],
    ['Wright', 'Eva', 285674, 225],
    ['White', 'David', 213456, 167]
]
 
with open('customers1.csv', 'w', encoding='UTF8', newline='') as file:
    # Create a writer object
    writer = csv.writer(file)
    # Write the header
    writer.writerow(header)
    # Add multiple rows of data
    writer.writerows(data)
 
# csv header
fieldnames = ['last_name', 'first_name', 'zip_code', 'spending']
 
# csv data
rows = [{
    'last_name': 'bloggs',
    'first_name': 'Joe',
    'zip_code': 986542,
    'spending': 367
},{
    'last_name': 'Soap',
    'first_name': 'Bob',
    'zip_code': 567890,
    'spending': 287
},{
    'last_name': 'farnsbarns',
    'first_name': 'Charlie',
    'zip_code': 123456,
    'spending': 245
}]

with open('customers2.csv', 'w', encoding='UTF8', newline='') as f:
    # Create a writer object
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # Write header
    writer.writeheader()
    # Write data from dictionary
    writer.writerows(rows)
    
# https://stackoverflow.com/questions/70428706/what-does-newline-mean-in-the-csv-library
# https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory
# https://stackoverflow.com/questions/18590545/open-csv-file-in-utf-8-with-python
# https://stackoverflow.com/questions/10918682/platform-independent-path-concatenation-using