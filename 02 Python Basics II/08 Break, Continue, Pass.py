my_list = [1,2,3,4,5]

# Break

for item in my_list:
    print(item)
    if item == 3:
        break

# Continue

for item in my_list:
    print(item)
    continue

i = 0
while i < len(my_list):
    continue # from here, goes to the top of the loop
    print(my_list[i])
    i += 1


# Pass

for item in my_list:
    pass # just a place holder for the indentation syntax error