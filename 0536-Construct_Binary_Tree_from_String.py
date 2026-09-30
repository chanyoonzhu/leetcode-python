# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs
- O(n^2), O(n)
"""
class Solution:
    
    # find next left and matching parenthesis
    def findSubStr(self, s, i):
        open_p = 0
        j = i
        while j < len(s):
            if s[j] == '(':
                open_p += 1
            elif s[j] == ')':
                open_p -= 1 
            if open_p == 0:
                break
            j += 1
        return i, j
    
    def findRootValAndNextIdx(self, s):
        i = 0
        if s[0] == '-':
            i += 1
        n = 0
        while i < len(s) and s[i].isdigit():
            n = n * 10 + ord(s[i]) - ord('0')
            i += 1
        return (-n if s[0] == '-' else n, i)
    
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        root_val, next_pi = self.findRootValAndNextIdx(s)
        root = TreeNode(root_val)
        p_start, p_end = self.findSubStr(s, next_pi)
        root.left = self.str2tree(s[p_start+1:p_end])
        next_pi = p_end + 1
        p_start, p_end = self.findSubStr(s, next_pi)
        root.right = self.str2tree(s[p_start+1:p_end])
        return root

"""
- stack
- O(n), O(n)
"""
class Solution:
    
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s: return None
        num, stack = '', []
        for i, c in enumerate(s):
            if c ==')':
                stack.pop()
            elif c.isdigit() or c == "-":
                num += c
                if i+1 == len(s) or not s[i+1].isdigit():
                    node, num = TreeNode(num), ''
                    if stack:
                        parent = stack[-1]
                        if parent.left:
                            parent.right = node
                        else:
                            parent.left = node
                    stack.append(node)
        return stack[0]