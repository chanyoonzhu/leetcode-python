"""
- dynamic programming (top-down)
- O(n), O(n)
"""
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        @lru_cache(None)
        def dp(i):
            if i >= len(stoneValue): return 0
            maxx = float("-inf")
            for step in range(1, 4):
                taken = sum(stoneValue[i: i + step])
                maxx = max(maxx, taken - dp(i + step))
            return maxx
        
        alice_max = dp(0)
        if alice_max == 0: return "Tie"
        if alice_max > 0: return "Alice"
        return "Bob"

"""
- dynamic programming (bottom-up)
- O(n), O(n) - space can be optimized to O(1) to store previous three steps
"""
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        dp = [0] * (N + 3)
        for i in range(N - 1, -1, -1):
            dp[i] = float("-inf")
            for step in range(1, 4):
                taken = sum(stoneValue[i: min(N, i + step)])
                dp[i] = max(dp[i], taken - dp[i + step])
        
        if dp[0] == 0: return "Tie"
        if dp[0] > 0: return "Alice"
        return "Bob"