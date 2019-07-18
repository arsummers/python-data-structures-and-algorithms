class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

class Stack:
    def __init__(self):
        self._lst = LinkedList()

    def peek(self):
        return self._lst.head and self._lst.head.value
    
    def push(self, value):
        self._lst.insert(value)
    
    def pop(self, value):
        pass
        # things
    
    
class Queue:
    def __init__(self):
        self._lst = LinkedList()

    def peek(self):
        return self._lst.head and self._lst.head.value

    def enqueue(self, value):
        self._lst.insert(value)

    def dequeue(self, value):
        pass