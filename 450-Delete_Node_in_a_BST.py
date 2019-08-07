# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left or not root.right:
                root = root.left if root.left else root.right
            else:
                curr = root.left
                while curr.right:
                    curr = curr.right
                root.val = curr.val
                root.left = self.deleteNode(root.left, curr.val)
        return root