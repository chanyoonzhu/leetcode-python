"""
- dynamic programming (top-down)
- O(n), O(n)
"""
class Solution:
    def knightDialer(self, n: int) -> int:
        next_num = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        
        MOD  = 10 ** 9 + 7
        
        @lru_cache(None)
        def dp(x, steps):
            if steps == 0:
                return 1
            ways = 0
            for next_x in next_num[x]:
                ways = (ways + dp(next_x, steps - 1)) % MOD
            return ways
        
        return sum(dp(x, n - 1) for x in range(10)) % MOD

"""
- dynamic programming (bottom-up)
- O(n), O(1)
"""
class Solution:
    def knightDialer(self, n: int) -> int:    
        MOD  = 10 ** 9 + 7
        prev_nums = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        prev_dp = [1] * 10
        for _ in range(1, n):
            dp = [0] * 10
            for x in range(10):
                for prev_x in prev_nums[x]:
                    dp[x] = (dp[x] + prev_dp[prev_x]) % MOD
            prev_dp = dp
        return sum(prev_dp) % MOD