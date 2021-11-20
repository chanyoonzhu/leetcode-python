"""
- two pointers
- O(n), O(n)
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        l, r = 0, N-1
        res = [0] * N
        for i in range(N-1, -1, -1):
            if abs(nums[l]) >= abs(nums[r]):
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1
        return res