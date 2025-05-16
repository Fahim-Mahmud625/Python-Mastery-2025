# Creating Generators

class Mygen():
    current = 0
    def __init__(self, last):
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if Mygen.current < self.last:
            num = Mygen.current
            Mygen.current += 1
            return num
        raise StopIteration
    

gen = Mygen(10)
for i in gen:
    print(i)