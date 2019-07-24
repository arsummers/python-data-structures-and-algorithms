# Node and Queue are taken directly from my Stacks and Queues file in data-structures

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

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

class FifoAnimalShelter:
    dogs = ['pug', 'lab', 'beagle']
    cats = ['tabby', 'calico', 'bengal']

    dog_queue = Queue()
    cat_queue = Queue()

    for dog in dogs:
        dog_queue.enqueue(dog)
    
    for cat in cats:
        cat_queue.enqueue(cat)