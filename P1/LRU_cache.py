class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def prepend(self,key,value):
        new_node = Node(key,value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node
        return new_node
    
    def delete_tail(self):
        assert self.head != None
        
        deleted_tail = self.tail
        if self.head == self.tail:
            deleted_tail = self.tail
            self.head = None
            self.tail = None
        else:
            self.tail.pre.next = None
            self.tail = self.tail.pre
        return deleted_tail
    
    def move_node_to_head(self,node):
        assert (self.head != None),"Cache cannot be empty."
        #node is head
        if self.head == node:
            return
        
        #node is tail
        elif self.tail == node:
            
            previous_node = node.pre
            previous_node.next = None           
            self.tail = previous_node
            
            self._adjust_head(node)
            
        #node is in the middle
        else:
            previous_node = node.pre
            next_node = node.next
            previous_node.next = next_node
            next_node.pre = previous_node
            
            self._adjust_head(node)
            
    def _adjust_head(self,node):
        node.next = self.head
        self.head.pre = node
        node.pre = None
        self.head = node
        
        
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = dict() #key to linkedlist node
        self.list = LinkedList()
        self.capacity = capacity
        self.size = 0
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            node = self.cache[key]
            self.list.move_node_to_head(node)
            return node.value            
        return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.get(key) == -1:   #if key is not present
            new_node = self.list.prepend(key,value)
            self.cache[key] = new_node  #link to the hashtable
            self.size += 1
        
        if self.size > self.capacity:
            deleted_tail = self.list.delete_tail()
            del self.cache[deleted_tail.key]
            self.size -= 1


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry