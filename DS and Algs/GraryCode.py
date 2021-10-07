

def Gray_Code(n):
   res = [0]
   for i in range(n):
      res+=(2**i+x for x in res[::-1])
      return res
      

