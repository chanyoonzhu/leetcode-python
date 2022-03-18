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
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[1]
       
    def dfs(self, node):
        if not node:
            return 0, None
        l_depth, l_tree = self.dfs(node.left)
        r_depth, r_tree = self.dfs(node.right)
        if l_depth == r_depth: # deep nodes in both left and right subtree
            return l_depth + 1, node
        elif l_depth > r_depth: # deep nodes in left tree only
            return l_depth + 1, l_tree
        else: # in right tree only
            return r_depth + 1, r_tree