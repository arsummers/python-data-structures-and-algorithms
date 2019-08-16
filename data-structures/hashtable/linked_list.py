class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, node_value):
        self.head = Node(node_value, self.head)

class Node:
    def __init__(self, node_value, next=None):
        self.node_value = node_value
        self.next = next

