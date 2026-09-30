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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_val = root.val
        res = float("inf")
        
        def dfs(node):
            nonlocal res
            if not node:
                return
            if node.val > min_val:
                res = min(res, node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res if res < float("inf") else -1