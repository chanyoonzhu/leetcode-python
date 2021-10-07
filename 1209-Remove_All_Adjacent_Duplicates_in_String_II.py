"""
- stack
- O(n), O(n)
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        
        return ''.join([c * n for c, n in stack])