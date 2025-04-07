# Simply a function that wraps another function or changes its behaviour
def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func


@my_decorator
def hello():
    print('helllooooo')

@my_decorator
def bye():
    print('see ya later')
    
bye() # super boosted our function adding extra functionality

# how does it work?
# a = my_decorator(hello) then a() is called 
# my_decorator(hello)()