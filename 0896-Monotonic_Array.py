"""
- array
- O(n), O(1)
"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_increasing = None
        for i in range(1, len(nums)):
            if is_increasing is None:
                if nums[i] > nums[i-1]:
                    is_increasing = True
                elif nums[i] < nums[i-1]:
                    is_increasing = False
            else:
                if nums[i] > nums[i-1] and not is_increasing:
                    return False
                if nums[i] < nums[i-1] and is_increasing:
                    return False
        return True
        