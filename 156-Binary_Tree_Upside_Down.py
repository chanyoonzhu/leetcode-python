# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs (recursive) - my solution
- O(n), O(n)
"""
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        self.new_root = None
    
        def _turn(node):
            if not node.left:
                self.new_root = node
                return
            _turn(node.left)
            new_root = node.left
            new_root.left = node.right
            new_root.right = node
            node.left, node.right = None, None
            
        _turn(root)
        return self.new_root

"""
- dfs (recursive) - cleaner solution
- O(n), O(n)
"""
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root and root.left :
            res = self.upsideDownBinaryTree(root.left)
            root.left.right = root
            root.left.left = root.right
            root.left, root.right = None, None
            return res
        else:
            return root