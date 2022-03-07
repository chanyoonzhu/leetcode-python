"""
- Divide and Conquer
- intuition: if a swapcase of a character is not in s, no qualifying substring can contain that character, recursively search its left and right strings and pick the longest
- O(n^2), O(n)
"""
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: return ""
        all_char = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in all_char:
                s_left = self.longestNiceSubstring(s[:i])
                s_right = self.longestNiceSubstring(s[i+1:])
                return max(s_left, s_right, key=len)
        return s
        