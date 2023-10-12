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
L1.insert(2)
L1.insert(4)
L1.insert(3)

L2 = LinkedList()
L2.insert(5)
L2.insert(6)
L2.insert(4)

def addTwoNumbers(L1, L2):

    def reverseLL(head):
        node = head
        prev = None

        while node:
            temp, node.next = node.next, prev
            prev, node = node, temp

        return prev

    def traverse(head):
        temp = []
        node = head
        while node:
            temp.append(str(node.val))
            #temp.append(node.val)
            node = node.next
        return temp

    def addTwoList(l1, l2):

        return str(int("".join(l1))+int("".join(l2)))

    l1 = reverseLL(L1)
    l2 = reverseLL(L2)

    l1_val = traverse(l1)
    l2_val = traverse(l2)

    sums = addTwoList(l1_val, l2_val)

    head = Node(int(sums[0]))
    for i in sums[1:]:
        curr = Node(int(i))
        curr.next = head
        head = curr

    return curr

def add_two_numbers(h1, h2):
    node = Node(data=None)
    carry = 0

    while h1 and h2:
        if carry!=0:
            h1.val+=1
            carry=0

        if h1.val+h2.val>=10:
            carry = 1
            node.val = 0
        else:
            node.val = h1.val+h2.val

        next_node = Node(data=None)
        next_node.next = node
        node = next_node
        h1, h2 = h1.next, h2.next

    return node.next

node = addTwoNumbers(L1.head, L2.head)

print(node.val)
print(node.next.val)
print(node.next.next.val)
#print(node.next.next.next.val)





