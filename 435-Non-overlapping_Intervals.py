class Solution(object):
    """
    - greedy, sweep lines
    - O(nlogn), O(n) - sorting, space can be O(1) based on API used
    - Algorithm: 
    1. sort by start time
    2. when overlapping, always remove the one ends later - greedy
    3. return total removed
    """
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x:x[0])
        prev_end = float("-inf")
        removed = 0
        for start, end in intervals:
            if start < prev_end:
                if end <= prev_end:
                    prev_end = end
                removed += 1
            else:
                prev_end = end
        return removed

    """
    - dynamic programming: todo
    """

s = Solution()
s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])