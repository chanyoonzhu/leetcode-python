class Solution(object):
    """
    - Sweep Lines
    - O(n), O(n)
    """
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
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        left = bisect.bisect_left([interval[0] for interval in intervals], toBeRemoved[0])
        right = bisect.bisect_right([interval[1] for interval in intervals], toBeRemoved[1])
        
        if left > 0:
            for i in range(left):
                result.append([intervals[i][0], intervals[i][1]])
            if intervals[left-1][1] > toBeRemoved[0]:
                result[left-1][1] = toBeRemoved[0]
        if right < len(intervals):
            for i in range(right, len(intervals)):
                result.append([intervals[i][0], intervals[i][1]])
            if intervals[right][0] < toBeRemoved[1]:
                result[left][0] = toBeRemoved[1]
        return result