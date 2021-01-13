class Solution(object):
    """
    - Sweep Lines
    - O(n), O(n1272-Remove_Interval)
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