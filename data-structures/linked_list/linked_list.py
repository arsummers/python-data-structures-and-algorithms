class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, animal_value):
        self.head = Node(animal_value, self.head)

    

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
    def __init__(self, animal_value, next):
        self.animal_value = animal_value
        self.next = next

try:
    LinkedList()

except ValueError:
    print('There has been an error with the value')

