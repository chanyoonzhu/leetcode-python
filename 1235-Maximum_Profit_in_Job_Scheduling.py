"""
- dynamic programming (top-down)
- O(nlogn), O(n)
"""
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sorted_all = sorted(zip(startTime, endTime, profit), key=lambda i: i[0]) # sort by start time
        sorted_start = [start for start, _, _ in sorted_all]
        N = len(sorted_all)
        
        @lru_cache(None)
        def dp(i):
            if i >= N:
                return 0
            total = dp(i + 1) # skip current
            _, end, profit = sorted_all[i]
            next_i = bisect.bisect_left(sorted_start, end)
            total = max(total, profit + dp(next_i)) # pick current
            return total
        
        return dp(0)