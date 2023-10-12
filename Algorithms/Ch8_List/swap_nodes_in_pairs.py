"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
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


L1 = LinkedList()
L1.insert(1)
L1.insert(2)
L1.insert(3)
L1.insert(4)
print("Original List")
node = L1.head
while node:
    print(node.val)
    node = node.next

def swapPairs(head):
    dummy = Node(None)
    prev, curr = dummy, head

    while curr and curr.next:
        nxtPair = curr.next.next
        second = curr.next

        # Reverse this pair
        second.next = curr
        curr.next = nxtPair
        prev.next = second

        # update ptrs
        prev = curr
        curr = nxtPair

    return dummy.next

swap_node = swapPairs(L1.head)
node = swap_node

print("Swapped")
while node:
    print(node.val)
    node = node.next
print("-======:")

def swapNodePair_Rec(head):
    if head and head.next:
        p = head.next
        head.next = swapNodePair_Rec(p.next)
        p.next = head
        return p
    return head

L1 = LinkedList()
L1.insert(1)
L1.insert(2)
L1.insert(3)
L1.insert(4)

node = swapNodePair_Rec(L1.head)
print("Swapped")
while node:
    print(node.val)
    node = node.next
print("-======:")
