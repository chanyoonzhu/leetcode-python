"""
- similar: 446-Arithmetic Slices II - Subsequence
"""
"""
- dynamic programming (bottom-up)
- O(n^2), O(nk)
"""
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        N = len(nums)
        dp = defaultdict(int)
        
        for i in range(1, N):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = max(dp[(i, diff)], dp[(j, diff)] + 1)
        return max(dp.values()) + 1