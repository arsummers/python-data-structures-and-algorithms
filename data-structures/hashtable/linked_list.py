class LinkedList:

    def __init__(self, head=None):
        self.head = None


    def insert(self, value):
        self.head = Node(value, self.head)

    def traverse(self):
        temp = self.head
        while(temp):
            temp = temp.next

    def append_val(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        end_point = self.head
        while (end_point.next):
            end_point = end_point.next
        end_point.next = new_node

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

