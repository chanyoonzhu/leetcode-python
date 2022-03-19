"""
- brute force
- O(n^2), O(n)
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal): return False
        
        for i in range(n):
            if s[i:] + s[:i] == goal:
                return True
        return False

"""
- rolling hash
- O(n), O(1)
"""
class Solution:
    
    def rotateString(self, s: str, goal: str) -> bool:
        self.mod = 10**9 + 7
        n = len(s)
        if n != len(goal): return False
        
        goal_hashed = self.hashString(goal)
        s_hashed = self.hashString(s)
        for i in range(n):
            if goal_hashed == s_hashed:
                return True
            s_hashed_first_removed = s_hashed - (ord(s[i]) - ord("a")) * (26 ** (n - 1))
            s_hashed = (s_hashed_first_removed * 26 + (ord(s[(i+n)%n]) - ord("a"))) % self.mod
        return False
    
    def hashString(self, s):
        hashed = 0
        for c in s:
            hashed = (hashed * 26 + ord(c) - ord("a")) % self.mod
        return hashed