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


