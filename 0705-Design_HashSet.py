"""
- modulo and separate chaining (with linkedlist)
- O(n/k): n-number of all possible values, k-number of buckets, O(k+m): m - number of unique values
"""
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class Bucket:
    
    def __init__(self):
        self.head = Node(-1)
        
    def insert(self, value):
        if not self.exists(value): # easy to miss: no duplicate
            newNode = Node(value, self.head.next)
            self.head.next = newNode
    
    def delete(self, value):
        if self.exists(value):
            prev, curr = self.head, self.head.next
            while curr.value != value:
                prev, curr = prev.next, curr.next
            prev.next = curr.next
        
    def exists(self, value):
        node = self.head.next
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1999 # prime number
        self.buckets = [Bucket() for _ in range(self.capacity)] # separate chaining
        
    def _hash(self, key):
        return key % self.capacity
        

    def add(self, key: int) -> None:
        self.buckets[self._hash(key)].insert(key)
        
    def remove(self, key: int) -> None:
        self.buckets[self._hash(key)].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.buckets[self._hash(key)].exists(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

"""
- todo:
- modulo and separate chaining (with bst)
- O(n/k): n-number of all possible values, k-number of buckets, O(k+m): m - number of unique values
"""