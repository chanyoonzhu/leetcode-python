"""
- dynamic programming
- O(n^2), O(n^2)
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        N = len(s)
        res = 0
        
        dp = [[False] * N for _ in range(N)] # dp[i][j] - if s[i:j+1] isPalindrom
        for diff in range(N):
            for l in range(N - diff):
                r = l + diff
                if diff == 0:
                    dp[l][r] = True
                elif diff == 1:
                    dp[l][r] = True if s[l] == s[r] else False
                else:
                    if s[l] == s[r]:
                        dp[l][r] |= dp[l+1][r-1]
                if dp[l][r]:
                    res += 1

        return res

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

"""
- Two pointers
- expand from middle
- O(n^2), O(1)
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        
        for i in range(len(s)):
            # odd:
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
            # even
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
