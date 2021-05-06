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
            if dp[i] != float("inf"):
                for j in range(i + 1, min(n, i + nums[i] + 1)):
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

 """
- O(n)
- Greedy
- use prev_reachable_index until it cannot reach current index, then update it to max current reachable. 
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