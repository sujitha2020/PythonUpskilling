# https://codeahoy.com/learn/tutorials/python-open/
# https://learnpython.com/blog/write-to-file-python/
# https://stackoverflow.com/questions/70428706/what-does-newline-mean-in-the-csv-library
import os
os.chdir("/home/asplap2314/Learnings/PythonConcepts/FileOperations")
    
with open("file.txt", "r") as file:
    data = file.readlines()
    print(data)
    for line in data:
        word = line.split()
        
with open("file.txt", "r") as file:
    data=file.read(5)
    print(data)


with open("file.txt", "a+") as f:
    f.write("New content")


# open and write to file
with open("file2.txt", "a") as file:
    file.writelines(["Hey there!\n", "LearnPython.com is awesome!\n"])
 
# open and read the file after the appending:
with open("file2.txt", "r") as file:
    print(file.read())
    
#!/usr/bin/python

# Open a file
fo = open("file.txt", "r+")
str = fo.read(10)
print("Read String is : ", str)

# Check current position
position = fo.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print("Again read String is : ", str)
# Close opend file
fo.close()