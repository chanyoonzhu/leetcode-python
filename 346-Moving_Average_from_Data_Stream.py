class MovingAverage(object):
    
    """
    - Queue
    
    def __init__(self, size):

        self.nums = []
        self.size = size
        

    def next(self, val):

        if len(self.nums) < self.size:
            self.nums.append(val)
            return sum(self.nums) / (len(self.nums) + 0.0)
        else:
            self.nums.pop(0)
            self.nums.append(val)
            return sum(self.nums) / (self.size + 0.0)
    """
    
    """
    - Queue with python's deque
    """

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.nums = collections.deque(maxlen=size)     

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.nums.append(val)
        return float(sum(self.nums)) / len(self.nums)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)