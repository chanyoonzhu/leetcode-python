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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if low > high or not root: return 0
        if low <= root.val <= high:
            return self.rangeSumBST(root.left, low, root.val - 1) + root.val + self.rangeSumBST(root.right, root.val + 1, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return self.rangeSumBST(root.right, low, high)