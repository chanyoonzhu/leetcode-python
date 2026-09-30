class MyCalendarThree:

    """
    - line sweeping with bisect: return the largest number of overlappings 
    - O(n^2), O(n)
    """
    def __init__(self):
        self.timelines = []
        self.max_booking = 0
        

    def book(self, start: int, end: int) -> int:
        
        bisect.insort(self.timelines, (start, 1))
        bisect.insort(self.timelines, (end, -1))
        
        booking = 0
        for _, _type in self.timelines:
            booking += _type
            self.max_booking = max(self.max_booking, booking)
        return self.max_booking
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)