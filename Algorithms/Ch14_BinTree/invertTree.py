import pdb

class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

root = TreeNode(1)
nl_1 = TreeNode(2)
nr_1 = TreeNode(3)
root.left = nl_1
root.right = nr_1
nl_1.left = TreeNode(4)
nl_1.right = TreeNode(5)

def invertTree(root):

    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root
    return None

def invertTree(root):
    def dfs(node):
        if not node:
            return
        else:
            node.right, node.left = node.left, node.right

        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return root

def invert_tree_bfs(root):
    queue = [root]

    while queue:
        v = queue.pop(0)
        if v:
            v.left, v.right = v.right, v.left
            queue.append(v.left)
            queue.append(v.right)

    return root


root = invertTree(root)

print(root.data)
print(root.left.data)
print(root.right.data)
print(root.right.left.data)
print(root.right.right.data)
