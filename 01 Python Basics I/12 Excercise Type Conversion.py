birth_year = input("What year were you born? ")
age = 2025 - int(birth_year) 
# input() always returns a string, so we need to convert it to an integer with int() to do the math

print(f"You will be {age} years old in 2025")