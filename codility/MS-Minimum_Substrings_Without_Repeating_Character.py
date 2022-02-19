"""
Given a string s, find the minimum number of substrings you can create without having the same letters repeating in each substring.
"""
import collections

class Solution:
    def findSubstringsWithoutRepeatingChars(self, s: str) -> list:
        seen = set()
        res = 0
        for c in s:
            if c in seen:
                res += 1
                seen.clear()
            seen.add(c)
        return res + 1

s = Solution()
print(s.findSubstringsWithoutRepeatingChars("world"))
print(s.findSubstringsWithoutRepeatingChars("dddd"))
print(s.findSubstringsWithoutRepeatingChars("abba"))
print(s.findSubstringsWithoutRepeatingChars("cycle"))
