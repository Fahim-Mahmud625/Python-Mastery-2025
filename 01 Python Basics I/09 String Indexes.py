selfish = '01234567'
         # 01234567
print(selfish)
print(selfish[0])
print(selfish[7])

# [start:stop:stepover] -> string slicing
print(selfish[0:8:2])
print(selfish[::-2])

# Strings are immutable
# selfish[0] = 8 # TypeError: 'str' object does not support item assignment as strings cannot be modified, only overwritten