class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        - expected sum minus sum of nums
        """
        n = len(nums)
        total = n * (n + 1) / 2
        return total - sum(nums)
    
        """
        - binary search
        """
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid
        return l