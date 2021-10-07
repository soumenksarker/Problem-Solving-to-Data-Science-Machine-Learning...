from itertools import count

def prime_factors(n):
    factors = []
    for i in count(2):
        while n % i == 0:
            n //= i
            factors.append(i)
        if 2 * i > n:
            return factors

n = int(input('Enter the integer you wish to find the prime factors of: '))
print(prime_factors(n))
