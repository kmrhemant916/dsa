# Write a python function which will print 5 times "gfg"

def printGFG(num):
    if num <= 0:
        return
    else:
        print("gfg")
        printGFG(num-1)
printGFG(6)