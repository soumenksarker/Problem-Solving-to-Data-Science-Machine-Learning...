from itertools  import*
def insert_at(x, L,N):
   return L[:N-1]+[x]+L[N-1:]
a = insert_at('alfa',['a','b','c','d'],2)
print(a)
