class Solution(object):

    """
    - Dynamic programming: dp[i] the largest sum that includes the number at index i
    - can also be understood as Greedy algorithm: 1. find current element 2. find current local maximum sum (at this given point) 3. find global maximum sum seen so far.
    - time O(n)
    - space O(n)
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums) + 1)
        max_sum = float("-inf")
        for i in range(1, len(nums) + 1):
            dp[i] = max(nums[i-1] + dp[i-1], nums[i-1]) # if some number is greater than itself plus preceeding numbers, can discard all its proceeding numbers
            max_sum = max(max_sum, dp[i]) 
        return max_sum

    """
    - Dynamic programming with space improved - only need dp[i-1] in each iteration
    - can also be understood as Greedy algorithm: 1. find current element 2. find current local maximum sum (at this given point) 3. find global maximum sum seen so far.
    - time O(n)
    - space O(1)
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, max_sum = 0, float("-inf")
        for n in nums:
            prev = max(prev + n, n)
            max_sum = max(max_sum, prev) 
        return max_sum

        """
        divide and conquer?
        """