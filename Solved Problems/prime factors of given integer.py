def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i==1:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
a = prime_factors(int(input("please enter a number to find the all prime factors")))
print(a)
