from linked_list import LinkedList, Node

class HashTable:
    def __init__(self):
        self.buckets = [LinkedList()] * 1024

    def hash(self, key):
        ascii_sum_for_key = sum([ord(char) for char in key])

        prime_num = 599

        hashing_index = (ascii_sum_for_key * prime_num) % len(self.buckets)

        return hashing_index


    def add(self, key, value):
        index = self.hash(key)

        bucket = self.buckets[index]
        
        # if there's no value in head bucket, insert the kvp
        # currently breaking because bucket doesn't have a head node
        # insert sets a head, but I need a way to hit an insert without it overwriting each time I call add(), What conditional would be best here?
        
        # breakpoint() 
        
        # if bucket.head:
        # bucket.append_val({'key':key, 'value':value})
        if bucket.head == None:
            # breakpoint() 
            bucket.append({'key':key, 'value':value})
        # elif bucket.head != None:
        #     bucket.append_val({'key':key, 'value':value})

      
            # bucket.insert({'key':None, 'value':None})
            # bucket.append_val({'key':key, 'value':value})


        # else traverse and insert
        # elif bucket.head.value:
        #     bucket.traverse()
        #     bucket.append_val({'key':key, 'value':value})



    def get(self, key):
      
        index = self.hash(key)
        bucket = self.buckets[index]

        for item in self.buckets:

            bucket.traverse()

            key_val_pair = bucket.head.value

            if key_val_pair['key'] == key:
                return key_val_pair['value']
            else:
                return None
                

    def contains(self, key):
        pass