# def is used to define a function

def say_hello():
    print('helllooooo')

say_hello()

# Functions are important for DRY
    # DRY -> Don't Repeat Yourself

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

def show_tree():
    fill = '*'
    empty = ' '
    for row in picture:
        for pixel in row:
            if pixel:
                print(fill, end = '')
            else:
                print(empty, end = '')
        print('')
        
show_tree()
show_tree()
show_tree()

print(show_tree)