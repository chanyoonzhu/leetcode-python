"""
- Dynamic programming: dp[i] the largest sum that includes the number at index i
- can also be understood as Greedy algorithm: 1. find current element 2. find current local maximum sum (at this given point) 3. find global maximum sum seen so far.
- O(n), O(n)
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float("-inf")] * (len(nums) + 1)
        
        for i, num in enumerate(nums):
            dp[i + 1] = max(dp[i] + num, num)
        
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
        prev, max_sum = 0, float("-inf")
        for n in nums:
            prev = max(prev + n, n)
            max_sum = max(max_sum, prev) 
        return max_sum

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
            
    