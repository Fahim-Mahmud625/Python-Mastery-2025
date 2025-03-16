print(list(range(0,100)))
print(list(range(0,100,2)))
print(list(range(101)))

sentence = '!'
new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'Eren'])
print(new_sentence)

sentence = ' '
new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'Eren'])
print(new_sentence)

# .join() is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string.
# the separator string is the string that the .join() method is called on, so for example, 
    # if we call .join() on the string ' ' then the list elements will be joined by a space.
    # if we call .join() on the string '!' then the list elements will be joined by an exclamation mark.

new_sentence = ' '.join(['Hi', 'my', 'name', 'is', 'Eren']) # list -> string
print(new_sentence)
