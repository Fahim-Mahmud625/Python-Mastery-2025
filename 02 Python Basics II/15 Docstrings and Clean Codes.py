def test(a):
    '''
    Info: this function tests and prints parameter a
    '''
    print(a)
    
test('!!!')
help(test)
print(test.__doc__)

# Clean Code

def is_even(num):
    return num % 2 == 0

print(is_even(50))

print(is_even(9))

# Why this is clean code:
# 1. Concise and Readable: The function name clearly conveys its purpose.
# 2. Single Responsibility: It checks evenness without unnecessary logic.
# 3. Reusability: Can be used anywhere without modification.