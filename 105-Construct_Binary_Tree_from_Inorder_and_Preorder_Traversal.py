# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
- dfs (preorder, inorder)
- O(n), O(n)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder.pop(0))
        root_index = inorder.index(root.val)
        root.left = self.buildTree(preorder[:root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index:], inorder[root_index + 1:])
        return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sl = Solution()
sl.buildTree(preorder, inorder)