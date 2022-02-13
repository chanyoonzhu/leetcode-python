"""
- stack
- O(n), O(n)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        func = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x // y if (x >= 0) == (y > 0) else -(abs(x) // abs(y)),
        }
        
        
        ops_stack = []
        for token in tokens:
            if token in "+-*/":
                op2, op1 = ops_stack.pop(), ops_stack.pop()
                ops_stack.append(func[token](op1, op2))
            else:
                ops_stack.append(int(token))
        return ops_stack[0]
                
        