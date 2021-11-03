"""
- Array
- O(n), O(1)
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # replace the number A with the number B which is just larger than itself among the numbers lying to its right section
        # find the number(A) before the longest non-increasing suffix
        right = len(nums)-1
        while right > 0 and nums[right-1] >= nums[right]:
            right -= 1
        if right == 0:
            return self.reverse(nums,0,len(nums)-1)
        # find pivot
        pivot = right - 1
        successor = 0
        # find the number(B) which is just larger than A among the numbers lying to its right section
        for i in range(len(nums) - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        # swap pivot and successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]  
        # reverse non-increasing suffix
        self.reverse(nums,pivot + 1,len(nums) - 1)
        
    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1