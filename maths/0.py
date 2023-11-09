# Count traling zero in a factorial

def countZeros(num):
    factorial=1
    count=0
    while num != 1:
        print(num, end=" ")
        factorial=factorial*num
        num-=1
    # print(factorial)
    while factorial % 10 == 0:
        count += 1
        factorial=factorial//10
    return count

print(countZeros(2))