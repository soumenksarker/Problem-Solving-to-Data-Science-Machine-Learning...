def insertion_sort(list):
     for index in range(len(list)):
          value = list[index]
          i = index - 1
          while i>=0 and (value<list[i]):
                  list[i+1] = list[i] #SHIFT NUMBER i to i+1
                  list[i] = value #shift value left into slot
                  i = i-1

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)
