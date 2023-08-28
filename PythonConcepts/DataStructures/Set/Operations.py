my_set = {1, 2, 3}  # Creating a set with three elements
another_set = set([3, 4, 5])  # Creating a set using the set() constructor
my_set = {1, 2, 3}
my_set.add(4)  # Adding an element to the set
my_set.remove(2)  # Removing an element from the set
my_set = {1, 2, 3}
if 2 in my_set:
    print("2 is in the set")
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2  # Union: {1, 2, 3, 4, 5}
intersection_set = set1 & set2  # Intersection: {3}
difference_set = set1 - set2  # Difference: {1, 2}

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3}

is_subset = set2.issubset(set1)  # True
is_superset = set1.issuperset(set2)  # True

set1 = {1, 2, 3}
set2 = {3, 4, 5}

symmetric_difference = set1 ^ set2  # {1, 2, 4, 5}