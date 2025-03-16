basket = [1, 2, 3, 4, 5]

# adding
basket.append(100)
new_list = basket
print(new_list) 
print(basket) 
# append changes the original list, changes the original list in place, it does not return anything 

basket.insert(4, 100)
print(basket)

basket.extend([100, 101])
print(basket)

# removing
basket = [1, 2, 3, 4, 5]
basket.pop()
print(basket) # pop removes the last item in the list
basket.pop(0)
print(basket) # pop removes the item at the index specified

basket.remove(4)
print(basket) # remove removes the first instance of the value specified, where pop removes the value at the index specified

new_list = basket.pop(2)
print(new_list) # pop returns the value that was removed, unlike other methods we have seen so far

basket.clear()
print(basket) # clear removes all the items in the list

# indexing
basket = ['a', 'b', 'c', 'd', 'e']
print(basket.index('d', 2, 4)) # index returns the index of the value specified, it can also take a start and end index

# in
print('d' in basket) # in checks if the value is in the list
print('x' in basket)
print('i' in 'hi my name is Fahim') # in can also be used with strings

# count
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
print(basket.count('d')) # count returns the number of times the value is in the list

# sorting
basket.sort()
print(basket)

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
new_list = sorted(basket)
print(new_list) # using 'sorted' function
# sorted provides a new list, while sort changes the original list in place

copied_basket = basket.copy()
print(copied_basket)

# reverse
basket.reverse()
print(basket) # switchign the order of the list by index 

basket.sort()
basket.reverse()
print(basket) # sorted reversed basket
# so methods change the original list, while functions return a new list