# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
- dfs
- O(n), O(n)
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.result = 0
        
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = left + right + 1
            self.result = max(self.result, diameter)
            return max(left, right) + 1
        
        dfs(root)
        return self.result - 1 # diameter = node number - 1

n1 = TreeNode(1)
n1.left = TreeNode(2)
n1.right = TreeNode(3)
n1.left.left = TreeNode(4)
n1.left.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(n1))