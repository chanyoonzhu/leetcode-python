class Node():
        
    def __init__(self, key, value):
        self.kv = [key, value]
        self.next = None

class MyHashMap(object):
    
    """
    - Naive solution
    
    def __init__(self):
        self.mem = [-1] * 1000000
        

    def put(self, key, value):
        self.mem[key] = value

    def get(self, key):
        return self.mem[key]
        

    def remove(self, key):
        self.mem[key] = -1
    """
    
    """
    - space optimized
    - 2D array, only set row to 1000 as new item comes
    
    def __init__(self):
        self.mem = [[] for _ in range(1001)]
        

    def put(self, key, value):
        row, col = divmod(key, 1000)
        if len(self.mem[row]) == 0:
            self.mem[row] = [-1] * 1000
        self.mem[row][col] = value

    def get(self, key):
    
        row, col = divmod(key, 1000)
        if len(self.mem[row]) == 0:
            return -1
        else:
            return self.mem[row][col]
        

    def remove(self, key):

        row, col = divmod(key, 1000)
        if len(self.mem[row]) != 0:
            self.mem[row][col] = -1
    """
    
    """
    - hash with chaining
    """
    
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = [None] * 1001
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        row = key // 1000
        if self.mem[row] is None:
            self.mem[row] = Node(key, value)
        else:
            prev = curr = self.mem[row]
            while curr:
                if curr.kv[0] == key:
                    curr.kv[1] = value
                    return
                else:
                    prev = curr
                    curr = curr.next
            prev.next = Node(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        row = key // 1000
        curr = self.mem[row]
        while curr:
            if curr.kv[0] == key:
                return curr.kv[1]
            else:
                curr = curr.next
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        row = key // 1000
        curr = prev = self.mem[row]
        if not curr: return
        if curr.kv[0] == key:
            self.mem[row] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.kv[0] == key:
                    prev.next = curr.next
                    break
                else:
                    curr, prev = curr.next, prev.next


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1000000,1)
obj.put(2,2)
print(obj.get(1))
print(obj.get(3))
obj.put(2,1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))