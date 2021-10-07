from itertools import *

print ('Doubles:')
for i in map(lambda x:2*x, range(5)):
    print (i)

print ('Multiples:')
for i in map(lambda x,y:(x, y, x*y), range(5), range(5,10)):
    print ('%d * %d = %d' % i)
