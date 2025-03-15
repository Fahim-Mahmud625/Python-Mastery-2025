greet = 'hellooooo'
print(len(greet))
print(greet[0:len(greet)])

# the difference between functions and methods is that methods are functions that belong to objects, here strings

quote = 'to be or not to be'
print(quote.upper()) # .upper() converts all characters to uppercase
print(quote.capitalize()) # .capitalize() converts the first character to uppercase
print(quote.title()) # .title() converts the first character of each word to uppercase
print(quote.find('be')) # .find() finds the index of a substring within a string
print(quote.replace('be', 'me')) # .replace() replaces a substring with another substring
print(quote) # original string is not modified as strings are immutable, we can only overwrite them, creating or destroying them

quote2 = quote.replace('be', 'me')
print(quote2) # this is the modified string, created by the .replace() method and quote stays the same

# for more methods, see https://docs.python.org/3/library/stdtypes.html#string-methods