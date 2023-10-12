# Basic 1
def recurvsive(n):
    if n==1:
        print(n)
        return 1
    else:
        print(n)
        return recurvsive(n-1)

recurvsive(10)
