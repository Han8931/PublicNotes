import pdb

class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class diameterBinTree():
    def __init__(self,):
        self.longest = 0 # This is very important

    def diameter(self, root):
        def dfs(node):
            if not node:
                return -1 # The height of Null node is treated as -1 

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right+2) # Diameter
            return max(left, right)+1  # Height

        dfs(root)
        return self.longest

# This is an incorrect solution due to the variable longest
def diameter(root):
    # This is an immutable variable, since it is an integer variabel
    longest = 0 

    def dfs(node):
        if not node:
            return -1 # The height of Null node is treated as -1 

        left = dfs(node.left)
        right = dfs(node.right)

        # This operation assigns 'longest' variable again as a local variable
        longest = max(longest, left+right+2) # Diameter
        return max(left, right)+1  # Height

    dfs(root)
    return longest

def diameter(root):
    longest = [0] 

    def dfs(node):
        if not node:
            return -1 # The height of Null node is treated as -1 

        left = dfs(node.left)
        right = dfs(node.right)

        longest[0] = max(longest[0], left+right+2) # Diameter
        return max(left, right)+1  # Height

    dfs(root)
    return longest[0]


root = TreeNode(1)
nl_1 = TreeNode(2)
nr_1 = TreeNode(3)
root.left = nl_1
root.right = nr_1
nl_1.left = TreeNode(4)
nl_1.right = TreeNode(5)

diam = diameterBinTree()
print(diam.diameter(root))

print(diameter(root))






