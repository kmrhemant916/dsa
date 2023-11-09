# palindrome using recursion

str="abba"
def palindrome(str, start, end):
    if start >= end:
        True
    if str[start] == str[end]:
        palindrome(str[start:end], start+1, end-1)
    else:
        return False

print(palindrome(str, 0, len(str)-1))