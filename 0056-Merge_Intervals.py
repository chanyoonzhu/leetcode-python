"""
- sweep lines
- O(nlog(n)), O(n)
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        prev_end = float("-inf")
        
        res = []
        for start, end in intervals:
            if not res:
                res.append([start, end])
            else:
                if start > res[-1][1]:
                    res.append([start, end])
                else:
                    res[-1][1] = max(end, res[-1][1])
        
        return res