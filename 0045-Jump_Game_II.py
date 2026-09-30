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
        cur_reachable = next_reachable = 0
        steps = 0
        for i in range(len(nums)):
            if cur_reachable < i: # not walk until can't reach
                steps += 1
                cur_reachable = next_reachable # when has to walk, greedily walk to the farthest 
            next_reachable = max(next_reachable, i + nums[i]) # keep track of the farthest one can walk to
        return steps