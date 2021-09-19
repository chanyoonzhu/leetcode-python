"""
- stack
- O(n), O(n)
"""
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = [] # stack[-1] stores the expression evaluation, stack[-2] stores the operator
        
        def compute(op, ex1, ex2):
            if op == '!':
                return not ex1
            elif op == '&':
                return ex1 and ex2
            elif op == '|':
                return ex1 or ex2
        
        for c in expression:
            if c in "!|&":
                stack.append(c)
                stack.append(False if c == '|' else True) # caveat: | needs to start with "False" as expression evaluation or else it will always evaluate to True
            elif c in '(,':
                continue
            elif c in "tf":
                stack[-1] = compute(stack[-2], True if c == 't' else False, stack[-1])
            elif c == ')':
                cur_ex = stack[-1]
                stack.pop()
                stack.pop()
                if not stack: return cur_ex
                stack[-1] = compute(stack[-2], cur_ex, stack[-1])

"""
- Recursive
"""
                