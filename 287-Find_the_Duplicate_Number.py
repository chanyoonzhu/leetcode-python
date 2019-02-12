class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        - caveat: a number may be duplicated more than once
        """
        
        def helper(nums, l, r):
            if l > r:
                return r
            mid = (l + r) // 2
            smaller = 0
            for i in nums:
                if i < mid:
                    smaller += 1
            if smaller <= mid - 1:
                return helper(nums, mid+1, r)
            else:
                return helper(nums, l, mid-1)
        
        return helper(nums, 1, len(nums)-1)
        