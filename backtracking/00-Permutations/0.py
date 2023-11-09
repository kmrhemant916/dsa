class Solution:
    def __init__(self, arrStr):
        self.arrStr = arrStr

    def permutationOfString(self):
        result = []
        def solve(arr,start,end):
            if start>=end:
                result.append(arr[:])
                return
            for i in range(start,end):
                arr[start], arr[i] = arr[i], arr[start]
                solve(arr,start+1,end)
                arr[start], arr[i] = arr[i], arr[start]
        solve(self.arrStr,0,len(self.arrStr))
        return result

testCase = ["A", "B", "C"]
sol = Solution(testCase)
print(sol.permutationOfString())

