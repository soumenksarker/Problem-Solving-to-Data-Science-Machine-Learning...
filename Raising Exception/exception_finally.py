import sys
import time
#f = None
try:
    f = open("poem.txt")
    #our usual reading file ideom
    while True:
        line = f.readline()
        if len(line) == 0:
             break
        print (line)
        #HERE I USE THIS STATEMENT TO PRINT THE LINE FAST
        sys.stdout.flush()
        print ("press cntrol+c now")
        # To make sure it runs for while
        time.sleep(2)
except IOError:
    print ("could not find file poem.txt")
except KeyboardInterrupt:
    print (" !! U cancelled the file from reading")

finally:
    if f:
        f.close()
    print ("(Cleaning up: Closed the file)")
