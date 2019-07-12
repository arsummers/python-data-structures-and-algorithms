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
            
            current = next

        return False

    
    def __str__(self):
        'this is a string'
        # current = self.head

        # while current != None:
        #     current = next
        #     return f'{self.head.animal_value} {self.head.next.animal_value}'
 
        # __str__(self.head.value)
    


    # method called __str__
        # returns a string representing all the values of the list


class Node:
    def __init__(self, animal_value, next):
        self.animal_value = animal_value
        self.next = next
