# Find 2^n

def twoThePower(n):
    if n==0:
        return 1
    chotiProblem = twoThePower(n-1)
    badiProblem = 2 * chotiProblem
    return badiProblem
print(twoThePower(4))