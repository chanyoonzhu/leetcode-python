"""
- Median
- O(nlogn), O(n)
- intuition: converge to median
"""
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [n for row in grid for n in row]

        # O(N) possible via "quick select"
        nums.sort()
        median = nums[len(nums)//2] 

        res = 0
        for n in nums:
            steps, mod = divmod(abs(n - median), x)
            if mod:
                return -1
            res += steps
        return res