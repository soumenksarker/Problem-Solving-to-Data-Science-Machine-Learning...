
def main():
    n=int(input("Enter the bit in Decimal"))
    for i in range(0, 1<<n):
        gray=i^(i>>1)
        #print(gray)
        print ("{0:0{1}b}".format(gray,n))

main()
