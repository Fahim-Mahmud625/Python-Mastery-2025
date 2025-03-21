def sum(num1, num2):
    return num1 + num2

print(sum(4, 5)) # a function either modifies something or returns something

# Should do one thing really well
# Should return something

total = sum(10, 5)
print(total)

print(sum(10, total))

def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)



total = sum(10, 20)
print(total)


# Excercise

age = input("What is your age?: ")

if int(age) < 18:
	print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
	print("Powering On. Enjoy the ride!");
elif int(age) == 18:
	print("Congratulations on your first year of driving. Enjoy the ride!")
 
# 1. 
    # Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
        # Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

def checkDriverAge():
    age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
        
checkDriverAge()

# 2.
    # Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
        #checkDriverAge(92);
        #it returns "Powering On. Enjoy the ride!"
    #also make it so that the default age is set to 0 if no argument is given.

def checkDriverAge(age = 0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
        
checkDriverAge(92)
checkDriverAge()