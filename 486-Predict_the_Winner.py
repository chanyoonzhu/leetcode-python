"""
- dynamic programming (top-down)
- O(n^2), O(n^2)
"""
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]
            return max(nums[i] - dp(i + 1, j), nums[j] - dp(i, j - 1))
        
        return dp(0, len(nums) - 1) >= 0

"""
- dynamic programming (bottom-up)
- O(n^2), O(n^2) - space can be optimized to O(n)
"""
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        N = len(nums)
        dp = [[0] * N for _ in range(N)]
        
        for d in range(N):
            for i in range(N - d):
                j = i + d
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
        return dp[0][-1] >= 0