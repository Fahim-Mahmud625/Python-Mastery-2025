from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5
    print('Damn')
        
long_time()

# Excercise 

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}



def authenticated(fn):
    def wrapper(x):
        if user1['valid']:
            return fn(x)
        else:
            pass
    return wrapper

@authenticated
def message_friends(x):
    print('message has been sent')

message_friends(user1)