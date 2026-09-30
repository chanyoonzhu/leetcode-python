"""
- binary search
- O(nlogn), O(n)
"""
class SummaryRanges:

    def __init__(self):
        self.starts = [] # start indexes of intervals
        self.ends = [] # end indexes of intervals
        

    def addNum(self, val: int) -> None:
        end_idx = bisect.bisect_right(self.starts, val)
        start_idx = bisect.bisect_left(self.ends, val)
        if end_idx == start_idx: # otherwise overlapped with existing interval
            # insert then merge
            self.starts.insert(end_idx, val)
            self.ends.insert(start_idx, val)
            self._merge(start_idx)
            
    def _merge(self, idx):
        left_merged = right_merged = False
        if idx > 0 and self.starts[idx] - 1 == self.ends[idx-1]:
            self.ends[idx-1] += 1
            left_merged = True
        if idx < len(self.starts) - 1 and self.ends[idx] + 1 == self.starts[idx+1]:
            self.starts[idx+1] -= 1
            right_merged = True
        if left_merged or right_merged:
            del self.starts[idx]
            del self.ends[idx]
        if left_merged and right_merged: # should also merge left and right
            self.starts[idx] = self.starts[idx-1]
            del self.starts[idx-1]
            del self.ends[idx-1]
            

    def getIntervals(self) -> List[List[int]]:
        return list(zip(self.starts, self.ends))
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()