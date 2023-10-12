import sys

def validate_btree(root):

    def validate(node, left, right):
        """
        left, right are boundaries
        """
        if not node:
            return True
        # Compare the parent node with left and right boundaries
        if not (node.val < right and node.val > left):
            return False

        return validate(node.left, left, node.val) and \
                validate(node.right, node.val, right)

    return validate(root, -sys.maxsize, sys.maxsize)


