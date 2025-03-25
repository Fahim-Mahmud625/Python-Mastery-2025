# Inheritance:
# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
# It promotes code reusability and establishes a hierarchical relationship between classes.

class User():  # Parent class
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')  # Gets overridden by derived classes

# Wizard and Archer inherit from User

class Wizard(User):  # Sub-class / Derived-class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):  # Overriding attack method
        print(f'attacking with power of {self.power}')

class Archer(User):  # Another Sub-class / Derived-class
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):  # Overriding attack method
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

# Creating instances

wizard1 = Wizard('Abra', 150)
archer1 = Archer('Tusk', 300)

# Checking inheritance relationships

print(isinstance(wizard1, Wizard))  # True
print(isinstance(wizard1, Archer))  # False
print(isinstance(wizard1, User))    # True
print(isinstance(wizard1, object))  # True (Everything in Python inherits from 'object')

# Polymorphism:
# Polymorphism allows methods to have the same name but different behaviors in different classes.
# This helps in writing flexible and reusable code.

def player_attack(character):
    character.attack()  # Calls the respective attack method of the object passed

# Demonstrating polymorphism using a loop

for char in [wizard1, archer1]:
    char.attack()  # Calls the overridden attack method of Wizard/Archer

# Importance of Polymorphism:
# 1. It allows different classes to be treated uniformly, improving code flexibility.
# 2. It enables method overriding, allowing different implementations for the same method in subclasses.
# 3. It enhances code maintainability by reducing dependencies on specific class types.