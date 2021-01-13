"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    """
    - priority queue
    - O(Clogc), O(C) C is the number of jobs across all employees.
    """
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        pq, res = [], []
        for intervals in schedule:
            for interval in intervals:
                heapq.heappush(pq, (interval.start, interval.end))
        while pq:
            start, end = heapq.heappop(pq)
            if pq:
                start_next, end_next = pq[0]
                if end < start_next:
                    res.append(Interval(end, start_next))
                elif end > end_next: # easy to miss this part
                    pq[0] = (pq[0][0], end)
        return res

    """
    - line sweeping solution - todo
    """

    """
    - O(Clogn) solution with priority queue: todo
    """