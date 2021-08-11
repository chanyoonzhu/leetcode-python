"""
- sliding window
- O(n), O(1)
"""
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        seen = set()
        result = 0
        
        l = 0
        for i in range(len(word)):
            c = word[i]
            if i > 0 and ord(c) < ord(word[i-1]):
                seen.clear()
                seen.add(c)
                l = i
                continue
            seen.add(c)
            if len(seen) >= 5:
                result = max(result, i - l + 1)
        return result       
            