class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.front = None

    def peek(self):
        if self.front is None:
            return 'Empty stack'

        return self.front.value

    def push(self, value):
  
        self.front = Node(value, self.front)
    
    def pop(self):
       
        if self.front is None:
            return 'Empty stack'
        value = self.front.value

        return value
        
        

class PseudoQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
        

    # # def peek(self):
    # #     return self.s1
    # def peek(self):
    #     return self._lst.head and self._lst.head.value

    def enqueue(self, value):
 
        if self.s1.peek() == None:
            self.s2.push(value)
            return

        self.s2.push(self.s1.pop())
        return self.enqueue(value)


    def dequeue(self):
        def dequeue_helper():
            if self.s2.peek() == None:
                return 'empty queue'
            self.s1.push(self.s2.pop())
            return dequeue_helper()

        dequeue_helper()
        
        return self.s1.pop()


