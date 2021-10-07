def combination(K, L):
        if K<=0:
            yield []
            return
        for i in range(len(L)):
            thisone = L[i:i+1]
            for another in combination(K-1, L[i+1:]):
                yield thisone + another
a =combination(3,['a','b','c','d','e','f'])
for i in a:
        print(i)
