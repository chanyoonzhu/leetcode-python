# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- recursive (pre-order traversal)
- O(n), O(n)
"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # easy to miss: do not return, modify in-place
        self.flattenNode(root)
    
    def flattenNode(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None
        
        if not node.left and not node.right:
            return node
        
        left_tail = self.flattenNode(node.left)
        self.flattenNode(node.right)
        
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        
        return right_tail if right_tail else left_tail

"""
- iterative: 
- algorithm:
    1. move right branch under the right most node of left branch
    2. move left branch as the right node of root
    3. root = root.right
- O(n), O(n)
"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            left_tail = self.findRightMost(node.left)
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            node = node.right       
        
    def findRightMost(self, node):
        if not node:
            return None
        while node.right:
            node = node.right
        return node
        
        