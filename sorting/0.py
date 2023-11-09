# Bubble Sort
# Run two loop and swap element if its greater
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]