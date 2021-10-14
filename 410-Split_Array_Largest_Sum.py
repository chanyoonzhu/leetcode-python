    """
    - dynamic programming (top-down)
    - O(n^2*m), O(n^2*m)
    - time limit exceeded
    """
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:       
        @lru_cache(None)
        def dfs(l, r, count):
            min_sum = sum(nums[l:r + 1])
            if count == 1:
                return min_sum
            for i in range(l, r + 1):
                min_sum = min(min_sum, max(dfs(l, i, 1), dfs(i + 1, r, count - 1)))
            return min_sum
            
        return dfs(0, len(nums) - 1, m)
    
"""
- dynamic programming (bottom-up)
- O(n^2*m), O(n*m)
- TLE
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:       
        
        N = len(nums)
        
        prefixes = [0] * (N + 1)
        for i in range(N):
            prefixes[i+1] = prefixes[i] + nums[i]
        
        dp = [[float("inf")] * (N + 1) for _ in range(m)]
        dp[0] = prefixes
        
        for mi in range(1, m):
            for ni in range(1, N + 1):
                for nj in range(1, ni + 1):
                    dp[mi][ni] = min(dp[mi][ni], max(dp[mi-1][nj-1], prefixes[ni] - prefixes[nj-1]))
        
        return dp[m-1][N]
    
"""
- binary search + greedy
- O(nlogk) - k is the sum of array, O(1)
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:       
        
        lo, hi = 0, sum(nums)
        
        def canSplit(s):
            cur_sum, groups = 0, 1
            for n in nums:
                if n > s: return False # easy to miss
                if cur_sum + n <= s:
                    cur_sum += n
                else:
                    cur_sum = n
                    groups += 1
                    if groups > m: return False
            return True
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if canSplit(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo