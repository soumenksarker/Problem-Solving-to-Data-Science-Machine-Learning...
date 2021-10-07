from itertools import chain, count

def prime_factors(n):
    for i in chain([2], count(3, 2)): # Try 2, 3, 5, 7, 9, 11, 13, 15...
        while n % i == 0:
            yield i
            n //= i
        if 2 * i > n:
            return 

n =prime_factors(int(input('Enter the integer you wish to find the prime factors of: ')))
for i in n:
    print(i)
