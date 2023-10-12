import pdb
import collections

def maxDepthBinTree(root):
    if not root:
        return 0
    else:
        left_h = maxDepthBinTree(root.left)
        right_h = maxDepthBinTree(root.right)

    return max(left_h, right_h)+1

def maxDepthBinTree2(root):
    if not root:
        return 0

    queue = [root]
    depth = 0

    while queue:
        depth+=1

        for _ in range(len(queue)):
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth
