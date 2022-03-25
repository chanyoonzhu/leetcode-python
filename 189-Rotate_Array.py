"""
- Array
- O(n), O(1)
- similar: 186-Reverse Words in a String II
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        self.reverse(nums, 0, n-1) # reverse entire array
        k %= n
        self.reverse(nums, 0, k-1) # reverse left part
        self.reverse(nums, k, n-1) # reverse right part
        
        
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1