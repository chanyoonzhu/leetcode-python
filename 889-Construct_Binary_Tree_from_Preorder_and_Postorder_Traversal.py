# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- dfs (preorder, postorder)
- O(n), O(n)
"""
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = TreeNode(preorder.pop(0))
        postorder.pop()
        if not postorder: return root
        left_index = postorder.index(preorder[0])
        root.left = self.constructFromPrePost(preorder[:left_index + 1], postorder[:left_index + 1])
        root.right = self.constructFromPrePost(preorder[left_index + 1:], postorder[left_index + 1:])
        return root

"""
- todo: real O(n) solution:
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161268/C%2B%2BJavaPython-One-Pass-Real-O(N)
"""