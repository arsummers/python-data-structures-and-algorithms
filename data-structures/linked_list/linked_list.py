class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, animal_value):
        self.head = Node(animal_value, self.head)

    # def append_val(self, animal_value):
    #     # self.head.next = Node(animal_value, self.head.next)
    #     current = self.head
    #     if current != None:
    #         current = current.next
    #     current = Node(animal_value, current.next)

    
    # def insert_before(self, exist_val, animal_value):
    #     current = self.head


        # current = self.head
        # while current.animal_value != exist_val:
        #     current = current.next
        # exist_val.next = Node(animal_value, self.head.next)
    
    def insert_after(self, targeted_node, animal_value):
 
        new_node = Node(animal_value, targeted_node)
        # try:
        new_node.next = targeted_node.next
        # except:
        #         breakpoint()
        targeted_node.next = new_node


    def includes_val(self, search_value):

        current = self.head
        while current != None:
            if current.animal_value == search_value:
                return True
            
            current = current.next

        return False
   
    def __str__(self):
        animal_str = ''
        current = self.head

        while current != None:

            animal_str += str(current.animal_value)
            current = current.next
            
        return animal_str

class Node:
    def __init__(self, animal_value, next=None):
        self.animal_value = animal_value
        self.next = next

try:
    LinkedList()

except ValueError:
    print('There has been an error with the value')

