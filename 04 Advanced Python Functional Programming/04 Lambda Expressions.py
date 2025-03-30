from functools import reduce

my_list = [1,2,3]

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item%2 != 0, my_list)))

print(reduce(lambda acc,item: acc + item, my_list, 0))

# Excercise

# make square
new_list = [5,4,3]

print(list(map(lambda item: item*item, new_list)))

# sort on the basis of 2nd element of the tuples

sort_list = [(0,2), (4,3), (9,9), (10,-1)]

sort_list.sort(key = lambda x: x[1])

print(sort_list)