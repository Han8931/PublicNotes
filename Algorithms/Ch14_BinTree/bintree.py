class Node: 
  def __init__(self , val): 
      self.val = val  
      self.left = None
      self.right = None


def sample_tree():
    """
       1
     2---3
    4  5---6
        7 8
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.right.left = Node(8)
    root.right.left.right = Node(7)
    return root
