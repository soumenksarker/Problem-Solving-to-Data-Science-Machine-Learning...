m = int(input("please enter the min integer "))
n = int(input("please enter the max integer "))
for num in range(m,n+1):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)
