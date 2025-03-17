dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}
# here 'a' is the key and 1 is the value, we use the key to access the value

print(dictionary['b']) # unordred key value pairs
print(dictionary['a'])
print(dictionary['a'][1]) 

my_list = [
    {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
    },
    {
    'a': [4, 5, 6],
    'b': 'byeee',
    'x': False
    }
]

print(my_list[0]['a'][2])
print(my_list[1]['a'][2])

# Another thing is that the keys can be any immutable data type, like a string, a number, or a tuple. Not a list, because lists are mutable
    # but the values can be anything, even another dictionary
# dictionaries are good for storing structured data wheares lists are good for storing ordered data
# keys are unique
    # if you have two keys with the same name, the second one will overwrite the first one
