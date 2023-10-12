from tree_sample import *
import pdb

queue = []

class TreeCodec():
    def serialization(self, root):
        queue = []
        if not root:
            return 

        def dfs(node):
            if not node:
                queue.append('#')
                return 
            queue.append(node.data)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return queue

    def deserialization(self, arr):
        self.i = 0

        def dfs():
            if arr[self.i]=='#':
                self.i+=1
                return None
            node = TreeNode(arr[self.i])
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
            


root = TreeNode(1)
nl_1 = TreeNode(2)
nr_1 = TreeNode(3)
root.left = nl_1
root.right = nr_1
nl_1.left = TreeNode(4)
nl_1.right = TreeNode(5)

print(serialization(root))
