"""
- Array
- intuition: replace the number A with the number B which is just larger than itself among the numbers lying to its right section
- O(n), O(1)
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        n = len(nums)
        if n == 1:
            return nums
        
        # from right to left, find first dip (decrease)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i == -1: # if increasing all the way from right to left, just reverse
            self.reverse(nums, 0, n-1)
            return
        
        
        # find minimum larger on the right of the dip
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # swap dip and the minimum larger
        nums[i], nums[j] = nums[j], nums[i]
        
        # reverse right side of the dip
        self.reverse(nums, i+1, n-1)
        
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1