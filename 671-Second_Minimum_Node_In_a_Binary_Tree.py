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
        if not root: return -1
        minimum = root.val
        second_min = self.dfs(root, minimum)
        return second_min if second_min < float("inf") else -1
    
    def dfs(self, node, minimum):
        if not node:
            return float("inf")
        if node.val > minimum:
            return node.val
        else:
            l_min = self.dfs(node.left, minimum)
            r_min = self.dfs(node.right, minimum)
            return min(l_min, r_min)