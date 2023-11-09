# Factorial

def factorial(n):
    if n==1:
        return 1
    chotiProblem=factorial(n-1)
    badiProblem=n*chotiProblem
    return badiProblem
print(factorial(4))