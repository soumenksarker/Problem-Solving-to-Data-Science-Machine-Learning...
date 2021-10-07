import random
def rnd_permu(L):
    return random.sample(L,len(L))
a = rnd_permu(['a','b','c','d','e','f'])
print(a)
