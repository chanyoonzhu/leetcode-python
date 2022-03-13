"""
- List
"""
class MovingAverage(object):
    
    def __init__(self, size):

        self.nums = []
        self.size = size
        
    # O(n) - list copy
    def next(self, val):

        if len(self.nums) < self.size:
            self.nums.append(val)
            return sum(self.nums) / (len(self.nums) + 0.0)
        else:
            self.nums.pop(0)
            self.nums.append(val)
            return sum(self.nums) / (self.size + 0.0)

    
"""
- Queue with python's deque
"""
class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.nums = collections.deque(maxlen=size)     

    # - O(k)
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.nums.append(val)
        return float(sum(self.nums)) / len(self.nums)

"""
- Queue with precalculated sums
"""
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.window_sum = 0
        self.window_size = 0
        

    # O(1)
    def next(self, val: int) -> float:
        if self.window_size < self.size:
            self.window_size += 1
        else:
            self.window_sum -= self.window.popleft()
        self.window_sum += val
        self.window.append(val)
        return self.window_sum / self.window_size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)