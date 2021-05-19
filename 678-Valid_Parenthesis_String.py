"""
- greedy
- intuition: number of left brackets can be expressed as a range [opens_min, opens_max]
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        opens_min, opens_max = 0, 0
        for c in s:
            if c == '(':
                opens_min += 1
                opens_max += 1
            elif c == '*':
                opens_min = max(opens_min - 1, 0)
                opens_max += 1
            elif c == ')':
                opens_min = max(opens_min - 1, 0)
                opens_max -= 1
            if opens_max < 0: return False
        return opens_min == 0