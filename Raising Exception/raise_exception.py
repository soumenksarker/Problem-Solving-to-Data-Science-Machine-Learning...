class ShortInputException(Exception):
    '''A user-defined exception class'''
    def __init__(self, length, atleast):
       Exception.__init__(self)
       self.length = length
       self.atleast = atleast
try:
    text = input('Enter something')
    if len(text)<3:
     raise ShortInputException(len(text), 3)
    #other work can continue as usual
except EOFError:
    print ('why did u do an EOF on me?')
except ShortInputException as ex:
    print (('ShortInputException: The input was' + '{} long, expected at least {}').format(ex.length, ex.atleast))
else:
     print ('no exception is raised')
    

