"""
- two stacks
- intuition: a regular stack and a max stack to store max number seen so far
    popMax can be tricky - need to find last max element, remove, and update everything after it (temporarily keep in an array)
- O(1) - peek, push, pop, O(n) - others
"""
class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.max_stack.append(max(self.max_stack[-1], x) if self.max_stack else x)
        

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def peekMax(self) -> int:
        return self.max_stack[-1]
        

    def popMax(self) -> int:
        # find last element equal to max and update everything after it
        max_ = self.max_stack[-1]
        need_update = [] # stores elements that need updates
        while self.top() != max_:
            need_update.append(self.pop())
        self.pop()
        while need_update:
            self.push(need_update.pop())
        return max_

"""
- treemap + doubly linked list
- O(1) for top, O(logn) for others
"""
from sortedcontainers import SortedDict
class MaxStack:
    # O(1)
    def __init__(self):
        self.stack = DoublyLinkedList()
        self.treemap = SortedDict({})
    
    # O(logn)
    def push(self, x: int) -> None:
        node = Node(x)
        self.stack.append(node)
        self.treemap.setdefault(x, [])
        self.treemap[x].append(node)
    
    # O(logn)
    def pop(self) -> int:
        val = self.stack.pop()
        self._pop_treemap(val)
        return val
    
    # O(1)
    def top(self) -> int:
        return self.stack.peek()
    
    # O(logn)
    def peekMax(self) -> int:
        return self.treemap.peekitem(-1)[0]  # peekitem returns (key, val)  O(logn)
    
    # O(logn)
    def popMax(self) -> int:
        max_val = self.peekMax()
        node = self._pop_treemap(max_val) # note: return popped
        return self.stack.remove(node)
    
    # O(logn)
    def _pop_treemap(self, val):
        nodes = self.treemap[val]
        node = nodes.pop() # caveat: If there is more than one maximum element, required to only remove the top-most one.
        if not nodes:
            del self.treemap[val]
        return node

class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
    
    def append(self, node):
        prev = self.tail.prev
        prev.next = self.tail.prev = node
        node.prev, node.next = prev, self.tail
        
    def remove(self, node):
        val = node.val
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        del node
        return val
        
    def pop(self):
        return self.remove(self.tail.prev)
    
    def peek(self):
        return self.tail.prev.val

# Your MaxStack object will be instantiated and called as such:
obj = MaxStack2()
obj.push(5)
obj.push(1)
obj.push(5)
obj.top()
obj.popMax()
obj.top()
obj.peekMax()
obj.pop()
obj.top()