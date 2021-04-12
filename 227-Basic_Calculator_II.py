class Solution(object):
    """
    - stack: two stacks
    - intuition: * and / are calculated immediately while + - are calculated altogether in the end
    - O(n), O(n)
    """
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
    def calculate(self, s: str) -> int:
        i, n = 0, len(s)
        stack = []
        prev_op = "+"
        while i < n:
            if s[i] == " ":
                i += 1
            elif not s[i].isdigit():
                prev_op = s[i]
                i += 1
            else:
                val = ""
                while i < n and s[i].isdigit():
                    val += s[i]
                    i += 1
                if prev_op == "*":
                    prev_num = stack.pop()
                    stack.append(prev_num * int(val))
                elif prev_op == "/":
                    prev_num = stack.pop()
                    if prev_num < 0:
                        stack.append(-(-prev_num // int(val))) # -5 // 2 = -3, so has to negate first
                    else:
                        stack.append(prev_num // int(val))
                elif prev_op == "+":
                    stack.append(int(val))
                elif prev_op == "-":
                    stack.append(-int(val))
                prev_op = "+"
        
        return sum(stack)
    
    """
    - no stack - three variables
    - O(n), O(1)
    """
    def calculate(self, s: str) -> int:
        pre = cur = result = 0
        op = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                cur = cur * 10 + int(c)
            if c in '+-*/' or i == len(s) - 1:
                if op == '+':
                    result, pre = pre + result, cur
                elif op == '-':
                    result, pre = pre + result, -cur
                elif op == '*':
                    pre *= cur
                elif op == '/':
                    if pre < 0:
                        pre = -((-pre) // cur)
                    else:
                        pre //= cur
                cur = 0
                op = c
        return result + pre

sl = Solution()
print(sl.calculate("3+2*2"))