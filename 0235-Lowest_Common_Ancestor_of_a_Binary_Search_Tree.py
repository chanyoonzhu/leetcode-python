# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
- recursive dfs
- O(n), O(n)
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        val = root.val
        if max(p.val, q.val) < val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
            