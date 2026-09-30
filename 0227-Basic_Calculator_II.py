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
        res = prev = cur = 0 # prev and cur handles all */, no */ calculation penetrates to res (only +- between res and prev)
        res_op = prev_op = "+" # op between res and prev; op between prev and cur
        
        for c in s + "+":
            if c == " ":
                continue
            if c.isdigit():
                cur = cur * 10 + ord(c) - ord("0")
            else:
                if prev_op in "*/": # calculates */ as we see them
                    prev = self.compute(prev, cur, prev_op)
                else:
                    res = self.compute(res, prev, res_op)
                    prev = cur
                    res_op = prev_op
                prev_op = c
                cur = 0
        return self.compute(res, prev, res_op)
                
    def compute(self, n1, n2, op):
        if op == "+":
            return n1 + n2
        elif op == "-":
            return n1 - n2
        elif op == "*":
            return n1 * n2
        elif op == "/":
            if (n1 >= 0) == (n2 >= 0):
                return n1 // n2
            return -(abs(n1) // abs(n2))

sl = Solution()
print(sl.calculate("3+2*2"))