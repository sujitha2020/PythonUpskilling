# In order to access the list items refer to the index number. 
# Use the index operator [ ] to access an item in a list. 
# The index must be an integer. Nested lists are accessed using nested indexing. 

List = ["Geeks", "For", "Geeks"]
 
# accessing a element from the
# list using index number
print("Accessing a element from the list")
print(List[0])
print(List[2])

List = [['Geeks', 'For'], ['Geeks']]
 
# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
 
# accessing an element using
# negative indexing
print("Accessing element using negative indexing")
 
# print the last element of list
print(List[-1])
 
# print the third last element of list
print(List[-3])