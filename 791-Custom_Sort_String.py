"""
- hashmap
- O(len(s)), O(1)
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        res = []
        for c in order:
            if c in counts:
                res.extend([c] * counts[c])
                del counts[c]
        for c in counts: # easy to miss: append those that are not in "order"
            res.extend([c] * counts[c])
        return "".join(res)