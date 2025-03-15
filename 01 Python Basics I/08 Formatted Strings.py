name = 'John'
age = 25
print(f'Hello, {name}. You are {age} years old.') # f-strings are the most readable

print('Hello, {1}. You are {0} years old.'.format(name, age)) # not as readable as f-strings

# f-strings are the most readable, but .format() is more versatile which we will see later