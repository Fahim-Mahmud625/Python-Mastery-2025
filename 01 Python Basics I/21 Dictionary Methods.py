user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print(user.get('age', 55)) # if the key doesn't exist, it will return None, but you can set a default value

user2 = dict(name='JohnJohn')
print(user2)
# another way to create a dictionary is to use the dict() function, and pass in key value pairs as arguments, not common

print('basket' in user) 
print('size' in user)

print(user.keys())
print('age' in user.keys()) # iterating over keys is the same as iterating over a list
print('hello' in user.values()) # iterating over values is the same as iterating over a list

print(user.items()) # returns a list of tuples, each tuple contains a key value pair, tuples we will learn about later

user2 = user.copy() 
print(user2)

user2.clear()
print(user2)

print(user.pop('age')) # removes the key value pair and returns the value
print(user)

print(user.popitem())
print(user) # important for destructuively iterating over a dictionary

user.update({'age': 55})
print(user) # updates the dictionary with the new key value pair, if the key doesn't exist, it will add it

# Exercise

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.

# 3 Add a new weapon to your user

# 4 Add a new key to include 'is_banned'. Set it to false

# 5 Ban the user by setting the previous key to True

# 6 create a new user2 by copying the previous user and update the age value and username value.

# solution:

profile = {
    'age': 0,
    'username': ' ',
    'weapons': 'BFG-900',
    'is_active': True,
    'clan': 'Neural Nexus'
}

print(profile.keys())
profile['weapons'] = 'Katana'
print(profile)
profile.update({'is_banned': False})
print(profile)
profile.update({'is_banned': True})
print(profile)

user2 = profile.copy()
print(user2)

user2.update(
    {
        'age': 23,
        'username': 'Deadexe'
    }
)

print(user2)

# for more methods, visit: https://www.w3schools.com/python/python_ref_dictionary.asp
