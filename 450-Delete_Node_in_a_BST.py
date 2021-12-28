# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
- binary search tree
- O(logn), O(logn)
"""
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root: return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            new_root = root.left
            # move new_root.right to as the left branch of the successor of root
            right_leftmost = root.right
            while right_leftmost.left:
                right_leftmost = right_leftmost.left
            right_leftmost.left = new_root.right
            new_root.right = root.right
            root = new_root
        return root