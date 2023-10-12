import pdb

def sortedArrayToBST(arr):
    if not arr:
        return 
    mid = len(arr)//2
    node = TreeNode(arr[mid])
    node.left = sortedArrayToBST(arr[:mid])
    node.right = sortedArrayToBST(arr[mid+1:])

    return node
