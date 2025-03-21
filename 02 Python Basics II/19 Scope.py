# Simply means what variable do I have access to?
a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())

# Notes on Scope:
# 1. **Global Scope:** The variable `a` outside the function is global and accessible everywhere.
# 2. **Local Scope:** The variable `a` inside `confusion()` is local and only exists within the function.
# 3. **Variable Shadowing:** The local `a` inside `confusion()` does not affect the global `a`.

def confusion():
        return a

print(confusion())

def parent():
    a = 10
    def confusion():
        return a
    return confusion()
    
print(parent())
    

# Rule
# 1 -> start with local
# 2 -> Parent local? 
