# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    longest = 0
    """
    - post-order traversal
    - O(n): every node is visited once -  The time complexity is the same as an post-order traversal of a binary tree with n nodes.
    - O(n): The extra space comes from implicit stack space due to recursion. For a skewed binary tree, the recursion could go up to nn levels deep.
    """
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.longest 
        
    def dfs(self, node):
        if node is None: 
            return (0, 0)
        left, right = node.left, node.right
        l_inc, l_dec = self.dfs(left)
        r_inc, r_dec = self.dfs(right)
        n_inc = n_dec = 1
        if left and left.val + 1 == node.val:
            n_inc = l_inc + 1
        if right and right.val + 1 == node.val:
            n_inc = max(n_inc, r_inc + 1)
        if left and left.val - 1 == node.val:
            n_dec = l_dec + 1
        if right and right.val - 1 == node.val:
            n_dec = max(n_dec, r_dec + 1)        
        self.longest = max(self.longest, n_inc + n_dec - 1)
        return(n_inc, n_dec)