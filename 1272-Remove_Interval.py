"""
- Sweep Lines
- O(n), O(n)
"""
class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for start, end in intervals:
            if end < toBeRemoved[0] or start > toBeRemoved[1]:
                res.append([start,end])
            else:
                if start < toBeRemoved[0]:
                    res.append([start, toBeRemoved[0]])
                if end > toBeRemoved[1]:
                    res.append([toBeRemoved[1], end])
        return res
    
"""
- binary search (with bisect)
- O(logn), O(n)
"""
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        i = bisect.bisect_right([end for _, end in intervals], toBeRemoved[0])
        j = bisect.bisect_left([start for start, _ in intervals], toBeRemoved[1])
        
        if i == j: # easy to miss, no overlap
            return intervals
        
        res = intervals[:i]
        # intervals [i+1:j-1] are guaranteed to be removed, so only need to handle to [i] and [j-1], use set to dedup if i == j-1
        for k in set([i, j-1]):
            start, end = intervals[k]
            if start < toBeRemoved[0]:
                res.append([start, toBeRemoved[0]])
            if end > toBeRemoved[1]:
                res.append([toBeRemoved[1], end])
        res.extend(intervals[j:])
        
        return res