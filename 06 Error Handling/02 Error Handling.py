while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you')
        break
    

def sum(a, b):
    try:
        return a + b
    except TypeError as err:
        print(f'please enter numbers {err}') # try to be more descriptive
    
sum('1', 2)

def div(a, b):
    try:
        return a / b
    except (TypeError, ZeroDivisionError) as err:
        print(f'opppss {err}') # try to be more descriptive
    
div(1, 0)
div(1, '2')