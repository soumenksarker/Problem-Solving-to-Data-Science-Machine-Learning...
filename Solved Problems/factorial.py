def factorial(n):
     if n==0:
          print("the factorial is 1")
     else:
         for i in range(1, n):
             n = n*i
         return n
a = factorial(int(input("pleaese enter a number")))
print('the factorial of given integer is ', a)
