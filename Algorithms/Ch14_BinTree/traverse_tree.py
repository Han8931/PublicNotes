from bintree import sample_tree

def inorder_rec(root):
    if not root:
        return 
    inorder_rec(root.left)
    print(root.val, end=' ')
    inorder_rec(root.right)

def inorder_iter(root):
    stack = [root]

    node = root
    while stack:
        if node.left:
            stack.append(node.left)
            node = node.left
        else:
            v = stack.pop()
            print(v.val, end=' ')
            if v.right:
                stack.append(v.right)
                node = v.right

def preorder_rec(root):
    if not root:
        return 
    print(root.val, end=' ')
    preorder_rec(root.left)
    preorder_rec(root.right)

def preorder_iter(root):
    stack = [root]
    visit = []

    while stack:
        v = stack.pop()
        visit.append(v)
        if v.left:
            stack.append(v.left)
        if v.right:
            stack.append(v.right)

    print(visit, end=' ')

def postorder_rec(root):
    if not root:
        return 
    postorder_rec(root.left)
    postorder_rec(root.right)
    print(root.val, end=' ')

def postorder_iter(root):
    stack = [root]
    visited = []

    while stack:
        root = stack.pop()
        visited.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)

    while visited:
        print(visited.pop(), end=' ')

root = sample_tree()
inorder_rec(root)
#inorder_iter(root)
#postorder_rec(root)
