def gcd(x,y):
    while(y):
      x,y = y, x%y
    return x
def coprime(x,y):
    return gcd(x,y)==1

print(coprime(14,15))
