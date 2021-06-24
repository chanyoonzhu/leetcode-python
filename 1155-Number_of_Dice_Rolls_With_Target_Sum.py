"""
- dp (top-down)
- O(d*t*f), O(d*t)
"""
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        @lru_cache(None)
        def dp(d, target):
            if d == 0 and target == 0: return 1
            if d == 0: return 0
            return sum(dp(d - 1, target - n) for n in range(1, f + 1))
        
        return dp(d, target) % (10 ** 9 + 7)

"""
- dp (bottom-up) dp[d][t] - number of possible ways to roll n dice to get sum: t
- O(d*t*f), O(d*t)
"""
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1
        
        for di in range(1, d + 1):
            for ti in range(1, target + 1):
                dp[di][ti] = sum(dp[di - 1][ti - n] if ti - n >= 0 else 0 for n in range(1, f + 1))
        
        return dp[d][target] % (10 ** 9 + 7)

"""
- dp (bottom-up) - space optimized
- O(d*t*f), O(t)
"""
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        prev_dp = [1] + [0] * target
        
        for di in range(1, d + 1):
            dp = [0] * (target + 1)
            for ti in range(1, target + 1):
                dp[ti] = sum(prev_dp[ti - n] if ti - n >= 0 else 0 for n in range(1, f + 1))
            prev_dp = dp
        
        return dp[target] % (10 ** 9 + 7)