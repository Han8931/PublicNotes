
"""
Tree traversal:
Left tree is a starting point

in-order: left root right
pre-order: root left right
post-order: left right root
"""

import pdb

class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, ):
        self.root = None
        
    def insert(self, data):
        self.root = self._insert_data(self.root, data)

    def _insert_data(self, node, data):
        if node is None:
            node = TreeNode(data)
        else:
            if node.data<data:
                node.right = self._insert_data(node.right, data)
            else:
                node.left = self._insert_data(node.left, data)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
#        if node is None or node.data == key:
#            return node is not None

        if node is None:
            return False
        elif node.data==key:
            return True
        elif node.data<key:
            return self._search(node.right, key)
        elif node.data>key:
            return self._search(node.left, key)

    def delete(self, key):
        deleted = self._delete(self.root, key)
        return deleted

    def _delete(self, node, key):
        if node is None:
            return False

        if key==node.data:
            deleted = True
            if node.left and node.right:
                child = node.left
                while child.right:
                    child = child.right
                node = child
                del child
            elif node.left==None and node.right==None:
                del node

            elif node.left or node.right:
                if node.left:
                    node = node.left 
                else:
                    node = node.right
            return deleted

        elif key<node.data:
            return self._delete(node.left, key)
        elif key>node.data:
            return self._delete(node.right, key)

#    def pre_order(self):
#        def _pre_order(node):
#            if node is not None:
#                print(node.data)
#                _pre_order(node.left)
#                _pre_order(node.right)
#
#        _pre_order(self.root)

#    def pre_order(self):
#        traverse = []
#        def _pre_order(node):
#            if node is not None:
#                traverse.append(node.data)
#                _pre_order(node.left)
#                _pre_order(node.right)
#
#        _pre_order(self.root)
#        return traverse

    def pre_order(self):
        traverse = []
        def _pre_order(node):
            if not node:
                return 
            traverse.append(node.data)
            _pre_order(node.left)
            _pre_order(node.right)

        _pre_order(self.root)
        return traverse

bst = BinarySearchTree()
value = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
for v in value:
    bst.insert(v)

test = bst.pre_order()
print(test)

#print("Before")
#print(bst.pre_order())
#bst.delete(55)
#print("After")

#print(bst.search(5))
#print(bst.search(6))
#print(bst.search(1))

            

