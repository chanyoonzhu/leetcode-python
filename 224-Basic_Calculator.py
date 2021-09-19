"""
- stack
- intuition: use a stack to store the calculated signs of surrounding parenthesis
"""
class Solution:
    def calculate(self, s: str) -> int:
        
        sign_stack = [1]
        result, num, sign = 0, 0, 1
        for c in s+"+": # adding "+" smart!
            if c.isdigit():
                num = 10 * num + ord(c) - ord('0')
            elif c in "+-":
                result += num * sign * sign_stack[-1]
                sign = 1 if c == "+" else -1
                num = 0
            elif c == '(':
                sign_stack.append(sign * sign_stack[-1]) # calculate and push the sign of current parenthesis
                sign = 1
            elif c == ')':
                result += num * sign * sign_stack[-1]
                num = 0
                sign_stack.pop()
        return result