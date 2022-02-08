"""
- dynamic programming (bottom-up): dp[i] minimum step to be at i
- O(n^2), -O(n)
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        for i in range(n):
            step = nums[i]
            for j in range(i + 1, min(i + step + 1, n)): # easy to miss: bound by n
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

"""
- O(n)
- Greedy
- intuition: for each i, get farthest it can reach (curr_reachable_index), only walk when prev can reach could not reach current index i
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prev_reachable_index = curr_reachable_index = 0
        result = 0
        
        for i in range(len(nums)):
            if prev_reachable_index < i:
                result += 1
                prev_reachable_index = curr_reachable_index
            curr_reachable_index = max(curr_reachable_index, i + nums[i])
        return result