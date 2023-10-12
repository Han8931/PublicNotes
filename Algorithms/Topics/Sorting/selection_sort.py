def selectionSort(inp_list):
    len_list = len(inp_list)
    for i in range(len_list-1):
        min_idx = i
        for j in range(i+1,len_list):
            if inp_list[min_idx]>inp_list[j]:
                min_idx = j

        inp_list[i], inp_list[min_idx] = inp_list[min_idx], inp_list[i]
#        temp = inp_list[i]
#        inp_list[i] = inp_list[min_idx]
#        inp_list[min_idx] = temp





