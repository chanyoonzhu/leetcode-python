# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- dfs (postorder, inorder)
- O(n), O(n)
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder: return None
        root = TreeNode(postorder.pop())
        root_index = inorder.index(root.val)
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1:], postorder[root_index:])
        return root

"""
- dfs (preorder) - optimized using hashmap
- O(n), O(n) - space optimized
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def dfs(inorder, postorder, il, ir, pl, pr):
            if pl > pr:
                return None
            root = TreeNode(postorder[pr])
            i = inorder_map[root.val]
            root.left = dfs(inorder, postorder, il, i - 1, pl, pl + i - il - 1)
            root.right = dfs(inorder, postorder, i + 1, ir, pl + i - il, pr - 1)
            return root
        
        n = len(inorder)
        inorder_map = dict()
        for i, val in enumerate(inorder):
            inorder_map[val] = i
        
        return dfs(inorder, postorder, 0, n - 1, 0, n - 1)