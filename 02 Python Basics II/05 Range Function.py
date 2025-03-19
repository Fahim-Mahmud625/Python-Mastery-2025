# range() is useful specially in for loops. It generates a sequence of numbers. 

for number in range(0, 100): # it is iterable
    print(number)

for _ in range(0, 10, 2): # _ is a common convention for a throwaway variable, as it tells the reader that the value is not going to be used
    print(_)
    
for _ in range(10, 0, -1):
    print(_)

for _ in range(2):
    print(list(range(10))) # range can be converted to a list 