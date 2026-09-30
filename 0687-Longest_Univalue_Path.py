# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- O(n), O(n)
- post-order dfs (get child nodes value from traversal)
"""
class Solution(object):
    
    longest = 0
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return max(self.longest - 1, 0) # easy to miss: length of edges, not nodes, thus -1, but return 0 not -1 for null nodes
        
    def dfs(self, node):
        if not node:
            return 0
        l_longest, r_longest = self.dfs(node.left), self.dfs(node.right)
        curr_longest = curr_longest_one_side = 1 
        if node.left and node.left.val == node.val:
            curr_longest += l_longest
            curr_longest_one_side = l_longest + 1
        if node.right and node.right.val == node.val:
            curr_longest += r_longest
            curr_longest_one_side = max(curr_longest_one_side, r_longest + 1)
        self.longest = max(self.longest, curr_longest)
        return curr_longest_one_side

"""
- O(n), O(n)
- post-order dfs: (get child nodes value from return value)
"""
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        
        def dfs(node):
            if not node:
                return (None, 0)
            l_val, l_length = dfs(node.left)
            r_val, r_length = dfs(node.right)
            max_length_one_side = 0
            if node.val == l_val:
                self.longest = max(self.longest,  l_length + 1)
                max_length_one_side = l_length + 1
            if node.val == r_val:
                self.longest = max(self.longest, max_length_one_side + r_length + 1) # caveat: have to add both sides when calculate longest
                max_length_one_side = max(length, r_length + 1) # only pick the longest side
            return (node.val, max_length_one_side)
        
        dfs(root)
        return self.longest
            
        