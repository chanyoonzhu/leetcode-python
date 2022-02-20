"""
- Hashmap + hashset
- O(n), O(1)
"""
class Solution:
    def numSplits(self, s: str) -> int:
        counts = Counter(s)
        res = 0
        left_seen = set() # left_distinct: len(left_seen)
        right_distinct = len(counts.keys())
        for c in s:
            left_seen.add(c)
            counts[c] -= 1
            if counts[c] == 0:
                right_distinct -= 1
            if len(left_seen) == right_distinct:
                res += 1
        return res