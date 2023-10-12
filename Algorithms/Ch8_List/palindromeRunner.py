
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
LL.insert(2)
LL.insert(1)

print("Original List")
LL.print_ll()


def isPalindromeLLRunner(head):
    """
    The Runner solution requies an understaning about multiple assignment.
    It might be temping to assign variables as follows:
        fast = fast.next.next
        rev, rev.next = slow, rev
        slow = slow.next
    However, if you assign like this, then the variable 'rev' and 'slow' become the same reference.
    it means rev and slow are pointing the same memory.

    Thus, we have to use a technique called 'multiple assigment' to assign variables at the same time
    """
    rev = None
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next

        # Multiple Assignment
        rev, rev.next, slow = slow, rev, slow.next

    # if the length of a list is odd then 
    # we need to exclude the mid value from checking below
    if fast:
        slow = slow.next

    while rev and rev.val==slow.val:
        slow, rev = slow.next, rev.next

    return not rev

print(isPalindromeLLRunner(LL.head))




