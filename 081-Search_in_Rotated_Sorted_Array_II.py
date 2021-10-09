"""
- binary search
- caveat: numbers are not unique, edge case eg. [1,0,1,1,1]
- O(log(n)), O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]: # why need left bound?
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # get rid of repetitive numbers
                l += 1
        return nums[r] == target