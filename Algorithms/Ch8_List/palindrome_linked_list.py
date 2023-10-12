
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
LL.insert(2)
LL.insert(1)
print("Original List")
LL.print_ll()


def isPalindromeLL(head):
    if not head:
        return head

    list_val = []

    list_val.append(head.val)
    while head.next:
        head = head.next
        list_val.append(head.val)

    if list_val==list_val[::-1]:
        return True
    else:
        return False

def isPalindromeLL2(head):
    if not head:
        return head

    list_val = []

    node = head
    while node is not None:
        list_val.append(node.val)
        node = node.next

    while len(list_val)>1:
        if list_val.pop(0)!=list_val.pop():
            return False

    return True

print(isPalindromeLL2(LL.head))

def isPalindromeLL3(head):
    if not head:
        return head

    q = collections.deque()

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q)>1:
        if q.popleft()!=q.pop():
            return False

    return True

print(isPalindromeLL3(LL.head))




