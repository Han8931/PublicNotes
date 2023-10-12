
def sort_list(root):
    node = root
    vals = []
    while node:
        vals.append(node.val)
        node = node.next

    vals.sort()

    node = root
    i = 0
    while node:
        node.val = vals[i]
        node = node.next
        i+=1

    return root
    
