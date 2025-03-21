def highest_even(list):
    h_even = 0
    for num in list:
        if num % 2 == 0:
            if num > h_even:
                h_even = num
    return h_even

print(highest_even([11,1,10,2,3,4,8]))