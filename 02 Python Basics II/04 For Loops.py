# Machines excel at repitive tasks
# For loops are used to iterate over a sequence (list, tuple, string, etc.)
# Iterables allow us to loop over a sequence of elements

for item in 'zero to mastery': # here item is a varibale, and 'zero to mastery' is a string which is an iterable
    print(item)

for item in [1,2,3,4,5]:
    print(item)

for item in {1,2,2,3,4,5}:
    print(item) # as set does not allow duplicates
    
for item in (1,2,3,4,5):
    print(item)

print(item) # this will print the last item, as when the loop ends the last value of item is stored in the memory

for item in [1,2,3,4,5]:
    for x in ['a','b','c']:
        print(item, x)

# iterable - list, dictionary, tuple, set, string (noun)
# iterate -> one by one check each item in the collection (verb)

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user:
    print(item)

for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item)
    
for item in user.keys():
    print(item)

# .items, .values, .keys are methods of dictionary that help us to iterate over the dictionary
# int object is not iterable, as it is not a collection of items

# Counter Exercise

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter += item
print(counter)