my_tuple = (1, 2, 3, 4, 5, 5) # In simple words, a tuple is a list that is immutable.
print(my_tuple[1])
print(5 in my_tuple)
# predictable, fast, and memory-efficient but not flexible

user = {
    (1, 2): [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user[(1, 2)]) # Tuples can be used as keys in dictionaries

new_tuple = my_tuple[1:2] # Slicing a tuple
print(new_tuple) # (2,) - a tuple with one element
print(my_tuple[1:4])

x,y,z, *other = (1, 2, 3, 4, 5)
print(z)
print(other)

print(my_tuple.count(5)) 
print(my_tuple.index(5))
print(len(my_tuple))