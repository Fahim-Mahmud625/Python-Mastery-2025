# Pure Functions

# A pure function is a function that:
# 1. Given the same input, always produces the same output.
# 2. Has no side effects (does not modify external variables, perform I/O operations, etc.).

# Example of a pure function:

def multiply_by2(li):
    new_list = []  # Creates a new list instead of modifying an existing one
    for i in li:
        new_list.append(i * 2)  # No external changes, only computation
    return new_list  # Always returns the same result for the same input

print(multiply_by2([1, 2, 3]))  # Output: [2, 4, 6]

# Why is this function pure?
# - It always returns the same result for the same input.
# - It does not change any external variables or cause side effects.