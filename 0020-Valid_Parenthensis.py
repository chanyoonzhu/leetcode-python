"""
https://leetcode.com/problems/valid-parentheses/
summary: cannot use three counters since the order among them matters eg. "({)}[]" is not valid, therefore needs a stack
"""

"""
- stack
- O(n), O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()
        return not stack