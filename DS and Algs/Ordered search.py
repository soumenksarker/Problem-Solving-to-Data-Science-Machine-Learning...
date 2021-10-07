def search(list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(list) and not found and not stop:
        if list[pos] == item:
            found = True
        else:
            if list[pos]>item:
                stop = True
            else:
                pos = pos + 1
    return found
print(search([1,2,4,5,6,7], 7))
print(search([12,13,14,15,17],18))
