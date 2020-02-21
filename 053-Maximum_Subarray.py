class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        if some number is greater than itself plus preceeding numbers, can discard all its proceeding numbers
        """
        res, cur = float('-inf'), 0
        for n in nums:
            cur = max(cur + n, n)
            res = max(res, cur)
        return res

        """
        divide and conquer?
        """