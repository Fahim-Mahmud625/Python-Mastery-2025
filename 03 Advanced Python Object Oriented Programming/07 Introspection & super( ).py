# Introspection:
# Introspection in Python refers to the ability to examine an object’s attributes and methods at runtime.

class User():  
    def __init__(self, email):
        self.email = email  # Email attribute

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')  # Placeholder method

# The super() function:
# `super()` allows a child class to inherit methods and properties from its parent class.
# It is used to call the constructor or other methods from the parent class, avoiding redundant code.

class Wizard(User):  
    def __init__(self, name, power, email):
        super().__init__(email)  # Calls the parent class's __init__ method
        self.name = name
        self.power = power

    def attack(self):  
        print(f'attacking with power of {self.power}')

# Creating an instance of Wizard
wizard1 = Wizard('Abra', 150, 'abra625@gmail.com')

# Using introspection to access attributes dynamically
print(wizard1.email)  

# dir() function lists all attributes and methods of the object
print(dir(wizard1))  # Displays all available properties, including inherited ones
