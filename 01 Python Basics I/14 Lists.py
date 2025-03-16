li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2,3.5, 'a', True]

# Data Structure is a way of organizing and storing data so that it can be accessed and worked with efficiently.
# Python has four built-in data structures: List, Tuple, Set and Dictionary.
# List is a collection which is ordered and changeable. Allows duplicate members.

amazon_cart = ['notebooks',
               'sunglasses',
               'toys',
               'grapes'
               ]

print(amazon_cart[0]) 

# List Slicing

print(amazon_cart[0:2]) 
print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'
print(amazon_cart) # lists are mutable

new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart) # slicing
print(amazon_cart) # original list is not affected

new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart) 
print(amazon_cart) # original list is affected

new_cart = amazon_cart[:] # copy of the list, does not affect the original list