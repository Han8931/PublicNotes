import pdb

import collections

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
print("Original List")
#LL.print_ll()

def reverseLL(head):
    node = head
    prev = None

    while node:
        temp = node.next # At the end, node.next==None, 
        node.next = prev
        prev = node
        node = temp # node will point None
    return prev

def reverseLL2(head):
    node = head
    prev = None

    while node:
        temp, node.next = node.next, prev
        prev, node = node, temp
    return prev

def revLLRec(head:Node)->Node:
    if not head or not head.next:
        return head

    temp = head.next
    head.next = revLLRec(temp.next)
    temp.next = head
    return temp

head = reverseLL(LL.head)
while head:
    print(head.val)
    head = head.next




