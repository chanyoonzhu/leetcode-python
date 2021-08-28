# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- bst + preorder traversal
- O(n^2), O(n)
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = TreeNode(preorder.pop(0))
        right_index = 0
        while right_index < len(preorder):
            if preorder[right_index] > root.val:
                break
            right_index += 1
        root.left = self.bstFromPreorder(preorder[:right_index])
        root.right = self.bstFromPreorder(preorder[right_index:])
        return root

"""
- bst + preorder traversal
- O(nlogn), O(n)
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        root = TreeNode(preorder.pop(0))
        right_index = bisect.bisect(preorder, root.val)
        root.left = self.bstFromPreorder(preorder[:right_index])
        root.right = self.bstFromPreorder(preorder[right_index:])
        return root

"""
- bst + preorder traversal
- O(n), O(n)
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.buildTree(preorder, float('inf'))

    def buildTree(self, preorder, bound):
        if not preorder or preorder[0] > bound: return None
        node = TreeNode(preorder.pop(0))
        node.left = self.buildTree(preorder, node.val)
        node.right = self.buildTree(preorder, bound)
        return node
        