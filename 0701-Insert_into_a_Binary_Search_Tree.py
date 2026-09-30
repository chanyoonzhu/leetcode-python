# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- BST (recursive)
- O(logn), O(n)
"""
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

"""
- BST (iterative)
- O(logn), O(n)
"""
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new = TreeNode(val)
        if not root:
            return new
        node = root
        while node:
            if val < node.val:
                if not node.left:
                    node.left = new
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = new
                    break
                else:
                    node = node.right
        return root
        