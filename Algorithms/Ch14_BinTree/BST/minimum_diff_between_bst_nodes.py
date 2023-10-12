"""
The description of this problem is confusing
We have to compute the minimum difference!
"""
import pdb
import sys

class Solution:
    result = sys.maxsize
    prev = -sys.maxsize

    def minDiff(self, root):
        if root.left:
            minDiff(root.left)

        self.result = min(self.result, root.val-self.prev)
        self.prev = root.val

        if root.right:
            minDiff(root.right)

    return self.result

class Solution:
    prev, res = None, float("inf")
    def minDiffBST(root):
        """
        In-order traversal
        """

        def dfs(node):
            if not node:
                return 

            dfs(node.left)
            if self.prev:
                self.res = min(self.res, node.val-self.prev.val)
            self.prev = node
            dfs(node.right)

        dfs(root)
        return res


def minDiffBST(root):
    """
    In-order traversal
    """
    # Considered to be global variables
    prev, res = None, float("inf")

    def dfs(node):
        if not node:
            return 

        dfs(node.left)
        nonlocal prev, res
        if prev:
            res = min(res, node.val-prev)
        prev = node
        dfs(node.right)

    dfs(root)
    return res



#class Solution_Iter:
#
#    return self.result
    
