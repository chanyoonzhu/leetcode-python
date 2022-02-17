"""
- sweep lines
- O(nlog(n)), O(n)
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        
        s_prev, e_prev = intervals[0]
        for s, e in intervals[1:]:
            if s > e_prev:
                res.append([s_prev, e_prev])
                s_prev, e_prev = s, e
            else:
                e_prev = max(e_prev, e)
        res.append([s_prev, e_prev])
        return res