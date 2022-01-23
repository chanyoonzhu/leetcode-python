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
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, float("-inf"))
        return self.res
        
    def dfs(self, node, path_max):
        if not node:
            return
        if path_max <= node.val:
            self.res += 1
        path_max = max(path_max, node.val)
        self.dfs(node.left, path_max)
        self.dfs(node.right, path_max)
        