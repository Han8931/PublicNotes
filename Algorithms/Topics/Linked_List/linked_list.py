import pdb

class LinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, target):
        node = self.__head
        while node and node.data!=target:
            node = node.next
        return node is not None

    def insertNode(self, data):
        node = __ListNode(data)
        node.next = head
        head = node

    def traversal(self):
        node = self.__head 
        while node:
            print(node.data)
            node = node.next

    def removeNode(self, target):
        prev = None
        node = self.__head
        while node and node.data!=target:
            prev = node
            node = node.next

        assert node is not None, "The item must be in the list"

        self.__size -=1

        if node==self.__head:
            self.__head = node.next
        else:
            prev.next = node.next

        return node.data

    def __iter__(self):
        return __Iterator(self.__head)

class __ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class __Iterator:
    def __init__(self, listHead):
        self.__curNode = listHead

    def __iter__(self):
        return self

    def next(self):
        if self._curNode == is None:
            raise StopIteration
        else:
            item = self._curNode.data
            self._curNode = self._curNode.next
            return item




