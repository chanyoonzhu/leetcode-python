"""
- two pointers
- O(n^2), O(logn)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        res = float("inf")
        for i in range(N-2):
            l, r = i + 1, N - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 - target == 0:
                    return target
                if abs(sum3 - target) < abs(res - target):
                    res = sum3
                if sum3 < target:
                    l += 1
                else:
                    r -= 1
        return res