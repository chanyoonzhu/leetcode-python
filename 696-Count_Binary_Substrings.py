"""
- Array scan
- group chars
- O(n), O(n) - space can be optimized to O(1)
"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        prev = s[0]
        for i in range(1, len(s)):
            cur = s[i]
            if cur != prev:
                groups.append(1)
                prev = cur
            else:
                groups[-1] += 1
        res = 0
        for i in range(1, len(groups)):
            longest_pair = min(groups[i-1], groups[i])
            res += longest_pair
        
        return res
                