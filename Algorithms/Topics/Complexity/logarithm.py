def ex(n):
    count = 0
    i = n
    while i>=1:
        count+=1
        i/=2
    return count

print(ex(16))
