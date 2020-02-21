class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.dp = [0] * (self.n + 1)
        for i in range(self.n):
            self.dp[i+1] = self.dp[i] + nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1] - self.dp[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)