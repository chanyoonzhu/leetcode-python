"""
- recursion
"""
class Solution:
    def calculate(self, s: str) -> int:
        
        def helper(s):
            
            def compute(n1, n2, op):
                if op == '+':
                    return n1 + n2
                if op == '-':
                    return n1 - n2
                if op == '*':
                    return n1 * n2
                if op == '/':
                    if n1 * n2 < 0:
                        return -(abs(n1) // abs(n2))
                    return n1 // n2
            
            result = prev = cur = 0
            prev_op = '+'

            i = 0
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    cur = cur * 10 + ord(c) - ord('0')
                elif c == '(':
                    nested_result, consumed_count = helper(s[i + 1:])
                    cur = nested_result
                    i += consumed_count # increase by consumed space in nested calculation
                elif c == ')':
                    prev = compute(prev, cur, prev_op)
                    result += prev
                    return (result, i + 1) # key: need to track spaces consumed
                else:
                    if prev_op in "*/":
                        prev = compute(prev, cur, prev_op)
                    else:
                        result += prev
                        prev = cur if prev_op == '+' else -cur
                    cur, prev_op = 0, c
                i += 1
            return (result + prev, i)
        
        return helper(s + '+')[0]