import os
import csv
os.chdir("/home/asplap2314/Learnings/PythonConcepts/FileOperations")
with open("customers.csv", "r") as handler:
 reader = csv.reader(handler, delimiter=',')
 for row in reader:
   print(row)
   
with open('customers.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        
with open("customers.csv","r") as csvfile:
    csv_test_bytes = csvfile.read(1024)  # Grab a sample of the CSV for format detection.
    csvfile.seek(0)  # Rewind
    has_header = csv.Sniffer().has_header(csv_test_bytes)  # Check to see if there's a header in the file.
    dialect = csv.Sniffer().sniff(csv_test_bytes)  # Check what kind of csv/tsv file we have.
    inputreader = csv.reader(csvfile, dialect)
    if has_header:
        next(inputreader) # Skip the header if we have one.
    for row in inputreader:
        print(row)
    
