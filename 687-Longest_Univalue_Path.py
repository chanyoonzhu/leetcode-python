# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):


    """
    - O(n), O(n)
    - post-order dfs
    """
    
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
            
        