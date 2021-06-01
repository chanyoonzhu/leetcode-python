"""
- sort and linear search
- O(nlogn + n), O(logn)
"""
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        low = 1
        n = len(nums)
        for i in range(n):
            if low <= n - i <= nums[i]:
                return n - i
            low = nums[i] + 1
        return -1

"""
- sort and binary search
- O(nlogn + logn), O(logn)
"""
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 1, len(nums)
        while left <= right:
            mid = (left + right) // 2
            idx = bisect_left(nums, mid)
            if len(nums) - idx == mid: return mid
            elif len(nums) - idx > mid: left = mid + 1
            else: right = mid - 1
        return -1