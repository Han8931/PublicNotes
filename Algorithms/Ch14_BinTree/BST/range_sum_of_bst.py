import pdb

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val>high:
            return self.rangeSumBST(root.left, low, high)
        if root.val<low:
            return self.rangeSumBST(root.right, low, high)
        return root.val+self.rangeSumBST(root.left, low, high)+self.rangeSumBST(root.right, low, high)

class Solution1:
    s = 0
    def rangeSumBST(root, L, R):
        if not root:
            return 

        def dfs(root):
            if not root:
                return 
            if root.val>L:
                dfs(root.left)
            if root.val<R:
                dfs(root.right)

            if root.val>=L and root.val<=R:
                self.s+=root.val 
    dfs(root)
    return self.s

class Solution2:
    def rangeSumBST(root, L, R):
        if not root:
            return 

        def dfs(node):
            if not node:
                return 0
            if node.val>L:
                return dfs(node.left)
            if root.val<R:
                return dfs(node.right)

            return node.val+dfs(node.left)+dfs(node.right)

    return dfs(root)
