"""
- sliding window
- O(n), O(n)
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pos = {'a': 0, 'b': 1, 'c': 2}
        counts = [0] * 3
        left, result = 0, 0
        for i in range(len(s)):
            counts[pos[s[i]]] += 1
            while all(counts):
                counts[pos[s[left]]] -= 1
                left += 1
            result += left
        return result