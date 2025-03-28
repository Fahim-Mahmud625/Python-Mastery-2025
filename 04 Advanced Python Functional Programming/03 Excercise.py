from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

# Solution

# 1

def capitalize_list(item):
    return item.capitalize()

print(list(map(capitalize_list, my_pets)))

# 2

my_numbers.sort()

print(list(zip(my_strings, my_numbers)))

# 3

def pass_over50(item):
    return item > 50

print(list(filter(pass_over50, scores)))

# 4

def accumulator(acc, item):
    return acc + item

x1 = reduce(accumulator, my_numbers, 0)
x2 = reduce(accumulator, scores, 0)
print(x1 + x2)

# other way

print(my_numbers + scores)
print(reduce(accumulator, (my_numbers + scores), 0))