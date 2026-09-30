"""
- modulo and separate chaining (with linkedlist)
- O(n/k): n-number of all possible values, k-number of buckets, O(k+m): m - number of unique values
- similar problem: 705-Design HashSet
"""
class MyHashMap:

    def __init__(self):
        self.hash_factor = 1999
        self.hashkey_to_ll = collections.defaultdict(LinkedList) # hashkey -> linkedlist
        
    def __hashfunc(self, key):
        return key % self.hash_factor
        

    def put(self, key: int, value: int) -> None:
        hashkey = self.__hashfunc(key)
        ll = self.hashkey_to_ll[hashkey]
        node = ll.find(key)
        if node:
            node.val = value
        else:
            ll.add(key, value)        

    def get(self, key: int) -> int:
        hashkey = self.__hashfunc(key)
        ll = self.hashkey_to_ll[hashkey]
        node = ll.find(key)
        if not node:
            return -1
        return node.val   

    def remove(self, key: int) -> None:
        hashkey = self.__hashfunc(key)
        ll = self.hashkey_to_ll[hashkey]
        ll.remove(key)
        
class LinkedNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self, hashed_key=None):
        self.hashkey = None
        self.head = LinkedNode()
    
    def add(self, key, val):
        node = LinkedNode(key, val)
        node.next = self.head.next
        self.head.next = node
        
    def remove(self, key):
        prev, node = self.head, self.head.next
        while node:
            if node.key == key:
                break
            prev = node
            node = node.next
        if node:
            prev.next = node.next
            del node
        
    def find(self, key):
        node = self.head
        while node:
            if node.key == key:
                return node
            node = node.next
        return None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)