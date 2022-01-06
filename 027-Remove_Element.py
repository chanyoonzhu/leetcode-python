"""
- two pointer
- intuition: fill first n position one by one using valid number
- O(n), O(1)
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

"""
- two pointer
- intuition: pointer r always have values to remove
- O(n), O(1)
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            if nums[l] == val:
                nums[l] = nums[r-1]
                r -= 1
            else:
                l += 1
        return r