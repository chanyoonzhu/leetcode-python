"""
- sliding window
- O(n), O(n) or O(min(m, n)) m: size of the alphabet
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        result = 0
        for r, c in enumerate(s):
            if c not in chars:
                result = max(result, r - l + 1)
            else:
                while c in chars:
                    chars.remove(s[l])
                    l += 1
            chars.add(c)
        return result