import random

def roll(a, b=6, c=0):
    sum = 0
    kostki = [3, 4, 6, 8, 10, 12, 100]
    if b in kostki:
        for i in range(0, b):
            sum += random.randint(1, a)
        return sum + c
    else:
        return "No such dice!"

print(roll(2, 10, 20))
print(roll(2, 10))
print(roll(2, 10, -20))
print(roll(3, 6, -3))
print(roll(3, 7, -3))

""""
def roll(a, b=6, c=0):

    kostki = (3, 4, 6, 8, 10, 12, 100)
    if b not in kostki:
        raise Exception()

    sum = 0
    for i in range(a):
    sum += random.randint(1, b)
    
    return sum + c
"""