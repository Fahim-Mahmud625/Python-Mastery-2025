# While loop is simply conditional loop, in simple words it will loop while the statement is true

i = 0
while i < 50:
    print(i)
    break

while i < 50:
    print(i)
    i += 1 # will break the loop when i becomes 50
else:
    print('Done with all the work') # nothing's happening so it will be executed    

i = 0
while i < 50:
    print(i)
    i += 1 
    break
else:
    print('Done with all the work')    # Note that it will only execute when the loop is complete, as we are brealing the loop it does not print
    
# For vs While loops
    # for simple loops, iterating over iterable, 'for' loops are great
    # for conditional cases and unknown iteration 'while' loops are superior

my_list = [1,2,3]

for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input('say something: ')
    if response == 'bye':
        break
