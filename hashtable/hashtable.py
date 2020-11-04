class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = MIN_CAPACITY
        # check and store
        self.storage = [None for i in range(self.capacity)]
        self.load = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.load / self.capacity

        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # hash_index = self.djb2(key) % self.capacity
        # self.storage[hash_index] = value
        idx = self.hash_index(key)
        
        node = self.storage[idx]
        
        new_node = HashTableEntry(key, value)
        
        if self.storage[idx] != None:
            if node.key == key:
                node.value = value
            else: 
                while node.next is not None:
                    if node.next.key == key:
                        node.next.value = value
                        break
                    else: 
                        node = node.next
                node.next = new_node
        else: 
            self.storage[idx] = new_node
            
        self.load += 1
        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # hash_index = self.djb2(key) % self.capacity
        # self.storage[hash_index] = None
        idx = self.hash_index(key)
        node = self.storage[idx]
        
        if node is None:
            print(f" The key '{key}' does not exist. ")
        elif node.key == key:
            node.key = None
            self.load -= 1
        else:
            prev_node = node
            curr_node = prev_node.next
            
            while curr_node is not None:
                if curr_node.key == key:
                    curr_node.key = None
                    break
                else: 
                    prev_node = curr_node
                    curr_node = curr_node.next
            self.load -= 1
            
        
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # hash_index = self.djb2(key) % self.capacity
        # return self.storage[hash_index]
        idx = self.hash_index(key)
        node = self.storage[idx]
        
        if node is None:
            print(f" The key '{key}' does not exist. ")
        else: 
            while node is not None:
                #check for target value
                if node.key == key:
                    # print(f" | {node.key}, {node.value}")
                    
                    return node.value
                #move to next node
                else:
                    node = node.next


    def resize(self, new_capacity=None):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        if self.get_load_factor() > 0.7:
            if new_capacity is None:
                new_capacity = self.capacity * 2
                
            old_storage = self.storage
            self.storage = [None] * new_capacity
            
            for node in old_storage:
                if node is not None:
                    self.put(node.key, node.value)
                    
                    curr_node = node
                    while curr_node.next is not None:
                        self.put(curr_node.next.key, curr_node.next.value)
                        
                        curr_node = curr_node.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
    
    htbl = HashTable(8)
    htbl.put('Lexy', 'Anderson')
    # print(htbl.storage)
    # print(htbl.get('Lexy'))
    # htbl.delete('Lexy')
    # print(htbl.storage)