class Binary_Heap:
    def __init__(self):
        self.heaplist = []
        self.current_size = 0
        
    def perc_up(self):
        while i//2 >= 0:
            if heaplist[i] > heaplist[i//2]:
                tmp = heaplist[i//2]
                heaplist[i//2] = heaplist[i]
                heaplist[i] = tmp
            i = i//2
            
    def insert(self,k):
        self.heaplist.append(k)
        self.current_size = current_size + 1
        self.perc_up(current_size)


    def parc_down(self,i):
        while (i*2) <= current_size:
            if 
        
