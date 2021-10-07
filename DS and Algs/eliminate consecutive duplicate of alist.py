from itertools import groupby

def compress(alist):
     return [key for key, group in groupby(alist)]
    
a=compress(['a','a','b','c','d','d','d','e','e'])
print(a)
