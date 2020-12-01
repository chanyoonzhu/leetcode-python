class Solution(object):

    """
    - my initial solution
    - dynamic programming: dp[i] - max stolen until house i (i has to be selected)
    - time O(n)
    - space O(n)
    """
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
    - dynamic programming: dp[i] - max stolen until house i (i doesn't have to be selected)
    - time O(n)
    - space O(n)
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = [0] * (len(nums) + 2)
        for i in range(2, len(nums)+2):
            t[i] = max(nums[i-2] + t[i-2], t[i-1])
        return t[-1]

    """
    - dynamic programming with space optimization - only need to track t[i-2] and t[i-1] for previous solution
    - time O(n)
    - space O(n)
    """
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        prev_max, prev2_max = 0, 0
        for i in range(len(nums)):
            curr_max = max(nums[i] + prev2_max, prev_max)
            prev2_max = prev_max
            prev_max = max(prev_max, curr_max)
        return prev_max
            