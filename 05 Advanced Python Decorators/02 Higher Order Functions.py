def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func

# Here both functions are higher order functions
# HOC are functrions that take other functions as arguments or return them as results 
# previously discussed map,filter,reduce are all higher order functions!