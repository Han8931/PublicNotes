import pdb

class ListNode:
    def __init__(data):
        self.data = data
        self.next = None

node = ListNode(2)
node = ListNode(52)
node = ListNode(18)
node = ListNode(36)
node = ListNode(13)

def traversal(head):
    node = head
    while node:
        print(node.data)
        node = node.next

def insertNode(head, item):
    node = ListNode(item)
    node.next = head
    head = node

def unorderedSearch(head, target):
    node = head
    while node and node.data!=target:
        node = node.next
    return node is not None

def removeNode(head, target):
    node = head
    prev = None
    while node and node.data!=target:
        prev = node
        node = node.next

    if node is not None:
        if node==head:
            head = node.next
        else:
            prev.next = node.next




