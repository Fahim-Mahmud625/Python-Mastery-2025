# Excercise
# 0 -> ' '
# 1 -> '*'
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

i = 0
while i < len(picture):
    # print(picture[i])
    j = 0
    while j < len(picture[i]):
        # print(picture[i][j])
        if picture[i][j] == 0:
            print(' ', end = '')
        else:
            print('*', end = '')
        j += 1
    print('')
    i += 1
    
# using 'for' loop

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(' ', end = '')
        else:
            print('*', end = '')
    print('')