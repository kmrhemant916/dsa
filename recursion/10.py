# Print n number using recursion
# Input = 5
# Output = 5 4 3 2 1

def printUsingRecursion(n):
    if n==0:
        return
    print(n)
    printUsingRecursion(n-1)

printUsingRecursion(5)
