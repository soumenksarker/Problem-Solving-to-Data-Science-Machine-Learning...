def searchList(list, item):
    pos = 0
    found = False
    while pos < len(list) and not found:
        if list[pos]== item:
            
           found = True
        else:
            pos +=1
    return found
print(searchList([1,34,12,24], 13))
