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
L1.insert(4)
print("Original List")
L1.print_ll()

L2 = LinkedList()
L2.insert(1)
L2.insert(3)
L2.insert(4)
print("Original List")
L2.print_ll()

def mergeTwoSortedList(l1, l2):

    # Assign an address
    head = Node(None) # tail
    curr = head

    left = l1
    right = l2

    while left and right:
        if left.val<right.val:
            curr.next = left
            left, curr  = left.next, left
        else:
            curr.next = right
            right, curr  = right.next, right
    
    while right:
        curr.next = right
        right, curr = right.next, right
    while left:
        curr.next = left
        left, curr = left.next, left

    return head.next

print("Merge")
llist = mergeTwoSortedList(L1.head, L2.head)

while llist:
    print(llist.val)
    llist = llist.next

#def mergeTwoList_Rec(l1, l2):
#    if (not l1)  or (l2 and l1.val>l2.val):
#        l1, l2 = l2, l1
#    if l1:
#        l1.next = mergeTwoList_Rec(l1.next, l2)
#    return l1
#
#llist = mergeTwoList_Rec(L1.head, L2.head)
#
#while llist:
#    print(llist.val)
#    llist = llist.next










    
