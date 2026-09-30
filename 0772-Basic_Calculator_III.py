"""
- recursion (a combination of 224(+- with parenthensis) and 227(+-*/ with no parenthesis))
- https://leetcode.com/problems/basic-calculator-iii/discuss/1805832/Solve-this-problem-combining-the-solution-to-Basic-Calculator-I-and-II-with-recursion
"""
class Solution:
    def calculate(self, s: str) -> int:
    
        def compute(n1, n2, op):
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
        
        def helper(s):
            res = prev = cur = 0 
            res_op = prev_op = "+"
            
            i = 0
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    cur = cur * 10 + ord(c) - ord("0")
                elif c in "*/+-)":
                    if prev_op in "*/":
                        prev = compute(prev, cur, prev_op)
                    elif prev_op in "+-":
                        res = compute(res, prev, res_op)
                        prev = cur
                        res_op = prev_op
                    prev_op = c
                    cur = 0
                    if c == ")":
                        return (compute(res, prev, res_op), i + 1)
                elif c == "(":
                    cur, consumed = helper(s[i+1:])
                    i += consumed
                i += 1
            return (compute(res, prev, res_op), i)
                
        return helper(s + "+")[0]

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