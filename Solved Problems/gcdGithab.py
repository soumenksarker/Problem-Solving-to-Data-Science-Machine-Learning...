def gcd(n, d):
    while n != d:
        if n > d:
            n = n - d
        else:
            d = d - n
    return n
class Fraction:
     def __init__(self, n, d):
         self.num = int(n/gcd(abs(n), abs(d)))
         self.den = int(d/gcd(abs(n), abs(d)))
         if self.den<0:
              self.den = abs(self.den)
              self.num = -1*self.num
         elif self.den == 0:
             raise ZeroDivisionError

     def Add(self, other):
         return self.num*other.den + other.den*self.num, self.den*other.den

     def Sub(self, other):
         return self.num*other.den - other.den*self.num, self.den*other.den

     def Mul(self, other):
         return self.num*other.num, self.den*other.den

     def Div(self, other):
         return self.num*other.den, self.den*other.num

def main():
    f1 = Fraction(1,1)
    f2 = Fraction(1,1)
    f3 = Fraction.Add(f1,f2)
    f4 = Fraction.Sub(f1,f2)
    f5 = Fraction.Mul(f1,f2)
    f6 = Fraction.Div(f1,f2)
    print(Fraction.__str__(f3),Fraction.__str__(f4),Fraction.__str__(f5),Fraction.__str__(f6))
    
if __name__ == '__main__':
    main()
