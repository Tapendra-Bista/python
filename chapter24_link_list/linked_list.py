'''A linked list is a collection of nodes, each made up of a reference and a value. Nodes are strung together into a
sequence using their references. Linked lists can be used to implement more complex data structures like lists,
stacks, queues, and associative arrays.'''

# Single linked list example
#This example implements a linked list with many of the same methods as that of the built-in list object.

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, val):
        self.data = val

    def setNext(self, val):
        self.next = val

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(new_node)

    def insert(self, position, item):
        if position == 0:
            self.add(item)
            return
        new_node = Node(item)
        current = self.head
        prev = None
        pos = 0
        while current is not None and pos < position:
            prev = current
            current = current.getNext()
            pos += 1
        prev.setNext(new_node)
        new_node.setNext(current)

    def printList(self):
        current = self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

ll = LinkedList()
ll.add('l')
ll.add('H')
ll.insert(1, 'e')
ll.append('l')
ll.append('o')
ll.printList()

