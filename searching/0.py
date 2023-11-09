# Binary search algorithm

# def binarySearch(list, num):
#     start=0
#     end=len(list)-1
#     while start <= end:
#         middle=(start+end)//2
#         if list[middle] == num:
#             return middle
#         elif list[middle] > num:
#             end=middle-1
#         else:
#             start=middle+1
#     return -1

# print(binarySearch([1,4,5,6,7,8,9], 61))

# Binary search using recursion

list=[1,4,5,6,7,8,9]
print(list[::-1])
# def binarySearchUsingRecursion(list, start,end, num):
#     middle=(start+end)//2
#     print(start,end)
#     if start>end:
#         return -1
#     if list[middle] == num:
#         return middle
#     elif list[middle] > num:
#         return binarySearchUsingRecursion(list, start, middle-1, num)
#     else:
#         return binarySearchUsingRecursion(list, middle+1, end, num)


# print(binarySearchUsingRecursion(list, 0, len(list)-1, 9))