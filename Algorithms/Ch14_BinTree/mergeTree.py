from bintree import sample_tree
import pdb

def mergeTrees(t1, t2):
    if not t1 and not t2:
        return None

    v1 = t1.val if t1 else 0
    v2 = t2.val if t2 else 0
    root = Node(v1+v2)

    root.left = mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
    root.right = mergeTrees(t1.right if t2 else None, t2.right if t2 else None)

    return root

def mergeTrees2(t1, t2):
    if t1 and t2:
        root = Node(v1+v2)
        root.left = mergeTrees2(t1.left, t2.left)
        root.right = mergeTrees2(t1.right, t2.right)
        return root
    else:
        # return one of node which is not none.
        return t1 or t2 

root = sample_tree()
#root = mergeTrees2(root)
print(root)
