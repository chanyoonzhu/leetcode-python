class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        - O(n^2), -O(n)
        - dynamic programming
        - dp[i] minimum step to be at i
        - time limit exceeded
        
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        
        for i in range(len(dp)):
            for j in range(i+1,min(i+nums[i]+1, len(dp))):
                dp[j] = min(dp[j], dp[i] + 1)
                
        return dp[-1]
        """
        
        """
        - O(n)
        - Greedy
        - prevReach indicate farthest x steps can reach, currReach indicates farthest index x + 1 step can reach 
        """
        res = 0
        prevReach = currReach = 0
        
        for i in range(len(nums)):
            if i > prevReach:
                prevReach = currReach
                res += 1
            currReach = max(currReach, i + nums[i])
            
        return res