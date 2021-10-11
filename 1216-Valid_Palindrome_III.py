"""
- dynamic programming (top-down)
- O(n^2), O(n^2*k)
"""
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        N = len(s)
        
        @lru_cache(None)
        def dp(i, j, k):
            if i >= j: return True
            
            if s[i] == s[j]:
                return dp(i + 1, j - 1, k)
            elif k > 0:
                return dp(i + 1, j, k - 1) or dp(i, j - 1, k - 1)
            return False
            
        return dp(0, N - 1, k)

"""
- dynamic programming (top-down)
- intuition: dp stores the min edit-distance to turn s[i:j+1] into a palindrome
- O(n^2), O(n^2)
"""
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        N = len(s)
        
        @lru_cache(None)
        def dp(i, j):
            if i >= j: return 0
            
            if s[i] == s[j]:
                return dp(i + 1, j - 1)
            else:
                return min(dp(i + 1, j), dp(i, j - 1)) + 1
            
        return dp(0, N - 1) <= k

"""
- dynamic programming (bottom-up)
- O(n^2), O(n^2)
"""
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
    
        N = len(s)
        if len(s) - k <= 1: return True
        dp = [[float("inf")] * N for _ in range(N)]

        for diff in range(N):
            for i in range(N - diff):
                j = i + diff
                if diff == 0:
                    dp[i][j] = 0
                elif diff == 1:
                    dp[i][j] = 0 if s[i] == s[j] else 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][-1] <= k 