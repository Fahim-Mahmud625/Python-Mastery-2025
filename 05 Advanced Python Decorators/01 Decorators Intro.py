def hello(func):
    func()
    
def greet():
    print('Still here!')
    
a = hello(greet)

print(a)

# So what happens here? The function hello is called with the function greet as an argument, acting like a varibale
# This is a decorator, which is a function that takes another function as an argument and extends its behavior without explicvitly modyfying it.