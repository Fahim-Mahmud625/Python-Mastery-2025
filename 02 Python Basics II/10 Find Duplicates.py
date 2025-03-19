# Excercise: Check for duplicates in list:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
i = 0
while i < len(some_list):
    j = i + 1
    while j < len(some_list):
        if some_list[i] == some_list[j]:
            duplicates.append(some_list[i])
        j += 1
    i += 1
    
print(duplicates)

# More robust and condensed :

for value in some_list:
    if some_list.count(i) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)