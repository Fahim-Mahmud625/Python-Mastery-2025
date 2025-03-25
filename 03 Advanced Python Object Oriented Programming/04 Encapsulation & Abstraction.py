# Encapsulation:
# Encapsulation is the bundling of data and methods that operate on the data within a single unit, such as a class.
# It helps in restricting direct access to some of the object's components, which prevents accidental modification.

# Abstraction:
# Abstraction is the concept of hiding implementation details and only exposing the necessary functionality to the user.
# It simplifies code usage by providing a clear interface without revealing the complex inner workings.

class PlayerCharacter:
    # The __init__ method is a constructor used to initialize the attributes of the class.
    def __init__(self, name, age):
        # Public variable (conventionally, but still accessible)
        self.name = name  # Can be accessed and modified from outside the class
        
        # Private variables (indicated by a single underscore _)
        # Not strictly private, but a convention to indicate internal use
        
        self._age = age  # Should not be accessed directly outside the class
    
    def run(self):
        print('run')

    def speak(self):
        # This method provides controlled access to private attributes
        print(f'my name is {self.name}, and I am {self._age} years old')

# Creating an instance of PlayerCharacter
player1 = PlayerCharacter('Ishtiaq', 23)

# Accessing a public variable
print(player1.name)  # Allowed, since it's a public attribute

# Accessing a private variable (Not recommended, but still possible)
print(player1._age)  # Works, but should be avoided according to convention

# Calling a method
player1.speak()  # Uses the method to access private attributes in a controlled manner

# In Python, there are no strict private variables. The convention is:
# - Public variables: `self.var` (can be accessed directly)
# - Protected variables: `self._var` (should be treated as private, but still accessible)
# - Private variables: `self.__var` (name-mangled to prevent direct access)
