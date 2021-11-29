"""
- dynamic programming
- O(n^2), O(n)
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        N = len(s)
        res = 1
        prev_dp = [0]
        
        for i in range(1, N):
            dp = [i]
            if s[i] == s[i-1]:
                dp.append(i-1)
            for start in prev_dp:
                if start > 0 and s[i] == s[start-1]:
                    dp.append(start-1)
            res += len(dp)
            prev_dp = dp
        
        return res