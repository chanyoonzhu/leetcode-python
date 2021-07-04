"""
- modulo and separate chaining (with linkedlist)
- O(n/k): n-number of all possible values, k-number of buckets, O(k+m): m - number of unique values
- similar problem: 705-Design HashSet
"""
class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next
    
    def add(self, key, val):
        prev = self
        while prev.next:
            cur = prev.next
            if cur and cur.key == key:
                cur.val = val
                return
            prev = cur
        prev.next = Node(key, val)
        
    def delete(self, key):
        prev = self
        while prev.next:
            cur = prev.next
            if cur and cur.key == key:
                prev.next = cur.next
                return
            prev = cur
    
    def find(self, key):
        prev = self
        while prev.next:
            cur = prev.next
            if cur and cur.key == key:
                return cur.val
            prev = cur
        return -1

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 1999
        self.buckets = [Node(-1, -1) for _ in range(self.base)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.base
        self.buckets[index].add(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.base
        return self.buckets[index].find(key)
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.base
        self.buckets[index].delete(key)