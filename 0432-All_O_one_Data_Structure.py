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
        # key: doubly-linkedlist with increasing value (key counts)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = collections.defaultdict(Node) # key to node
        
    def _insert_before(self, next, key):
        if next.count - 1 != next.prev.count: # node with target count doesn't exist, need to create a new node
            node = Node(next.count - 1)
            node.next, node.prev = next, next.prev
            node.prev.next = node.next.prev = node
        else: # node with target count exists, reuse existing node
            node = next.prev
        node.keys.add(key)
        return node
    
    def _insert_after(self, prev, key):
        if prev.count + 1 != prev.next.count: # node with target count doesn't exist, need to create a new node
            node = Node(prev.count + 1)
            node.prev, node.next = prev, prev.next
            node.prev.next = node.next.prev = node
        else: # node with target count exists, reuse existing node
            node = prev.next
        node.keys.add(key)
        return node  
        
    def _remove_node(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        del node          
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with count 1. Or increments an existing key count by 1.
        """
        if key not in self.key_to_node:
            self.key_to_node[key] = self._insert_after(self.head, key)
        else:
            node = self.key_to_node[key]
            self.key_to_node[key] = self._insert_after(node, key)
            node.keys.remove(key)
            if not node.keys:
                self._remove_node(node)
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's count is 1, remove it from the data structure.
        """
        node = self.key_to_node[key]
        node.keys.remove(key)
        del self.key_to_node[key]
        if node.count > 1:
            self.key_to_node[key] = self._insert_before(node, key)
        if not node.keys:
            self._remove_node(node)


    def getMinKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.head.next.keys:
            num = self.head.next.keys.pop() # get random from set
            self.head.next.keys.add(num)
            return num
        return ""
        

    def getMaxKey(self) -> str:
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