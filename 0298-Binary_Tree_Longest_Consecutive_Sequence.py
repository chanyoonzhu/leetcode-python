# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Questions:
- validity of number (floats, negative integer and 0)
"""
"""
- top-down solution (pre-order traversal)
- O(n): every node is visited once -  The time complexity is the same as an in-order traversal of a binary tree with n nodes.
- O(n): The extra space comes from implicit stack space due to recursion. For a skewed binary tree, the recursion could go up to nn levels deep.
"""
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, -100, 0) # provided that node values are all positive
        
    def dfs(self, node, prev_val, _max):
        if node is None:
            return _max
        if node.val != prev_val + 1:
            return max(_max, self.dfs(node.left, node.val, 1), self.dfs(node.right, node.val, 1))
        if node.val == prev_val + 1:
            return max(self.dfs(node.left, node.val, _max+1), self.dfs(node.right, node.val, _max+1))


"""
- bottom-up solution 
- O(n), O(n)
"""
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.maximum_length = 0
        
        def helper(root):
            if not root:
                return 0
            length = 1
            # easy to miss: need to call helper even if node doesn't connect downwards
            l = helper(root.left)
            r = helper(root.right)
            if root.left and root.left.val == root.val + 1:
                length = max(length, 1 + l)
            if root.right and root.right.val == root.val + 1:
                length = max(length, 1 + r)
            self.maximum_length = max(self.maximum_length, length)
            return length
        
        helper(root)
        return self.maximum_length
        