# Ref - https://www.youtube.com/watch?v=tWnHbSHwNmA&t=713s
# Basically you have to solve the first level of recursion tree
class Solution:
    def possibleWords(self,a,N):
        mapDigit={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        result=[]
        def solve(a,currIndexInArray,currStrArr):
            if currIndexInArray==len(a):
                result.append(''.join(currStrArr))
                return
            for elem in mapDigit[a[currIndexInArray]]:
                currStrArr.append(elem)
                solve(a,currIndexInArray+1,currStrArr)
                currStrArr.pop()
        solve(a,0,[])
        return sorted(result)