# List comprehensions provide a concise and readable way to create lists in Python.
# They allow you to generate a new list by applying an expression to each item in an 
# existing iterable (like a list, tuple, or range), and optionally applying conditions 
# to filter elements. List comprehensions are a powerful and efficient tool for 
# creating lists in a single line of code. 
# Here's the basic syntax of a list comprehension:
# new_list = [expression for item in iterable if condition]

# Creating a new list with squared values:
original_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in original_list]
print(squared_list)

#Filtering even numbers:
original_list = [1, 2, 3, 4, 5]
even_numbers = [x for x in original_list if x % 2 == 0]
print(even_numbers)

#Creating pairs from two lists:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
pairs = [(x, y) for x in list1 for y in list2]
print(pairs)

#Nested list comprehension (matrix transpose):
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)

#Using conditions with else:
numbers = [1, 2, 3, 4, 5]
new_list = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(new_list)