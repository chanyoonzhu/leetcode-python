class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
    
    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar:
    """
    - bst
    - O(n^2) - with Python, tree might not be balanced, if using Java TreeMap can be O(nlogn), O(n) 
    """

    def __init__(self):
        self.root = None
        

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))
    
    """
    - line sweeping (stream) with bisect
    - O(n^2), O(n)
    """
    def __init__(self):
        self.timelines = []
        

    def book(self, start: int, end: int) -> bool:
        bisect.insort(self.timelines, (start, 1))
        bisect.insort(self.timelines, (end, -1))
        booking = 0
        for _, time_type in self.timelines:
            booking += time_type
            if booking == 2:
                self.timelines.remove((start, 1))
                self.timelines.remove((end, -1))
                return False
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)