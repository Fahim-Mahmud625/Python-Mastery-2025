# Difference between Function and Method in Python

# 1. Function:
#    - A function is an independent block of reusable code.
#    - It is defined using the `def` keyword and can be called using its name.
#    - Built-in functions like `len()`, `max()`, `sum()`, etc., are examples.

# Using built-in function `len()`
my_list = [1, 2, 3, 4]
print(len(my_list))  

# Using built-in function `max()`
print(max(my_list))  

# 2. Method:
#    - A method is a function that is associated with an object.
#    - It is defined inside a class or belongs to a data type.
#    - Built-in methods like `.append()`, `.upper()`, `.sort()`, etc., are examples.

# Using built-in method `.append()` (belongs to list objects)
my_list.append(5)
print(my_list)  

# Using built-in method `.upper()` (belongs to string objects)
text = "hello"
print(text.upper())  

# Key Differences:
# - Functions are standalone; Methods belong to objects.
# - Functions can be called directly; Methods need an instance to be called.
# - Methods operate on object data (`self`), Functions work independently.