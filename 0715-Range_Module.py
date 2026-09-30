"""
- binary search
- log(n), O(n)
"""
class RangeModule:

    def __init__(self):
        self.intervals = []
        

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.intervals, left)
        end = bisect.bisect_right(self.intervals, right)
        sub_interval = []
        if start % 2 == 0: sub_interval.append(left)
        if end % 2 == 0: sub_interval.append(right)
        self.intervals[start: end] = sub_interval

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.intervals, left) # note, bisect_right
        end = bisect.bisect_left(self.intervals, right) # note, bisect_left
        return start == end and start % 2 == 1
        
    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.intervals, left)
        end = bisect.bisect_right(self.intervals, right)
        sub_interval = []
        if start % 2 == 1: sub_interval.append(left)
        if end % 2 == 1: sub_interval.append(right)
        self.intervals[start: end] = sub_interval



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)