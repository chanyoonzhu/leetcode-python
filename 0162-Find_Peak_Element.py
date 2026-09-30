"""
- binary search
- key: how can we use binary search in an unsorted array? because nums[-1] = nums[n] = -∞
- O(log(n)), O(1)
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid + 1]: # l - mid can be strictly increasing and no peak, but mid - r must have a peak since nums[n] = -∞
                l = mid + 1 
            else:
                r = mid
        return l