import pdb

class Node:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        else:
            self.head = node

    def print_ll(self,):
        if self.head:
            curr = self.head
            while curr:
                print(curr.val)
                curr = curr.next
        else:
            print("Empty list.")


LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.insert(6)
print("Original List")

def reverseLL(head, m, n):
    #assert m<n "m has to be smaller than n"

    if not head:
        return 

    root = start = Node(None)
    root.next = head

    for _ in range(m-1):
        start = start.next

    end = start.next

    for _ in range(n-m):
        temp, end.next, start.next = start.next, end.next.next, end.next
        start.next.next = temp

    return root.next

node = reverseLL(LL.head, 2, 5)
print(node.val)
print(node.next.val)
print(node.next.next.val)
print(node.next.next.next.val)
print(node.next.next.next.next.val)
print(node.next.next.next.next.next.val)



