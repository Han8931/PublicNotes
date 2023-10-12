import pdb

def balancedBT(root):
    if not root:
        return

    def recursion(node):
        if not node:
            return 0
        left = recursion(node.left)
        right = recursion(node.right)
        if left==-1 or right==-1 or abs(left-right)>1:
            return -1
        return max(left, right)+1

    return recursion(root)!=-1

