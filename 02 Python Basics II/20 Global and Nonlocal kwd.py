# Global

total = 0

def count():
    global total 
    total += 1
    return total

count()
count()
print(count())

print(total)

# another way :

def count(total):
    total += 1
    return total

print(count(count(count(total))))

# Non local
# Notes on `nonlocal`:
# - The `nonlocal` keyword is used inside a nested function to modify a variable from its enclosing (but non-global) scope.
# - It prevents Python from treating the variable as a new local variable inside the nested function.
# - If `nonlocal` is not used, assigning a value to the variable inside the inner function creates a new local variable instead of modifying the outer one.

# - Example:

def outer():
    x = 'local'
    def inner():
        nonlocal x 
        x = 'nonlocal'
        print('inner:', x)
    
    inner()
    print('outer:', x)

outer()    

#   - Before calling `inner()`, `x = 'local'` in `outer()`.
#   - After `inner()`, `x = 'nonlocal'`, showing that `nonlocal` modified the enclosing scope variable.