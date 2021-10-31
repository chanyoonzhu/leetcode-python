"""
- stack (optimized)
- O(n), O(1)
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        result = 0
        for c in s:
            if c == "(":
                open += 1
            else:
                if not open:
                    result += 1
                else:
                    open -= 1
        return result + open