from bintree import sample_tree
import pdb

def longest_value_path(root):
    longest = [0]
    def recursion(node, parent=None):
        if not node:
            return 0
        left = recursion(node.left)
        right = recursion(node.right)

        if node.left and node.val==node.left.val:
            left+=1
        else:
            left = 0
        if node.right and node.val==node.right.val:
            right+=1
        else:
            right = 0

        longest[0] = max(longest[0], left+right)
        return max(left, right)


    recursion(root)

    return longest[0]

root = sample_tree()
print(longest_value_path(root))






