class Node:
    def __init__(self, data, next=None):
        self.data = data
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
                print(curr.data)
                curr = curr.next
        else:
            print("Empty list.")

    def delete(self, data):

if __name__=="__main__":
    linked_list = LinkedList() # Create an empty list

    for i in range(3):
        linked_list.insert(i)

    linked_list.print_ll()

#    LL.insert(1) # First node is head
#    LL.insert(2) # Insert node2
#    LL.insert(3)
#    LL.insert(4)
#    LL.print_ll()

