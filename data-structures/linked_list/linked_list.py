class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, animal_value):
        self.head = Node(animal_value, self.head)

    def append_val(self, animal_value):
        new_node = Node(animal_value)

        if self.head is None:
            self.head = new_node
            return
        
        end_point = self.head
        while (end_point.next):
            end_point = end_point.next
        end_point.next = new_node

    
    def insert_before(self, targeted_value, animal_value):
        new_node = Node(animal_value)
        
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        if current.next.animal_value == targeted_value:
            current = Node(animal_value, current.next)
           
    
    def insert_after(self, targeted_value, animal_value):
        new_node = Node(animal_value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        if current.animal_value == targeted_value:
            current = new_node
            current.next = Node(animal_value, current.next)



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

