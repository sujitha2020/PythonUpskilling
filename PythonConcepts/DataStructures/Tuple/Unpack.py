#Packing tuple
fruits = ("apple", "banana", "cherry")
#Unpacking a tuple:
#Extract the values back into variables. This is called "unpacking":
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using Asterisk*
# If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable 
# as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)