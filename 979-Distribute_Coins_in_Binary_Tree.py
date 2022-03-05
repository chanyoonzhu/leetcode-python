# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- dfs
- intuition: https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal
- O(n), O(n)
"""
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        
        # returns: number of tokens (x) need move between itself and its parent: 
        # when x > 0 -> need to move x to its parent, when x < 0 -> need to move x from parent to itself
        def dfs(node): 
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            self.res += abs(l) + abs(r)
            return node.val + l + r - 1 # -1 -> one token for itself
        
        dfs(root)
        return self.res