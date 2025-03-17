# Sets are unordered collections of unique elements.

my_set = {1, 2, 3, 4, 5, 5}
print(my_set) # duplicates are removed

my_set.add(100)
my_set.add(2)
print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))

print(1 in my_set) # does not support indexing
print(my_set)
print(len(my_set))

new_set = my_set.copy()
print(new_set)

my_set.clear()
print(my_set)

# Methods

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set)) # returns a new set with the differences between my_set and your_set
print(my_set)

print(my_set.discard(5)) # removes the element from the set
print(my_set)

my_set = {1, 2, 3, 4, 5}

print(my_set.difference_update(your_set)) # removes the elements that are the same in both sets, modifies the original set
print(my_set)

my_set = {1, 2, 3, 4, 5}

print(my_set.intersection(your_set)) # returns a new set with the elements that are the same in both sets
print(my_set & your_set) # same as above

print(my_set.isdisjoint(your_set)) # returns True if the sets have no elements in common

print(my_set.union(your_set)) # returns a new set with all the elements from both sets, removes duplicates
print(my_set | your_set) # same as above

my_set = {4, 5}
print(my_set.issubset(your_set)) # returns True if all the elements in my_set are in your_set

print(your_set.issuperset(my_set)) # returns True if all the elements in my_set are in your_set

# You don't need to memorize all of these methods, you can always look them up in the documentation.
# for more methods, visit: https://w3schools.com/python/python_ref_set.asp