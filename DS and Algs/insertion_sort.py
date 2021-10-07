def insertion_sort(list):
    for i in range(1,len(list)):
        #print(i)
        current_value = list[i]
        pos = i
        while pos>0 and list[pos - 1] > current_value:
            list[pos] = list[pos-1]
            pos = pos - 1
        list[pos] = current_value
list = [54,26,93,17,77,31,20]
insertion_sort(list)
print(list)
