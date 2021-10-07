import random
def rnd_select(N,M):
    
   return random.sample(range(1, M+1),N)
a = rnd_select(['a','b','c','d','e','f'],3)
print(a)
