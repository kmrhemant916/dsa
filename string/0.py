# Palindrome check

# abba
# aba
# Algo - Two pointer start and end, go till end >= start. Check from odd and even string example

def checkPalndrome(s):
    start=0
    end=len(s)-1
    while end>=start:
        if s[start]!=s[end]:
            return False
        start += 1
        end -= 1
    return True
print(checkPalndrome("a"))