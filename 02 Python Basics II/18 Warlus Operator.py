# assigns values to variables as a part of larger expression
a = 'helloooooooo'

if (n := len(a)) > 10:
    print(f'Too long {n} elements')
    
while (n := len(a)) > 1:
    print(n)
    a = a[:-1]