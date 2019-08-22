from linked_list import LinkedList, Node

class HashTable:
    def __init__(self):
        self.buckets = [LinkedList() for i in range(1024)]

    def hash(self, key):
        ascii_sum_for_key = sum([ord(char) for char in key])

        prime_num = 599

        hashing_index = (ascii_sum_for_key * prime_num) % len(self.buckets)

        return hashing_index


    def add(self, key, value):
        index = self.hash(key)

        bucket = self.buckets[index]
        
        bucket.insert({'key':key, 'value':value})
        
        
    def get(self, key):
      
        index = self.hash(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current:
            key_val_pair = current.value
            if key_val_pair['key'] == key:
                return key_val_pair['value']
            current = current.next
            
        else:
            raise(ValueError)

    def contains(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        current = bucket.head
        
        while current:
            key_val_pair = current.value
            if key_val_pair['key'] == key:
                return True
            current = current.next 
            
            


        