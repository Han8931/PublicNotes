def bubbleSort(inp_list):
    swap = False
    for i in range(len(inp_list)-1):
        for j in range(0,len(inp_list)-i-1):
            a = inp_list[j]
            b = inp_list[j+1]
            if a>b:
                swap=True
                inp_list[j] = b
                inp_list[j+1] = a
        if not swap:
            return

def bubbleSort2(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(0,length-i-1):
            a = arr[j]
            b = arr[j+1]
            if a>b:
                arr[j],arr[j+1] = arr[j+1], arr[j]

test = [2, 4, 1, 6, 3]
print(test)
bubbleSort3(test)
print(test)



