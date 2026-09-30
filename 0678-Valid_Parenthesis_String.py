"""
- greedy
- intuition: number of left brackets can be expressed as a range [opens_min, opens_max]
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        opens_min, opens_max = 0, 0
        for c in s:
            if c == '(':
                opens_min += 1
                opens_max += 1
            elif c == '*':
                opens_min = max(opens_min - 1, 0)
                opens_max += 1
            elif c == ')':
                opens_min = max(opens_min - 1, 0)
                opens_max -= 1
            if opens_max < 0: return False
        return opens_min == 0

"""
- dynamic programming
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        
        @lru_cache(None)
        def dp(i, open_count):
            if i == N:
                return open_count == 0
            if s[i] == "(":
                return dp(i + 1, open_count + 1)
            elif s[i] == ")":
                if open_count < 1: return False
                return dp(i + 1, open_count - 1)
            else:
                return dp(i + 1, open_count + 1) or dp(i + 1, open_count) or (open_count >= 1 and dp(i + 1, open_count - 1))
            
        return dp(0, 0)