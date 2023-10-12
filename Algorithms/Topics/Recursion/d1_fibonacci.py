# Basic 1
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-2)+fibo(n-1)

out = fibo(4)
print(out)


def fibo2():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for i in fibo2():
    if i>100:
        break

