"""
- similar problem: 1039. Minimum Score Triangulation of Polygon 
"""
"""
- dp top-down: 
    dp[i][j] = maximum coins bursting subset nums[i:j] (including i and j) 
- O(n^3), O(n^2)
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @lru_cache(None)
        def dp(left, right):
            if left > right: return 0
            cost = 0
            # key: k is the LAST ballon to pop between [left, right], not the first
            for k in range(left, right + 1):
                cost = max(cost, dp(left, k-1) + nums[left-1] * nums[k] * nums[right+1] + dp(k+1, right))
            return cost
        
        return dp(1, len(nums) - 2)

"""
- dp bottom-up: dp[i][j] = maximum coins bursting subset nums[i:j] (excluding i and j)
- O(n^3), O(n^2)
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for diff in range(2, n):
            for l in range(n - diff):
                r = l + diff
                for k in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], dp[l][k] + dp[k][r] + nums[l] * nums[k] * nums[r])
        return dp[0][n - 1]