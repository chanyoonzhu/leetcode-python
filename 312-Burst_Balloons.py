"""
- similar problem: 1039. Minimum Score Triangulation of Polygon 
"""
"""
- dp top-down: 
    dp[i][j] = maximum coins bursting subset nums[i:j] (excluding i and j) 
    dp[i][j] = max(dp[l][r], dp[l][k] (popped) + dp[k][r] (popped) + nums[l] * nums[k] * nums[r] (to pop at this round))
- O(n^3), O(n^2)
- exceeds time limit 
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        nums = [1] + nums + [1]
        n = len(nums)
        def dfs(l, r):
            if (l, r) not in memo:
                memo[l, r] = max([dfs(l, k) + dfs(k, r) + nums[l] * nums[k] * nums[r] for k in range(l + 1, r)] or [0])
            return memo[l, r]
        return dfs(0, len(nums) - 1)
    

"""
- dp bottom-up: dp[i][j] = maximum coins bursting subset nums[i:j] (excluding i and j)
- O(n^3), O(n^2)
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for sub_size in range(2, n):
            for l in range(n - sub_size):
                r = l + sub_size
                for k in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], dp[l][k] + dp[k][r] + nums[l] * nums[k] * nums[r])
        return dp[0][n - 1]