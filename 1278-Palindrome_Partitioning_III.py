"""
- dynamic programming (top-down)
- O(n^2*k), O(max(n^2, n*k)
"""
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        N = len(s)
        
        @lru_cache(None)
        def get_change_counts(i, j):
            change_counts = 0
            while i < j:
                if s[i] != s[j]:
                    change_counts += 1
                i += 1
                j -= 1
            return change_counts
            
        
        @lru_cache(None)
        def dp(i, k):
            nonlocal N
            
            if i + 1 < k: return float("inf") # need to divide into exactly k subsets
            
            if k == 1: 
                return get_change_counts(0, i)
            
            min_changes = N
            for j in range(i + 1):
                min_changes = min(min_changes, get_change_counts(j, i) + dp(j - 1, k - 1))
            return min_changes
            
        return dp(len(s) - 1, k)

"""
- dynamic programming (bottom-up)
- O(n^2*k), O(max(n^2, n*k) # space can be optimized to O(k)
"""
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        @lru_cache(None)
        def get_change_counts(i, j):
            change_counts = 0
            while i < j:
                if s[i] != s[j]:
                    change_counts += 1
                i += 1
                j -= 1
            return change_counts

        N = len(s)
        dp = [[float("inf")] * (N + 1) for _ in range(k)]
        for ki in range(k):
            for ni in range(1, N + 1):
                if ki == 0:
                    dp[ki][ni] = get_change_counts(0, ni - 1)
                else:
                    dp[ki][ni] = N
                    for nj in range(1, ni + 1):
                        dp[ki][ni] = min(dp[ki][ni], get_change_counts(nj - 1, ni - 1) + dp[ki-1][nj-1])
        return dp[k-1][N]