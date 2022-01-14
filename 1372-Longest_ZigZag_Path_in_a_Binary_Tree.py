# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs
- O(n), O(n)
"""
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.longest = 0
        self.dfs(root)
        return self.longest - 1
    
    def dfs(self, node):
        if not node:
            return (0, 0)
        ll, lr = self.dfs(node.left)
        rl, rr = self.dfs(node.right)
        self.longest = max(self.longest, max(lr + 1, rl + 1))
        return (lr + 1, rl + 1)
        