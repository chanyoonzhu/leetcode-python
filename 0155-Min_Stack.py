"""
- stack and binary search (too obvious, not recommended)
- push: O(logn), pop:(log(n)), top:O(1), getMin:O(1); space: O(n)
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.ordered = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        bisect.insort(self.ordered, val)
        

    def pop(self) -> None:
        top = self.stack.pop()
        i = bisect.bisect_left(self.ordered, top)
        del self.ordered[i]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ordered[0]

"""
- stack: value and min pairs
- push: O(1), pop:(1), top:O(1), getMin:O(1); space: O(n)
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append((val, min(self.getMin(), val)))        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][-1]
        return float("inf")