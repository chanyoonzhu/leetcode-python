"""
- stack: one stack only with prev_op variable
- O(n), O(n)
"""
class Solution:
    def calculate(self, s: str) -> int:
        
        def compute(n1, n2, op):
            if op == '*':
                return n1 * n2
            if op == '/':
                if n1 * n2 < 0:
                    return -(abs(n1) // abs(n2)) # easy to miss: -3 // 2 should equal to -1 not -2
                return n1 // n2
        
        s += '+' # smart: avoids handling end of string in a separate condition
        stack = []
        num, op = 0, '+'
        for i in range(len(s)):
            c = s[i]
            if c == ' ': # easy to miss
                continue
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            else:
                if op == '*' or op == '/':
                    stack.append(compute(stack.pop(), num, op))
                else:
                    stack.append(num if op == '+' else -num)
                num, op = 0, c
        return sum(stack)
    
"""
- no stack - three variables
- O(n), O(1)
"""
class Solution:
    def calculate(self, s: str) -> int:
        # .... + x    (+-*/)    y   (+-*/)
        #   res prev prev_op   cur  cur_op
        result = prev = cur = 0
        prev_op = '+'
        s += '+' # smart!
        for i in range(len(s)):
            c = s[i]
            if c == ' ':
                continue
            if c.isdigit():
                cur = cur * 10 + ord(c) - ord('0')
            else:
                if prev_op == '*':
                    prev *= cur
                elif prev_op == '/':
                    if prev * cur < 0: 
                        prev = -(abs(prev) // abs(cur))
                    else:
                        prev //= cur
                else:
                    result += prev
                    prev = cur if prev_op == "+" else -cur
                cur, prev_op = 0, c
        return result + prev

sl = Solution()
print(sl.calculate("3+2*2"))