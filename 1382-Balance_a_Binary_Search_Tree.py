"""
https://leetcode.com/problems/balance-a-binary-search-tree/
- BST (sort and inorder-traversal)
- O(nlogn), O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def sortedValsToBST(sorted_vals, i, j):
            if i > j: return None
            mid = i + (j - i) // 2
            root = TreeNode(sorted_vals[mid])
            root.left = sortedValsToBST(sorted_vals, i, mid-1)
            root.right = sortedValsToBST(sorted_vals, mid+1, j)
            return root
   
        sorted_vals = inorder(root)
        return sortedValsToBST(sorted_vals, 0, len(sorted_vals) - 1)