# Parameters
    # parameters are used when we define a fucntion
def say_hello(name, emoji):
    print(f'helllooooo {name} {emoji}')

# Postional Arguments
    # arguments are used when we call/invoke a fucntion
say_hello('Ishtiaq', '😸')

# need to be at the defined position

# Keyword Arguments

say_hello(name = 'BiBi', emoji = '😸') 

# Deafult Parameter 

def say_hello(name = 'Darth Maw', emoji = '😾'):
    print(f'helllooooo {name} {emoji}')
    
say_hello()
say_hello('Timmy')
say_hello('Ishtiaq', '😸')