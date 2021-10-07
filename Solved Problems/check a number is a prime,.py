def main():
 n = int(input("Please enter a number:"))
 is_prime(n)

def is_prime(a):
    x = True 
    for i in range(2, a):
            while x:
               if a%i == 0:
                   x = False
               break


    if x:
        print("OH! yeah! its a prime number")
    else:
        print("sorry! it's not prime")

main()
