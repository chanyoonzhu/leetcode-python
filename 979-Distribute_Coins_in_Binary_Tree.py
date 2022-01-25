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
        
        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            self.res += abs(l) + abs(r) # number of moves needed to distribute to all children
            # number of tokens need move to(+)/from(-) parent
            # if need move >= 1: keep 1 for itself (-1)
            # if need move <= 0: need 1 from parent abs(need move) += 1 (by -1)
            return node.val + l + r - 1
        
        dfs(root)
        return self.res