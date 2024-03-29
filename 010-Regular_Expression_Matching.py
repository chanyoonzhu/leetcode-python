"""
- edge cases:
(ab, c*ab) => True c* can match empty string
"""


"""
- dynamic programming (top-down)
- O(sp), O(sp)
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.match(s, p)
        
    @lru_cache(None)
    def match(self, s, p):
        if not p:
            return not s
        
        can_first_match = len(s) and (s[0] == p[0] or p[0] == ".")
        
        if len(p) > 1 and p[1] == "*":
            # match first or skip
            return (can_first_match and self.match(s[1:], p)) or self.match(s, p[2:])
        else:
            return can_first_match and self.match(s[1:], p[1:])

"""
- dynamic programming (bottom-up)
- O(sp), O(sp)
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s, p = ' ' + s, ' ' + p
        dp = [[False] * len(s) for c in p]
        dp[0][0] = True
        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if p[i].isalpha() and p[i] == s[j] or p[i] == '.' and s[j] != ' ': # single char match
                    dp[i][j] = dp[i-1][j-1]
                elif p[i] == '*': # kleene star case
                    dp[i][j] = dp[i-1][j]  # when * matches 1 more chars
                    if i-2 >= 0:
                        dp[i][j] = dp[i][j] or dp[i-2][j] # when * matches 0 chars
                    if p[i-1] == s[j] or p[i-1]  == '.':
                        dp[i][j] = dp[i][j] or dp[i][j-1] # or itself matches p[i-1]*
                        
        return dp[-1][-1]
        
        
        

sl = Solution()
print(sl.isMatch("aaa", ".*"))
        
        
        