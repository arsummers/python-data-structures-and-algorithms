class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, node_value):
        self.head = Node(node_value, self.head)

    def append_val(self, node_value):
        new_node = Node(node_value)

        if self.head is None:
            self.head = new_node
            return
        
        end_point = self.head
        while (end_point.next):
            end_point = end_point.next
        end_point.next = new_node

    
    def insert_before(self, targeted_value, node_value):
        new_node = Node(node_value)
        
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        if current.next.node_value == targeted_value:
            current = Node(node_value, current.next)
           
    
    def insert_after(self, targeted_value, node_value):
        new_node = Node(node_value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        if current.node_value == targeted_value:
            current = new_node
            current.next = Node(node_value, current.next)

    def kth_from_end(self, k):
        # basic_counter = 0


    def includes_val(self, search_value):
        current = self.head
        while current != None:
            if current.node_value == search_value:
                return True
            
            current = current.next

        return False
   
    def __str__(self):
        node_str = ''
        current = self.head

        while current != None:

            node_str += str(current.node_value)
            current = current.next
            
        return node_str

class Node:
    def __init__(self, node_value, next=None):
        self.node_value = node_value
        self.next = next

try:
    LinkedList()

except ValueError:
    print('There has been an error with the value')

