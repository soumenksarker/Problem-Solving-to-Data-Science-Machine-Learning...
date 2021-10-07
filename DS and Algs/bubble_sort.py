def bubble_sort(alist):
    exchanges = True
    num_pass = len(alist) -1
    for i in range(num_pass):
        exchanges = False
        if alist[i]>alist[i+1]:
           exchanges = True
           temp = alist[i]
           alist[i] = alist[i+1]
           alist[i+1] = temp
    num_pass = num_pass - 1
a = [11,141,12,141,415,777]
bubble_sort(a)
print(a)


