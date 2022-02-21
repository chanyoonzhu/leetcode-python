"""
- Array
- O(n), O(1)
"""
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]
        return not diffs or len(diffs) == 2 and diffs[0][::-1] == diffs[1]
        