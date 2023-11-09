# print element of an array recursively

list=[1]
def printArrayRecursive(list, n):
    if len(list) == 1:
        print(list[0])
    else:
        print(list[0], end=" ")
        printArrayRecursive(list[-n+1:], n-1)
    

printArrayRecursive(list, len(list))