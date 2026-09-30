 """
- binary search
- two passes: find rotate index, then search in the right portion
- O(logN), O(1)
"""
class Solution(object):
    def search(self, nums, target):
        def helper(left, right):
            if nums[left] <= nums[right]: # easy to miss this base condition
                return left
            if left + 1 == right and nums[right] < nums[left]:
                return right
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                return helper(mid, right)
            return helper(left, mid)
        
        def helper2(nums, left, right, target):
            if left > right:
                return -1
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return helper2(nums, left, mid - 1, target)
            if target > nums[mid]:
                return helper2(nums, mid + 1, right, target)
        
        n = len(nums)
        smallest_index = helper(0, n - 1)
        ordered_nums = nums[smallest_index:] + nums[:smallest_index]
        if target > nums[n - 1]: # use this, no need to use an ordered array
            return helper2(nums, 0, smallest_index - 1, target)
        return helper2(nums, smallest_index, n - 1, target)

"""
- binary search
- intuition: at least one half of the array is in order, figure out which part is strictly increasing by comparing nums[low] with nums[mid], find number is in the strictly increasing half or the other half
- O(logN), O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]: # low - mid is strictly increasing
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]: # mid - high is strictly increasing
                    low = mid + 1
                else:
                    high = mid - 1

        return -1