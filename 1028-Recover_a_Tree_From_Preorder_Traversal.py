# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    """
    - dfs (preorder) recursive with stack: my solution (# todo: better recursive solution)
    - O(n) - n is the length of S, O(n)
    """
    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.stack = []
        
        def dfs(i, depth):
            if i >= len(S):
                return None
            num = ""
            while i < len(S) and S[i] != "-":
                num += S[i]
                i += 1
            node = TreeNode(int(num))
            self.stack.append(node)
            j = i
            while j < len(S) and S[j] == "-":
                j += 1
            next_depth = j - i 
            if next_depth == (depth + 1):
                node.left = dfs(j, depth + 1)
            else:
                self.stack = self.stack[:next_depth]
                if self.stack:
                    parent = self.stack[-1] # need to store since self.stack changes between recursions
                    parent.right = dfs(j, next_depth)
            return node
        
        return dfs(0, 0)

    """
    - dfs (preorder) iterative with stack
    - O(n) - n is the length of S, O(n)
    """
    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.stack = []
        n = len(S)
        i = 0
        while i < n:
            depth, val = 0, ""
            while i < n and S[i] == "-":
                depth += 1
                i += 1
            while i < n and S[i] != "-":
                val += S[i]
                i += 1
            node = TreeNode(int(val))
            while depth < len(self.stack):
                self.stack.pop()
            if self.stack and not self.stack[-1].left:
                self.stack[-1].left = node
            elif self.stack:
                self.stack[-1].right = node
            self.stack.append(node)
        
        return self.stack[0]
                
        
        