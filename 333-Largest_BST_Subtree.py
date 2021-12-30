# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right    
"""
- bst
- easy to miss: 
    1. in BST, a node value has to be larger than the value of all nodes in its left subtree, not just the value of its left child
    2. any part of a subtree is not a BST prevents the node to be a BST (has to ask in clarification question), need a (boolean)variable to keep this info.
- O(n), O(n)
"""
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        
        def helper(node):
            if not node:
                return (0, True, None, None)
            l_sum, l_bst, l_min, l_max = helper(node.left)
            r_sum, r_bst, r_min, r_max = helper(node.right)
            if not l_bst or not r_bst or (l_max and node.val <= l_max) or (r_min and r_min <= node.val):
                return (0, False, None, None)
            total = 1 + l_sum + r_sum
            self.maximum = max(self.maximum, total)
            return total, True, l_min or node.val, r_max or node.val
        
        helper(root)
        return self.maximum
        