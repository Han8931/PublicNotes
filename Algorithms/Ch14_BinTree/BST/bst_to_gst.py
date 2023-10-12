
class Solution():
    val = 0

    def bstToGst(self, root):
        if root:
            self.bstToGst(root.right)
            self.val+=root.val
            self.root=self.val
            self.bstToGst(root.left)

        return root

