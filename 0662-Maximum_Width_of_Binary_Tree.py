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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_right = []
        self.dfs(root, 0, 0, left_right)
        res = 0
        for left, right in left_right:
            res = max(res, right - left + 1)
        return res
        
    
    def dfs(self, node, row, col, left_right):
        if not node:
            return
        if row == len(left_right):
            left_right.append((col, col))
        else:
            left, right = left_right[row]
            left_right[row] = (min(left, col), max(right, col))
        self.dfs(node.left, row + 1, col * 2, left_right)
        self.dfs(node.right, row + 1, col * 2 + 1, left_right)

"""
- bfs
"""
        