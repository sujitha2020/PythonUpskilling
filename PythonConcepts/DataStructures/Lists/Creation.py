# Creating a List
print("Blank List")
List = []
print(List)

# Creating list of  numbers
print("\nList of numbers: ")
List = [10,23, 56,100]
print(List)

# Creating list of  strings
print("\nList of strings: ")
List = ["Hello","World"]
print(List)

#A list may contain duplicate values
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with duplicate values: ")
print(List)

# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)

# List of list
List = [['a','b'],['c','d'],['e','f']]
print("\nList of list: ")
print(List)

# Create list of list using append function.
# Create 2 independent lists
list_1 = ['a','b','c']
list_2 = ['d','e','f']

# Create an empty list
list = []

# Create List of lists
list.append(list_1)
list.append(list_2)
print("\nList of list: ")
print (list)

#Create a list of lists using the list initializer in Python
list = []

# Create List of lists
list =[list_1, list_2]
print("\nList of list: ")
print (list)

#using  list comprehension
l1 = ['a','b','c']
list = [l1 for i in range(3)]
print(list)

#using for loop
list = []

# Create List of list
for i in range(2):
    list.append([])
    for j in range(3): 
        list[i].append(j)

print("\nList of list: ")
print (list)

