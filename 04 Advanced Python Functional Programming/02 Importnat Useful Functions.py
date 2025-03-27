from functools import reduce

# map function
# - Applies a given function to all items in an iterable (e.g., list, tuple)
# - Returns a map object (which can be converted to a list)

def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1,2,3])))

# filter function
# - Filters elements from an iterable based on a condition
# - Returns a filter object (convertible to a list)

def only_odds(item):
    return item % 2 != 0

print(list(filter(only_odds, [1,2,3])))

# zip function
# - Combines multiple iterables element-wise into tuples
# - Stops at the shortest iterable if they have different lengths

my_list = [1,2,3]
your_list = [10,20,30]
their_list = [5,4,3]

print(list(zip(my_list, your_list, their_list)))

# reduce function
# - Applies a function cumulatively to elements in an iterable
# - Reduces the iterable to a single accumulated value


def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))
print(reduce(accumulator, my_list, 10))