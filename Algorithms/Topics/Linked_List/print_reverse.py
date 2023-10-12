def printReverse(head):
    node = head
    if node is not None:
        printReverse(node.next)
        print(node.data)

