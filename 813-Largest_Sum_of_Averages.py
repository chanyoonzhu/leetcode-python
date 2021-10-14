"""
- dynamic programming (bottom-up)
- O(n^2*k), O(max(n^2, n*k) # space can be optimized to O(k)
"""
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        N = len(nums)
        
        dp = [[0] * (N + 1) for _ in range(k)]
        
        prefixes = [0] * (N + 1)
        for i in range(N):
            prefixes[i+1] = prefixes[i] + nums[i]
        
        for ki in range(k):
            for ni in range(1, N + 1):
                if ki == 0: # one partition
                    dp[ki][ni] = prefixes[ni] / ni
                else:
                    for nj in range(1, ni + 1):
                        dp[ki][ni] = max(dp[ki][ni], dp[ki-1][nj-1] + (prefixes[ni] - prefixes[nj-1]) / (ni - nj + 1.0))
        
        return dp[k-1][N]