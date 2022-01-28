"""
- Math: median
- key: the median of the sorted must be the number all others should move to
- intuition: nums[0] and nums[n-1] cost same moves when converge to anything in between;
    likely, nums[1] and nums[n-2] cost same moves when converge to anything in between, 
    so we also make nums[0] and nums[n-1] to converge to something between nums[1] and nums[n-2] to get minimum move
    recusively, we find that all numbers should converge to median
- O(nlogn), O(logn)
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        half_n = n // 2
        if n % 2:
            median = nums[half_n]
        else:
            median = (nums[half_n-1] + nums[half_n]) // 2
            
        return sum(abs(n - median) for n in nums)