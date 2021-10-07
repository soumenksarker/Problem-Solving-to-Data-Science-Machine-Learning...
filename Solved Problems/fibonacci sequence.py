def fibonacci(n):
     a= 0
     b=1

     for i in range(n-2):
         c = a+b
         print(c)
         a=b
         b=c

def main():
    n = input('Enter an integer')
    fibonacci(int(n))

if __name__ == '__main__':
    main()
