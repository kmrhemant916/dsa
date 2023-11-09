# Check of parenthesis

def ispar(x):
    stack=[]
    stack.append(x[0])
    for str in x[1:]:
        print(stack[-1], str)
        if stack[-1] == str:
            stack.pop()
        else:
            stack.append(str)
    if stack == []:
        return True
    else:
        return False
print(ispar("()]}"))