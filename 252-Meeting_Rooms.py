class Solution(object):
    """
    - sorting
    - O(nlogn), O(1) (O(n) with current implementation, copies array)
    """
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals = sorted(intervals, key = lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i+1][0] < intervals[i][1]:
                return False
        return True