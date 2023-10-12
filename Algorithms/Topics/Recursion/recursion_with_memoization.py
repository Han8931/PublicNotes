# Basic 1
def fibo(n):
    cache = {}

    def recur_fib(n):
        if n in cache:
            return cache[n]
        if n<2:
            result = n
        else:
            result = recur_fib(n-2)+recur_fib(n-1)
        cache[n] = result
        return result

    return recur_fib(n)

out = fibo(5)
print(out)
