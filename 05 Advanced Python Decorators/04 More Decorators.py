def my_decorator(func):
    def wrap_func(*x, **y):
        print('**********')
        func(*x, **y)
        print('**********')
    return wrap_func

@my_decorator
def hello(greeting, emoji = ':('):
    print(greeting, emoji)

hello('Hi there eveyone!', '😃')
hello('Sup?')