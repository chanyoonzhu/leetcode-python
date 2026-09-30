"""
- dynamic programming (top-down)
- O(SP(S + P)), O(SP): (S + P) is the time to create the hash
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def dp(s, p):
            if not p and not s:
                return True
            if not p and s:
                return False
            if not s and p:
                return p == '*'
            if p[0] == '?':
                return dp(s[1:], p[1:])
            elif p[0] != '*': # single char
                return s[0] == p[0] and dp(s[1:], p[1:])
            else:
                return dp(s, p[1:]) or dp(s[1:], p)
        
        # getting rid of duplicate *
        new_p = ""
        for c in p:
            if not new_p or c != "*" or (new_p and new_p[-1] != "*"):
                new_p += c
        return dp(s, new_p)

                