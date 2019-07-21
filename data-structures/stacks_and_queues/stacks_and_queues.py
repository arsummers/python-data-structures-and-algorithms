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

        value = self._lst.head.value
        self._lst.head= self._lst.head.next
        
        
    
    
class Queue:
   
    def __init__(self):
        self.front = self.rear = None
    
    def empty_queue(self):
        return self.front == None

    def peek(self):
        return self.front and self.front.value

    def enqueue(self, value):
        mover = Node(value)

        if self.rear == None:
            # sets everything to None if everything should be == None
            self.front = self.rear = mover
            return

        self.rear.next = mover
        self.rear = mover




    def dequeue(self):
        
        if self.empty_queue():
            return
        
        mover = self.front
        self.front = mover.next

        if (self.front == None):
            self.rear == None
        return (mover.value)

       


