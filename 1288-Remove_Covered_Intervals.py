class Solution:
    """
    - Sweep lines (greedy)
    - O(nlogn), O(n) - for sorting
    """
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        prev_end = float("-inf")
        removed = 0
        for start, end in intervals:
            if end <= prev_end:
                removed += 1
            else: 
                prev_end = end
        return len(intervals) - removed