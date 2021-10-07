import random
def rnd_select(N,M):
    return random.sample(range(1,M+1),N)
a = rnd_select(10,49)
print(a)
