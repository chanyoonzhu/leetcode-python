"""
- dfs
- O(n), O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        l = self.invertTree(root.right)
        r = self.invertTree(root.left)
        root.left, root.right = l, r
        return root