import pdb

def inorder(root):
    res = []

    def traverse(node):
        if not node:
            return
        
        traverse(node.left)
        res.append(node.val)
        traverse(node.right)

    traverse(root)

    return res

def preorder(root):
    res = []

    def traverse(node):
        if not node:
            return
        
        res.append(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(root)

    return res

def postorder(root):
    res = []

    def traverse(node):
        if not node:
            return
        
        traverse(node.left)
        traverse(node.right)
        res.append(node.val)

    traverse(root)

    return res
