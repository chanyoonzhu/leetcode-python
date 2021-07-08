"""
- Pre-computing with prefix sum
- initiation: O(n), O(1), sumRange: O(1), O(1)
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] + [0] * len(nums)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i] 

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)