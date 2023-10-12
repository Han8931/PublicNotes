def printRev(n):
    if n>0:
        print(n)
        printRev(n-1)

print("printRev")
printRev(4)

def printInc(n):
    if n>0:
        printInc(n-1)
        print(n)

print("printInc")
printInc(4)
