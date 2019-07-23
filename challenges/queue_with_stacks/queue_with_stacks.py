class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.front = None

    def peek(self):
        if self.front is None:
            return 'Empty queue'

        return self.front.value

    def push(self, value):
  
        self.front = Node(value, self.front)
    
    def pop(self):
       
        if self.front is None:
            return 'Empty queue'
        value = self.front.value

        return value
        
        

class PseudoQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
   
    def enqueue(self, value):
 
        self.s1.push(value)

        if self.s1.front.next == None:
            # same end-goal as pushing a new value into stack 1, but gives the test a front attribute to hang onto so it doesn't error out, like self.s1.push(value) gave me when I tried it down here

            self.front = self.s1.front
           

    def dequeue(self):


        def dequeue_helper(value):
            self.s1.push(value)

            if self.s1.front.next == None:
                return 'empty queue'

            self.s2.push(self.s1.pop())
            return dequeue_helper(value)
        
        return self.s2.pop()


