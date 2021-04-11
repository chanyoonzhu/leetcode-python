# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    - stack (two stacks)
    - hard: answer copied; has other solutions such as using parser
    """
    def expTree(self, s: str) -> 'Node':
        
        ops = []
        digits = []
        
        def construct():
            r = digits.pop()
            l = digits.pop()
            digits.append(Node(ops.pop(), l, r))
        
        for c in s:
            if c.isdigit():
                digits.append(Node(c))
            elif c in ["+", "-"]:
                while ops and ops[-1] in ["+", "-", "*", "/"]:
                    construct()
                ops.append(c)
            elif c in ["*", "/"]:
                while ops and ops[-1] in ["*", "/"]:
                    construct()
                ops.append(c)
            elif c == "(":
                ops.append(c)
            elif c == ")":
                while ops[-1] != "(":
                    construct()
                ops.pop()
        while ops:
            construct()
        return digits[0]