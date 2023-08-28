#copy(): Creates a shallow copy of the list.
#The copy() method returns a new list. It doesn't modify the original list.
import copy

original_list = [1, 2, 3,4,5]
copied_list = copy.copy(original_list)
print("original_list=", original_list)
print("Copied_List=",copied_list)
print("original_list index 0 id",id(original_list[0]))
print("copied_list index 0 id",id(copied_list[0]))
original_list[0]=5
print("original_list index 0 id",id(original_list[0]))
print("copied_list index 0 id",id(copied_list[0]))
print("original_list=", original_list)
print("Copied_List=",copied_list)

old_list = [[1,2],[3,4,5]]
new_list = copy.copy(old_list)
print("Old list:", old_list)
print("New list:", new_list)
print("Old list index [1][0] id",id(old_list[1][0]))
print("New list  index [1][0] id",id(new_list[1][0]))

old_list[1][0] = 8
print("Old list index [1][0] id",id(old_list[1][0]))
print("New list  index [1][0] id",id(new_list[1][0]))

print("Old list:", old_list)
print("New list:", new_list)


# original_list = [1, 2, 3]
# copied_list = original_list
# print(original_list)
# print(copied_list)
# copied_list[0]=5
# print(original_list)
# print(copied_list)

# # shallow copy using the slicing syntax

# # mixed list
# list = ['cat', 0, 6.7]

# # copying a list using slicing
# new_list = list[:]


# # Adding an element to the new list
# new_list[0]='dog'
# #new_list.append('dog')

# # Printing new and old list
# print('Old List:', list)
# print('New List:', new_list)

# import copy

# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.deepcopy(old_list)

# old_list[1][0] = 'BB'

# print("Old list:", old_list)
# print("New list:", new_list)