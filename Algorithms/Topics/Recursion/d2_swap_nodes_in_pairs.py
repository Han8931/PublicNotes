# Basic 1
def reverse(list_s):
    if len(list_s)==1:
        return print(list_s[0])
    else:
        print(list_s[-1])
        list_s = list_s[:-1]
        return reverse(list_s)

def reverse2(list_s):
    if len(list_s)==0:
        return []
    else:
        return [list_s.pop()]+reverse2(list_s)

list_s = [1, 3, 4]
reverse(list_s)

list_s = [1, 3, 4]
print(reverse2(list_s))

list_s = [1, 3, 4]
print(list_s[::-1])
