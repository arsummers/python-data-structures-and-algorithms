class LinkedList:

    def __init__(self, head=None):
        self.head = None


    def insert(self, value):
        self.head = Node(value, self.head)

    def traverse(self):
        temp = self.head
        while(temp):
            temp = temp.next

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

