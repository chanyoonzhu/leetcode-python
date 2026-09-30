"""
- dynamic programming
- O(n), O(n)
"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        M = len(days)
        costs_and_durations = list(zip(costs, [1, 7, 30]))
        
        @lru_cache(None)
        def dp(i):
            if i >= M:
                return 0
            min_cost = float("inf")
            for cost, duration in costs_and_durations:
                next_day = days[i] + duration
                min_cost = min(min_cost, cost + dp(bisect.bisect_left(days, next_day, i)))
            return min_cost
        
        return dp(0)