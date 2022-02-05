"""
- dynamic programming 
- dp[i] - (min, max) of subarray ending at nums[i]
- O(n), O(n) - space can be improved to O(1) if only keeping min_max of the previous item
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [(1, 1)] # min, max
        for n in nums:
            prev_min, prev_max = dp[-1]
            if n == 0:
                dp.append((0, 0))
            elif n > 0:
                dp.append((prev_min * n, max(prev_max * n, n)))
            else:
                dp.append((min(prev_max * n, n), prev_min * n))
        return max(max_ for _, max_ in dp[1:])