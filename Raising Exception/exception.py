try:
    text = input('Enter something')
except EOFError:
    print ('why did u do an EOF on me')
except keyboardInterrupt:
    print ('U cancelled the program')
else:
    print ('You entered {}'.format(text))

