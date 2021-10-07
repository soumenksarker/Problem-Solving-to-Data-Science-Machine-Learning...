from itertools import*
def dupli(L,N):
    return [x for x in L for i in range(N)]
a = dupli(['a','b','v'], 10)
print(a)
