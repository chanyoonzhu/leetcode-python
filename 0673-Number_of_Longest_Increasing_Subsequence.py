"""
- dynamic programming
- O(n^2), O(n)
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[1, 1] for _ in range(N)] # (max_len, max_len count)
        max_len = 1
        
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0] + 1, dp[j][1]]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
                    max_len = max(max_len, dp[i][0])
        
        return sum(count for l, count in dp if l == max_len)