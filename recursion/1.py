# Print n number using recursion
# Input = 5
# Output = 1 2 3 4 5


def printUsingRecursion(n):
    if n==0:
        return
    printUsingRecursion(n-1) # this will print 1 2 3 4 (smaller problem)
    print(n) # this will print 5 (bigger problem)

printUsingRecursion(5)
