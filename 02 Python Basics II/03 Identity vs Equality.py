# equality (==) operator checks the value
print(True == 1)
print([] == 1)
print([] == [])
print('' == 1)
print(10 == 10.0)

# identity (is) operator checks the memory location
print(True is 1)
print([] is 1)
print([1,2,3] is [1,2,3]) # evertime we create a new list, it is stored in a different memory location, hence the output is False
print('' is 1)
print(10 is 10.0)
# for more visit https://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is-in-python
