my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
another_dict = dict(key1="value1", key2="value2", key3="value3")  # Using dict() constructor

my_dict = {"name": "Alice", "age": 30, "city": "New York"}
name = my_dict["name"]
name = my_dict.get("name")

my_dict = {"name": "Alice", "age": 30}
my_dict["age"] = 31  # Modifying the value associated with the key "age"
my_dict.update({"age": 20})
keys = my_dict.keys() #before the change
print(keys)
values = my_dict.values()
print(values)

print(my_dict) 
my_dict["city"] = "New York"  # Adding a new key-value pair
keys = my_dict.keys() #after the change
print(keys)
values = my_dict.values()
print(values)

my_dict.update({"Educational Qualification": "BE"})

# The items() method will return each item in a dictionary, as tuples in a list.
items = my_dict.items()
print(items)
#Check if Key Exists
if "city" in thisdict:
  print("Yes, 'city' is one of the keys in the my_dict dictionary")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Merging dictionaries with the .update() method in Python
dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}

dict1.update(dict2)
print(dict1)

#LOOP THROUGH A DICTIONARY

#Print all key names in the dictionar
for x in thisdict:
  print(x)
  
#Print all values in the dictionary
for x in thisdict:
  print(thisdict[x])
  
#The values() method to return values of a dictionary
for x in thisdict.values():
  print(x)
  
#The keys() method to return keys of a dictionary
for x in thisdict.keys():
  print(x)
  
# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)
  
#Nested Dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])