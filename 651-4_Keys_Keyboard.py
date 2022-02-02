"""
- dynamic programming
- MLE
"""
class Solution:
    def maxA(self, n: int) -> int:
        
        @lru_cache(None)
        def backtrack(n, total, buffer_size):
            if n <= 0:
                return total
            # print A
            new_total = backtrack(n - 1, total + 1, buffer_size)
            # copy
            new_total = max(new_total, backtrack(n - 2, total, total))
            # paste
            new_total = max(new_total, backtrack(n - 1, total + buffer_size, buffer_size))
            return new_total
        
        return backtrack(n, 0, 0)

"""
- dynamic programming
- intuition: First of all, we can know that if N < 7, then f[N] = N
since double current list length need 3 operations (ACP) and ACP must generate longer list than PPP for list with length > 3, the maximum for f[i] only have 3 choices:

from f[i - 3], by ACP total length : f[i - 3] * 2
from f[i - 4], by ACP + P total length : f[i - 4] * 3
from f[i - 5], by ACP + PP total length : f[i - 5] * 4
That's all. for i - 6 and smaller ACP + ACP longer than ACP + PPP. so we can get it from f[i - 3]
- O(n), O(n)
"""
class Solution:
    def maxA(self, n: int) -> int:
        
        dp = list(range(n+1))
        
        for i in range(7, n + 1):
            # max of ACP, ACPP, ACPPP
            dp[i] = max(dp[i-3] * 2, dp[i-4] * 3, dp[i-5] * 4)
        return dp[n]