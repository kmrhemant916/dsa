# Step 1 - Draw recursion tree using pen and paper
# Basically you have to solve the first level of recursion tree
# Ref: https://www.youtube.com/watch?v=V0IgCltYgg4&t=897s
# Algorithm:
    # You have two choices either take or not take the current element
    # When you take the current element, rest of them can be solved using recursion
    # Same thing we need to do for when we don't take the element
    # And call the recursion
class Solution:
    def __init__(self, arrNum) -> None:
        self.arrNum = arrNum
    def printSubsets(self):
        finalResult=[]
        def solve(arrNum,index,result):
            if index==len(arrNum):
                finalResult.append(result[:])
                return
            result.append(arrNum[index])
            solve(arrNum,index+1,result)
            result.pop()
            solve(arrNum,index+1,result)
        solve(self.arrNum,0,[])
        return finalResult

sol=Solution("ABC")
res = sol.printSubsets()
for elem in res:
    print(elem)