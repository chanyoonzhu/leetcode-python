"""
- O(n), O(1)
- intuition: when every () appears, calculate its value considering depth(opening)
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        result = opening = 0
        for i, c in enumerate(s):
            if c == '(':
                opening += 1
            else:
                opening -= 1
                if s[i - 1] == '(':
                    result += 2 ** opening # score are only calculated when seeing "()" 
        return result

"""
- stack: stack[-1] is the current score earned so far
- - O(n), O(n)
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                score = stack.pop()
                stack[-1] = max(score * 2, 1) + stack[-1]
        return stack[0]