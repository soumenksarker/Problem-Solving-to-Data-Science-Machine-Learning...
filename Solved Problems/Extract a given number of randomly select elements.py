import random
def rnd_select(L,N):
    return random.sample(L, N)
a= rnd_select(['a','b','c','d','e','f','g','h'],3)
print(a)
