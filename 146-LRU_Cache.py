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
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.key_to_node = defaultdict(Node)
        self.dll = DoublyLinkedList()
        

    def get(self, key: int) -> int:
        # get the value
        if key not in self.key_to_node:
            return -1
        val = self.key_to_node[key].val
        # move to front
        self.dll.remove(self.key_to_node[key])
        self.dll.add_to_front(self.key_to_node[key])
        return val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node: # create
            if self.size == self.capacity: # needs remove
                removed_key = self.dll.remove(self.dll.tail.prev)
                del self.key_to_node[removed_key]
            else:
                self.size += 1 # just add
            self.key_to_node[key] = Node(key, value)
            self.dll.add_to_front(self.key_to_node[key])
        else: # update
            # update value
            self.key_to_node[key].val = value
            # move to front
            self.dll.remove(self.key_to_node[key])
            self.dll.add_to_front(self.key_to_node[key])
  
class Node:
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
        
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        node.prev = node.next = None
        return node.key
        
    def add_to_front(self, node):
        next = self.head.next
        node.prev, node.next = self.head, next
        self.head.next = next.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

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


