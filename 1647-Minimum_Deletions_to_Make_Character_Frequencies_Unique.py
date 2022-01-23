"""
- hashset
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        freq_seen = set()
        res = 0
        for c, freq in counter.items():
            while freq and freq in freq_seen:
                freq -= 1
                res += 1
            freq_seen.add(freq)
        return res