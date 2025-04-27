# A generator is a special type of iterator that allows you to iterate over a sequence of values without storing them all in memory at once.
# Generators are defined using the `yield` keyword, which allows the function to return a value and pause its execution, resuming later from where it left off.

range(100)
list(range(100))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    
    return result

my_list = make_list(100)
print(my_list)

# here list takes up a lot of memory
# but we can use a generator to save memory

# generators are iterables but all iterables are not generators

def generator_function(num):
    for i in range(num):
        yield i*2
        
g = generator_function(100)
next(g) # can be called multiple times to get the next value in the sequence until the generator is finished
next(g)
print(next(g)) 

# yield vs return :
# yield returns a value and pauses the function, while return exits the function completely
        
        
for item in generator_function(1000):
    print(item)
    
