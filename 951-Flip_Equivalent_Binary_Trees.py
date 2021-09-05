# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs recursive
- easy to miss: not all nodes requires flip (flip some is also okay)
- O(n), O(n)
"""
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2: return root1 == root2 == None
        return root1.val == root2.val and (
            self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))