import math

def CalculateE(x):

    E = round(math.e, x)
    return E

roundTo = input('Enter a number of digit that u want after the decimal point of e')
roundint = int(roundTo)
print (CalculateE(roundint))

