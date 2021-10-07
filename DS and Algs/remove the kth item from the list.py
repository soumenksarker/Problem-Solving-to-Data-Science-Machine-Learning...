from itertools import*
def remove(L,N):
   return L[N-1], L[:N-1] + L[N:]
a = remove(['a','b','c','d'],2)
print(a)
