# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- Q: does every right node have a sibling?
- Q: how to handle children of right node? (no children on right node)
"""

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

"""
- dfs (iterative)
- O(n), O(n)
"""
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        
        new_root = stack[-1]
        while len(stack) > 1:
            node = stack.pop()
            node.left = stack[-1].right
            node.right = stack[-1]
            stack[-1].left, stack[-1].right = None, None
        return new_root