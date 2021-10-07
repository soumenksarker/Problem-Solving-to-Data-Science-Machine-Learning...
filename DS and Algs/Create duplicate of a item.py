from itertools import*
def dupli(L):
    return [x for x in L for i in (1,2)]
a = dupli(['a','b','c'])
print(a)
