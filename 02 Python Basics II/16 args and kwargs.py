# args
# any no of arguments
# by putting *

def super_func(*args):
    print(args)
    return(sum(args))

print(super_func(1,2,3,4,5))

# kwargs
# can put keywords
# by putting **

def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return(sum(args) + total)

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))

# Rule: params, *args, default params, **kwargs
    # it is not recommended to use all of these in one function as it becomes very messy

def super_func(name, *args, i = 'hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return(sum(args) + total)

print(super_func('Meaw', 1,2,3,4,5, num1 = 5, num2 = 10))