# sum of digits using recursion

def sumofdigit(num):
    if num < 10:
        return num
    return (num % 10 ) + sumofdigit(num//10)

print(sumofdigit(121111))
