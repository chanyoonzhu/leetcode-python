"""
Given a string s, find the minimum number of substrings you can create without having the same letters repeating in each substring.
"""
import collections

class Solution:
    def findSubstringsWithoutRepeatingChars(self, s: str) -> list:
        counter = collections.Counter()
        res = 0
        for i, c in enumerate(s):
            if counter[c] > 0:
                res += 1
                counter = collections.Counter()
            counter[c] += 1
        return res + 1

s = Solution()
print(s.findSubstringsWithoutRepeatingChars("world"))
print(s.findSubstringsWithoutRepeatingChars("dddd"))
print(s.findSubstringsWithoutRepeatingChars("abba"))
print(s.findSubstringsWithoutRepeatingChars("cycle"))
