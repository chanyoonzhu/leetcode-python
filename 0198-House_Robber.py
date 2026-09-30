"""
- my initial solution
- dynamic programming: dp[i] - max stolen until house i (i has to be selected)
- time O(n)
- space O(n)
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums) + 3)
        for i in range(3, len(nums) + 3):
            dp[i] = max(dp[i-3] + nums[i-3], dp[i-2] + nums[i-3])
        return max(dp[-1], dp[-2])

"""
- dynamic programming: dp[i] - max stolen until house i (i doesn't necessarily have to be selected)
- time O(n)
- space O(n)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i, num in enumerate(nums):
            dp[i + 2] = max(dp[i + 1], dp[i] + num)
        return dp[-1]

"""
- dynamic programming with space optimization - only need to track t[i-2] and t[i-1] for previous solution
- time O(n)
- space O(1)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_two = [0, 0]
        result = 0
        for i, n in enumerate(nums):
            result = max(prev_two[1], prev_two[0] + n)
            prev_two = [prev_two[1], result]
        return result
            