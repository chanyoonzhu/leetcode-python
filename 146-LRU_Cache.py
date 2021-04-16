"""
- hashmap + doubly-linkedlist: official solution
- get: O(1), put: O(1)
- instinct: O(1) get can be achieved through hashmap; O(1) move elements can be achieved through linkedlist and hashmap
- caveat: use dummy node for linkedlist avoids checking edge cases
"""
class LinkedNode:
    
    # doubly-linkedList
    def __init__(self, key=-1, val=-1): 
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        pointer = self.head.next
        node = self.dic[key]
        self.remove(node)
        self.insertAtTail(node)
        return node.val      

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.dic:
            self.dic[key] = LinkedNode(key, value)
            if self.size == self.capacity:
                del self.dic[self.head.next.key]
                self.remove(self.head.next)
            else:
                self.size += 1
        else:
            self.dic[key].val = value
            self.remove(self.dic[key])
        self.insertAtTail(self.dic[key])   
    
    def insertAtTail(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
"""
- hashmap + doubly-linkedlist: my solution
- get: O(1), put: O(1)
- instinct: O(1) get can be achieved through hashmap; O(1) move elements can be achieved through linkedlist and hashmap
- caveat: use dummy node for linkedlist avoids checking edge cases
"""
class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0)  # dummy head, all keys are positive so using 0 is safe
        self.tail = Node(0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.dict:
            val, node = self.dict[key]
            self.move_to_head(node)
            return val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key][0] = value
            self.move_to_head(self.dict[key][1])
        else:
            node = Node(key)
            self.dict[key] = [value, node]
            self.make_head(node)  
        if len(self.dict) > self.capacity:
            self.remove_from_tail()
    
    def make_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def move_to_head(self, node):
        if node.prev != self.head:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.make_head(node)
    
    def remove_from_tail(self): # can be optimized to remove any node, which move_to_head can call.
        node = self.tail.prev
        del self.dict[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value) 
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lru = LRUCache(1)
lru.put(2,1)
lru.get(2)
lru.put(3,2)
print(lru.get(2))
lru.get(3)
# print(lru.queue)


