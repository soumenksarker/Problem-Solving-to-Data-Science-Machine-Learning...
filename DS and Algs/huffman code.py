def huffman(freqtable):
    #this code going to check this
##   huffman(freqtable = dict(a=45, b=13, c=12, d=16, e=9, f=5))  
    from collections import defaultdict
    from heapq import heappush,heappop,heapify
    #mapping of letters to code
    code = defaultdict(list)
    #Using a heap makes it to easy to pull items with lowestfrequency
    #items in the heap are tuple containing the letters and the combined frequency letter of the list
    heap = [(freq,[ltr]) for ltr , freq in freqtable.items()]
    heapify(heap)

  # Reduce the heap to a single item by combining the two items
    # with the lowest frequencies.


    
    while len(heap) > 1:
        freq0, letters0 = heappop(heap)
        for ltr in letters0:
            code[ltr].insert(0,'0')

        freq1, letters1 = heappop(heap)
        for ltr in letters1:
            code[ltr].insert(0,'1')

        heappush(heap, (freq0+freq1, letters0+letters1))
    for k,v in code.items():
        code[k] = ''.join(v)
    return code
if __name__ == "__main__":
   import doctest
   doctest.testmod(verbose = True)
