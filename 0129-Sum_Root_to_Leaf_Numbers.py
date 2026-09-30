# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
- dfs - recursive
- O(n), O(n)
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
        
    def dfs(self, node, total):
        if not node:
            return 0
        total = total * 10 + node.val
        if not node.left and not node.right:
            return total
        l = self.dfs(node.left, total)
        r = self.dfs(node.right, total)
        return l + r

"""
- dfs - iterative
- O(n), O(n)
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        root_to_leaf = 0
        stack = [(root, 0)]
        
        while stack:
            root, curr_number = stack.pop()
            if root:
                curr_number = curr_number * 10 + root.val
                # if it's a leaf, update root-to-leaf sum
                if not root.left and not root.right:
                    root_to_leaf += curr_number
                else:
                    stack.append((root.left, curr_number))
                    stack.append((root.right, curr_number))
                        
        return root_to_leaf