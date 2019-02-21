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
        - bit manipulation
        """
        numsFull = [i for i in range(len(nums)+1)]
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
            res ^= numsFull[i]
            
        res ^= numsFull[-1]
        
        return res
    
        """
        - binary search
        - if array sorted
        """
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid
        return l