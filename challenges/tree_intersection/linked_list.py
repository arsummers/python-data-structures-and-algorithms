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

        basic_counter = 0
        length = 0
        current = self.head

        while current.next:
            length += 1
            current = current.next
        
        if k > length:
            return 'This value is beyond the scope of the list'
        elif length >= 1:
            k_endpoint = ((length + 1) - k)
        elif length <= 1:
            k_endpoint = (length - k)

        while basic_counter != k_endpoint:
            current = self.head
            basic_counter += 1
            current = current.next
    
        # tests for k is at the end of a list with length > 1
        if length > 1 and k < 1:
            return current.next.next.node_value

        # tests for k being the same range as the length - means that the targeted node will always be the head value
        elif k == length:
            return self.head.node_value

        # tests for basic happy case
        elif k >= 1:
            return current.next.node_value 
        
        # tests for k is list length == 1
        elif k < 1 and length <= 1:
            return self.head.node_value
        

    def merge_lists(self, ll_1):
        current_1 = self.head
        current_2 = ll_1.head


        while current_1 != None and current_2 != None:
            # saves referecnces
            current_1_next = current_1.next
            current_2_next = current_2.next

            # switches pointer
            current_2.next = current_1_next,
            current_1_next = current_2_next
            
            current_1 = current_1_next
            current_2 = current_2_next

        ll_1.head = current_1
        return ll_1.head.node_value




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

