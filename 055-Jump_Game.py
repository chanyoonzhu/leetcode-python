"""
- dp (bottom-up): dp[i] - whether index i is reachable
- O(n*k) k - avg(steps), O(n)
- time limit exceeded
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        
        for i, steps in enumerate(nums):
            if dp[i]:
                dp[i + 1:i + steps + 1] = True
                for j in range(i + 1, min(n, i + steps + 1)):
                    dp[j] = True 
        return dp[-1]

"""
- dp (bottom-up)
- reachable problem: dp[i] - farthest index that can be reached next (considering all previous indexes)
- O(n), O(n)
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            if dp[i-1] > i - 1:
                dp[i] = max(dp[i-1], i + nums[i])
        return dp[-1] >= n - 1

"""
- dp (bottom-up)
- reachable problem: dp[i] - farthest index that can be reached next (considering all previous indexes)
- O(n), O(1) - space optimized, only need to track previous reachable
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        prev_reachable_index = nums[0]
        
        for i in range(1, n):
            if prev_reachable_index > i - 1:
                prev_reachable_index = max(prev_reachable_index, i + nums[i])
        return prev_reachable_index >= n - 1
                
                
            
        
        