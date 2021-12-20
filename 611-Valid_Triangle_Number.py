"""
- binary search
- O(n^2logn), O(logn)-for sorting
"""
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3:
            return 0
        
        nums.sort()
        res = 0
        
        for i1, n1 in enumerate(nums):
            for i2 in range(i1 + 1, N):
                smaller_sides_sum = n1 + nums[i2]
                i3 = bisect.bisect_left(nums, smaller_sides_sum) - 1
                if i3 > i2:
                    res += (i3 - i2)
                    
        return res

"""
- two pointer
- O(n^2), O(1)
"""
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        N = len(nums)
        for i3 in range(2, N):
            i1, i2 = 0, i3-1
            while i1 < i2:
                if nums[i1] + nums[i2] > nums[i3]:
                    res += (i2 - i1)
                    i2 -= 1
                else:
                    i1 += 1
        return res