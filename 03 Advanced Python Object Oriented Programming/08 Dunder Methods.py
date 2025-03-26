# Dunder (Magic) Methods:
# Dunder (Double Underscore) methods, also known as magic methods, allow objects to define behaviors for built-in operations.
# These methods start and end with double underscores (e.g., __init__, __str__, __len__, etc.).

class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'MawMaw',
            'pets': False
        }
    
    def __str__(self):
        # Defines how the object is represented as a string
        return f'{self.color}'
    
    def __len__(self):
        # Defines the behavior of len(object)
        return 5
    
    def __call__(self):
        # Allows the object to be called like a function
        return 'yess??'
    
    def __getitem__(self, i):
        # Allows access to dictionary-like key-value pairs
        return self.my_dict[i]

# Creating an instance of Toy
action_figure = Toy('red', 0)

# Using dunder methods
print(action_figure.__str__())  # Calls __str__() explicitly
print(str(action_figure))       # Calls __str__() implicitly
print(str('action_figure'))     # Default behavior for string objects

print(len(action_figure))       # Calls __len__()

print(action_figure())          # Calls __call__()

print(action_figure['name'])    # Calls __getitem__()

# Excercise

# Extending Built-in Classes:
# Python allows us to extend built-in types like list, dict, and str by creating subclasses.

print(dir(list))  # Lists all attributes and methods of list

class SuperList(list):  
    def __len__(self):
        # Overrides len() method to always return 1000
        return 1000

# Creating an instance of SuperList
superlist1 = SuperList([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(superlist1)         
print(len(superlist1))    
superlist1.append(5)      
print(superlist1)         

print(issubclass(SuperList, list))  # Checking if SuperList is a subclass of list
