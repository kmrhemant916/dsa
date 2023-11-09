# Average of a list in python

def avgListUsingLoop(list):
    sum=0
    for i in list:
        sum += i
    return sum/len(list)
print(avgListUsingLoop([1,2,3,4,2]))


list=[1,2,3,4,2]
def avgListUsingRecursion(list):
    print(list)
    if len(list) == 1:
        return list[0]
    else:
        end=len(list)-1
        return list[end] + avgListUsingRecursion(list[:end])
sum=avgListUsingRecursion(list)
print(sum/len(list))