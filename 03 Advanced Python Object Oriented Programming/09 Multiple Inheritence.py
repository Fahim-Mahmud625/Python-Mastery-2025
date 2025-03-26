# Multiple Inheritance:
# Multiple inheritance is when a class inherits from more than one parent class.
# This allows a child class to combine functionalities from multiple base classes.

class User:  
    def sign_in(self):
        print('logged in')

class Wizard(User):  
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):  
        print(f'attacking with power of {self.power}')

class Archer(User):  
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):  
        print(f'{self.num_arrows} arrows remaining')
        
    def run(self):
        print('ran really fast')

# HybridBorg inherits from both Wizard and Archer
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        # Explicitly calling parent class constructors
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)

# Creating an instance of HybridBorg
hb1 = HybridBorg('Borgie', 50, 150)

# Using methods from both parent classes
hb1.attack()        # Inherited from Wizard
hb1.check_arrows()  # Inherited from Archer
hb1.sign_in()       # Inherited from User

# With great power comes great responsibility! 