"""
- stack
- O(n), O(n)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        
        def compute(op2, op1, operator):
            if operator == "+":
                return op1 + op2
            elif operator == "-":
                return op1 - op2
            elif operator == "*":
                return op1 * op2
            elif operator == "/":
                if (op1 > 0) == (op2 > 0): # easy to miss
                    return op1 // op2
                else:
                    return math.ceil(op1 / op2)
                
        def parseNum(token):
            if token[0] == "-":
                return -int(token[1:])
            return int(token)
        
        for token in tokens:
            if token in "/+*-":
                operands.append(compute(operands.pop(), operands.pop(), token))
            else:
                operands.append(parseNum(token))
                
        return operands[-1]
                
        