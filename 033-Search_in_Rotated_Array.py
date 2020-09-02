class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        """
        - two passes: find rotate index, then search in the right portion
        - O(logN), O(1)
        """
        
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
        - One pass: is each half sorted? what determines whether target is in which half?
        - O(logN), O(1)
        """
        def helper(left, right):
            if left > right:
                return -1
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]: # if you do nums[mid] > nums[left], you will fail certain edge cases like ([3,1], 1) will return -1 where it should return 1. Because // 2 will truncate. So either use nums[mid] < nums[right] or nums[mid] >= nums[left] 
                if nums[mid] < target <= nums[right]:
                    return helper(mid + 1, right)
                else:
                    return helper(left, mid - 1)
            else:
                if nums[left] <= target < nums[mid]:
                    return helper(left, mid - 1)
                else:
                    return helper(mid + 1, right)
        
        return helper(0, len(nums) - 1)