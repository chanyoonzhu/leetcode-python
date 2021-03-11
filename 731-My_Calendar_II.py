class MyCalendarTwo:

    """
    - line sweeping with bisect: return false when three consecutive start are seen 
    - O(n^2), O(n)
    """
    def __init__(self):
        self.record = []
        self.count = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        bisect.insort(self.record,(start, 1))
        bisect.insort(self.record,(end, -1))
        
        booking = 0
        for _, _type in self.record:
            booking += _type
            if booking == 3:
                self.record.remove((start, 1))
                self.record.remove((end, -1))
                return False
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)