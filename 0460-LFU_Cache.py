import collections

"""
- hashmap + doubly linked list: my solution
- all O(1)
- intuition: one doubly linked list for each access count
- better solution: https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list
"""
class Node:
    
    def __init__(self, key, val=0, count=0):
        self.key = key
        self.val = val
        self.count = count
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
    def __init__(self):
        self.count = count
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head
    
    def add(self, node):
        node.next, node.prev = self.head.next, self.head
        node.next.prev = node.prev.next = node
        return node
    
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        node.next = node.prev = None
        return node
    
    
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_count = float("inf")
        self.count_map = collections.defaultdict(DoublyLinkedList) # one doubly linked list for each access count
        self.key_map = collections.defaultdict(Node)
        

    def get(self, key: int) -> int:
        if key in self.key_map:
            node = self.key_map[key]
            self.update_count(node)
            return node.val
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self.update_count(node)
        else:
            if self.size and self.size == self.capacity: # edge case: capacity can be 0
                self.remove()
                self.size -= 1
            node = Node(key, value, 0)
            self.size += 1
            if self.size <= self.capacity:
                self.key_map[key] = node
                self.update_count(node)
    
    def update_count(self, node):
        if node.next: # existing node, has to remove from current doubly-linked-list
            linked_list_prev = self.count_map[node.count]
            linked_list_prev.remove(node)
            if linked_list_prev.head.next == linked_list_prev.tail:
                if node.count == self.min_count:
                    self.min_count += 1
                del self.count_map[node.count]
        node.count += 1
        if node.count not in self.count_map:
            self.count_map[node.count] = DoublyLinkedList()
            self.min_count = min(self.min_count, node.count)
        self.count_map[node.count].add(node)
    
    def remove(self):
        linked_list = self.count_map[self.min_count]
        removed = linked_list.remove(linked_list.tail.prev)
        if linked_list.head.next == linked_list.tail:
            del self.count_map[self.min_count]
            self.min_count = float("inf")
        del self.key_map[removed.key]        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        

    """ for debugging
    def toString(self):
        print(f"capacity: {self.capacity}; size: {self.size}, key_maps: {self.key_map}, count_maps={self.count_map}, mix_count={self.min_count}")

        for count, linkedlist in self.count_map.items():
            print(f"count map for count: {count}")
            ptr = linkedlist.head.next
            while ptr and ptr.key != -1:
                print((ptr.key, ptr.val, ptr.count))
                ptr = ptr.next 
    """      
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
            
        


# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
obj.put(3,3)
obj.get(2)
obj.get(3)
obj.put(4,4)
obj.get(1)
obj.get(3)
obj.get(4)

# obj = LFUCache(1)
# obj.put(2,1)
# obj.get(2) # 1
# obj.put(3,2)
# obj.get(2) # null
# obj.get(3) # 2

# obj = LFUCache(2)
# obj.put(2,1)
# obj.put(2,2)
# obj.get(2) # 2
# obj.put(1,1)
# obj.put(4,1)
# obj.get(2) # 2

