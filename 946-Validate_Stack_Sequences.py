"""
- stack
- O(n), O(n)
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i_pop = 0
        for n1 in pushed:
            stack.append(n1)
            while stack and stack[-1] == popped[i_pop]:
                stack.pop()
                i_pop += 1
        return not stack