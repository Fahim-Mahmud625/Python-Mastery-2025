print(4 > 5)
print(4 < 5)
print(4 >= 5)
print(4 <= 5)
print(4 == 5)
print(4 != 5)
print('a' == 'a')
print('a' == 'A')
print('a' < 'b') # because of the ASCII value
print('a' > 'A') # because of the ASCII value

print(1 < 2 < 3 < 4)
print(1 < 2 > 3 < 4) # short circuits and returns False

print(not(True)) # a keyword and also a function
print(not 1 == 2)

#Exercise
is_magician = False
is_expert = True

# check if magician AND expert: 'you are a master magician'
# check if magician but not expert: 'at least you are getting there'
# check if you are not a magician: 'you need magic powers'

if is_magician and is_expert:
    print('You are a master magician!')
elif is_magician and not is_expert:
    print('At least you are getting there!')
elif not is_magician:
    print('You need magic powers!')
# try to code more efficiently and produce more readable code