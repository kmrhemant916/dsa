# sum of n natural numbers

def sum(num):
    if num == 0:
        return 0
    return num + sum(num-1)
print(sum(10))