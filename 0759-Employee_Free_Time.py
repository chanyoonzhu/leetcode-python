"""
# Definition for an Interval.
"""
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end


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
    - line sweeping solution
    """
    class Solution:
        def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
            schedules = []
            for s_list in schedule:
                schedules.extend(s_list)
            schedules = sorted(schedules, key=lambda x: x.start)
            res = []
            prev_start, prev_end = schedules[0].start, schedules[0].end
            for s in schedules[1:]:
                start, end = s.start, s.end
                if start > prev_end:
                    res.append(Interval(prev_end, start))
                prev_start, prev_end = start, max(prev_end, end)
            return res

    """
    - O(Clogn) solution with priority queue: todo
    """