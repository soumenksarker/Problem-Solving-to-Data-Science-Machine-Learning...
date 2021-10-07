from itertools import*

def pack(alist):
     return [list(group) for key, group in groupby(alist)]
a = pack(['a','a','a','b','b','b','c','c'])
print(a)
