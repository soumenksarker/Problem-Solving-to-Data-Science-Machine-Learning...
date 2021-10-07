def hash(string, table_size):
    sum = 0
    for pos in range(len(string)):
        sum = sum + ord(string[pos])

    return sum%table_size
print(hash(input('plz enter a string'),11))
