"""
- stack: two stacks
- intuition: * and / are calculated immediately while + - are calculated altogether in the end
- O(n), O(n)
"""
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        numStack = []
        opStack = []
        
        for c in s:
            if c == ' ':
                continue
            elif c == '+' or c == '-' or c == '*' or c == '/':
                opStack.append(c)
            else:
                if not numStack:
                    numStack.append(int(c))
                    continue
                op = opStack[-1]
                if op == '*':
                    prevNum = numStack.pop()
                    numStack.append(prevNum * int(c))
                elif op == '/':
                    prevNum = numStack.pop()
                    numStack.append(prevNum // int(c))
                else:
                    numStack.append(int(c))
                    
        while opStack:
            op = opStack.pop()
            oprand2 = numStack.pop()
            oprand1 = numStack.pop()
            if op == '+':
                numStack.append(oprand1 + oprand2)
            else:
                numStack.append(oprand1 - oprand2)
        
        return numStack.pop()
    
"""
- stack: two stacks
- O(n), O(n)
"""
class Solution:
    def calculate(self, s: str) -> int:
        i, n = 0, len(s)
        ops, nums = [], []
        
        def compute():
            op = ops.pop()
            r = nums.pop()
            l = nums.pop()
            if op == "+":
                nums.append(l + r)
            elif op == "-":
                nums.append(l - r)
            elif op == "*":
                nums.append(l * r)
            elif op == "/":
                nums.append(l // r)
        
        while i < n:
            val, op = "", ""
            if s[i] == " ":
                i += 1
            elif not s[i].isdigit():
                if s[i] in ["+", "-"]:
                    while ops:
                        compute()
                elif s[i] in ["*", "/"]:
                    while ops and ops[-1] in ["*", "/"]:
                        compute()
                ops.append(s[i])
                i += 1
            else:
                while i < n and s[i].isdigit():
                    val += s[i]
                    i += 1
                nums.append(int(val))
        while ops:
            compute()
        return nums[0]

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
            if c == ' ':
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
        
        stack = []
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