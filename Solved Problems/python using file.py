poem = '''\
programming is fun when the work is done if u wanna make your life fun try python!
'''
#open for writing
#f = open('poem.txt','w')
#f.write(poem)
#f.close()
#if no mode is specified then the read mood is taken by default of python
f = open('poem.txt')
while True:
     line = f.readline()
     if len(line) == 0:
      break
     print (line, end='')
     f.close()
    
