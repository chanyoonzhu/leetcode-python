# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs
- clarification: definition of path is tricky: path with no fork, does not need to go through root nor leaf
- O(n), O(n)
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node: Optional[TreeNode]) -> int:
        
        if not node: return 0
        
        left_side_max = max(0, self.dfs(node.left)) # only use when positive
        right_side_max = max(0, self.dfs(node.right))
        
        self.max_sum = max(self.max_sum, left_side_max + right_side_max + node.val)
        
        return max(left_side_max, right_side_max) + node.val

n1 = TreeNode(-2)
n1.left = TreeNode(6)
# n1.right = TreeNode(20)
n1.left.left = TreeNode(0)
n1.left.right = TreeNode(-6)

print(Solution().maxPathSum(n1))