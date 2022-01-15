# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- BST dfs
- O(n), O(n)
"""
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        self.dfs(root)
        return self.maximum
        
    def dfs(self, node):
        if not node:
            return (float("inf"), float("-inf"), 0)
        val = node.val
        lmin, lmax, lsum = self.dfs(node.left)
        rmin, rmax, rsum = self.dfs(node.right)
        if lmax < val < rmin: # is BST
            sum_ = lsum + rsum + val
            self.maximum = max(self.maximum, sum_)
            return (min(lmin, val), max(rmax, val), lsum + rsum + val)
        return (float("-inf"), float("inf"), 0) # not a BST