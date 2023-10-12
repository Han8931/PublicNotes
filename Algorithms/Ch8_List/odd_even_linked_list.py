"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
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


# def oddEven(head):
#     node = head

#     odd = odd_root = Node(None)
#     even = even_root = Node(None)
#     i = 1

#     while node:
#         temp = node.next
#         if i%2==0:
#             even.next = node
#             even = node
#             even.next = None
#         else:
#             odd.next = node
#             odd = node
#             odd.next = None
#         node = temp
#         i+=1

#     odd.next = even_root.next

#     return odd_root.next

def oddEven(head):
    odd = head
    even, even_head = head.next, head.next

    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = even_head

    return head

L1 = LinkedList()
L1.insert(1)
L1.insert(2)
L1.insert(3)
L1.insert(4)
L1.insert(5)
L1.print_ll()


node = oddEven(L1.head)

print("Two")
while node:
    print(node.val)
    node = node.next







