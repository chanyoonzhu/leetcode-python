"""
- binary_search
- O(n^2*logn), O(logn) or O(n) - depend on sorting
- similar: 015 - 3 Sum
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0
        nums.sort()
        for i, num in enumerate(nums):
            for j in range(i + 1, n):
                k = bisect.bisect_left(nums, target - num - nums[j], j + 1, n) - 1
                result += k - j
        return result

"""
- two pointers with sort
- O(n^2), O(logn) or O(n) - depend on sorting
- similar: 015 - 3 Sum
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0
        nums.sort()
        for i, num in enumerate(nums):
            l, r = i + 1, n - 1
            while l < r:
                _sum = nums[l] + nums[r] + num
                if _sum >= target:
                    r -= 1
                else:
                    result += (r - l)
                    l += 1
        return result