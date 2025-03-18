is_old = False
is_licenced = True

if is_old:
    print('You are old enough to drive!')
elif is_licenced:
    print('You can drive now!')
else:
    print('You are not old enough to drive!')

print('ok ok')

is_old = True
is_licenced = True 

if is_old and is_licenced:
    print('You are old enough to drive, and you have a licence!')
else:
    print('You are not old enough to drive!')

# indentation is important in python, it is used to define the scope of the code and the block of code
    # have to be careful with it

# Truthy and Falsy values
# Truthy values: values that are considered true when encountered in a Boolean context
print(bool('hello'))
print(bool(5))
# Falsy values: values that are considered false when encountered in a Boolean context
print(bool(''))
print(bool(0))

# for more visit https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false

username = 'johnmaw'
password = '123456'

if username and password:
    print('You are logged in!')
else:
    print('You are not logged in!')

# Ternary Operator
    # conditional expression that evaluates something based on a condition being true or false

# condition_if_true if condition else condition_if_false

is_friend = True
can_message = 'message allowed' if is_friend else 'not allowed to message'
print(can_message)

# Short Circuiting
# for 'or operator' and 'and operator'
# so basically it is called short circuiting because if the first condition is true (or)/false (and), then the second condition is not checked

is_friend = True
is_user = True
if is_friend or is_user:
    print('Best friends forever!')