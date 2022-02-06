"""
https://leetcode.com/problems/maximum-subarray/
- summary: numbers can be negative, use dp (dp[i] the largest sum that ends at number at index i)
"""

"""
- Dynamic programming: dp[i] the largest sum that ends at number at index i
- can also be understood as Greedy algorithm: 1. find current element 2. find current local maximum sum (at this given point) 3. find global maximum sum seen so far.
- O(n), O(n)
"""
class Solution(object):
    def maxSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        dp = nums[:] # i - max sum ending at number with idx i
        
        for i in range(1, N):
            x = nums[i]
            dp[i] = max(dp[i-1] + x, dp[i])
        
        return max(dp)

"""
- Dynamic programming with space improved - only need dp[i-1] in each iteration
- can also be understood as Greedy algorithm: 1. find current element 2. find current local maximum sum (at this given point) 3. find global maximum sum seen so far.
- O(n), O(n)
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        global_max = prev_max = nums[0]
        
        for i in range(1, N):
            prev_max = max(nums[i], prev_max + nums[i])
            global_max = max(prev_max, global_max)
        
        return global_max

"""
- divide and conquer
- O(nlogn), O(logn)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def divideAndConquer(i, j):
            if i == j:
                return nums[i]
            mid = i + (j - i) // 2
            all_in_left_max = divideAndConquer(i, mid)
            all_in_right_max = divideAndConquer(mid + 1, j)
            
            # left max contain nums[mid]
            left = leftPartialMax = nums[mid]
            for n in range(mid - 1, i - 1, -1):
                left += nums[n]
                leftPartialMax = max(left, leftPartialMax)

            # right max contain nums[mid + 1]
            right = rightPartialMax = nums[mid + 1]
            for n in range(mid + 2, j + 1):
                right += nums[n]
                rightPartialMax = max(right, rightPartialMax)

            half_left_half_right_max = leftPartialMax + rightPartialMax
            return max(all_in_left_max, all_in_right_max, half_left_half_right_max)
        
        return divideAndConquer(0, len(nums) - 1)
            
    