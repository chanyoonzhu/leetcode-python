"""
- backtracking
- O(n*2^n), O(n)
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        def backtrack(s, seen):
            if not s:
                return 0
            res = 0
            for i in range(1, len(s) + 1):
                if s[:i] not in seen and len(s) - i + 1 > res:
                    seen.add(s[:i])
                    res = max(res, 1 + backtrack(s[i:], seen))
                    seen.remove(s[:i])
            return res
        return backtrack(s, seen)

"""
- enumeration with bitmask
- O(n*2^n), O(n)
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        result = 0
        for mask in range(2 ** len(s)):
            substrings = set()
            prev = 0
            for i in range(len(s)):
                if ((mask << 1) + 1) & (1 << len(s) - 1 - i):
                    if s[prev:i + 1] in substrings:
                        break
                    substrings.add(s[prev:i + 1])
                    prev = i + 1
            result = max(result, len(substrings))
        return result