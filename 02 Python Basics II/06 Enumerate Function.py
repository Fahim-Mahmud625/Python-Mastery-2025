# enumerate() will take a iterable and return a tuple with the index and the value of the element
    # gives index counter and the item that index

for i, char in enumerate('Helllooo'):
    print(i, char)

for i,value in enumerate([1,2,3]):
    print(i, value)

for i,value in enumerate((1,2,3)):
    print(i, value)

# important if index counter is needed

for i, value in enumerate(list(range(100))):
    if value == 50:
        print(f'The index of 50 is: {i}')