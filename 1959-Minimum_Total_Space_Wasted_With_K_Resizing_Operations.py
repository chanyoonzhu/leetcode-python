"""
- dynamic programming 
- dp(i, k): the minimum space wasted if we can resize k times of nums[i..n-1].
- O(N ^ 2 * K), O(N * K)
"""
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        @lru_cache(None)
        def dp(i, k):
            if i == N: return 0
            if k == -1: return float("inf")
            res = float("inf")
            max_num = nums[i]
            total = 0
            for j in range(i, N):
                max_num = max(max_num, nums[j])
                total += nums[j]
                wasted = max_num * (j - i + 1) - total
                res = min(res, dp(j + 1, k - 1) + wasted)
            return res

        return dp(0, k)