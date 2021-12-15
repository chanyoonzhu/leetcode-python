"""
- data structure problem: hashmap + hashset + doubly linked list
- all O(1)
"""
class Node:
    
    def __init__(self, count=0):
        
        self.count = count
        self.keys = set() # key: all the keys that has count = self.count
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key: doubly-linkedlist with decreasing value (key counts)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = collections.defaultdict(Node) # key to node
        
    def _insert_before(self, next, key):
        if next.count + 1 != next.prev.count: # node with target count doesn't exist, need to create a new node
            node = Node(next.count + 1)
            node.next, node.prev = next, next.prev
            node.prev.next = node.next.prev = node
        else: # node with target count exists, reuse existing node
            node = next.prev
        node.keys.add(key)
        return node
    
    
    def _insert_after(self, prev, key):
        if prev.count - 1 != prev.next.count: # node with target count doesn't exist, need to create a new node
            node = Node(prev.count - 1)
            node.prev, node.next = prev, prev.next
            node.prev.next = node.next.prev = node
        else: # node with target count exists, reuse existing node
            node = prev.next
        node.keys.add(key)
        return node
            
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.cache:
            self.cache[key] = self._insert_before(self.tail, key)
        else:
            node = self.cache[key]
            self.cache[key] = self._insert_before(node, key)
            node.keys.remove(key)
            if not node.keys:
                node.prev.next, node.next.prev = node.next, node.prev
                node.next = node.prev = None # del node
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        node = self.cache[key]
        node.keys.remove(key)
        del self.cache[key]
        if node.count > 1:
            self.cache[key] = self._insert_after(node, key)
        if not node.keys:
            node.prev.next, node.next.prev = node.next, node.prev
            node.next = node.prev = None


    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.head.next.keys:
            num = self.head.next.keys.pop() # get random from set
            self.head.next.keys.add(num)
            return num
        return ""
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.tail.prev.keys:
            num = self.tail.prev.keys.pop()
            self.tail.prev.keys.add(num)
            return num
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()