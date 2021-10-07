def gcd(x,y):
    while(y):
      x,y = y, x%y
    return x
def coprime(x,y):
    return gcd(x,y)==1

def phi(m):
    if m == 1:
        return 1
    else:
        r = [n for n in range(1,m) if coprime(m,n)]
        return len(r)
