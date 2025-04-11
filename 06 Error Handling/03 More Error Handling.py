while True:
    try:
        age = int(input('what is your age? '))
        10/age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you')
        break
    finally:
        print('ok, i am finally done')
    print('can you hear me?') # it will not be printed if the exception is raised, but it will be printed if the exception is not raised
    
# raise

while True:
    try:
        age = int(input('what is your age? '))
        10/age
        raise Exception('hey cut it out!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you')
        break
    
# anticapte errors and handle them