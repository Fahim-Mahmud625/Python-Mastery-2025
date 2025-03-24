class PlayerCharacter:
    # Class object attribute (shared among all instances)
    membership = True  # This is a class attribute, meaning all instances share this.

    def __init__(self, name='anonymus', age=0):  # Constructor method (initializer)
        # Default values: name = 'anonymus', age = 0
        if age > 18:  # Only assigns name and age if age is greater than 18
            self.name = name  # Instance attribute (specific to each object)
            self.age = age  # Instance attribute

    def run(self):
        return self
    
    def shout(self):  # Instance method
        print(f'My name is {self.name} !!!')  # Prints the player's name
    
    @classmethod  # Class method decorator (modifies the method to work with class itself)
    def adding_things1(cls, num1, num2):  # cls refers to the class itself, not an instance
        return cls('Hosico', num1 + num2)  # Creates a new instance of PlayerCharacter

    @staticmethod  # Static method decorator (does not use instance or class attributes)
    def adding_things2(num1, num2):
        return num1 + num2  # Just returns the sum, does not interact with the class or instance

# Creating instances of PlayerCharacter
player1 = PlayerCharacter('Cindy', 44)  # Cindy, age 44 (valid since age > 18)
player2 = PlayerCharacter('Tom', 21)  # Tom, age 21 (valid since age > 18)
player2.attack = 50  # Adding a new attribute 'attack' to player2 dynamically

# Printing attributes of player1 and player2
print(player1.age)  # Output: 44
print(player2.name)  # Output: Tom
print(player2.attack)  # Output: 50 (dynamically assigned attribute)

# Checking class attribute membership
print(player2.membership)  # Output: True (shared by all instances)

# Calling the instance method 'shout'
player2.shout()  # Output: My name is Tom !!!
print(player2.shout())  # Output: My name is Tom !!! (prints None because print() is used on a method that returns nothing)

# Creating an instance using the class method
player3 = PlayerCharacter.adding_things1(20, 5)  # Creates player3 with name 'Hosico' and age 25
print(player3.age)  # Output: 25
print(player3.name)  # Output: Hosico

# Using the static method
print(PlayerCharacter.adding_things2(3, 2))  # Output: 5 (simply returns the sum, no instance creation)

print(player3.run().run()) # paradox

# DETAILED EXPLANATION:
# 1. 'PlayerCharacter' is a class that represents a player in a game.
# 2. 'membership' is a class attribute that is shared by all instances of the class.
# 3. '__init__' is the constructor method that initializes attributes like 'name' and 'age'.
#    - It assigns these attributes only if 'age' is greater than 18.
# 4. 'shout()' is an instance method that prints the player's name.
# 5. '@classmethod' decorator is used to create a class method.
#    - It takes 'cls' as the first argument, referring to the class itself.
#    - 'adding_things1()' creates a new PlayerCharacter instance.
# 6. '@staticmethod' decorator is used for a method that does not depend on the class or instance.
#    - 'adding_things2()' simply adds two numbers and returns the result.
# 7. Instances of the class are created using 'PlayerCharacter()'.
# 8. 'player2.attack = 50' dynamically adds a new attribute only to 'player2'.
# 9. 'player3' is created using the class method 'adding_things1()', giving it default name 'Hosico' and age 25.
# 10. The static method 'adding_things2()' is used to add two numbers without interacting with the class itself.