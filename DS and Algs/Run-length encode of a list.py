from itertools import*
def encode(alist):
     return [[len(list(group)), key] for key, group in groupby(alist)]
a = encode(['a','a','a','b','b','b',1,2,3])
print(a)
