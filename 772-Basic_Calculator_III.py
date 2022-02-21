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

"""
- two stacks
"""
class Solution:
    def calculate(self, s: str) -> int:
        funcs = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "*": lambda a,b: a*b,
            "/": lambda a,b: a//b if (a >= 0) == (b >= 0) else -(abs(a) // abs(b)),
        }
        precedences = {
            "(": -1,
            "+": 0,
            "-": 0,
            "*": 1,
            "/": 1
        }
        
        def operate():
            print(operands, operators)
            c = operators.pop()
            a = operands.pop()
            b = operands.pop()
            return funcs[c](b,a)
        
        def compare(op1, op2):
            return precedences[op1] - precedences[op2]
        
        operands = []
        operators = []
        
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                val = int(c)
                while i + 1 < len(s) and s[i+1].isdigit():
                    val = 10 * val + int(s[i+1])
                    i += 1
                operands.append(val)
            elif c == " ":
                continue
            elif c == "(":
                operators.append(c)
            elif c == ")":
                while (operators[-1] != '('):
                    operands.append(operate())
                operators.pop() # easy to miss: pop "("
            else:
                while operators and compare(c, operators[-1]) <= 0: # calculate if prev operator has higher precedence
                    operands.append(operate())
                operators.append(c)
            i += 1
        
        while operators:
            operands.append(operate())
        
        return operands[-1]