"""
- sliding window
- O(n), O(n) or O(min(m, n)) m: size of the alphabet
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        res = 0
        for r, c in enumerate(s):
            if c not in chars:
                res = max(res, r - l + 1)
                chars.add(c)
            else:
                while s[l] != c:
                    chars.remove(s[l])
                    l += 1
                l += 1
        return res