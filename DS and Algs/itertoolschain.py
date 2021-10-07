from itertools import*

for i in chain([1, 2, 3], ['a', 'b', 'c'],['d', 'f', 'e']):
    print(i)
