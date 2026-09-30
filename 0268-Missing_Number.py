"""
- Gauss Sum
- O(n), O(1)
"""
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
- bitwise operation
- [0, 1, 3, 4] -> result = 4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4) =(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2 = 0∧0∧0∧0∧2 = 2
​- O(n), O(1)
"""
class Solution(object):
    def missingNumber(self, nums):
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result
    
"""
- binary search
- O(nlogn), (logn)
"""
class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid
        return l