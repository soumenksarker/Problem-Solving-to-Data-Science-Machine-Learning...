def main():
    #find the prime number
    def prime(n):
      prime = True
      for i in range(2, n):
          if (n%i == 0):
              return False
      if prime:
              return True

    #enter the range and find the primes number

    r1=(int(input("Enter the LOWER of the number")))
    r2=(int(input("Enter the UPPER of the number")))
    for even in range(r1, r2+1):
          if even%2 == 0:
              print(even)
              for a in range(1, even+1):
                 if prime(a):
                     for b in range(1, even+1):
                          if prime(b):
                              if(a+b==even):
                                  if (a <= b):
                                      print(" " ,"=",a,"+",b)
main()
