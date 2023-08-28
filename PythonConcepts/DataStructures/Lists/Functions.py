#len(list): Returns the number of elements in the list.
my_list = [1, 2, 3, 4]
length = len(my_list)  # Returns 4
#max(list) and min(list): Returns the maximum and minimum values in the list, respectively.
my_list = [10, 5, 20, 15]
max_value = max(my_list)  # Returns 20
min_value = min(my_list)  # Returns 5
#sum(list): Returns the sum of all elements in the list (works for numeric types).
my_list = [1, 2, 3, 4]
total_sum = sum(my_list)  # Returns 10
#append(element): Adds an element to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
# Now my_list is [1, 2, 3, 4]
#insert(index, element): Inserts an element at a specific index in the list.
my_list = [1, 2, 3]
my_list.insert(1, 5)  # Inserts 5 at index 1
# Now my_list is [1, 5, 2, 3]
#extend(iterable): Adds elements from an iterable (list, tuple, etc.) to the end of the list.
my_list = [1, 2, 3]
my_list.extend([4, 5])
# Now my_list is [1, 2, 3, 4, 5]
my_list = [1, 2, 3]
my_list.extend((4, 5))
print(my_list)
# remove(element): Removes the first occurrence of a specific element from the list.
my_list = [1, 2, 3, 2]
my_list.remove(2)  # Removes the first 2
# Now my_list is [1, 3, 2]
#pop(index): Removes and returns the element at the specified index. If no index is provided, the last element is removed.
my_list = [1, 2, 3, 4]
popped_element = my_list.pop(1)  # Removes and returns 2

# Removes and returns the element at the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Now my_list is [1, 3, 4]
#index(element): Returns the index of the first occurrence of a specific element.
my_list = [10, 20, 30, 20]
index = my_list.index(20)  # Returns 1
#count(element): Returns the number of occurrences of a specific element in the list.
my_list = [1, 2, 2, 3, 2]
count = my_list.count(2)  # Returns 3
#sort(): Sorts the list in ascending order (modifies the original list).
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.sort()
# Now my_list is [1, 1, 2, 3, 4, 5, 6, 9]
#reverse(): Reverses the elements in the list (modifies the original list).
my_list = [1, 2, 3, 4, 5]
my_list.reverse()

#clear method
prime_numbers = [2, 3, 5, 7, 9, 11]

# remove all elements
prime_numbers.clear()

# Updated prime_numbers List
print('List after clear():', prime_numbers)
# Now my_list is [5, 4, 3, 2, 1]
#copy(): Creates a shallow copy of the list.
#The copy() method returns a new list. It doesn't modify the original list.
original_list = [1, 2, 3]
copied_list = original_list.copy()
print(original_list)
print(copied_list)
copied_list.append(4)
print(original_list)
print(copied_list)
#We can also use the = operator to copy a list.
#If you modify new_list, old_list is also modified. 
# It is because the new list is referencing or pointing to the same old_list object.
original_list = [1, 2, 3]
copied_list = original_list
print(original_list)
print(copied_list)
copied_list.append(4)
print(original_list)
print(copied_list)

# shallow copy using the slicing syntax

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]


# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)