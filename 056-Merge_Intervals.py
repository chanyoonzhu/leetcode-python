# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        """
        - heap
        - not recommended
        
        if not intervals or len(intervals) == 0:
            return []
        
        import heapq
        
        heap = [(interval.start, interval.end) for interval in intervals]
        heapq.heapify(heap)
        first = heapq.heappop(heap)
        res = [Interval(first[0], first[1])]
        
        while heap:
            curr = heapq.heappop(heap)
            if res[-1].end < curr[0]:
                res.append(Interval(curr[0], curr[1]))
            else:
                res[-1].end = max(res[-1].end, curr[1])
            
        return res
        """
        
        """
        -O(nlog(n)), -O(n)
        """
        res = []
        for i in sorted(intervals, key=lambda x:x.start):
            if res:
                if res[-1].end < i.start:
                    res.append(i)
                else:
                    res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res