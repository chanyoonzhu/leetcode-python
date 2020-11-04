# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    """
    - easy to miss: 
        1. in BST, a node value has to be larger than the value of all nodes in its left subtree, not just the value of its left child
        2. any part of a subtree is not a BST prevents the node to be a BST (has to ask in clarification question), need a (boolean)variable to keep this info.

    - O(n), O(n)
    """
    largest = 0
    
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.largest
        
    def dfs(self, node):
        if not node:
            return (0, True, float('-inf'), float('inf'))
        l_sum, l_is_bst, l_min, l_max = self.dfs(node.left)
        r_sum, r_is_bst, r_min, r_max = self.dfs(node.right)
        _sum, is_bst = l_sum + r_sum + 1, True
        _min, _max = l_min if node.left else node.val, r_max if node.right else node.val # don't miss where child is null
        if (node.left and l_max >= node.val o # l_max, not node.left.val
            or node.right and r_min <= node.val # r_min, not node.right.val
            or not l_is_bst or not r_is_bst): # cannot use l/r_sum to determine l/r_is_bst
            _sum, is_bst = 0, False
        self.largest = max(self.largest, _sum)
        return (_sum, is_bst, _min, _max)
        