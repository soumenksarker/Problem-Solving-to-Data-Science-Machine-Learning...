from itertools import*

def drop(L, N):
    return [x for i, x in enumerate(L) if (i+1)%N]

a = drop(['a','b','c','d','e','f','g','h','i','k'],3)
print(a)

