"""
- dynamic programming (top-down)
- O(n), O(n)
"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dp(i, color):
            if i == -1: return 0
            min_cost = float("inf")
            for c in range(3):
                if c != color:
                    min_cost = min(min_cost, costs[i][c] + dp(i - 1, c))
            return min_cost
        
        return dp(len(costs) - 1, -1)

"""
- dynamic programming (bottom-up)
- O(n), O(1)
"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
    
        prev_dp = costs[0]
        for i in range(1, len(costs)):
            dp = [float("inf")] * 3
            for c in range(3):
                for prev_c in range(3):
                    if c != prev_c:
                        dp[c] = min(dp[c], prev_dp[prev_c] + costs[i][c])
            prev_dp = dp
        return min(prev_dp)
    