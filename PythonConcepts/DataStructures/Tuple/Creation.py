# Using parentheses
my_tuple = (1, 2, 3)
print(my_tuple)

# Without parentheses (implicitly creates a tuple)
another_tuple = 4, 5, 6
print(another_tuple)

# To create a tuple with only one item, you have to add a comma after the item, 
# otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)