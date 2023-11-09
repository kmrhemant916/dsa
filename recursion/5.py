# unique paths
# https://leetcode.com/problems/unique-paths/

def uniquePaths(m, n):
    if m == 1 or n == 1:
        return 1
    else:
        return uniquePaths(m-1,n) + uniquePaths(m,n-1)
print(uniquePaths(3,2))