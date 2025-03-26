# Method Resolution Order (MRO) in Python

# MRO determines the order in which methods are inherited and searched in a class hierarchy.
# Python follows the C3 Linearization (C3 MRO) algorithm to ensure a consistent inheritance structure.

# Example 1: Simple Multiple Inheritance
class A:
    pass

class B:
    pass

class C(A, B):  # C inherits from A and B
    pass

class D(C, B):  # D inherits from C and B
    pass

# Checking MRO of class D
print(D.mro())  # Displays the order in which methods will be resolved

# Explanation:
# - D is searched first.
# - Then C (since it’s inherited first in D).
# - C inherits from A, so A comes before B.
# - Finally, B is checked, followed by the built-in object class.

# Example 2: MRO with a Superclass Restriction
class A:
    pass

class B(A):  # B inherits from A
    pass

class C(A):  # C also inherits from A
    pass

class D(B, C):  # D inherits from B and C
    pass

# Checking MRO of class D
print(D.mro())  # Displays the method resolution order

# Explanation:
# - D is searched first.
# - Then B, because it is inherited first in D.
# - B inherits from A, but C is also a parent of D.
# - C is checked next, ensuring A appears after C.
# - Finally, A is checked before the built-in object class.

# Key Rules of MRO (C3 Linearization):
# 1. Child classes come before parent classes.
# 2. Left-to-right order matters in multiple inheritance.
# 3. A superclass cannot appear before a subclass in MRO.